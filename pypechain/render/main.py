"""Functions to render Python files from an abi usng a jinja2 template."""

from __future__ import annotations

import os
from pathlib import Path

from pypechain.render.contract import ContractInfosByName, render_contract_file
from pypechain.render.types import render_types_file
from pypechain.utilities.abi import AbiInfo, get_events_for_abi, get_structs_for_abi
from pypechain.utilities.file import write_string_to_file
from pypechain.utilities.format import format_file


def render_files(abi_infos: list[AbiInfo], output_dir: str, line_length: int = 120) -> list[str]:
    """Processes a single JSON file to generate class and types files."""

    # This helps us organize structs and events by the contracts they are defined in.
    # Because structs can be defined in one file, and used in another, we need to avoid duplication
    # of the definitions.
    contract_infos = ContractInfosByName()

    # Populate contract_infos with all the structs, events, whole ABIs, bytecodes and contract names.
    for abi_info in abi_infos:
        structs = get_structs_for_abi(abi_info.abi)
        events = get_events_for_abi(abi_info.abi)
        contract_infos.add_structs(structs)
        contract_infos.add_events(events, abi_info.contract_name)
        contract_infos.add_abi_info(abi_info, abi_info.contract_name)

    # This is what we return.
    file_names: list[str] = []

    # Now, for every [ContractName]
    # generate a:
    #    1. [ContractName]Contract.py
    #    2. [ContractName]Types.py
    #  The Contract file defines the Contract class and functions.
    #  The Types file has the structs and events defined in the solidity contract.
    for contract_info in contract_infos.values():
        rendered_contract_code = render_contract_file(contract_info)

        file_path = Path(output_dir)
        contract_file_name = contract_info.contract_name + "Contract.py"
        contract_file_path = Path(os.path.join(file_path, contract_file_name))
        write_string_to_file(contract_file_path, rendered_contract_code)
        format_file(contract_file_path, line_length)
        file_names.append(f"{contract_info.contract_name}Contract")

        rendered_types_code = render_types_file(contract_info)
        if rendered_types_code:
            types_file_name = contract_info.contract_name + "Types.py"
            types_file_path = Path(os.path.join(file_path, types_file_name))
            write_string_to_file(types_file_path, rendered_types_code)
            format_file(types_file_path, line_length)
            file_names.append(f"{contract_info.contract_name}Types")

    return file_names

    # try:
    #     # render files from a json
    # except NoABIFunctionsFound:
    #     # TODO: use logging
    #     print(f"No ABI Functions found in {json_file}, skipping...")
    # except BaseException as err:
    #     print(f"Error creating types for {json_file}")
    #     raise err
