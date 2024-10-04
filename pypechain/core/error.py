"""Defines the base error class for all subclasses of errors."""

# TODO do we want to change these to match events?

from dataclasses import dataclass


@dataclass
class ErrorParams:
    """Parameter info for custom contract errors."""

    name: str
    solidity_type: str
    python_type: str


@dataclass
class ErrorInfo:
    """Custom contract error information."""

    name: str
    selector: str
    signature: str
    inputs: list[ErrorParams]
