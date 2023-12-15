"""Functions to render Python files from an abi usng a jinja2 template."""

import os
from pathlib import Path

from pypechain.render.contract import render_contract_file
from pypechain.render.types import render_types_file
from pypechain.utilities.file import write_string_to_file
from pypechain.utilities.format import format_file


def render_files(abi_file_path: str, output_dir: str, line_length: int = 120) -> list[str]:
    """Processes a single JSON file to generate class and types files."""

    # get names
    file_path = Path(abi_file_path)
    output_path = Path(output_dir)
    filename = file_path.name
    contract_name = os.path.splitext(filename)[0].replace("-", "")
    contract_path = output_path.joinpath(f"{contract_name}")

    # render the code for each file
    rendered_contract_code = render_contract_file(contract_name, file_path)
    rendered_types_code = render_types_file(contract_name, file_path)

    # keep track of file names to return
    file_names: list[str] = []

    contract_file_path = Path(f"{contract_path}Contract.py")
    write_string_to_file(contract_file_path, rendered_contract_code)
    format_file(contract_file_path, line_length)
    file_names.append(f"{contract_name}Contract")

    if rendered_types_code:
        types_file_path = Path(f"{contract_path}Types.py")
        write_string_to_file(types_file_path, rendered_types_code)
        format_file(types_file_path, line_length)
        file_names.append(f"{contract_name}Types")

    return file_names
