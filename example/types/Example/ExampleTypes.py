"""Dataclasses for all structs in the Example contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.48.
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

# We import this contract itself to ensure all nested structs have a fully qualified name.
# We use this to avoid namespace collisions, as well as having a uniform
# type structure to do lookups when functions return these structs.
# pylint: disable=import-self


from __future__ import annotations

from dataclasses import dataclass

from pypechain.core import BaseEvent, BaseEventArgs, ErrorInfo, ErrorParams

from ..Example import ExampleTypes as Example


@dataclass(kw_only=True)
class FlipEvent(BaseEvent):
    """The event type for event Flip"""

    @dataclass(kw_only=True)
    class FlipEventArgs(BaseEventArgs):
        """The args to the event Flip"""

        flip: int

    # We redefine the args field with the specific event arg type.
    args: FlipEventArgs  # type: ignore[override]

    __name__: str = "Flip"


@dataclass(kw_only=True)
class FlopEvent(BaseEvent):
    """The event type for event Flop"""

    @dataclass(kw_only=True)
    class FlopEventArgs(BaseEventArgs):
        """The args to the event Flop"""

        flop: int

    # We redefine the args field with the specific event arg type.
    args: FlopEventArgs  # type: ignore[override]

    __name__: str = "Flop"


@dataclass
class SimpleStruct:
    """SimpleStruct struct."""

    intVal: int
    strVal: str


@dataclass
class InnerStruct:
    """InnerStruct struct."""

    boolVal: bool


@dataclass
class NestedStruct:
    """NestedStruct struct."""

    intVal: int
    strVal: str
    innerStruct: Example.InnerStruct


WrongChoiceError = ErrorInfo(
    inputs=[
        ErrorParams(name="answer", python_type="int", solidity_type="uint8"),
        ErrorParams(name="errorMessage", python_type="str", solidity_type="string"),
    ],
    name="WrongChoice",
    selector="0xc13b30d4",
    signature="WrongChoice(uint8,string)",
)
