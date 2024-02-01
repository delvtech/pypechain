"""Functions to render Python files from an abi usng a jinja2 template."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, NamedTuple

from web3.types import ABI

from pypechain.utilities.abi import (
    AbiInfo,
    ErrorInfo,
    EventInfo,
    StructInfo,
    get_abi_constructor,
    get_abi_items,
    get_errors_for_abi,
    get_events_for_abi,
    get_input_names,
    get_input_names_and_types,
    get_input_types,
    get_output_names,
    get_output_names_and_types,
    get_output_types,
    get_structs_for_abi,
    is_abi_event,
    is_abi_function,
)
from pypechain.utilities.format import capitalize_first_letter_only
from pypechain.utilities.templates import get_jinja_env
from pypechain.utilities.types import EventData, FunctionData, SignatureData


@dataclass
class ContractInfo:
    """Contract Information.  This is the set of information needed to populate both the Contact.py
    and Types.py file for each solidity contract."""

    abi: ABI
    bytecode: str
    contract_name: str
    structs: dict[str, StructInfo]
    events: dict[str, EventInfo]
    errors: dict[str, ErrorInfo]


def get_contract_infos(abi_infos: list[AbiInfo]) -> dict[str, ContractInfo]:
    """Gets a dictionary of ContractInfos keyed by contract name from an AbiInfos list.

     This helps us organize structs and events by the contracts they are defined
     in. Because structs can be defined in one file, and used in another, we
     need to avoid duplication of the definitions.

    Parameters
    ----------
    abi_infos : list[AbiInfo]
        A list of AbiInfos, which contain the ABI itself along with the contract name and the bytecode.

    Returns
    -------
    dict[str, ContractInfo]
        A dictionary of ContractInfos keyed by the contract names.
    """
    contract_infos: dict[str, ContractInfo] = {}

    # Populate contract_infos with all the structs, events, whole ABIs, bytecodes and contract names.
    for abi_info in abi_infos:
        structs = get_structs_for_abi(abi_info.abi)
        events = get_events_for_abi(abi_info.abi)
        errors = get_errors_for_abi(abi_info.abi)
        contract_infos[abi_info.contract_name] = ContractInfo(
            abi=abi_info.abi,
            bytecode=abi_info.bytecode,
            contract_name=abi_info.contract_name,
            structs={},
            events={},
            errors={},
        )
        _add_structs(contract_infos, structs)
        _add_events(contract_infos, events, abi_info.contract_name)
        _add_errors(contract_infos, errors, abi_info.contract_name)

    return contract_infos


def _add_structs(contract_infos: dict[str, ContractInfo], structs: StructInfo | list[StructInfo]):
    """Adds structs in-place to contract_infos.

    Because we know from the ABI json the contract name that a struct is defined in, we can avoid
    creating duplicate definitions in the generated pypechain types.

    Parameters
    ----------
    contract_infos : dict[str, ContractInfo] structs : StructInfo | list[StructInfo]
        A dictionary of ContractInfos keyed by the contract names.
    structs : StructInfo | list[StructInfo]
        The structs to add to the contract infos.  This is a deduping process since we key by
        contract name then struct name.
    """
    if not isinstance(structs, list):
        structs = [structs]
    for struct in structs:
        info = contract_infos.get(struct.contract_name)
        if info:
            info.structs[struct.name] = struct
        else:
            contract_infos[struct.contract_name] = ContractInfo(
                abi=[],
                bytecode="",
                contract_name=struct.contract_name,
                structs={struct.name: struct},
                events={},
                errors={},
            )


def _add_events(contract_infos: dict[str, ContractInfo], events: EventInfo | list[EventInfo], contract_name: str):
    """Adds events in-place to contract_infos.

    Parameters
    ----------
    contract_infos : dict[str, ContractInfo] structs : StructInfo | list[StructInfo]
        A dictionary of ContractInfos keyed by the contract names.
    events : EventInfo | list[EventInfo]
        The events to add to the contract infos.  There isn't enough information in the ABI jsons to
        know if a contract is using an interface imported event, so there may be duplicates.  This
        is not as big of an issue for events though since we never pass them as inputs, which python
        would complain about.
    contract_name : str
        The name of the contract for the abi the events were found in.
    """
    if not isinstance(events, list):
        events = [events]
    for event in events:
        info = contract_infos.get(contract_name)
        if info:
            info.events[event.name] = event
        else:
            contract_infos[contract_name] = ContractInfo(
                abi=[],
                bytecode="",
                contract_name=contract_name,
                structs={},
                events={event.name: event},
                errors={},
            )


def _add_errors(contract_infos: dict[str, ContractInfo], errors: ErrorInfo | list[ErrorInfo], contract_name: str):
    """Adds events in-place to contract_infos.

    Parameters
    ----------
    contract_infos : dict[str, ContractInfo] structs : StructInfo | list[StructInfo]
        A dictionary of ContractInfos keyed by the contract names.
    events : EventInfo | list[EventInfo]
        The events to add to the contract infos.  There isn't enough information in the ABI jsons to
        know if a contract is using an interface imported event, so there may be duplicates.  This
        is not as big of an issue for events though since we never pass them as inputs, which python
        would complain about.
    contract_name : str
        The name of the contract for the abi the events were found in.
    """
    if not isinstance(errors, list):
        errors = [errors]
    for error in errors:
        info = contract_infos.get(contract_name)
        if info:
            info.errors[error.name] = error
        else:
            contract_infos[contract_name] = ContractInfo(
                abi=[],
                bytecode="",
                contract_name=contract_name,
                structs={},
                events={},
                errors={error.name: error},
            )


def render_contract_file(contract_info: ContractInfo) -> str | None:
    """Returns the serialized code of the contract file to be generated.

    Parameters
    ----------
    contract_template : Template
        A jinja template containging types for all structs within an abi.
    abi_file_path : Path
        The path to the abi file to parse.

    Returns
    -------
    str
        A serialized python file.
    """
    # pylint: disable=too-many-locals
    # if the abi is empty, then we are dealing with an interface or library so we don't want to
    # create a contract file for it.
    if contract_info.abi == []:
        return None
    # TODO: break this function up or bundle arguments to save on variables

    env = get_jinja_env()
    templates = get_templates_for_contract_file(env)

    function_datas, constructor_data = get_function_datas(contract_info.abi)
    event_datas = get_event_datas(contract_info.abi)
    error_infos = contract_info.errors.values()

    has_bytecode = bool(contract_info.bytecode)
    has_events = bool(len(event_datas.values()))
    # if any function has overloading
    has_overloading = any(function_data["has_overloading"] for function_data in function_datas.values())

    structs_used = get_structs_for_abi(contract_info.abi)

    functions_block = templates.functions_template.render(
        abi=contract_info.abi,
        contract_name=contract_info.contract_name,
        functions=function_datas,
        # TODO: use this data to add a typed constructor
        constructor=constructor_data,
    )

    events_block = templates.events_template.render(
        contract_name=contract_info.contract_name,
        events=event_datas,
    )

    has_errors = bool(len(error_infos))
    errors_block = templates.errors_template.render(
        contract_name=contract_info.contract_name,
        errors=error_infos,
    )

    abi_block = templates.abi_template.render(
        abi=contract_info.abi,
        bytecode=contract_info.bytecode,
        contract_name=contract_info.contract_name,
    )

    contract_block = templates.contract_template.render(
        has_bytecode=has_bytecode,
        has_events=has_events,
        has_errors=has_errors,
        contract_name=contract_info.contract_name,
        constructor=constructor_data,
        functions=function_datas,
    )

    # if any function has overloading
    has_overloading = any(function_data["has_overloading"] for function_data in function_datas.values())
    has_multiple_return_values = any(
        function_data["has_multiple_return_values"] for function_data in function_datas.values()
    )

    # Render the template
    return templates.base_template.render(
        contract_name=contract_info.contract_name,
        structs_used=structs_used,
        has_overloading=has_overloading,
        has_multiple_return_values=has_multiple_return_values,
        has_bytecode=has_bytecode,
        functions_block=functions_block,
        has_events=has_events,
        events_block=events_block,
        has_errors=has_errors,
        errors_block=errors_block,
        abi_block=abi_block,
        contract_block=contract_block,
        # TODO: use this data to add a typed constructor
        # constructor_data=constructor_data,
    )


def get_has_multiple_return_signatures(signature_datas: list[SignatureData]) -> bool:
    """If there are multiple return signatures for a smart contract function, we'll need to overload
       the call() method.  This method compares the output types of all the signatures of a method.

    Parameters
    ----------
    signature_datas : list[SignatureData]
        a list of SignatureData's to compare.

    Returns
    -------
    bool
        If there are multiple return signatures or not.
    """
    lists_equal = True
    first_output_types: list[str] | None = None
    for signature_data in signature_datas:
        if first_output_types is None:
            first_output_types = signature_data["output_types"]
        else:
            lists_equal = all(
                output_types_to_compare[0] == output_types_to_compare[1]
                for output_types_to_compare in zip(first_output_types, signature_data["output_types"])
            )
            if not lists_equal:
                break

    return not lists_equal


def get_has_multiple_return_values(signature_datas: list[SignatureData]) -> bool:
    """If there are multiple return values for a smart contract function, we'll need to overload
       the call() method. This method compares the output types of all the values of a method.

    Parameters
    ----------
    signature_datas : list[SignatureData]
        a list of SignatureData's to compare.

    Returns
    -------
    bool
        If there are multiple return signatures or not.
    """
    for signature_data in signature_datas:
        if len(signature_data["outputs"]) > 1:
            return True
    return False


class ContractTemplates(NamedTuple):
    """Templates for the generated contract file."""

    base_template: Any
    functions_template: Any
    events_template: Any
    errors_template: Any
    abi_template: Any
    contract_template: Any


def get_templates_for_contract_file(env):
    """Templates for the generated contract file."""
    return ContractTemplates(
        base_template=env.get_template("contract.py/base.py.jinja2"),
        functions_template=env.get_template("contract.py/functions.py.jinja2"),
        events_template=env.get_template("contract.py/events.py.jinja2"),
        errors_template=env.get_template("contract.py/errors.py.jinja2"),
        abi_template=env.get_template("contract.py/abi.py.jinja2"),
        contract_template=env.get_template("contract.py/contract.py.jinja2"),
    )


class GetFunctionDatasReturnValue(NamedTuple):
    """Return value for get_function_datas"""

    function_datas: dict[str, FunctionData]
    constructor_data: SignatureData | None


def get_function_datas(abi: ABI) -> GetFunctionDatasReturnValue:
    """Gets the information needed for the generated Contract file.

    Parameters
    ----------
    abi : ABI
        An application boundary interface for smart contract in json format.

    Returns
    -------
    tuple[dict[str, FunctionData], SignatureData | None]
        A tuple where the first value is a dictionary of FunctionData's keyed by function name and
        the second value is SignatureData for the constructor.
    """

    # handle constructor
    abi_constructor = get_abi_constructor(abi)
    constructor_data: SignatureData | None = (
        {
            "input_names_and_types": get_input_names_and_types(abi_constructor),
            "input_names": get_input_names(abi_constructor),
            "input_types": get_input_types(abi_constructor),
            "outputs": get_output_names(abi_constructor),
            "output_types": get_output_names_and_types(abi_constructor),
        }
        if abi_constructor
        else None
    )

    # handle all other functions
    function_datas: dict[str, FunctionData] = {}
    for abi_function in get_abi_items(abi):
        if is_abi_function(abi_function):
            name = abi_function.get("name", "")
            name = re.sub(r"\W|^(?=\d)", "_", name)
            signature_data: SignatureData = {
                "input_names_and_types": get_input_names_and_types(abi_function),
                "input_names": get_input_names(abi_function),
                "input_types": get_input_types(abi_function),
                "outputs": get_output_names(abi_function),
                "output_types": get_output_types(abi_function),
            }

            function_data: FunctionData = {
                "name": name,
                "capitalized_name": capitalize_first_letter_only(name),
                "signature_datas": [signature_data],
                "has_overloading": False,
                "has_multiple_return_signatures": False,
                "has_multiple_return_values": False,
            }
            if not function_datas.get(name):
                function_datas[name] = function_data
                function_datas[name]["has_multiple_return_values"] = get_has_multiple_return_values([signature_data])
            else:
                signature_datas = function_datas[name]["signature_datas"]
                signature_datas.append(signature_data)
                function_datas[name]["has_overloading"] = len(signature_datas) > 1
                function_datas[name]["has_multiple_return_signatures"] = get_has_multiple_return_signatures(
                    signature_datas
                )
                function_datas[name]["has_multiple_return_values"] = get_has_multiple_return_values(signature_datas)
    return GetFunctionDatasReturnValue(function_datas, constructor_data)


def get_event_datas(abi: ABI) -> dict[str, EventData]:
    """Gets the event datas required for the events template.

    Parameters
    ----------
    abi : ABI
        An application boundary interface for smart contract in json format.

    Returns
    -------
    dict[str, EventData]
        A dictionary of EventData's keyed by event name.
    """
    event_datas: dict[str, EventData] = {}
    for abi_event in get_abi_items(abi):
        if is_abi_event(abi_event):
            name = abi_event.get("name", "")
            event_data: EventData = {
                "name": name,
                "capitalized_name": capitalize_first_letter_only(name),
            }
            event_datas[name] = event_data
    return event_datas
