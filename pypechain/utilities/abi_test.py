"""Tests for ABI utilities."""
import json
import os

from .abi import get_structs_for_abi

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


class TestStructs:
    """Tests pipeline from bots making trades to viewing the trades in the db"""

    def test_hyperdrive_structs(
        self,
    ):
        """Runs the entire pipeline and checks the database at the end.
        All arguments are fixtures.
        """

        json_file_path = os.path.join(project_root, "example/abis/IHyperdrive.json")
        with open(json_file_path, "r", encoding="utf8") as file:
            data = json.load(file)

        structs = get_structs_for_abi(data["abi"])

        actual = list(structs)
        print(f"{actual=}")
        expected = [
            "Checkpoint",
            "MarketState",
            "Fees",
            "PoolConfig",
            "PoolInfo",
            "WithdrawPool",
        ]
        assert actual == expected
        assert all(a == b for a, b in zip(actual, expected))
