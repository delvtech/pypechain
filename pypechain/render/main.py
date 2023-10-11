"""Functions to render Python files from an abi usng a jinja2 template."""

import os
from pathlib import Path

from pypechain.render.contract import render_contract_file
from pypechain.render.types import render_types_file
from pypechain.utilities.file import write_string_to_file
from pypechain.utilities.format import apply_black_formatting
from pypechain.utilities.templates import setup_templates


def render_files(abi_file_path: str, output_dir: str, line_length: int) -> None:
    """Processes a single JSON file to generate class and types files."""

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
