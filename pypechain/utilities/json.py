"""Utilities for working with json's that contain smart contract information."""

from __future__ import annotations

from pypechain.foundry.types import FoundryJson
from pypechain.foundry.utilities import get_bytecode_from_foundry_json, is_foundry_json
from pypechain.hardhat.types import HardhatJson
from pypechain.hardhat.utilities import get_bytecode_from_hardhat_json, is_hardhat_json
from pypechain.solc.utilities import get_bytecode_from_solc_json, is_solc_json


def get_bytecode_from_json(json_abi: HardhatJson | FoundryJson) -> str:
    """Gets the bytecode from any supported json format."""
    if is_foundry_json(json_abi):
        return get_bytecode_from_foundry_json(json_abi)
    if is_solc_json(json_abi):
        return get_bytecode_from_solc_json(json_abi)
    if is_hardhat_json(json_abi):
        return get_bytecode_from_hardhat_json(json_abi)

    raise ValueError("Unable to retrieve bytecode, JSON in unknown format.")
