"""Dataclasses for all structs in the StructsC contract.

DO NOT EDIT.  This file was generated by pypechain.  See documentation at
https://github.com/delvtech/pypechain """

# super() call methods are generic, while our version adds values & types
# pylint: disable=arguments-differ

# contracts have PascalCase names
# pylint: disable=invalid-name
# contracts control how many attributes and arguments we have in generated code
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# unable to determine which imports will be used in the generated code
# pylint: disable=unused-import
# we don't need else statement if the other conditionals all have return,
# but it's easier to generate
# pylint: disable=no-else-return
from __future__ import annotations

from dataclasses import dataclass

from . import IStructsTypes as IStructs


@dataclass
class InnyStruct:
    """InnyStruct struct."""

    innerVal: int


@dataclass
class NestedStruct:
    """NestedStruct struct."""

    inner: InnyStruct


@dataclass
class OuterStruct:
    """OuterStruct struct."""

    nested: NestedStruct


@dataclass
class CStruct:
    """CStruct struct."""

    inner: IStructs.InnerStruct


@dataclass
class ErrorInfo:
    """Custom contract error information."""

    name: str
    selector: str
    signature: str
    inputs: list[ErrorParams]


@dataclass
class ErrorParams:
    """Parameter info for custom contract errors."""

    name: str
    solidity_type: str
    python_type: str