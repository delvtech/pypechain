"""Tests for overloading methods."""

from __future__ import annotations

import pytest
from web3.exceptions import ContractCustomError

from pypechain.core import PypechainCallException

from .types.Errors import Ages, ErrorsContract


@pytest.mark.usefixtures("process_contracts")
class TestErrors:
    """Tests events emitted from the contracts."""

    def test_error_one(self, w3):
        """Test that we can decode just the selector."""
        deployed_contract = ErrorsContract.deploy(w3=w3, account=w3.eth.accounts[0])

        # Test error handling with "call"

        # Calls should fail and caught with custom error
        try:
            _ = deployed_contract.functions.revertWithErrorOne().call()
            assert False, "Expected exception."
        except PypechainCallException as err:
            # Catch custom error
            assert isinstance(err.orig_exception, ContractCustomError)
            assert err.decoded_error == "One()"
            assert err.decoded_error_name == "One"
            assert err.decoded_error_args == ()
            assert err.contract_call_type == "call"
            assert err.function_name == "revertWithErrorOne"
            assert err.fn_args == ()
            assert err.fn_kwargs == {}
            # Call functions don't write a block, so the block should be identical
            assert err.block_number == deployed_contract.w3.eth.get_block_number()

        # Calls should fail and caught with original web3 error
        try:
            _ = deployed_contract.functions.revertWithErrorOne().call()
            assert False, "Expected exception."
        except ContractCustomError as err:
            # Errors should still be caught with the original type.
            assert err.message == ErrorsContract.errors.One.selector

        # Test error handling with "transact"

        try:
            deployed_contract.functions.revertWithErrorOne().transact()
        except PypechainCallException as err:
            # Catch custom error
            assert isinstance(err.orig_exception, ContractCustomError)
            assert err.decoded_error == "One()"
            assert err.decoded_error_name == "One"
            assert err.decoded_error_args == ()
            assert err.contract_call_type == "transact"
            assert err.function_name == "revertWithErrorOne"
            assert err.fn_args == ()
            assert err.fn_kwargs == {}
            # We default the block number to be the "pending" block.
            # Since this transaction failed, and the chain is on "mine to transact"
            # mode, we expect the block number to be the next block.
            assert err.block_number == deployed_contract.w3.eth.get_block_number() + 1

        try:
            deployed_contract.functions.revertWithErrorOne().transact()
        except ContractCustomError as err:
            # Errors should still be caught with the original type.
            assert err.message == ErrorsContract.errors.One.selector

    def test_error_two(self, w3):
        """Test that we can decode strings."""
        deployed_contract = ErrorsContract.deploy(w3=w3, account=w3.eth.accounts[0])

        # Test error handling with "call"

        # Calls should fail and caught with custom error
        try:
            _ = deployed_contract.functions.revertWithErrorTwo().call()
            assert False, "Expected exception."
        except PypechainCallException as err:
            # Catch custom error
            assert isinstance(err.orig_exception, ContractCustomError)
            assert err.decoded_error == (
                "Two(I will not pledge allegiance to Bart., 0x0000000000000000000000000000000000000000, 255)"
            )
            assert err.decoded_error_name == "Two"
            # Args keep orig type
            assert err.decoded_error_args == (
                "I will not pledge allegiance to Bart.",
                "0x0000000000000000000000000000000000000000",
                255,
            )
            assert err.contract_call_type == "call"
            assert err.function_name == "revertWithErrorTwo"
            assert err.fn_args == ()
            assert err.fn_kwargs == {}
            # Call functions don't write a block, so the block should be identical
            assert err.block_number == deployed_contract.w3.eth.get_block_number()

        # Calls should fail and caught with original web3 error
        try:
            _ = deployed_contract.functions.revertWithErrorTwo().call()
            assert False, "Expected exception."
        except ContractCustomError as err:
            # Errors should still be caught with the original type.
            assert err.message
            assert err.message[:10] == ErrorsContract.errors.Two.selector

        # Test error handling with "transact"

        # Calls should fail and caught with custom error
        try:
            _ = deployed_contract.functions.revertWithErrorTwo().transact()
            assert False, "Expected exception."
        except PypechainCallException as err:
            # Catch custom error
            assert isinstance(err.orig_exception, ContractCustomError)
            assert err.decoded_error == (
                "Two(I will not pledge allegiance to Bart., 0x0000000000000000000000000000000000000000, 255)"
            )
            assert err.decoded_error_name == "Two"
            # Args keep orig type
            assert err.decoded_error_args == (
                "I will not pledge allegiance to Bart.",
                "0x0000000000000000000000000000000000000000",
                255,
            )
            assert err.contract_call_type == "transact"
            assert err.function_name == "revertWithErrorTwo"
            assert err.fn_args == ()
            assert err.fn_kwargs == {}
            # We default the block number to be the "pending" block.
            # Since this transaction failed, and the chain is on "mine to transact"
            # mode, we expect the block number to be the next block.
            assert err.block_number == deployed_contract.w3.eth.get_block_number() + 1

        # Calls should fail and caught with original web3 error
        try:
            _ = deployed_contract.functions.revertWithErrorTwo().transact()
            assert False, "Expected exception."
        except ContractCustomError as err:
            # Errors should still be caught with the original type.
            assert err.message
            assert err.message[:10] == ErrorsContract.errors.Two.selector

    def test_error_three(self, w3):
        """Test that we can decode structs and enums."""
        deployed_contract = ErrorsContract.deploy(w3=w3, account=w3.eth.accounts[0])

        in_struct = Ages(bart=1, lisa=2, homer=3, marge=4)

        # Test error handling with "call"

        # Calls should fail and caught with custom error
        try:
            _ = deployed_contract.functions.revertWithErrorThree(in_struct).call()
            assert False, "Expected exception."
        except PypechainCallException as err:
            # Catch custom error
            assert isinstance(err.orig_exception, ContractCustomError)
            assert err.decoded_error == ("Three(False, (1, 2, 3, 4), 0)")
            assert err.decoded_error_name == "Three"
            # Args keep orig type
            assert err.decoded_error_args == (
                False,
                (1, 2, 3, 4),  # TODO we may want to decode this into a struct
                0,
            )
            assert err.contract_call_type == "call"
            assert err.function_name == "revertWithErrorThree"
            assert err.fn_args == ((1, 2, 3, 4),)
            assert err.fn_kwargs == {}
            # Call functions don't write a block, so the block should be identical
            assert err.block_number == deployed_contract.w3.eth.get_block_number()

        # Calls should fail and caught with original web3 error
        try:
            _ = deployed_contract.functions.revertWithErrorThree(in_struct).call()
            assert False, "Expected exception."
        except ContractCustomError as err:
            # Errors should still be caught with the original type.
            assert err.message
            assert err.message[:10] == ErrorsContract.errors.Three.selector

        # Test error handling with "transact"

        # Calls should fail and caught with custom error
        try:
            _ = deployed_contract.functions.revertWithErrorThree(in_struct).transact()
            assert False, "Expected exception."
        except PypechainCallException as err:
            # Catch custom error
            assert isinstance(err.orig_exception, ContractCustomError)
            assert err.decoded_error == ("Three(False, (1, 2, 3, 4), 0)")
            assert err.decoded_error_name == "Three"
            # Args keep orig type
            assert err.decoded_error_args == (
                False,
                (1, 2, 3, 4),  # TODO we may want to decode this into a struct
                0,
            )
            assert err.contract_call_type == "transact"
            assert err.function_name == "revertWithErrorThree"
            assert err.fn_args == ((1, 2, 3, 4),)
            assert err.fn_kwargs == {}
            # We default the block number to be the "pending" block.
            # Since this transaction failed, and the chain is on "mine to transact"
            # mode, we expect the block number to be the next block.
            assert err.block_number == deployed_contract.w3.eth.get_block_number() + 1

        # Calls should fail and caught with original web3 error
        try:
            _ = deployed_contract.functions.revertWithErrorThree(in_struct).transact()
            assert False, "Expected exception."
        except ContractCustomError as err:
            # Errors should still be caught with the original type.
            assert err.message
            assert err.message[:10] == ErrorsContract.errors.Three.selector
