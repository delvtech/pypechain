"""Tests for overloading methods."""

from __future__ import annotations

import os

import pytest
from web3.exceptions import MismatchedABI

from pypechain.test.overloading.types import OverloadedMethodsContract

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.mark.usefixtures("process_contracts")
class TestOverloading:
    """Tests pipeline from bots making trades to viewing the trades in the db"""

    def test_overloading(self, w3):
        """Runs the entire pipeline and checks the database at the end.
        All arguments are fixtures.
        """

        deployed_contract = OverloadedMethodsContract.deploy(w3=w3, account=w3.eth.accounts[0])

        s = "test string"
        x = 1
        y = 2

        result = deployed_contract.functions.doSomething(s).call()
        assert result == "test string"

        result = deployed_contract.functions.doSomething(x).call()
        assert result == 1 * 2

        result = deployed_contract.functions.doSomething(x, y).call()
        assert result == 1 + 2

        with pytest.raises(MismatchedABI) as err:
            result = deployed_contract.functions.doSomething(x, y, s).call()  # type: ignore
        assert "Could not identify the intended function with name `doSomething`" in str(err.value)
