"""Functions to render Python files from an abi usng a jinja2 template."""

from pathlib import Path

from jinja2 import Template

from pypechain.utilities.abi import (
    get_abi_items,
    get_input_names,
    get_input_names_and_values,
    get_output_names,
    is_abi_constructor,
    is_abi_function,
)
from pypechain.utilities.format import capitalize_first_letter_only
from pypechain.utilities.sort import get_intersection_and_unique


def render_contract_file(
    contract_name: str, contract_template: Template, abi_file_path: Path
) -> str:
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

    # TODO:  return types to function calls
    # Extract function names and their input parameters from the ABI
    function_datas = {}
    constructor_data = {}
    for abi_function in get_abi_items(abi_file_path):
        if is_abi_function(abi_function):
            # TODO: investigate better typing here?  templete.render expects an object so we'll have
            # to convert.

            # hanndle constructor
            if is_abi_constructor(abi_function):
                constructor_data = {
                    "input_names_and_types": [get_input_names_and_values(abi_function)],
                    "input_names": [get_input_names(abi_function)],
                    "outputs": [get_output_names(abi_function)],
                }

            # handle functions
            else:
                name = abi_function.get("name", "")
                if name and name not in function_datas:
                    function_data = {
                        # TODO: pass a typeguarded ABIFunction that has only required fields?
                        # name is required in the typeguard.  Should be safe to default to empty string.
                        "name": name,
                        "capitalized_name": capitalize_first_letter_only(name),
                        "input_names_and_types": [
                            get_input_names_and_values(abi_function)
                        ],
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
                    function_datas[name]["outputs"].append(
                        get_output_names(abi_function)
                    )
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
                    (
                        shared_input_names,
                        unique_input_names,
                    ) = get_intersection_and_unique(function_datas[name]["input_names"])
                    function_datas[name]["required_input_names"] = shared_input_names
                    function_datas[name]["optional_input_names"] = unique_input_names

    # Render the template
    return contract_template.render(
        contract_name=contract_name,
        functions=list(function_datas.values()),
        # TODO: use this data to add a typed constructor
        constructor=constructor_data,
    )
