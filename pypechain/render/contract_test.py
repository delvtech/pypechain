"""Tests for rendering the contract file."""

import json
import os

from eth_typing import ABI

from pypechain.render.contract import get_function_datas
from pypechain.utilities.abi import get_events_for_abi
from pypechain.utilities.templates import get_jinja_env

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


class TestOverloading:
    """Tests overloading for code gen using snapshots"""

    def test_overloading(self, snapshot):
        """Tests overloading for code gen using snapshots"""

        env = get_jinja_env()
        functions_template = env.get_template("contract.py/functions.py.jinja2")

        # TODO: add return types to function calls

        abi_str = """
            [
                {
                    "constant": true,
                    "inputs": [],
                    "name": "balanceOf",
                    "outputs": [{"name": "", "type": "uint256"}],
                    "payable": false,
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "constant": true,
                    "inputs": [{"name": "who", "type": "address"}],
                    "name": "balanceOf",
                    "outputs": [{"name": "", "type": "uint256"}],
                    "payable": false,
                    "stateMutability": "view",
                    "type": "function"
                }
            ]
        """

        abi: ABI = json.loads(abi_str)

        function_datas, constructor_data = get_function_datas(abi)
        has_overloading = any(len(function_data["signature_datas"]) > 1 for function_data in function_datas.values())
        contract_name = "Overloaded"

        functions_block = functions_template.render(
            abi=abi,
            contract_name=contract_name,
            functions=function_datas,
            # TODO: use this data to add a typed constructor
            constructor=constructor_data,
        )
        assert has_overloading is True

        snapshot.snapshot_dir = "snapshots"  # This line is optional.
        snapshot.assert_match(functions_block, "expected_overloading.py")

    def test_notoverloading(self, snapshot):
        """Tests not overloading for code gen using snapshots"""

        env = get_jinja_env()
        functions_template = env.get_template("contract.py/functions.py.jinja2")

        # TODO: add return types to function calls

        # different names, should NOT be overloaded
        abi_str = """
            [
                {
                    "constant": true,
                    "inputs": [],
                    "name": "balanceOf",
                    "outputs": [{"name": "", "type": "uint256"}],
                    "payable": false,
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "constant": true,
                    "inputs": [{"name": "who", "type": "address"}],
                    "name": "balanceOfWho",
                    "outputs": [{"name": "", "type": "bool"}],
                    "payable": false,
                    "stateMutability": "view",
                    "type": "function"
                }
            ]
        """

        abi: ABI = json.loads(abi_str)

        function_datas, constructor_data = get_function_datas(abi)
        has_overloading = any(len(function_data["signature_datas"]) > 1 for function_data in function_datas.values())
        contract_name = "Overloaded"

        functions_block = functions_template.render(
            abi=abi,
            contract_name=contract_name,
            functions=function_datas,
            # TODO: use this data to add a typed constructor
            constructor=constructor_data,
        )
        assert has_overloading is False

        snapshot.snapshot_dir = "snapshots"
        snapshot.assert_match(functions_block, "expected_not_overloading.py")

    def test_has_events(self, snapshot):
        """Tests that events are created."""

        env = get_jinja_env()
        events_template = env.get_template("contract.py/events.py.jinja2")

        # different names, should NOT be overloaded
        abi_str = """
            [
                {
                    "anonymous": false,
                    "inputs": [
                        {
                        "indexed": true,
                        "internalType": "address",
                        "name": "from",
                        "type": "address"
                        },
                        {
                        "indexed": true,
                        "internalType": "address",
                        "name": "to",
                        "type": "address"
                        },
                        {
                        "indexed": false,
                        "internalType": "uint256",
                        "name": "value",
                        "type": "uint256"
                        }
                    ],
                    "name": "Transfer",
                    "type": "event"
                },
                {
                    "anonymous": false,
                    "inputs": [
                        {
                        "indexed": true,
                        "internalType": "address",
                        "name": "owner",
                        "type": "address"
                        },
                        {
                        "indexed": true,
                        "internalType": "address",
                        "name": "spender",
                        "type": "address"
                        },
                        {
                        "indexed": false,
                        "internalType": "uint256",
                        "name": "value",
                        "type": "uint256"
                        }
                    ],
                    "name": "Approval",
                    "type": "event"
                }
            ]
        """

        abi: ABI = json.loads(abi_str)

        event_datas = get_events_for_abi(abi)
        contract_name = "Overloaded"

        events_block = events_template.render(
            abi=abi,
            contract_name=contract_name,
            events=event_datas,
        )

        snapshot.snapshot_dir = "snapshots"
        snapshot.assert_match(events_block, "has_events.py")
