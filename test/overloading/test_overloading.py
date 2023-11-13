"""Tests for overloading methods."""
import os

import web3 as w3

from pypechain.utilities.templates import get_jinja_env

from .pypechain_types.OverloadedMethodsContract import OverloadedMethodsContract

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


class TestOverloading:
    """Tests pipeline from bots making trades to viewing the trades in the db"""

    def test_overloading(self, local_chain):
        """Runs the entire pipeline and checks the database at the end.
        All arguments are fixtures.
        """

        overloaded_methods_contract = OverloadedMethodsContract()
        tx_hash = OverloadedMethodsContract.constructor().transact()
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        tx_receipt.contractAddress

        a = 1
        overloaded_methods_contract.functions.doSomething(a)

        assert has_overloading is True
