"""Tests for overloading methods."""

from __future__ import annotations

import os

import pytest
from eth_abi.codec import ABICodec
from eth_abi.registry import registry as default_registry
from hexbytes import HexBytes
from web3.exceptions import ContractCustomError

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
            assert selector == ErrorsContract.errors.One.selector

            data = err.message[10:]
            assert data == ""

            types = ()
            abi_codec = ABICodec(default_registry)
            decoded = abi_codec.decode(types, HexBytes(data))
            assert not decoded

    def test_error_two(self, w3):
        """Test that we can decode strings."""
        deployed_contract = ErrorsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        try:
            deployed_contract.functions.revertWithErrorTwo().transact()
        except ContractCustomError as err:
            assert err.message

            selector = err.message[:10]
            assert selector == ErrorsContract.errors.Two.selector

            data = err.message[10:]

            types = ("string", "address", "uint8")
            abi_codec = ABICodec(default_registry)
            decoded = abi_codec.decode(types, HexBytes(data))
            assert decoded == (
                "I will not pledge allegiance to Bart. I will not pledge allegiance to Bart. I will not pledge allegiance to Bart.",
                "0x0000000000000000000000000000000000000000",
                255,
            )

    def test_error_three(self, w3):
        """Test that we can decode structs and enums."""
        deployed_contract = ErrorsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        try:
            deployed_contract.functions.revertWithErrorThree().transact()
        except ContractCustomError as err:
            assert err.message

            selector = err.message[:10]
            assert selector == ErrorsContract.errors.Three.selector

            data = err.message[10:]

            types = ("bool", "(uint256,uint256,uint256,uint256)", "uint8")
            abi_codec = ABICodec(default_registry)
            decoded = abi_codec.decode(types, HexBytes(data))
            assert decoded == (False, (1, 2, 3, 4), 0)
