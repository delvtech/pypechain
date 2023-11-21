"""Tests for overloading methods."""
from __future__ import annotations

import os

import pytest
from web3 import Web3

from pypechain.test.return_types.types.ReturnTypesTypes import InnerStruct, NestedStruct, SimpleStruct

from .types import ReturnTypesContract

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.fixture
def deployed_contract(w3: Web3):
    """Deploys a ReturnTypes contract."""
    deployer = ReturnTypesContract.factory(w3=w3)
    tx_hash = deployer.constructor().transact({"from": w3.eth.accounts[0]})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # contractAddress not recognized for some reason, adding type ignore
    return deployer(address=tx_receipt.contractAddress)  # type: ignore


class TestReturnTypes:
    """Tests pipeline from bots making trades to viewing the trades in the db"""

    def test_no_name_single_value(self, deployed_contract: ReturnTypesContract):
        """Tests single value"""
        result: int = deployed_contract.functions.noNameSingleValue(1).call()
        assert result == 1

    def test_no_name_two_values(self, deployed_contract: ReturnTypesContract):
        """Tests two values"""
        result: tuple[str, int] = deployed_contract.functions.noNameTwoValues("a string").call()
        assert result == ("a string", 2)

    def test_named_single_value(self, deployed_contract: ReturnTypesContract):
        """Tests named single value"""
        result: int = deployed_contract.functions.namedSingleValue(1, 2).call()
        assert result == 3

    def test_named_two_values(self, deployed_contract: ReturnTypesContract):
        """Tests two named values"""
        result = deployed_contract.functions.namedTwoValues(1, 2).call()
        assert result == (2, 1)

    def test_single_simple_struct(self, deployed_contract: ReturnTypesContract):
        """Tests a struct"""
        result = deployed_contract.functions.singleSimpleStruct().call()
        assert result == SimpleStruct(1, "You are number 1")

    def test_single_nested_struct(self, deployed_contract: ReturnTypesContract):
        """Tests a nested struct"""
        result = deployed_contract.functions.singleNestedStruct().call()
        assert result == NestedStruct(1, "You are number 1", InnerStruct(True))

    def test_two_simple_structs(self, deployed_contract: ReturnTypesContract):
        """Tests two structs"""
        result = deployed_contract.functions.twoSimpleStructs().call()
        assert result == (SimpleStruct(1, "You are number 1"), SimpleStruct(2, "You are number 2"))

    def test_two_mixed_structs(self, deployed_contract: ReturnTypesContract):
        """Tests two structs, one nested"""
        result = deployed_contract.functions.twoMixedStructs().call()
        assert result == (SimpleStruct(1, "You are number 1"), NestedStruct(2, "You are number 2", InnerStruct(True)))

    def test_named_single_struct(self, deployed_contract: ReturnTypesContract):
        """Tests a named struct"""
        result = deployed_contract.functions.namedSingleStruct().call()
        assert result == SimpleStruct(1, "You are number 1")

    def test_named_two_mixed_structs(self, deployed_contract: ReturnTypesContract):
        """Tests two named structs, one nested"""
        result = deployed_contract.functions.namedTwoMixedStructs().call()
        assert result == (SimpleStruct(1, "You are number 1"), NestedStruct(2, "You are number 2", InnerStruct(True)))

    def test_mix_structs_and_primitives(self, deployed_contract: ReturnTypesContract):
        """Tests two structs, one nested, and other values returned"""
        result = deployed_contract.functions.mixStructsAndPrimitives().call()
        assert result == (
            SimpleStruct(1, "You are number 1"),
            NestedStruct(2, "You are number 2", InnerStruct(True)),
            1,
            "ReturnTypesContract",
            False,
        )
