"""Tests for sign and transact."""

from __future__ import annotations

import os

import pytest
from eth_account.account import Account
from eth_account.signers.local import LocalAccount
from eth_utils.conversions import to_bytes
from eth_utils.crypto import keccak
from eth_utils.curried import text_if_str
from hexbytes import HexBytes
from web3 import Web3

from pypechain.core import PypechainCallException

from .types.Transact import TransactContract

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name


def make_private_key(extra_entropy: str = "SOME STRING") -> str:
    """Make a private key.

    Arguments
    ---------
    extra_entropy: str, optional
        Any string used to add entropy to the keccak hash.
        Defaults to "SOME STRING".

    Returns
    -------
    str
        The private key.
    """
    extra_key_bytes = text_if_str(to_bytes, extra_entropy)
    key_bytes = keccak(os.urandom(32) + extra_key_bytes)
    return HexBytes(key_bytes).hex()


@pytest.mark.usefixtures("process_contracts")
class TestStructs:
    """Tests pipeline from bots making trades to viewing the trades in the db"""

    def test_sign_and_transact(self, w3: Web3):
        """Test the sign and transact function"""
        deployed_contract = TransactContract.deploy(w3=w3, account=w3.eth.accounts[0])

        # Make a new account that's not a default anvil account
        account: LocalAccount = Account().from_key(make_private_key())

        # Fund the account with eth
        w3.provider.make_request(method="anvil_setBalance", params=[account.address, hex(int(1e18))])

        # Expect failure with transaction without signing
        with pytest.raises(PypechainCallException):
            _ = deployed_contract.functions.TransactFunction().transact({"from": account.address})

        # Expect success with sign and transact
        tx_hash = deployed_contract.functions.TransactFunction().sign_and_transact(account=account)
        receipt = w3.eth.get_transaction_receipt(tx_hash)
        out_events = deployed_contract.events.Success().process_receipt_typed(receipt)
        assert len(list(out_events)) == 1
