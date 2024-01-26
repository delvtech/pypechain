"""Utilities for working with hardhat."""

from typing import TypeGuard

from pypechain.hardhat.types import HardhatJson


def is_hardhat_json(val: object) -> TypeGuard[HardhatJson]:
    """Determines whether a json object is a HardhatJson."""
    required_keys = {"_format", "contractName", "sourceName"}

    has_required_keys = isinstance(val, dict) and required_keys.issubset(val.keys())
    if has_required_keys:
        _format: str = val.__dict__.get("_format", "")
        return _format == "hh-sol-artifact-1"
    return False


def get_bytecode_from_hardhat_json(json_abi: HardhatJson) -> str:
    """Gets the bytecode from a hardhat json file."""
    return json_abi.get("bytecode")
