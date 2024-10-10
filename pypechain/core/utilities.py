"""Utility functions for the pypechain generated files."""

from __future__ import annotations

from dataclasses import fields, is_dataclass
from typing import Any, Iterable, Tuple, TypeVar, cast, get_args

from eth_typing import ABIFunction
from eth_utils.abi import collapse_if_tuple

T = TypeVar("T")


def tuple_to_dataclass(cls: type[T], structs: dict[str, Any], tuple_data: Any | Tuple[Any, ...]) -> T:
    """
    Converts a tuple (including nested tuples) to a dataclass instance.  If cls is not a dataclass,
    then the data will just be passed through this function.

    Parameters
    ----------
    cls: type[T]
        The dataclass type to which the tuple data is to be converted.
    structs: dict[str, Any]
        Mapping from a struct name (key) to the run-time type definition (value).
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
        if field_type in structs:
            field_type = structs[field_type]
        if is_dataclass(field_type):
            # Type narrowing
            assert isinstance(field_type, type)
            # Recursively convert nested tuples to nested dataclasses
            field_values[field_name] = tuple_to_dataclass(field_type, structs, value)
        elif isinstance(value, tuple) and not getattr(field_type, "_name", None) == "Tuple":
            # If it's a tuple and the field is not intended to be a tuple, assume it's a nested dataclass
            # Type narrowing
            assert isinstance(field_type, type)
            field_values[field_name] = tuple_to_dataclass(field_type, structs, value)
        else:
            # Otherwise, set the primitive value directly
            field_values[field_name] = value

    return cls(**field_values)


def dataclass_to_tuple(instance: Any) -> Any:
    """Convert a dataclass instance to a tuple, handling nested dataclasses.
    If the input is not a dataclass, return the original value.

    Parameters
    ----------
    instance : Any
        The dataclass instance to convert to a tuple.  If it is not it passes through.

    Returns
    -------
    Any
        either a tuple or the original value
    """
    # We expect vector inputs as lists, as set by the type hint of
    # the function arguments.
    if isinstance(instance, list):
        return [dataclass_to_tuple(x) for x in instance]

    if not is_dataclass(instance):
        return instance

    def convert_value(value: Any) -> Any:
        """Convert nested dataclasses to tuples recursively, or return the original value."""
        if is_dataclass(value):
            return dataclass_to_tuple(value)
        return value

    return tuple(convert_value(getattr(instance, field.name)) for field in fields(instance))


def get_arg_type_names(in_args: tuple[Any, ...] | list[Any] | Any) -> str:
    """Returns the types of an input sequence of arguments recursively.

    Parameters
    ----------
    in_args : tuple[Any, ...] | list[Any] | Any
        The input sequence of arguments.

    Returns
    -------
    str
        The types of the input sequence of arguments.
    """
    if isinstance(in_args, tuple):
        out = f"({', '.join(get_arg_type_names(arg) for arg in in_args)})"
        return out
    if isinstance(in_args, list):
        # We only look at the first element of the list for types
        # if it's a list, as we expect a list input be mapped to
        # a vector input type in solidity, which must all be of
        # the same type. This is also ensured via type hinting in
        # the contract function.
        out = f"list[{get_arg_type_names(in_args[0])}]"
        return out
    return type(in_args).__name__


def expand_struct_type_str(in_type: tuple[str, ...] | str, structs: dict[str, Any]) -> str:
    """Given a type string, expand any structs to tuples."""
    if isinstance(in_type, str):
        # handle list[types]
        if in_type.startswith("list[") and in_type.endswith("]"):
            return f"list[{expand_struct_type_str(in_type[5:-1], structs)}]"

        if in_type in structs:
            # Expand struct types to tuples
            f = [expand_struct_type_str(str(field.type), structs) for field in fields(structs[in_type])]
            return f"({', '.join(f)})"
        return in_type

    if isinstance(in_type, tuple):
        return f"({', '.join(expand_struct_type_str(field, structs) for field in in_type)})"

    raise TypeError(f"Unsupported type: {in_type}")


def rename_returned_types(
    structs: dict[str, Any], return_types: list[Any] | Any, raw_values: list[str | int | tuple] | str | int | tuple
) -> tuple:
    """Convert structs in the return value to known dataclasses.

    Parameters
    ----------
    return_types : list[str] | str
        The type or list of types returned from a contract.
    raw_values : list[str  |  int | tuple] | str | int | tuple
        The actual returned values from the contract.

    Returns
    -------
    tuple
        The return types.
    """
    # cover case of multiple return values
    if isinstance(return_types, list):
        # Ensure raw_values is a tuple for consistency
        if not isinstance(raw_values, list):
            raw_values = (raw_values,)

        # Convert the tuple to the dataclass instance using the utility function
        converted_values = []
        for return_type, value in zip(return_types, raw_values):
            if type(return_type) == type(list[Any]):  # pylint: disable=unidiomatic-typecheck
                raise NotImplementedError("Multiple return values of type list[...] is not supported.")
            converted_values.append(tuple_to_dataclass(return_type, structs, value))
        converted_values = tuple(converted_values)

        return converted_values

    # cover case of single return type
    # single return type is a list of SomeType, aka `list[SomeType]`
    if type(return_types) == type(list[Any]):  # pylint: disable=unidiomatic-typecheck
        inner_types = get_args(return_types)
        # make sure there is only one inner type
        if len(inner_types) != 1:
            raise NotImplementedError("Only a single inner type in list[...] is supported")
        inner_type = inner_types[0]
        # make sure the type is not also a list
        if type(inner_type) == type(list[Any]):  # pylint: disable=unidiomatic-typecheck
            raise NotImplementedError("Type list[list[...]] is not supported.")
        # type narrowing
        assert isinstance(raw_values, Iterable)
        # loop over inner values & convert those to dataclasses
        converted_value = []
        for value in raw_values:
            converted_value.append(tuple_to_dataclass(inner_type, structs, value))
        return tuple(converted_value)

    # single return type is a standard type or dataclass
    converted_value = tuple_to_dataclass(return_types, structs, raw_values)
    return converted_value


def get_abi_input_types(abi: ABIFunction) -> list[str]:
    """Gets all the solidity input types for a function or error.

    Cribbed from web3._utils.abi.py file.

    Parameters
    ----------

    abi: ABIFunction
        The ABIFunction or ABIError that we want to get input types for.

    Returns
    -------
    list[str]
        A list of solidity input types.

    """

    if "inputs" not in abi and (abi.get("type") == "fallback" or abi.get("type") == "receive"):
        return []
    return [collapse_if_tuple(cast(dict[str, Any], arg)) for arg in abi.get("inputs", [])]
