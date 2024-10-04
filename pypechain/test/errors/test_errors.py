"""Tests for overloading methods."""

from __future__ import annotations

import os
from typing import cast

import pytest
from eth_abi.codec import ABICodec
from eth_abi.registry import registry as default_registry
from eth_typing import ABIFunction
from hexbytes import HexBytes
from web3.exceptions import ContractCustomError

from pypechain.core import get_abi_input_types

from .types import ErrorsContract

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.mark.usefixtures("process_contracts")
class TestErrors:
    """Tests events emitted from the contracts."""

    def test_error_one(self, w3):
        """Test that we can decode just the selector."""
        deployed_contract = ErrorsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        try:
            deployed_contract.functions.revertWithErrorOne().transact()
        except ContractCustomError as err:
            assert err.message

            selector = err.message[:10]
            data = err.message[10:]
            assert selector == ErrorsContract.errors.One.selector

            error_abi = cast(
                ABIFunction,
                [item for item in ErrorsContract.abi if item.get("name") == "One" and item.get("type") == "error"][0],
            )
            types = get_abi_input_types(error_abi)
            assert types == []
            abi_codec = ABICodec(default_registry)
            decoded = abi_codec.decode(types, HexBytes(data))
            assert not decoded

            assert ErrorsContract.errors.One.decode_error_data(HexBytes(data)) == decoded
            assert ErrorsContract.errors.decode_custom_error(err.message) == decoded

    def test_error_two(self, w3):
        """Test that we can decode strings."""
        deployed_contract = ErrorsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        try:
            deployed_contract.functions.revertWithErrorTwo().transact()
        except ContractCustomError as err:
            assert err.message

            selector = err.message[:10]
            data = err.message[10:]
            assert selector == ErrorsContract.errors.Two.selector

            error_abi = cast(
                ABIFunction,
                [item for item in ErrorsContract.abi if item.get("name") == "Two" and item.get("type") == "error"][0],
            )
            types = get_abi_input_types(error_abi)
            assert types == ["string", "address", "uint8"]
            abi_codec = ABICodec(default_registry)
            decoded = abi_codec.decode(types, HexBytes(data))
            assert decoded == (
                "I will not pledge allegiance to Bart. I will not pledge allegiance to Bart. I will not pledge allegiance to Bart.",  # pylint: disable=line-too-long
                "0x0000000000000000000000000000000000000000",
                255,
            )
            assert ErrorsContract.errors.Two.decode_error_data(HexBytes(data)) == decoded
            assert ErrorsContract.errors.decode_custom_error(err.message) == decoded

    def test_error_three(self, w3):
        """Test that we can decode structs and enums."""
        deployed_contract = ErrorsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        try:
            deployed_contract.functions.revertWithErrorThree().transact()
        except ContractCustomError as err:
            assert err.message

            selector = err.message[:10]
            data = err.message[10:]
            assert selector == ErrorsContract.errors.Three.selector

            error_abi = cast(
                ABIFunction,
                [item for item in ErrorsContract.abi if item.get("name") == "Three" and item.get("type") == "error"][0],
            )
            types = get_abi_input_types(error_abi)
            assert types == ["bool", "(uint256,uint256,uint256,uint256)", "uint8"]

            abi_codec = ABICodec(default_registry)
            decoded = abi_codec.decode(types, HexBytes(data))
            assert decoded == (False, (1, 2, 3, 4), 0)

            assert ErrorsContract.errors.Three.decode_error_data(HexBytes(data)) == decoded
            assert ErrorsContract.errors.decode_custom_error(err.message) == decoded
