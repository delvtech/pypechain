"""Tests for overloading methods."""

from __future__ import annotations

import os

import pytest
from eth_account.account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3
from web3.types import RPCEndpoint

from pypechain.test.deployment.types import ConstructorWithStructArgsContract
from pypechain.test.deployment.types.ConstructorWithStructArgsTypes import Config, Items

from .types import ConstructorNoArgsContract, ConstructorWithArgsContract, NoConstructorContract

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
class TestNoConstructorContract:
    """Tests deployment methods for contracts with no constructor"""

    def test_deployment_with_constructor_and_default_signer(self, w3):
        """Tests deployment using the constructor method instead of the deploy method."""
        # transact() uses the default signer in the web3 instance
        tx_hash = NoConstructorContract.factory(w3).constructor().transact()
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        assert receipt["status"] == 1

    def test_deployment_with_constructor_and_local_signer(self, w3: Web3, local_account: LocalAccount):
        """Tests deployment using the constructor method instead of the deploy method."""
        # Get the deployment transaction
        deployment_tx = NoConstructorContract.factory(w3).constructor().build_transaction()
        current_nonce = w3.eth.get_transaction_count(local_account.address, "pending")
        deployment_tx.update({"nonce": current_nonce})

        # Sign the transaction with local account private key
        signed_tx = local_account.sign_transaction(deployment_tx)

        # Send the signed transaction and wait for receipt
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        # Assert deployment success based on receipt
        assert receipt["status"] == 1  # or other relevant assertion

    def test_deploy_method_with_default_signer(self, w3, local_account):
        """Tests deployment using the constructor method instead of the deploy method."""
        # transact() uses the default signer in the web3 instance
        deployed_contract = NoConstructorContract.deploy(w3, local_account)
        name = deployed_contract.functions.name().call()
        assert name == "default"

    def test_deploy_method_with_local_signer(self, w3: Web3, local_account: LocalAccount):
        """Tests deployment using the constructor method instead of the deploy method."""
        # Get the deployment transaction
        deployed_contract = NoConstructorContract.deploy(w3, local_account)

        name = deployed_contract.functions.name().call()
        assert name == "default"


class TestConstructorNoArgs:
    """Tests deployment methods for contracts with a constructor that has no arguments."""

    def test_deployment_with_constructor_and_default_signer(self, w3):
        """Tests deployment using the constructor method instead of the deploy method."""
        # transact() uses the default signer in the web3 instance
        tx_hash = ConstructorNoArgsContract.factory(w3).constructor().transact()
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        assert receipt["status"] == 1

    def test_deployment_with_constructor_and_local_signer(self, w3: Web3, local_account: LocalAccount):
        """Tests deployment using the constructor method instead of the deploy method."""
        # Get the deployment transaction
        deployment_tx = ConstructorNoArgsContract.factory(w3).constructor().build_transaction()
        current_nonce = w3.eth.get_transaction_count(local_account.address, "pending")
        deployment_tx.update({"nonce": current_nonce})

        # Sign the transaction with local account private key
        signed_tx = local_account.sign_transaction(deployment_tx)

        # Send the signed transaction and wait for receipt
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        # Assert deployment success based on receipt
        assert receipt["status"] == 1  # or other relevant assertion

    def test_deploy_method_with_default_signer(self, w3, local_account):
        """Tests deployment using the constructor method instead of the deploy method."""
        # transact() uses the default signer in the web3 instance
        deployed_contract = ConstructorNoArgsContract.deploy(w3, local_account)
        name = deployed_contract.functions.name().call()
        assert name == "default"

    def test_deploy_method_with_local_signer(self, w3: Web3, local_account: LocalAccount):
        """Tests deployment using the constructor method instead of the deploy method."""
        # Get the deployment transaction
        deployed_contract = ConstructorNoArgsContract.deploy(w3, local_account)

        name = deployed_contract.functions.name().call()
        assert name == "default"


class TestConstructorWithArgs:
    """Tests deployment methods for contracts with a constructor that has arguments."""

    def test_deployment_with_constructor_and_default_signer(self, w3):
        """Tests deployment using the constructor method instead of the deploy method."""
        # transact() uses the default signer in the web3 instance
        tx_hash = ConstructorWithArgsContract.factory(w3).constructor("name").transact()
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        assert receipt["status"] == 1

    def test_deployment_with_constructor_and_local_signer(self, w3: Web3, local_account: LocalAccount):
        """Tests deployment using the constructor method instead of the deploy method."""
        # Get the deployment transaction
        deployment_tx = ConstructorWithArgsContract.factory(w3).constructor("name").build_transaction()
        current_nonce = w3.eth.get_transaction_count(local_account.address, "pending")
        deployment_tx.update({"nonce": current_nonce})

        # Sign the transaction with local account private key
        signed_tx = local_account.sign_transaction(deployment_tx)

        # Send the signed transaction and wait for receipt
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        # Assert deployment success based on receipt
        assert receipt["status"] == 1  # or other relevant assertion

    def test_deploy_method_with_default_signer(self, w3, local_account):
        """Tests deployment using the constructor method instead of the deploy method."""
        # transact() uses the default signer in the web3 instance
        deployed_contract = ConstructorWithArgsContract.deploy(
            w3, local_account, constructor_args=ConstructorWithArgsContract.ConstructorArgs("not default")
        )
        name = deployed_contract.functions.name().call()
        assert name == "not default"

    def test_deploy_method_with_local_signer(self, w3: Web3, local_account: LocalAccount):
        """Tests deployment using the constructor method instead of the deploy method."""
        # Get the deployment transaction
        deployed_contract = ConstructorWithArgsContract.deploy(
            w3, local_account, constructor_args=ConstructorWithArgsContract.ConstructorArgs("not default")
        )

        name = deployed_contract.functions.name().call()
        assert name == "not default"


class TestConstructorWithStructArgs:
    """Tests deployment methods for contracts with a constructor that has complex arguments."""

    def test_deployment_with_constructor_and_default_signer(self, w3):
        """Tests deployment using the constructor method instead of the deploy method."""
        # transact() uses the default signer in the web3 instance
        config = Config(name="name", items=Items(thing="thang", yesOrNo=True))
        tx_hash = ConstructorWithStructArgsContract.factory(w3).constructor(config).transact()
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        assert receipt["status"] == 1

    def test_deployment_with_constructor_and_local_signer(self, w3: Web3, local_account: LocalAccount):
        """Tests deployment using the constructor method instead of the deploy method."""
        # Get the deployment transaction
        config = Config(name="name", items=Items(thing="thang", yesOrNo=True))
        deployment_tx = ConstructorWithStructArgsContract.factory(w3).constructor(config).build_transaction()
        current_nonce = w3.eth.get_transaction_count(local_account.address, "pending")
        deployment_tx.update({"nonce": current_nonce})

        # Sign the transaction with local account private key
        signed_tx = local_account.sign_transaction(deployment_tx)

        # Send the signed transaction and wait for receipt
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        # Assert deployment success based on receipt
        assert receipt["status"] == 1  # or other relevant assertion

    def test_deploy_method_with_default_signer(self, w3, local_account):
        """Tests deployment using the constructor method instead of the deploy method."""
        # transact() uses the default signer in the web3 instance
        config = Config(name="name", items=Items(thing="thang", yesOrNo=True))
        args = ConstructorWithStructArgsContract.ConstructorArgs(config)
        deployed_contract = ConstructorWithStructArgsContract.deploy(w3, local_account, constructor_args=args)
        name = deployed_contract.functions.name().call()
        assert name == "name"

    def test_deploy_method_with_local_signer(self, w3: Web3, local_account: LocalAccount):
        """Tests deployment using the constructor method instead of the deploy method."""
        # Get the deployment transaction
        config = Config(name="name", items=Items(thing="thang", yesOrNo=True))
        args = ConstructorWithStructArgsContract.ConstructorArgs(config)
        deployed_contract = ConstructorWithStructArgsContract.deploy(w3, local_account, constructor_args=args)

        name = deployed_contract.functions.name().call()
        assert name == "name"
