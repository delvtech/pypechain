"""Script to generate typed web3.py classes for solidity contracts."""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from dataclasses import asdict
from pathlib import Path
from typing import NamedTuple, Sequence

from jinja2 import Template
from web3.types import ABIFunction, ABIFunctionComponents, ABIFunctionParams

from pypechain.utilities.abi import (
    get_abi_items,
    get_events_for_abi,
    get_param_name,
    get_structs_for_abi,
    is_abi_function,
    load_abi_from_file,
)
from pypechain.utilities.file import write_string_to_file
from pypechain.utilities.format import (
    apply_black_formatting,
    avoid_python_keywords,
    capitalize_first_letter_only,
)
from pypechain.utilities.sort import get_intersection_and_unique
from pypechain.utilities.templates import setup_templates
from pypechain.utilities.types import solidity_to_python_type


def setup_directory(directory: str) -> None:
    """Set up the output directory. If it exists, clear it. Otherwise, create it."""

    # If the directory exists, remove it
    if os.path.exists(directory):
        shutil.rmtree(directory)

    # Create the directory
    os.makedirs(directory)


class Args(NamedTuple):
    """Command line arguments for pypechain."""

    abi_file_path: str
    output_dir: str
    line_length: int


def namespace_to_args(namespace: argparse.Namespace) -> Args:
    """Converts argprase.Namespace to Args."""
    return Args(
        abi_file_path=namespace.abi_file_path,
        output_dir=namespace.output_dir,
        line_length=namespace.line_length,
    )


def main() -> None:
    """Generates class files for a given abi.

    Arguments
    ---------
    abi_file_path : str
        Path to the abi JSON file.
    output_dr: str
        Path to the directory where files will be generated.
    line_length : int
        Optional argument for the output file's maximum line length. Defaults to 80.
    """
    parser = argparse.ArgumentParser(
        description="Generates class files for a given abi."
    )
    parser.add_argument(
        "abi_file_path",
        help="Path to the abi JSON file or directory containing multiple JSON files.",
    )

    parser.add_argument(
        "--output_dir",
        default="pypechain_types",
        help="Path to the directory where files will be generated. Defaults to pypechain_types.",
    )
    parser.add_argument(
        "--line_length",
        type=int,
        default=80,
        help="Optional argument for the output file's maximum line length. Defaults to 80.",
    )

    # If no arguments were passed, display the help message and exit
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args: Args = namespace_to_args(parser.parse_args())
    abi_file_path, output_dir, line_length = args

    # Set up the output directory
    setup_directory(output_dir)

    # Check if provided path is a directory or file
    if os.path.isdir(abi_file_path):
        # If directory, process all JSON files in the directory
        for json_file in Path(abi_file_path).glob("*.json"):
            process_file(str(json_file), output_dir, line_length)
    else:
        # Otherwise, process the single file
        process_file(abi_file_path, output_dir, line_length)


def process_file(abi_file_path: str, output_dir: str, line_length: int) -> None:
    """Processes a single JSON file to generate class files."""

    # get names
    file_path = Path(abi_file_path)
    output_path = Path(output_dir)
    filename = file_path.name
    contract_name = os.path.splitext(filename)[0]
    contract_path = output_path.joinpath(f"{contract_name}")

    # grab the templates
    contract_template, types_template = setup_templates()

    # render the code
    rendered_contract_code = render_contract_file(
        contract_name, contract_template, file_path
    )
    rendered_types_code = render_types_file(contract_name, types_template, file_path)

    # Format the generated code using Black
    formatted_contract_code = apply_black_formatting(
        rendered_contract_code, line_length
    )
    formatted_types_code = apply_black_formatting(rendered_types_code, line_length)

    # Write the code to file
    write_string_to_file(f"{contract_path}Contract.py", formatted_contract_code)
    write_string_to_file(f"{contract_path}Types.py", formatted_types_code)


def render_contract_file(
    contract_name: str, contract_template: Template, abi_file_path: Path
) -> str:
    """Returns a string of the contract file to be generated.

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

    # TODO:  return types to function calls
    # Extract function names and their input parameters from the ABI
    function_datas = {}
    for abi_function in get_abi_items(abi_file_path):
        if is_abi_function(abi_function):
            # TODO: investigate better typing here?  templete.render expects an object so we'll have to convert.
            name = abi_function.get("name", "")
            if name not in function_datas:
                function_data = {
                    # TODO: pass a typeguarded ABIFunction that has only required fields?
                    # name is required in the typeguard.  Should be safe to default to empty string.
                    "name": name,
                    "capitalized_name": capitalize_first_letter_only(name),
                    "input_names_and_types": [get_input_names_and_values(abi_function)],
                    "input_names": [get_input_names(abi_function)],
                    "outputs": [get_output_names(abi_function)],
                }
                function_datas[name] = function_data
            else:  # this function already exists, presumably with a different signature
                function_datas[name]["input_names_and_types"].append(
                    get_input_names_and_values(abi_function)
                )
                function_datas[name]["input_names"].append(
                    get_input_names(abi_function)
                )
                function_datas[name]["outputs"].append(get_output_names(abi_function))
                # input_names_and_types will need optional args at the end
                (
                    shared_input_names_and_types,
                    unique_input_names_and_types,
                ) = get_intersection_and_unique(
                    function_datas[name]["input_names_and_types"]
                )
                function_datas[name][
                    "required_input_names_and_types"
                ] = shared_input_names_and_types
                function_datas[name]["optional_input_names_and_types"] = []
                for name_and_type in unique_input_names_and_types:  # optional args
                    name_and_type += " | None = None"
                    function_datas[name]["optional_input_names_and_types"].append(
                        name_and_type
                    )
                # we will also need the names to be separated
                shared_input_names, unique_input_names = get_intersection_and_unique(
                    function_datas[name]["input_names"]
                )
                function_datas[name]["required_input_names"] = shared_input_names
                function_datas[name]["optional_input_names"] = unique_input_names
    # Render the template
    return contract_template.render(
        contract_name=contract_name, functions=list(function_datas.values())
    )


def render_types_file(
    contract_name: str, types_template: Template, abi_file_path: Path
) -> str:
    """Returns a string of the types file to be generated.

    Arguments
    ---------
    contract_name : str
        The name of the contract to be parsed.
    types_template : Template
        A jinja template containging types for all structs within an abi.
    abi_file_path : Path
        The path to the abi file to parse.

    Returns
    -------
    str
        A serialized python file.
    """

    abi = load_abi_from_file(abi_file_path)

    structs_by_name = get_structs_for_abi(abi)
    structs_list = list(structs_by_name.values())
    structs = [asdict(struct) for struct in structs_list]
    events = [asdict(event) for event in get_events_for_abi(abi)]
    has_events = bool(events)
    has_event_params = any(len(event["inputs"]) > 0 for event in events)

    return types_template.render(
        contract_name=contract_name,
        structs=structs,
        events=events,
        has_events=has_events,
        has_event_params=has_event_params,
    )


def get_input_names_and_values(function: ABIFunction) -> list[str]:
    """Returns function input name/type strings for jinja templating.

    i.e. for the solidity function signature: function doThing(address who, uint256 amount, bool
    flag, bytes extraData)

    the following list would be returned: ['who: str', 'amount: int', 'flag: bool', 'extraData:
    bytes']

    Arguments
    ---------
    function : ABIFunction
        A web3 dict of an ABI function description.

    Returns
    -------
    list[str]
        A list of function names and corresponding python values, i.e. ['arg1: str', 'arg2: bool']
    """
    stringified_function_parameters: list[str] = []
    for _input in function.get("inputs", []):
        if name := get_param_name(_input):
            python_type = solidity_to_python_type(_input.get("type", "unknown"))
        else:
            raise ValueError("Solidity function parameter name cannot be None")
        stringified_function_parameters.append(
            f"{avoid_python_keywords(name)}: {python_type}"
        )
    return stringified_function_parameters


def get_function_parameter_names(
    parameters: Sequence[ABIFunctionParams | ABIFunctionComponents],
) -> list[str]:
    """Parses a list of ABIFunctionParams or ABIFUnctionComponents and returns a list of parameter
    names."""

    stringified_function_parameters: list[str] = []
    arg_counter: int = 1
    for _input in parameters:
        if name := get_param_name(_input):
            stringified_function_parameters.append(avoid_python_keywords(name))
        else:
            name = f"arg{arg_counter}"
            arg_counter += 1
    return stringified_function_parameters


def get_input_names(function: ABIFunction) -> list[str]:
    """Returns function input name strings for jinja templating.

    i.e. for the solidity function signature:
    function doThing(address who, uint256 amount, bool flag, bytes extraData)

    the following list would be returned:
    ['who', 'amount', 'flag', 'extraData']

    Arguments
    ---------
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

    Arguments
    ---------
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


if __name__ == "__main__":
    main()
