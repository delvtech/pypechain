"""Example showcasing pypechain."""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from web3 import Web3
from web3.contract.contract import Contract

from example.types import ExampleContract
from example.types.ExampleTypes import InnerStruct, NestedStruct, SimpleStruct
from pypechain.utilities.abi import load_abi_infos_from_file

from .types.ExampleContract import ExampleFlipFlopContractFunction

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name
# pylint: disable=invalid-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.mark.usefixtures("process_contracts")
class TestExampleContract:
    """Tests pipeline from bots making trades to viewing the trades in the db"""

    def test_using_vanilla_web3py(self, w3: Web3):
        """Tests with vanilla web3py"""

        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the file relative to the script directory
        file_path = Path(os.path.join(script_dir, "abis", "Example.sol/Example.json"))
        # Open the json and grab the abi and bytecode
        abi_info = load_abi_infos_from_file(file_path)[0]

        ExampleContract = w3.eth.contract(abi=abi_info.abi, bytecode=abi_info.bytecode)

        # Submit the transaction that deploys the contract
        tx_hash = ExampleContract.constructor("example").transact()
        # Wait for the transaction to be mined, and get the transaction receipt
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        deployed_contract: Contract = w3.eth.contract(
            address=tx_receipt.contractAddress, abi=abi_info.abi  # type: ignore
        )

        result = deployed_contract.functions.flipFlop(1, 2).call()
        assert result == [2, 1]

        crazy_result = deployed_contract.functions.singleNestedStruct((1, "string", (True,))).call()
        assert crazy_result == (1, "string", (True,))

    def test_flip_flop(self, w3):
        """Tests single value"""

        deployed_contract = ExampleContract.deploy(
            w3=w3, account=w3.eth.accounts[0], constructor_args=ExampleContract.ConstructorArgs("example")
        )

        flip = 1
        flop = 2
        result: ExampleFlipFlopContractFunction.ReturnValues = deployed_contract.functions.flipFlop(flip, flop).call()

        assert result == (flop, flip)

    def test_simple_structs(self, w3):
        """Tests single value"""

        deployed_contract = ExampleContract.deploy(
            w3=w3, account=w3.eth.accounts[0], constructor_args=ExampleContract.ConstructorArgs("example")
        )

        input_struct: SimpleStruct = SimpleStruct(1, "string")
        output_struct = deployed_contract.functions.singleSimpleStruct(input_struct).call()

        assert output_struct.intVal == 1
        assert output_struct.strVal == "string"

    def test_nested_structs(self, w3):
        """Tests single value"""

        deployed_contract = ExampleContract.deploy(
            w3=w3, account=w3.eth.accounts[0], constructor_args=ExampleContract.ConstructorArgs("example")
        )

        input_struct = NestedStruct(1, "string", InnerStruct(True))
        output_struct: NestedStruct = deployed_contract.functions.singleNestedStruct(input_struct).call()

        assert output_struct.intVal == 1
        assert output_struct.strVal == "string"
        assert output_struct.innerStruct == InnerStruct(boolVal=True)
