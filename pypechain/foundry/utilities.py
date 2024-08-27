"""Utilities for working with foundry-rs."""

from typing import TypeGuard

from pypechain.foundry.types import FoundryJson


def is_foundry_json(val: object) -> TypeGuard[FoundryJson]:
    """Determines whether a json object is a FoundryJson."""
    required_keys = {"abi", "bytecode", "deployedBytecode", "methodIdentifiers", "rawMetadata", "metadata", "id"}
    if isinstance(val, dict) and required_keys.issubset(val.keys()):
        # Only support files with abis
        return len(val["abi"]) > 0
    return False


def get_bytecode_from_foundry_json(json_abi: FoundryJson) -> str:
    """Gets the bytecode from a foundry json file."""
    return json_abi.get("bytecode").get("object")
