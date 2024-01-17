"""Utilities to help with Solidity types."""


import logging
from typing import TypedDict


class SignatureData(TypedDict):
    """Define the structure of the signature_datas dictionary"""

    input_names_and_types: list[str]
    input_names: list[str]
    input_types: list[str]
    outputs: list[str]
    output_types: list[str]


class FunctionData(TypedDict):
    """Define the structure of the function_data dictionary"""

    name: str
    capitalized_name: str
    signature_datas: list[SignatureData]
    has_overloading: bool
    has_multiple_return_signatures: bool
    has_multiple_return_values: bool


class EventData(TypedDict):
    """Define the structure of the event_data dictionary"""

    name: str
    capitalized_name: str


def solidity_to_python_type(solidity_type: str) -> str:
    """Returns the stringfied python type for the gien solidity type.

    Arguments
    ---------
    solidity_type : str
        A solidity variable type string, i.e. 'uint8'...'uint256', 'bool', 'address',
        'bytes2'...'bytes32' etc.

    Returns
    -------
        A python variable type string, i.e. 'int', 'bool', 'address'
    """
    # TODO: use an exhaustive match statement to cover all cases.
    # pylint: disable=too-many-return-statements

    # uints and ints

    if solidity_type in [
        "uint8",
        "uint16",
        "uint24",
        "uint32",
        "uint40",
        "uint48",
        "uint56",
        "uint64",
        "uint72",
        "uint80",
        "uint88",
        "uint96",
        "uint104",
        "uint112",
        "uint120",
        "uint128",
        "uint136",
        "uint144",
        "uint152",
        "uint160",
        "uint168",
        "uint176",
        "uint184",
        "uint192",
        "uint200",
        "uint208",
        "uint216",
        "uint232",
        "uint240",
        "uint248",
        "uint256",
        "int8",
        "int16",
        "int24",
        "int32",
        "int40",
        "int48",
        "int56",
        "int64",
        "int72",
        "int80",
        "int88",
        "int96",
        "int104",
        "int112",
        "int120",
        "int128",
        "int136",
        "int144",
        "int152",
        "int160",
        "int168",
        "int176",
        "int184",
        "int192",
        "int200",
        "int208",
        "int216",
        "int224",
        "int232",
        "int240",
        "int248",
        "int256",
    ]:
        return "int"
    # Fixed-size arrays of uints and ints
    if any(solidity_type.startswith(x) for x in ["uint", "int"]) and solidity_type.endswith("]"):
        # TODO: use a package like 'array' or 'numpy' to provide fixed arrays.
        # Extract the size of the array, e.g., "uint8[3]" -> 3
        # size = int(solidity_type.split("[")[-1].split("]")[0])
        # Return a list of 'int' of the given size
        return "list[int]"

    # addresses
    if solidity_type == "address":
        return "str"
    if solidity_type == "address[]":
        return "list[str]"

    # bools
    if solidity_type == "bool":
        return "bool"
    if solidity_type == "bool[]":
        return "list[bool]"

    # bytes
    # for bytes1[], bytes2[],...,bytes32[]
    if solidity_type == "bytes":
        return "bytes"
        # TODO this should actually be a BytesLike string or something.
    if solidity_type.startswith("bytes") and solidity_type.endswith("]"):
        return "list[bytes]"
    # for bytes1, bytes2,...,bytes32
    if solidity_type.startswith("bytes"):
        return "bytes"

    # strings
    if solidity_type == "string":
        return "str"
    if solidity_type == "string[]":
        return "list[str]"

    # tuple
    if solidity_type == "tuple":
        return "tuple"

    # If the Solidity type isn't recognized, make a warning.  This can happen when an internal type
    # is expeected for an input parameter or returned in an output.
    logging.warning("Unknown Solidity type: %s", solidity_type)

    return solidity_type


def gather_matching_types(function_datas: list[FunctionData], known_types: list[str]) -> list[str]:
    """Gather matching types from inputs and outputs in the function_datas.

    Parameters
    ----------
    function_datas : list[FunctionData]
        A list of function datas.
    known_types : list[str]
        A list of known types.

    Returns
    -------
    list[str]
        The matching list of types.
    """
    matching_types = []

    for function_data in function_datas:
        for signature_data in function_data["signature_datas"]:
            # Check input types
            for input_type in signature_data["input_types"]:
                if input_type in known_types:
                    matching_types.append(input_type)

            # Check output types
            for output_type in signature_data["output_types"]:
                if output_type in known_types:
                    matching_types.append(output_type)

    return list(set(matching_types))
