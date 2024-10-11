"""Functions to render __init__.py from a list of filenames usng a jinja2 template."""

import importlib.metadata
from pathlib import Path

from pypechain.utilities.file import write_string_to_file
from pypechain.utilities.templates import get_jinja_env
from pypechain.utilities.types import RenderOutput


def render_init_file(output_dir: Path, file_outputs: list[RenderOutput]):
    """Creates an __init__.py file that imports all other files."""
    env = get_jinja_env()
    init_template = env.get_template("init.py.jinja2")
    init_code = init_template.render(
        pypechain_version=importlib.metadata.version("pypechain"),
        file_outputs=file_outputs,
    )
    init_file_path = Path(f"{output_dir}/__init__.py")
    write_string_to_file(init_file_path, init_code)
