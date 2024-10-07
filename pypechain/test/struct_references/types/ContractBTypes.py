"""Dataclasses for all structs in the ContractB contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.41.
See documentation at https://github.com/delvtech/pypechain """

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

from . import ContractATypes as ContractA


@dataclass
class InnerStruct:
    """InnerStruct struct."""

    intVal: int
    strVal: str


@dataclass
class StructsB:
    """StructsB struct."""

    structA: ContractA.StructsA
    structB: InnerStruct
