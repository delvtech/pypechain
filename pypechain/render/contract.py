"""Functions to render Python files from an abi usng a jinja2 template."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any, NamedTuple

from web3.types import ABI

from pypechain.utilities.abi import (
    get_abi_constructor,
    get_abi_items,
    get_input_names,
    get_input_names_and_types,
    get_input_types,
    get_output_names,
    get_output_names_and_types,
    get_output_types,
    get_structs_for_abi,
    is_abi_event,
    is_abi_function,
    load_abi_from_file,
)
from pypechain.utilities.format import capitalize_first_letter_only
from pypechain.utilities.templates import get_jinja_env
from pypechain.utilities.types import EventData, FunctionData, SignatureData, gather_matching_types


def render_contract_file(contract_name: str, abi_file_path: Path) -> str:
    """Returns the serialized code of the contract file to be generated.

    Arguments
    ---------
    contract_template : Template
        A jinja template containging types for all structs within an abi.
    abi_file_path : Path
        The path to the abi file to parse.

    Returns
    -------
    str
        A serialized python file.
    """

    # TODO: break this function up or bundle arguments to save on variables
    # pylint: disable=too-many-locals

    env = get_jinja_env()
    templates = get_templates_for_contract_file(env)

    abi, bytecode = load_abi_from_file(abi_file_path)
    function_datas, constructor_data = get_function_datas(abi)
    event_datas = get_event_datas(abi)

    has_bytecode = bool(bytecode)
    has_events = bool(len(event_datas.values()))
    # if any function has overloading
    has_overloading = any(function_data["has_overloading"] for function_data in function_datas.values())

    structs_for_abi = get_structs_for_abi(abi)
    structs_used = gather_matching_types(list(function_datas.values()), list(structs_for_abi.keys()))

    functions_block = templates.functions_template.render(
        abi=abi,
        contract_name=contract_name,
        functions=function_datas,
        # TODO: use this data to add a typed constructor
        constructor=constructor_data,
    )

    events_block = templates.events_template.render(
        contract_name=contract_name,
        events=event_datas,
    )

    abi_block = templates.abi_template.render(
        abi=abi,
        bytecode=bytecode,
        contract_name=contract_name,
    )

    contract_block = templates.contract_template.render(
        has_bytecode=has_bytecode,
        has_events=has_events,
        contract_name=contract_name,
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
        contract_name=contract_name,
        structs_used=structs_used,
        structs_for_abi=structs_for_abi,
        has_overloading=has_overloading,
        has_multiple_return_values=has_multiple_return_values,
        has_bytecode=has_bytecode,
        has_events=has_events,
        functions_block=functions_block,
        events_block=events_block,
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
    abi_template: Any
    contract_template: Any


def get_templates_for_contract_file(env):
    """Templates for the generated contract file."""
    return ContractTemplates(
        base_template=env.get_template("contract.py/base.py.jinja2"),
        functions_template=env.get_template("contract.py/functions.py.jinja2"),
        events_template=env.get_template("contract.py/events.py.jinja2"),
        abi_template=env.get_template("contract.py/abi.py.jinja2"),
        contract_template=env.get_template("contract.py/contract.py.jinja2"),
    )


class GetFunctionDatasReturnValue(NamedTuple):
    """Return value for get_function_datas"""

    function_datas: dict[str, FunctionData]
    constructor_data: SignatureData | None


def get_function_datas(abi: ABI) -> GetFunctionDatasReturnValue:
    """Gets the information needed for the generated Contract file.

    Arguments
    ---------
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

    Arguments
    ---------
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
