"""Tests for utility functions """

from dataclasses import dataclass
from typing import TypeVar

from pypechain.core.utilities import dataclass_to_tuple, rename_returned_types, tuple_to_dataclass

T = TypeVar("T")

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


@dataclass
class SimpleClass:
    a: int
    b: str


@dataclass
class NestedClass:
    c: SimpleClass
    d: int


class TestTupleToDataClass:
    def test_simple_dataclass_conversion(self):
        """Test conversion of a simple tuple to a dataclass."""

        input_tuple = (1, "test")
        result = tuple_to_dataclass(SimpleClass, {}, input_tuple)

        assert isinstance(result, SimpleClass)
        assert result.a == 1
        assert result.b == "test"

    def test_nested_dataclass_conversion(self):
        """Test conversion of a nested tuple to a nested dataclass."""

        input_tuple = ((1, "nested"), 2)
        result = tuple_to_dataclass(NestedClass, {}, input_tuple)

        assert isinstance(result, NestedClass)
        assert isinstance(result.c, SimpleClass)
        assert result.c.a == 1
        assert result.c.b == "nested"
        assert result.d == 2

    def test_non_dataclass_passthrough(self):
        """Test that non-dataclass types are passed through without modification."""

        input_data = "not a dataclass"
        result = tuple_to_dataclass(str, {}, input_data)

        assert result == "not a dataclass"


structs = {"SimpleClass": SimpleClass, "NestedClass": NestedClass}


class TestRenameReturnedTypes:
    def test_single_return_type(self):
        """Test single return type conversion."""

        raw_value = (1, "test")
        result = rename_returned_types(structs, SimpleClass, raw_value)

        assert isinstance(result, SimpleClass)
        assert result.a == 1
        assert result.b == "test"

    def test_multiple_return_types(self):
        """Test multiple return types conversion."""

        raw_values = [((1, "nested"), 2), "simple"]
        return_types = [NestedClass, str]
        result = rename_returned_types(structs, return_types, raw_values)

        assert isinstance(result, tuple)
        assert isinstance(result[0], NestedClass)
        assert isinstance(result[0].c, SimpleClass)
        assert result[0].d == 2
        assert result[0].c.a == 1
        assert result[0].c.b == "nested"
        assert result[1] == "simple"

    def test_non_dataclass_passthrough(self):
        """Test that non-dataclass types are passed through without modification."""

        raw_value = "not a dataclass"
        result = rename_returned_types(structs, "str", raw_value)

        assert result == "not a dataclass"


class TestDataclassToTuple:
    """Test suite for dataclass_to_tuple function."""

    def test_simple_dataclass(self):
        """Test conversion of a simple dataclass to a tuple."""
        instance = SimpleClass(1, "test")
        result = dataclass_to_tuple(instance)
        assert isinstance(result, tuple)
        assert result == (1, "test")

    def test_nested_dataclass(self):
        """Test conversion of a nested dataclass to a tuple."""
        nested_instance = SimpleClass(2, "nested")
        instance = NestedClass(nested_instance, 3)
        result = dataclass_to_tuple(instance)
        assert isinstance(result, tuple)
        assert result == ((2, "nested"), 3)

    def test_non_dataclass_passthrough(self):
        """Test that non-dataclass types are passed through without modification."""
        non_dataclass_instance = "not a dataclass"
        result = dataclass_to_tuple(non_dataclass_instance)
        assert result == "not a dataclass"

    # Add any additional test cases here
