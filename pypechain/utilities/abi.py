"""Utilities for solidity contract ABIs."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, NamedTuple, Sequence, TypeGuard, cast

from eth_typing import ABI, ABIComponent, ABIElement, ABIError, ABIEvent, ABIFunction
from eth_utils.abi import collapse_if_tuple, function_signature_to_4byte_selector
from eth_utils.hexadecimal import encode_hex

from pypechain.foundry.types import FoundryJson
from pypechain.hardhat.types import HardhatJson
from pypechain.hardhat.utilities import is_hardhat_json
from pypechain.solc.types import SolcJson
from pypechain.solc.utilities import is_solc_json
from pypechain.utilities.bytecode import get_bytecode_from_json, get_bytecode_link_references_from_json, is_foundry_json
from pypechain.utilities.format import avoid_python_keywords, capitalize_first_letter_only
from pypechain.utilities.types import LinkReferences, solidity_to_python_type


class AbiJson(NamedTuple):
    """A JSON representation of a solidity contract's Application Boundary Interface."""

    abi: Sequence[ABIElement]


def load_abi(abi_path: str) -> AbiJson:
    """Loads the abi file into a json.

    Parameters
    ----------
    abi_path : str
        Where the abi json is location.

    Returns
    -------
    AbiJson
        A named tuple representation of an abi json file.
    """

    with open(abi_path, "r", encoding="utf-8") as abi_file:
        data = json.load(abi_file)

        # Assuming that the ABI data structure is at the top level of the JSON
        # (i.e., the file is a list of ABI items):
        abi_items = [cast(ABIElement, item) for item in data]

        return AbiJson(abi=abi_items)


def is_abi_function(item: ABIElement) -> TypeGuard[ABIFunction]:
    """Typeguard function for ABIFunction.

    Parameters
    ----------
    item:  Any
        The item we are confirming is an ABIFunction

    Returns
    -------
    TypeGuard[ABIFunction]
    """
    # Check if the required keys exist
    required_keys = ["type", "inputs"]

    # Check if the required keys exist
    if not all(key in item for key in required_keys):
        return False

    # Check if the type is a function
    if item.get("type") not in ["function", "constructor", "fallback", "receive"]:
        return False

    return True


def get_abi_constructor(abi: ABI) -> ABIFunction | None:
    """Returns the constructor item if it exists.

    Parameters
    ----------
    abi: ABI
        The contract's abi json to parse.

    Returns
    -------
    ABIFunction | None
        The constructor information returned as an abi function since they have the same pattern.
    """

    result = next((x for x in abi if x.get("type", "") == "constructor"), None)
    return result if result and is_abi_function(result) else None


def is_abi_constructor(item: ABIElement) -> TypeGuard[ABIFunction]:
    """Typeguard function for ABIFunction.

    Parameters
    ----------
    item:  Any
        The item we are confirming is an ABIFunction

    Returns
    -------
    TypeGuard[ABIFunction]
    """
    # Check if the required keys exist
    required_keys = ["type", "inputs"]

    # Check if the required keys exist
    if not all(key in item for key in required_keys):
        return False

    # Check if the type is a constructor function
    if item.get("type") != "constructor":
        return False

    return True


def is_abi_event(item: ABIElement) -> TypeGuard[ABIEvent]:
    """Typeguard function for ABIEvent.

    Parameters
    ----------
    item:  Any
        The item we are confirming is an ABIFunction

    Returns
    -------
    TypeGuard[ABIEvent]
    """
    # Check if the required keys exist
    required_keys = ["type", "name", "inputs"]

    # Check if the required keys exist
    if not all(key in item for key in required_keys):
        return False

    # Check if the type is "event"
    if item.get("type") != "event":
        return False

    return True


def is_abi_error(item: ABIElement) -> TypeGuard[ABIError]:
    """Typeguard function for ABIError.

    Parameters
    ----------
    item:  Any
        The item we are confirming is an ABIError

    Returns
    -------
    TypeGuard[ABIError]
    """
    # Check if the required keys exist
    required_keys = ["type", "name", "inputs"]

    # Check if the required keys exist
    if not all(key in item for key in required_keys):
        return False

    # Check if the type is "event"
    if item.get("type") != "error":
        return False

    return True


def filter_abi_items_by_type(item_type: str | list[str], contract_abi: ABI) -> list[ABIElement]:
    """Filters ABIItems by type.

    Parameters
    ----------
    item_type : str | list[str]
        Item or list of items to filter by
    contract_abi : ABI
        The ABI to filter

    Returns
    -------
    list[ABIFunction | ABIEvent]

    """

    if isinstance(item_type, str):
        item_type = [item_type]

    return [abi for abi in contract_abi if abi.get("type", "") in item_type]


@dataclass
class StructInfo:
    """Solidity struct information needed for codegen."""

    name: str
    contract_name: str
    values: list[StructValue]


@dataclass
class StructValue:
    """The name and python type of a solidity struct value."""

    name: str
    # TODO: type this better with an exahaustive list of python type strings.  Even better, maybe a
    # mapping from solidity to python types?
    solidity_type: str
    python_type: str
    is_struct: bool
    contract_name: str | None


@dataclass
class EventInfo:
    """Solidity struct information needed for codegen."""

    name: str
    capitalized_name: str
    anonymous: bool
    inputs: list[EventParams]


@dataclass
class EventParams:
    """Solidity struct information needed for codegen."""

    indexed: bool
    name: str
    solidity_type: str
    python_type: str


@dataclass
class ErrorInfo:
    """Solidity struct information needed for codegen."""

    name: str
    selector: str
    signature: str
    inputs: list[ErrorParams]


@dataclass
class ErrorParams:
    """Solidity struct information needed for codegen."""

    name: str
    solidity_type: str
    python_type: str


def get_structs(
    function_params: Sequence[ABIComponent],
    structs: dict[str, StructInfo] | None = None,
) -> dict[str, StructInfo]:
    """Recursively gets all the structs for a contract by walking all function parameters.

     Pseudo code of the shape of a Sequence[ABIComponent]:
     [
        { #ABIFunctionParams
            name:
            type: asdf
            internalType:
            components:
        },
        { #ABIFunctionParams
            name:
            type:
            internalType:
            components: [ #Sequence[ABIComponent]
                { #ABIComponent
                    name:
                    type:
                },
                { #ABIComponent
                    name:
                    type:
                    internalType:
                    components: # Sequence[ABIComponent]
                }
            ]
        },
    ]

    Parameters
    ----------
    function_params : Sequence[ABIFunctionParams] | Sequence[ABIFunctionComponents]
        The function parameter lists to parse structs from.

    structs : dict[str, StructInfo] | None = None
         A dictionary of StructInfos keyed by struct name that is populated during recursion.

    Returns
    -------
    dict[str, StructInfo]
        The completed dictionary of StructInfos keyed by struct name.
    """
    if structs is None:
        structs = {}
    for param in function_params:
        components = param.get("components")
        internal_type = cast(str, param.get("internalType", ""))

        # If we find a struct, we'll add it to the dict of StructInfo's
        if is_struct(internal_type) and components:
            struct_name = get_struct_name(param)
            struct_file_name = get_struct_contract_name(param)
            struct_values: list[StructValue] = []

            # Walk over the components of the struct
            for component in components:
                component_internal_type = cast(str, component.get("internalType", ""))

                # Do recursion if nested struct
                contract_name: str | None = None
                if is_struct(component_internal_type):
                    structs = get_structs([component], structs)
                    contract_name = get_struct_contract_name(component)

                # Get the component name and type
                component_name = get_param_name(component)  # strip [] if it is an array
                component_type = (
                    get_struct_type(component) if is_struct(component_internal_type) else component.get("type", "")
                )
                python_type = solidity_to_python_type(
                    component_type, custom_types=[struct.name for struct in structs.values()]
                )

                # Collect information
                struct_values.append(
                    StructValue(
                        name=component_name,
                        solidity_type=component_type,
                        python_type=python_type,
                        is_struct=is_struct(component_internal_type),
                        contract_name=contract_name,
                    )
                )

            # Add the struct to the dict
            structs[f"{struct_file_name}.{struct_name}"] = StructInfo(
                name=struct_name, contract_name=struct_file_name, values=struct_values
            )

    return structs


def get_structs_for_abi(abi: ABI) -> list[StructInfo]:
    """Gets all the structs for a given abi.
    These are found by parsing function inputs and outputs for internalType's.

    Parameters
    ----------
    abi : ABI
        An Application Boundary Interface object.

    Returns
    -------
    dict[str, StructInfo]
        A dictionary of StructInfos keyed by name.
    """
    structs: dict[str, StructInfo] = {}
    for item in abi:
        if is_abi_function(item):
            fn_inputs = item.get("inputs")
            fn_outputs = item.get("outputs")
            if fn_inputs:
                input_structs = get_structs(fn_inputs, structs)
                structs.update(input_structs)
            if fn_outputs:
                output_structs = get_structs(fn_outputs, structs)
                structs.update(output_structs)
    return list(structs.values())


def is_struct(internal_type: str) -> bool:
    """Returns True if the internal type of the parameter is a solidity struct.

    Parameters
    ----------
    internal_type : str
        The internalType attribute of an ABIFunctionParams or ABIFunctionComponents.  If the
        internal type has the form 'struct ContractName.StructName' then we know we are dealing with
        solidity struct.  Otherwise it will be equivalent to the 'type' attribute.

    Returns
    -------
    bool
        If the type is a struct.
    """
    # internal_type looks like 'struct ContractName.StructName' if they are structs
    return bool(internal_type.startswith("struct"))


def get_events_for_abi(abi: ABI) -> list[EventInfo]:
    """Gets all the events for a given abi.

    Parameters
    ----------
    abi : ABI
        An Application Boundary Interface object.

    Returns
    -------
    list[ABIEvent]
        A dictionary of StructInfos keyed by name.
    """

    events: list[EventInfo] = []

    anonymous_event_counter: int = 0

    for item in abi:
        if is_abi_event(item):
            event: ABIEvent = item
            event_inputs = event.get("inputs", [])
            inputs: list[EventParams] = []

            arg_counter: int = 1
            for i in event_inputs:
                indexed = i.get("indexed", False)
                name = i.get("name", "annonymous")

                # Event names can be unnamed
                if name == "":
                    name = f"arg{arg_counter}"

                solidity_type = i.get("type")
                if not solidity_type:
                    raise ValueError("Type not known for event input.")

                python_type = solidity_to_python_type(solidity_type)
                event_input = EventParams(
                    indexed=indexed,
                    name=avoid_python_keywords(name),
                    solidity_type=solidity_type,
                    python_type=python_type,
                )

                inputs.append(event_input)
                arg_counter += 1

            anonymous = item.get("anonymous", False)
            name = item.get("name", f"Annonymous{anonymous_event_counter or None}")
            # TODO add test for multiple anonymous events
            events.append(
                EventInfo(
                    name=name,
                    capitalized_name=capitalize_first_letter_only(name),
                    anonymous=anonymous,
                    inputs=inputs,
                )
            )

    return events


def get_errors_for_abi(abi: ABI) -> list[ErrorInfo]:
    """Gets all the errors for a given abi.

    Parameters
    ----------
    abi : ABI
        An Application Boundary Interface object.

    Returns
    -------
    list[ErrorInfo]
        A dictionary of StructInfos keyed by name.
    """

    errors: list[ErrorInfo] = []

    for item in abi:
        if is_abi_error(item):
            error_inputs = item.get("inputs", [])
            inputs: list[ErrorParams] = []

            for i in error_inputs:
                name = i.get("name", "")
                solidity_type = i.get("type")
                if not solidity_type:
                    raise ValueError("Type not known for event input.")

                python_type = solidity_to_python_type(solidity_type)
                error_input = ErrorParams(
                    name=name,
                    solidity_type=solidity_type,
                    python_type=python_type,
                )

                inputs.append(error_input)

            signature = _abi_to_signature(dict(item)).replace(" ", "")
            selector = encode_hex(function_signature_to_4byte_selector(signature))

            errors.append(
                ErrorInfo(
                    name=item.get("name"),
                    selector=selector,
                    signature=signature,
                    inputs=inputs,
                )
            )

    return errors


def _abi_to_signature(abi: dict[str, Any]) -> str:
    fn_input_types = ",".join([collapse_if_tuple(abi_input) for abi_input in abi.get("inputs", [])])
    function_signature = f"{abi['name']}({fn_input_types})"
    return function_signature


def get_struct_name(
    param_or_component: ABIComponent,
) -> str:
    """Returns the name of the given struct.

    For example, a struct in an abi json will look like:

    {
    "components": [
      # components listed here
    ],
    "internalType": "struct ContractName.SimpleStruct",
    "name": "simpleStruct",
    "type": "tuple"
    }

    We are assuming 'internalType's value to have the form:
    'struct [ContractName].[StructName]' or 'struct [StructName]'

    Parameters
    ----------
    param_or_component: ABIFunctionParams | ABIFunctionComponents


    Returns
    -------
    str
        The name of the item.
    """
    internal_type = cast(str, param_or_component.get("internalType", ""))
    # grab subtype if there is one
    if "." in internal_type:
        internal_type = internal_type.split(".")[1]
    # it is possible that the internal type has a "struct" label
    # we want to strip that to only include the struct name itself
    internal_type = internal_type.replace("struct ", "")
    struct_name = internal_type.rstrip("[]")
    return capitalize_first_letter_only(struct_name)


def get_struct_type(param_or_component: ABIComponent) -> str:
    """Returns the type of the given struct.

    This works the same as `get_struct_name`, except that we account for arrays by
    wrapping the name in `list[...]`.

    Parameters
    ----------
    param_or_component: ABIFunctionParams | ABIFunctionComponents

    Returns
    -------
    str
        The type of the item.
    """
    internal_type = cast(str, param_or_component.get("internalType", ""))
    # grab subtype if there is one
    if "." in internal_type:
        internal_type = internal_type.split(".")[1]
    # it is possible that the internal type has a "struct" label
    # we want to strip that to only include the struct name itself
    internal_type = internal_type.replace("struct ", "")
    if internal_type[-2:] == "[]":  # ends with [] indicates an array
        return "list[" + get_struct_name(param_or_component) + "]"
    return get_struct_name(param_or_component)


def get_struct_contract_name(param_or_component: ABIComponent) -> str:
    """Returns the contract name that the given struct is defined in.

    For example, a struct in an abi json will look like:

    {
    "components": [
      # components listed here
    ],
    "internalType": "struct ContractName.SimpleStruct",
    "name": "simpleStruct",
    "type": "tuple"
    }

    We are assuming 'internalType's value to have the form:
    'struct [ContractName].[StructName]'

    Parameters
    ----------
    param : ABIFunctionParams | ABIFunctionComponents


    Returns
    -------
    str
        The name of the item.
    """
    internal_type = cast(str, param_or_component.get("internalType", ""))
    contract_name_and_struct_name = internal_type.replace("struct ", "")
    contract_name = contract_name_and_struct_name.split(".")[0]
    return capitalize_first_letter_only(contract_name)


def get_param_name(
    param_or_component: ABIComponent,
) -> str:
    """Returns the name for a given ABIFunctionParams or ABIFunctionComponents.

    If the item is a struct, then we pull the name from the internalType attribute, otherwise we use
    the name if available.

    Parameters
    ----------
    param : ABIFunctionParams | ABIFunctionComponents

    Returns
    -------
    str
        The name of the item.
    """
    return param_or_component.get("name", "").lstrip("_").rstrip("[]")


@dataclass
class AbiInfo:
    """Information about an ABI"""

    abi: ABI
    bytecode: str
    contract_name: str
    # Bytecode link references is a dictionary keyed by a contract name,
    # valued with the hex code placeholder in the bytecode.
    bytecode_link_references: list[LinkReferences]


def load_abi_infos_from_file(file_path: Path) -> list[AbiInfo]:
    """Loads a contract ABI from a file.

    Parameters
    ----------
    file_path : Path
        The path to the ABI file.

    Returns
    -------
    tuple[ABI, str]
        ABI: An object containing the contract's abi.
        str: The bytecode.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        json_file = json.load(file)

        # solc jsons list all the contracts and their abis in one file, so we process it first.
        if is_solc_json(json_file):
            return _get_abis_from_solc_json(json_file)

        if is_hardhat_json(json_file):
            abi = get_abi_from_json(json_file)
            bytecode = get_bytecode_from_json(json_file)
            # hardhat jsons have the contract name as a field.
            contract_name = json_file.get("contractName")
            # TODO get bytecode link references and add here
            return [AbiInfo(abi=abi, bytecode=bytecode, contract_name=contract_name, bytecode_link_references=[])]

        if is_foundry_json(json_file):
            abi = get_abi_from_json(json_file)
            bytecode = get_bytecode_from_json(json_file)
            bytecode_link_references = get_bytecode_link_references_from_json(json_file)
            # foundry saves contracts to self-named files.
            contract_name = file_path.name.removesuffix(".json")
            return [
                AbiInfo(
                    abi=abi,
                    bytecode=bytecode,
                    contract_name=contract_name,
                    bytecode_link_references=bytecode_link_references,
                )
            ]

        raise ValueError("Unknown ABI Json format")


def get_abi_items(abi: ABI) -> list[ABIElement]:
    """Gets all of the functions and events in the ABI.

    Parameters
    ----------
    file_path : Path
        the file path to the ABI.

    Returns
    -------
    List[ABIElement]
        A list of all the ABI elements.
    """

    abi_functions_and_events = filter_abi_items_by_type(["function", "event"], abi)
    return abi_functions_and_events


def get_function_parameter_names(
    parameters: Sequence[ABIComponent],
) -> list[str]:
    """Parses a list of ABIComponent and returns a list of parameter
    names."""

    stringified_function_parameters: list[str] = []
    arg_counter: int = 1
    for _input in parameters:
        if name := get_param_name(_input):
            stringified_function_parameters.append(avoid_python_keywords(name))
        else:
            name = f"arg{arg_counter}"
            stringified_function_parameters.append(avoid_python_keywords(name))
        arg_counter += 1
    return stringified_function_parameters


def get_input_names(function: ABIFunction) -> list[str]:
    """Returns function input name strings for jinja templating.

    i.e. for the solidity function signature:
    function doThing(address who, uint256 amount, bool flag, bytes extraData)

    the following list would be returned:
    ['who', 'amount', 'flag', 'extraData']

    Parameters
    ----------
    function : ABIFunction
        A web3 dict of an ABI function description.

    Returns
    -------
    list[str]
        A list of function names i.e. ['arg1', 'arg2']
    """
    return get_function_parameter_names(function.get("inputs", []))


def get_output_names(function: ABIFunction) -> list[str]:
    """Returns function output name strings for jinja templating.

    i.e. for the solidity function signature: function doThing() returns (address who, uint256
    amount, bool flag, bytes extraData)

    the following list would be returned: ['who', 'amount', 'flag', 'extraData']

    Parameters
    ----------
    function : ABIFunction
        A web3 dict of an ABI function description.

    Returns
    -------
    list[str]
        A list of function names i.e. [{name: 'arg1', type: 'int'}, { name: 'TransferInfo',
        components: [{
            name: 'from', type: 'str'}, name: '
        }]]
    """
    return get_function_parameter_names(function.get("outputs", []))


def get_input_names_and_types(function: ABIFunction) -> list[str]:
    """Returns function input name/type strings for jinja templating.

    i.e. for the solidity function signature: function doThing(address who, uint256 amount, bool
    flag, bytes extraData)

    the following list would be returned: ['who: str', 'amount: int', 'flag: bool', 'extraData:
    bytes']

    Parameters
    ----------
    function : ABIFunction
        A web3 dict of an ABI function description.

    Returns
    -------
    list[str]
        A list of function names and corresponding python types, i.e. ['arg1: str', 'arg2: bool']
    """
    return _get_names_and_types(function, "inputs")


def get_input_types(function: ABIFunction) -> list[str]:
    """Returns function input type strings for jinja templating.

    i.e. for the solidity function signature: function doThing(address who, uint256 amount, bool
    flag, bytes extraData)

    the following list would be returned: ['str', 'int', 'bool', 'bytes']

    Parameters
    ----------
    function : ABIFunction
        A web3 dict of an ABI function description.

    Returns
    -------
    list[str]
        A list of function python types, i.e. ['str', 'bool']
    """
    return _get_param_types(function, "inputs")


def get_output_types(function: ABIFunction) -> list[str]:
    """Returns function output type strings for jinja templating.

    i.e. for the solidity function signature: function doThing(address who, uint256 amount, bool
    flag, bytes extraData)

    the following list would be returned: ['str', 'int', 'bool', 'bytes']

    Parameters
    ----------
    function : ABIFunction
        A web3 dict of an ABI function description.

    Returns
    -------
    list[str]
        A list of function python types, i.e. ['str', 'bool']
    """
    return _get_param_types(function, "outputs")


def get_output_names_and_types(function: ABIFunction) -> list[str]:
    """Returns function input name/type strings for jinja templating.

    i.e. for the solidity function signature: function doThing(address who, uint256 amount, bool
    flag, bytes extraData)

    the following list would be returned: ['who: str', 'amount: int', 'flag: bool', 'extraData:
    bytes']

    Parameters
    ----------
    function : ABIFunction
        A web3 dict of an ABI function description.

    Returns
    -------
    list[str]
        A list of function names and corresponding python types, i.e. ['arg1: str', 'arg2: bool']
    """
    return _get_names_and_types(function, "outputs")


def _get_names_and_types(function: ABIFunction, parameters_type: Literal["inputs", "outputs"]) -> list[str]:
    """Returns function input or output name/type strings for jinja templating.

    i.e. for the solidity function signature: function doThing(address who, uint256 amount, bool
    flag, bytes extraData)

    the following list would be returned: ['who: str', 'amount: int', 'flag: bool', 'extraData:
    bytes']

    Parameters
    ----------
    function : ABIFunction
        A web3 dict of an ABI function description.
    parameters_type : Literal["inputs", "outputs"]
        If we are looking at the inputs or outputs of a function.

    Returns
    -------
    list[str]
        A list of function names and corresponding python types, i.e. ['arg1: str', 'arg2: bool']
    """
    stringified_function_parameters: list[str] = []
    for index, param in enumerate(function.get(parameters_type, []), start=1):
        name = get_param_name(param)
        if not name:
            name = f"arg{index}"
        python_type = get_param_type(param)
        stringified_function_parameters.append(f"{avoid_python_keywords(name)}: {python_type}")
    return stringified_function_parameters


def _get_param_types(function: ABIFunction, parameters_type: Literal["inputs", "outputs"]) -> list[str]:
    """Returns function input or output type strings for jinja templating.

    i.e. for the solidity function signature: function doThing(address who, uint256 amount, bool
    flag, bytes extraData)

    the following list would be returned: ['who: str', 'amount: int', 'flag: bool', 'extraData:
    bytes']

    Parameters
    ----------
    function : ABIFunction
        A web3 dict of an ABI function description.
    parameters_type : Literal["inputs", "outputs"]
        If we are looking at the inputs or outputs of a function.

    Returns
    -------
    list[str]
        A list of function parameter python types, i.e. ['str', 'bool']
    """
    stringified_function_parameters: list[str] = []
    inputs_or_outputs = function.get(parameters_type, [])
    inputs_or_outputs = cast(list[ABIComponent], inputs_or_outputs)

    for param in inputs_or_outputs:
        python_type = get_param_type(param)
        stringified_function_parameters.append(f"{python_type}")
    return stringified_function_parameters


def get_param_type(param: ABIComponent):
    """Gets the associated python type, including generated dataclasses"""
    internal_type = cast(str, param.get("internalType", ""))
    # if we find a struct, we'll add it to the dict of StructInfo's
    if is_struct(internal_type):
        python_type = get_struct_type(param)
    else:
        python_type = solidity_to_python_type(param.get("type", "unknown"))
    return python_type


def get_abi_from_json(json_abi: FoundryJson | HardhatJson | ABI) -> ABI:
    """Gets the ABI from a supported json format.
    Note that solc is not included here because it can have multiple contracts per json."""
    if is_foundry_json(json_abi):
        return _get_abi_from_foundry_json(json_abi)
    if is_hardhat_json(json_abi):
        return _get_abi_from_hardhat_json(json_abi)
    if is_abi(json_abi):
        return json_abi

    raise ValueError("Unable to identify an ABI for the given JSON.")


def is_abi(maybe_abi: object) -> TypeGuard[ABI]:
    """Typeguard for ABI's"""
    if not isinstance(json, list):
        return False  # ABI should be a list

    # Check if there's at least one entry with 'name', 'inputs', and 'type'
    for entry in maybe_abi:  # type: ignore
        if isinstance(entry, dict) and {"name", "inputs", "type"}.issubset(entry.keys()):
            return True

    return False  # No entry with the required fields was found


def _get_abi_from_foundry_json(json_abi: FoundryJson) -> ABI:
    return json_abi.get("abi")


def _get_abi_from_hardhat_json(json_abi: HardhatJson) -> ABI:
    return json_abi.get("abi")


def _get_abis_from_solc_json(json_abi: SolcJson) -> list[AbiInfo]:
    contracts = json_abi.get("contracts")
    infos: list[AbiInfo] = []

    for key, value in contracts.items():
        contract_name = key.split(":")[1]
        abi = value.get("abi")
        binary = value.get("bin")
        bytecode = f"0x{binary}"
        # TODO get bytecode link references and add here
        infos.append(AbiInfo(abi=abi, contract_name=contract_name, bytecode=bytecode, bytecode_link_references=[]))

    return infos
