"""Formatting utilities."""

import json
import keyword
import os
import subprocess
from pathlib import Path

import isort


def avoid_python_keywords(name: str) -> str:
    """Make sure the variable name is not a reserved Python word.  If it is, prepend with an
    underscore.

    Parameters
    ----------
    name : str
       unsafe variable name.

    Returns
    -------
    str
        A string prepended with an underscore if it was a python reserved word.
    """
    if keyword.iskeyword(name) or keyword.issoftkeyword(name) or isbuiltin(name):
        return "_" + name

    return name


builtin_function_names = [
    "abs",
    "aiter",
    "all",
    "any",
    "ascii",
    "bin",
    "bool",
    "breakpoint",
    "bytearray",
    "bytes",
    "callable",
    "chr",
    "classmethod",
    "compile",
    "complex",
    "delattr",
    "dict",
    "dir",
    "divmod",
    "enumerate",
    "eval",
    "exec",
    "filter",
    "float",
    "format",
    "frozenset",
    "getattr",
    "globals",
    "hasattr",
    "hash",
    "help",
    "hex",
    "id",
    "input",
    "int",
    "isinstance",
    "issubclass",
    "iter",
    "len",
    "list",
    "locals",
    "map",
    "max",
    "min",
    "next",
    "object",
    "oct",
    "open",
    "ord",
    "pow",
    "print",
    "property",
    "repr",
    "reversed",
    "round",
    "set",
    "setattr",
    "slice",
    "sorted",
    "staticmethod",
    "str",
    "sum",
    "super",
    "tuple",
    "type",
    "vars",
    "zip",
    "import",
]

isbuiltin = frozenset(builtin_function_names).__contains__


def capitalize_first_letter_only(string: str) -> str:
    """Capitalizes the first letter of a string without affecting the rest of the string.
    capitalize() will lowercase the rest of the letters."""

    if len(string) < 2:
        return string
    return string[0].upper() + string[1:]


def format_file(file_path: Path, line_length: int = 120, quiet=True, remove_unused_imports=True) -> None:
    """Formats a file with isort and black.

    Parameters
    ----------
    file_path : Path
        The file to be formatted.
    line_length : int, optional
        Black's line-length config option.
    """

    quiet_flag = "--quiet" if quiet else ""
    if remove_unused_imports:
        subprocess.run(
            f"autoflake --in-place {quiet_flag} --remove-all-unused-imports {file_path}", shell=True, check=True
        )
    isort.file(file_path, config=isort.Config(quiet=quiet))
    subprocess.run(f"black {quiet_flag} --line-length={line_length} {file_path}", shell=True, check=True)


def format_json_dir(json_dir):
    """Recursively format json files under a directory."""
    for root, dirs, files in os.walk(json_dir):
        # Format any outer json files
        for file in files:
            if file.endswith(".json"):
                json_file = os.path.join(root, file)
                # Format the JSON file
                with open(json_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                with open(json_file, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=2)

        for d in dirs:
            format_json_dir(d)
