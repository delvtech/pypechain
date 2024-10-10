"""Defines the base error class for all subclasses of errors."""

# TODO do we want to change these to match events?
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from eth_abi.codec import ABICodec
from eth_abi.registry import registry as default_registry
from hexbytes import HexBytes

from .combomethod_typed import combomethod_typed


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


class PypechainBaseError:
    """The base class for a single error in a contract."""

    name: str
    # 4 byte error selector
    selector: str
    # error signature, i.e. customerror(uint256,bool)
    signature: str
    # Solidity error input types
    input_types: list[str]

    @combomethod_typed
    def decode_error_data(
        self,
        data: HexBytes,
        # TODO: instead of returning a tuple, return a dataclass with the input names and types just like we do for functions
    ) -> tuple[Any, ...]:
        """Decodes error data returns from a smart contract."""
        abi_codec = ABICodec(default_registry)
        decoded = abi_codec.decode(self.input_types, data)
        return decoded


class PypechainBaseContractErrors:
    """The base class for a collection of errors within a contract."""

    _all: list[PypechainBaseError]

    def decode_custom_error(self, data: str | None) -> tuple[str, tuple[Any, ...]]:
        """Decodes a custom contract error."""
        if data is None:
            return ("UnknownError", tuple())

        selector = data[:10]
        for err in self._all:
            if err.selector == selector:
                return (err.name, err.decode_error_data(data=HexBytes(data[10:])))

        # If a selector isn't found, we return the name as itself
        return (data, tuple())
