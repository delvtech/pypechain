"""Functions to render Python files from an abi usng a jinja2 template."""
from __future__ import annotations

from pathlib import Path
from typing import TypedDict

from web3.types import ABI

from pypechain.utilities.abi import (
    get_abi_items,
    get_input_names,
    get_input_names_and_values,
    get_output_names,
    is_abi_constructor,
    is_abi_function,
    load_abi_from_file,
)
from pypechain.utilities.format import capitalize_first_letter_only
from pypechain.utilities.templates import get_jinja_env


class SignatureData(TypedDict):
    """Define the structure of the signature_datas dictionary"""

    input_names_and_types: list[str]
    input_names: list[str]
    outputs: list[str]


class FunctionData(TypedDict):
    """Define the structure of the function_data dictionary"""

    name: str
    capitalized_name: str
    signature_datas: list[SignatureData]


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
    env = get_jinja_env()
    base_template = env.get_template("contract.py/base.py.jinja2")
    functions_template = env.get_template("contract.py/functions.py.jinja2")
    abi_template = env.get_template("contract.py/abi.py.jinja2")
    contract_template = env.get_template("contract.py/contract.py.jinja2")

    # TODO: add return types to function calls

    abi = load_abi_from_file(abi_file_path)
    function_datas, constructor_data = get_function_datas(abi)
    has_overloading = any(len(function_data["signature_datas"]) > 1 for function_data in function_datas.values())

    functions_block = functions_template.render(
        abi=abi,
        contract_name=contract_name,
        functions=function_datas,
        # TODO: use this data to add a typed constructor
        constructor=constructor_data,
    )

    abi_block = abi_template.render(
        abi=abi,
        contract_name=contract_name,
    )

    contract_block = contract_template.render(
        contract_name=contract_name,
        functions=function_datas,
    )

    # Render the template
    return base_template.render(
        contract_name=contract_name,
        has_overloading=has_overloading,
        functions_block=functions_block,
        abi_block=abi_block,
        contract_block=contract_block,
        # TODO: use this data to add a typed constructor
        # constructor_data=constructor_data,
    )


def get_function_datas(abi: ABI) -> tuple[dict[str, FunctionData], SignatureData | None]:
    """_summary_

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
    function_datas: dict[str, FunctionData] = {}
    constructor_data: SignatureData | None = None
    for abi_function in get_abi_items(abi):
        if is_abi_function(abi_function):
            # TODO: investigate better typing here?  templete.render expects an object so we'll have
            # to convert.
            # hanndle constructor
            if is_abi_constructor(abi_function):
                constructor_data = {
                    "input_names_and_types": get_input_names_and_values(abi_function),
                    "input_names": get_input_names(abi_function),
                    "outputs": get_output_names(abi_function),
                }

            # handle all other functions
            else:
                name = abi_function.get("name", "")
                signature_data: SignatureData = {
                    "input_names_and_types": get_input_names_and_values(abi_function),
                    "input_names": get_input_names(abi_function),
                    "outputs": get_output_names(abi_function),
                }
                function_data: FunctionData = {
                    # TODO: pass a typeguarded ABIFunction that has only required fields?
                    # name is required in the typeguard.  Should be safe to default to empty string.
                    "name": name,
                    "capitalized_name": capitalize_first_letter_only(name),
                    "signature_datas": [signature_data],
                }
                if not function_datas.get(name):
                    function_datas[name] = function_data
                else:
                    function_datas[name]["signature_datas"].append(signature_data)
    return function_datas, constructor_data
