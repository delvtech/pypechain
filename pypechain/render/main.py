"""Functions to render Python files from an abi usng a jinja2 template."""

from __future__ import annotations

import os
from pathlib import Path

from pypechain.render.contract import get_contract_infos, render_contract_file
from pypechain.render.types import render_types_file
from pypechain.utilities.abi import AbiInfo
from pypechain.utilities.file import write_string_to_file
from pypechain.utilities.format import format_file


def render_files(
    abi_infos: list[AbiInfo], output_dir: str, line_length: int = 120, apply_formatting: bool = True
) -> list[str]:
    """Processes a single JSON file to generate class and types files.


    Parameters
    ----------
    abi_infos : list[AbiInfo]
        A list of objects containing each ABI and metadata.
    output_dir : str
        The directory where files will be written to.
    line_length : int, optional
        Black's line-length config option.
    apply_formatting : bool, optional
        If True, autoflake, isort and black will be applied to the file in that order, by default True.

    Returns
    -------
    list[str]
        A list of filenames for the generated files.
    """

    contract_infos = get_contract_infos(abi_infos)

    # This is what we return.
    file_names: list[str] = []

    # Now, for every [ContractName]
    # generate a:
    #    1. [ContractName]Contract.py
    #    2. [ContractName]Types.py
    #  The Contract file defines the Contract class and functions.
    #  The Types file has the structs and events defined in the solidity contract.
    for contract_info in contract_infos.values():
        file_path = Path(output_dir)

        rendered_contract_code = render_contract_file(contract_info)
        if rendered_contract_code:
            contract_file_name = contract_info.contract_name + "Contract.py"
            contract_file_path = Path(os.path.join(file_path, contract_file_name))
            write_string_to_file(contract_file_path, rendered_contract_code)
            if apply_formatting is True:
                format_file(contract_file_path, line_length)
            file_names.append(f"{contract_info.contract_name}Contract")

        rendered_types_code = render_types_file(contract_info)
        if rendered_types_code:
            types_file_name = contract_info.contract_name + "Types.py"
            types_file_path = Path(os.path.join(file_path, types_file_name))
            write_string_to_file(types_file_path, rendered_types_code)
            if apply_formatting is True:
                format_file(types_file_path, line_length)
            file_names.append(f"{contract_info.contract_name}Types")

    return file_names
