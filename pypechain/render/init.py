"""Functions to render __init__.py from a list of filenames usng a jinja2 template."""
from pypechain.utilities.file import write_string_to_file
from pypechain.utilities.format import apply_black_formatting
from pypechain.utilities.templates import get_jinja_env


def render_init_file(output_dir: str, file_names: list[str], line_length):
    """Creates an __init__.py file that imports all other files."""
    env = get_jinja_env()
    init_template = env.get_template("init.py.jinja2")
    init_code = init_template.render(file_names=file_names)
    formatted_init_code = apply_black_formatting(init_code, line_length)
    write_string_to_file(f"{output_dir}/__init__.py", formatted_init_code)
