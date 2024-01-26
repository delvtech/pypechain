"""Utilities for templating."""

import os

from jinja2 import Environment, FileSystemLoader


def get_jinja_env() -> Environment:
    """Returns the jinja environment."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to your templates directory.
    templates_dir = os.path.join(script_dir, "../templates")
    env = Environment(loader=FileSystemLoader(templates_dir))
    env.filters["wrap_with_dataclass_to_tuple"] = wrap_with_dataclass_to_tuple

    return env


def wrap_with_dataclass_to_tuple(items: list[str]) -> list[str]:
    """Wraps a string with with the tuple_to_dataclass function.

    Parameters
    ----------
    items: list[str]
        a list of variables to wrap with the function `dataclass_to_tuple`

    Returns
    -------
    list[str]
        A list of wrapped strings.
    """
    return [f"dataclass_to_tuple({item})" for item in items]
