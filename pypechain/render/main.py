"""Functions to render Python files from an abi usng a jinja2 template."""

import os
from pathlib import Path

from pypechain.render.contract import render_contract_file
from pypechain.render.types import render_types_file
from pypechain.utilities.file import write_string_to_file
from pypechain.utilities.format import apply_black_formatting


def render_files(abi_file_path: str, output_dir: str, line_length: int) -> list[str]:
    """Processes a single JSON file to generate class and types files."""

    # get names
    file_path = Path(abi_file_path)
    output_path = Path(output_dir)
    filename = file_path.name
    contract_name = os.path.splitext(filename)[0]
    contract_path = output_path.joinpath(f"{contract_name}")

    # render the code
    rendered_contract_code = render_contract_file(contract_name, file_path)
    # TODO: if there are no types generated, then this should return None
    rendered_types_code = render_types_file(contract_name, file_path)

    file_names: list[str] = []
    # Format the generated code using Black and rite the code to file
    formatted_contract_code = apply_black_formatting(rendered_contract_code, line_length)
    write_string_to_file(f"{contract_path}Contract.py", formatted_contract_code)
    file_names.append(f"{contract_name}Contract")

    # TODO: write tests for this conditional write.
    if rendered_types_code:
        formatted_types_code = apply_black_formatting(rendered_types_code, line_length)
        write_string_to_file(f"{contract_path}Types.py", formatted_types_code)
        file_names.append(f"{contract_name}Types")

    return file_names
