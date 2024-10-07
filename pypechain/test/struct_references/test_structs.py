"""Tests for overloading methods."""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from web3 import Web3

from .types import StructsAContract, StructsBContract

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.fixture
def deployed_contracts(w3: Web3) -> tuple[StructsAContract, StructsBContract]:
    """Deploys a StructsA contract and StructsB."""
    structs_a = StructsAContract.deploy(w3=w3, account=w3.eth.accounts[0])
    structs_b = StructsBContract.deploy(w3=w3, account=w3.eth.accounts[0])
    return structs_a, structs_b


@pytest.mark.usefixtures("process_contracts")
class TestStructs:
    """Tests pipeline from bots making trades to viewing the trades in the db"""

    def test_correct_files_exit(self):
        """StructsA and StructsB both inherit from IStructs.  StructsA also declares it's own
        struct.  Therefore we should expect to see types files for IStructs and StructsA, but not
        for StructsB since it doesn't declare its own.  IStructs is an interface file though, there
        is no ABI for it, so we shouldn't create a contract file."""

        expected_files = [
            "types/__init__.py",
            "types/IStructsTypes.py",
            "types/StructsAContract.py",
            "types/StructsATypes.py",
            "types/StructsBContract.py",
        ]

        results: list[tuple[bool, Path]] = []
        for file_path in expected_files:
            full_path = Path(current_path) / file_path
            results.append((full_path.exists(), full_path))

        failed_tests = [full_path for exists, full_path in results if not exists]

        assert len(failed_tests) == 0, f"Several files don't exist: {failed_tests=}"
