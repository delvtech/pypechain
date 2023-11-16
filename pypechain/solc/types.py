"""Types for solc."""

from typing import TypedDict

from web3.types import ABI


class SolcContract(TypedDict):
    """Foundry"""

    abi: ABI
    bin: str
    metadata: str


class SolcJson(TypedDict):
    """Foundry"""

    contracts: dict[str, SolcContract]
    version: str
