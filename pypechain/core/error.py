"""Defines the base error class for all subclasses of errors."""

# TODO do we want to change these to match events?
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, cast

from eth_abi.codec import ABICodec
from eth_abi.registry import registry as default_registry
from eth_typing import ABI, ABIFunction
from hexbytes import HexBytes

from .combomethod_typed import combomethod_typed
from .utilities import get_abi_input_types


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
    # The full abi that defines this error
    abi: ABI

    @combomethod_typed
    def decode_error_data(
        self,
        data: HexBytes,
        # TODO: instead of returning a tuple, return a dataclass
        # with the input names and types just like we do for functions.
        # https://github.com/delvtech/pypechain/issues/138
    ) -> tuple[Any, ...]:
        """Decodes error data returns from a smart contract."""

        error_abi = cast(
            ABIFunction,
            [item for item in self.abi if item.get("name") == self.name and item.get("type") == "error"][0],
        )
        types = get_abi_input_types(error_abi)
        abi_codec = ABICodec(default_registry)
        decoded = abi_codec.decode(types, data)
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
