"""Formatting utilities."""
import keyword
import re

import black


def avoid_python_keywords(name: str) -> str:
    """Make sure the variable name is not a reserved Python word.  If it is, prepend with an
    underscore.

    Arguments
    ---------
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


def apply_black_formatting(code: str, line_length: int) -> str:
    """Formats a code string with Black on default settings.

    Arguments
    ---------
    code : str
        A string containing Python code
    line_length : int
        Output file's maximum line length.

    Returns
    -------
    str
        A string containing the Black-formatted code
    """
    # remove extra newlines and let Black sort it out
    formatted_code = re.sub(r"^[\s\t]*\n\n", "\n", code, flags=re.MULTILINE)
    formatted_code = code.replace(", )", ")")  # remove trailing comma
    try:
        return black.format_file_contents(
            formatted_code, fast=False, mode=black.Mode(line_length=line_length)
        )
    except ValueError as exc:
        raise ValueError(f"cannot format with Black\n code:\n{code}") from exc
