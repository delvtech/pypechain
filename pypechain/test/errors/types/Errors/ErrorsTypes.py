"""Dataclasses for all structs in the Errors contract.

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

from pypechain.core import ErrorInfo, ErrorParams


@dataclass
class Ages:
    """Ages struct."""

    bart: int
    lisa: int
    homer: int
    marge: int


OneError = ErrorInfo(
    inputs=[],
    name="One",
    selector="0xbe0c2110",
    signature="One()",
)

ThreeError = ErrorInfo(
    inputs=[
        ErrorParams(name="trueOrFalse", python_type="bool", solidity_type="bool"),
        ErrorParams(name="theSimpsons", python_type="tuple", solidity_type="tuple"),
        ErrorParams(name="who", python_type="int", solidity_type="uint8"),
    ],
    name="Three",
    selector="0x09b8b989",
    signature="Three(bool,(uint256,uint256,uint256,uint256),uint8)",
)

TwoError = ErrorInfo(
    inputs=[
        ErrorParams(name="message", python_type="str", solidity_type="string"),
        ErrorParams(name="who", python_type="str", solidity_type="address"),
        ErrorParams(name="value", python_type="int", solidity_type="uint8"),
    ],
    name="Two",
    selector="0x01e3e2f6",
    signature="Two(string,address,uint8)",
)
