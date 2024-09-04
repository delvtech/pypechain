"""Utilities for working with foundry-rs."""

from typing import TypeGuard

from web3 import Web3

from pypechain.foundry.types import FoundryJson
from pypechain.utilities.types import LinkReferences


def is_foundry_json(val: object) -> TypeGuard[FoundryJson]:
    """Determines whether a json object is a FoundryJson."""
    required_keys = {"abi", "bytecode", "deployedBytecode", "methodIdentifiers", "rawMetadata", "metadata", "id"}
    return isinstance(val, dict) and required_keys.issubset(val.keys())


def get_bytecode_from_foundry_json(json_abi: FoundryJson) -> str:
    """Gets the bytecode from a foundry json file."""
    return json_abi.get("bytecode").get("object")


def get_bytecode_link_references_from_foundry_json(json_abi: FoundryJson) -> list[LinkReferences]:
    """Gets the bytecode from a foundry json file."""
    link_references = json_abi.get("bytecode").get("linkReferences")

    # Rework link references to be a dictionary keyed by a contract name, valued with
    # the hex code placeholder in the bytecode.
    out_link_references = []
    for function_path, value in link_references.items():
        for contract_name, _ in value.items():
            fully_qualified_lib_name = f"{function_path}:{contract_name}"
            hex_code = Web3.keccak(text=fully_qualified_lib_name).hex()
            # Hex returns raw hex without 0x. We take the 34 character prefix, and add the placeholder
            # token
            placehoder_code = f"__${hex_code[0:34]}$__"
            # TODO there may be scoping issues here
            out_link_references.append(LinkReferences(contract_name=contract_name, placeholder_code=placehoder_code))

    return out_link_references
