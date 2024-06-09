"""Conversion helpers."""

from __future__ import annotations

from dataclasses import fields, is_dataclass
from typing import Any, Tuple, TypeVar, cast

T = TypeVar("T")


def tuple_to_dataclass(cls: type[T], tuple_data: Any | Tuple[Any, ...]) -> T:
    """
    Converts a tuple (including nested tuples) to a dataclass instance.  If cls is not a dataclass,
    then the data will just be passed through this function.

    Parameters
    ----------
    cls: type[T]
        The dataclass type to which the tuple data is to be converted.
    tuple_data: Any | Tuple[Any, ...]
        A tuple (or nested tuple) of values to convert into a dataclass instance.

    Returns
    -------
    T
        Either an instance of cls populated with data from tuple_data or tuple_data itself.
    """
    if not is_dataclass(cls):
        return cast(T, tuple_data)

    field_types = {field.name: field.type for field in fields(cls)}
    field_values = {}

    for (field_name, field_type), value in zip(field_types.items(), tuple_data):
        if is_dataclass(field_type):
            # Recursively convert nested tuples to nested dataclasses
            field_values[field_name] = tuple_to_dataclass(field_type, value)
        elif isinstance(value, tuple) and not getattr(field_type, "_name", None) == "Tuple":
            # If it's a tuple and the field is not intended to be a tuple, assume it's a nested dataclass
            field_values[field_name] = tuple_to_dataclass(field_type, value)
        else:
            # Otherwise, set the primitive value directly
            field_values[field_name] = value

    return cls(**field_values)
