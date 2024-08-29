"""Tests for deploying contracts with linked libraries methods."""

from __future__ import annotations

import os

import pytest
from eth_account.account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3
from web3.types import RPCEndpoint

from .types import ContractContract, MyLibraryContract

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name
current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.fixture
def local_account(w3) -> LocalAccount:
    """Generates a random local account.

    Returns
    -------
    LocalAccount
        An account with a random private key and therefore public key.
    """
    local_account = Account.create("")

    amount_wei = int(100 * 1e18)
    params = [local_account.address, hex(amount_wei)]  # account, amount
    w3.provider.make_request(method=RPCEndpoint("anvil_setBalance"), params=params)

    return local_account


@pytest.mark.usefixtures("process_contracts")
class TestDeployLinking:
    """Tests deployment methods for contracts with no constructor"""

    def test_deployment_requires_contract_linking(self, w3: Web3, local_account: LocalAccount):
        """Tests contract deployment fails if contract linking is not provided."""
        # This should fail: Contract requires linked references
        with pytest.raises(TypeError):
            _ = ContractContract.deploy(w3, local_account)  # type: ignore # pylint: disable=no-value-for-parameter

    def test_deployment_with_contract_linking(self, w3: Web3, local_account: LocalAccount):
        """Tests deployment using contract linking in deploy."""

        # Deploy the library first
        library_contract = MyLibraryContract.deploy(w3, local_account)
        contract = ContractContract.deploy(
            w3,
            local_account,
            link_references=ContractContract.LinkReferences(
                MyLibrary=library_contract,
            ),
        )

        assert contract.functions.add(1, 2).call() == 3
