"""Utilities for working with solc."""
from typing import TypeGuard

from pypechain.solc.types import SolcJson


def is_solc_json(val: object) -> TypeGuard[SolcJson]:
    """Determines whether a json object is a SolcJson."""
    return (
        isinstance(val, dict)
        and "contracts" in val
        and isinstance(val["contracts"], dict)
        and all(
            isinstance(contract, dict) and "abi" in contract and "bin" in contract and "metadata" in contract
            for contract in val["contracts"].values()
        )
        and "version" in val
    )


def get_bytecode_from_solc_json(json_abi: SolcJson) -> str:
    """Gets the bytecode from a foundry json file."""
    # assume one contract right now
    contract = list(json_abi.get("contracts").values())[0]
    binary = contract.get("bin")
    return f"0x{binary}"
