"""Functions to render Python files from an abi usng a jinja2 template."""

import os
import subprocess
from pathlib import Path

from pypechain.render.contract import render_contract_file
from pypechain.render.types import render_types_file
from pypechain.utilities.file import write_string_to_file
from pypechain.utilities.format import apply_black_formatting


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
    format_file(contract_file_path)
    file_names.append(f"{contract_name}Contract")

    # TODO: write tests for this conditional write.
    if rendered_types_code:
        types_file_path = Path(f"{contract_path}Types.py")
        formatted_types_code = apply_black_formatting(rendered_types_code, line_length)
        write_string_to_file(types_file_path, formatted_types_code)
        format_file(types_file_path)
        file_names.append(f"{contract_name}Types")

    return file_names


def format_file(file_path: Path, line_length: int = 120) -> None:
    """Formats a file with isort and black.

    Parameters
    ----------
    file_path : Path
        The file to be formatted.
    line_length : int, optional
        Black's line-length config option.
    """

    subprocess.run(f"isort {file_path}", shell=True, check=True)
    subprocess.run(f"black --line-length={line_length} {file_path}", shell=True, check=True)
