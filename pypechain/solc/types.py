"""Types for solc."""

from typing import TypedDict

from web3.types import ABI


class SolcContract(TypedDict):
    """SolcContract"""

    abi: ABI
    bin: str
    metadata: str


class SolcJson(TypedDict):
    """SolcJson"""

    contracts: dict[str, SolcContract]
    version: str
