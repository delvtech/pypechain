"""Tests for overloading methods."""
from __future__ import annotations

import os

import pytest
from multimethod import DispatchError

from pypechain.test.overloading.types.OverloadedMethodsContract import OverloadedMethodsContract

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


class TestOverloading:
    """Tests pipeline from bots making trades to viewing the trades in the db"""

    def test_overloading(self, w3):
        """Runs the entire pipeline and checks the database at the end.
        All arguments are fixtures.
        """

        # TODO: add the factory to the constructor so we can do:
        # deployed_contract = MyContract(w3=w3, address=address)
        # or:
        # ContractDeployer =  MyContract(w3)
        # deployed_contract = ContractDeployer.deploy(arg1, arg2)
        deployer = OverloadedMethodsContract.factory(w3=w3)

        # TODO: put this into a deploy method and add the address automatically
        tx_hash = deployer.constructor().transact({"from": w3.eth.accounts[0]})
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        deployed_contract = deployer(address=tx_receipt.contractAddress)

        s = "test string"
        x = 1
        y = 2

        # TODO:
        result = deployed_contract.functions.doSomething(s).call()
        assert result == "test string"

        result = deployed_contract.functions.doSomething(x).call()
        assert result == 1 * 2

        result = deployed_contract.functions.doSomething(x, y).call()
        assert result == 1 + 2

        result = deployed_contract.functions.doSomething(x, s).call()
        assert result == (x, s)

        # checks that it fails
        # TODO ensure this throws validation error
        with pytest.raises(DispatchError) as err:
            result = deployed_contract.functions.doSomething(x, y, s).call()

        # checks error string
        try:
            result = deployed_contract.functions.doSomething(x, y, s).call()
        except TypeError as err:
            assert (
                "OverloadedMethodsDoSomethingContractFunction.__call__() takes 3 positional arguments but 4 were given"
                in str(err.__context__)
            )
