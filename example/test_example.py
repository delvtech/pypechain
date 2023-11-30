"""Example showcasing pypechain."""
from __future__ import annotations

import os

import pytest
from web3 import Web3

from example.types import ExampleContract

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.fixture
def deployed_contract(w3: Web3):
    """Deploys the ExampleContract contract."""
    return ExampleContract.deploy(w3=w3, signer=w3.eth.accounts[0])


@pytest.mark.usefixtures("process_contracts")
class TestExampleContract:
    """Tests pipeline from bots making trades to viewing the trades in the db"""

    def test_flip_flop(self, deployed_contract: ExampleContract):
        """Tests single value"""

        flip = 1
        flop = 2
        result: ExampleContract.functions.flipFlop.ReturnValues = deployed_contract.functions.flipFlop(
            flip, flop
        ).call()

        assert result == (flop, flip)
