"""Formatting utilities."""

import keyword
import re
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


def camel_to_snake(camel_string: str) -> str:
    """Convert camel case string to snake case string.

    NOTE this takes care of strings containing multiple capital letters in a row.
    Examples:
    camel_to_snake("myLibrary")
    >>> "my_library"
    camel_to_snake("MyLibrary")
    >>> "my_library"
    camel_to_snake("LPMath")
    >>> "lp_math"


    Arguments
    ---------
    camel_string: str
        The string to convert.

    Returns
    -------
    str
        The snake case string.
    """
    return re.sub("((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))", r"_\1", camel_string).lower()


def format_file(file_path: Path, line_length: int = 120, quiet=True) -> None:
    """Formats a file with isort and black.

    Parameters
    ----------
    file_path : Path
        The file to be formatted.
    line_length : int, optional
        Black's line-length config option.
    """

    quiet_flag = "--quiet" if quiet else ""
    subprocess.run(f"autoflake --in-place {quiet_flag} --remove-all-unused-imports {file_path}", shell=True, check=True)
    isort.file(file_path, config=isort.Config(quiet=quiet))
    subprocess.run(f"black {quiet_flag} --line-length={line_length} {file_path}", shell=True, check=True)
