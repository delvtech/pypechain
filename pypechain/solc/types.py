"""Types for solc."""

from typing import TypedDict

from eth_typing import ABI


class SolcContract(TypedDict):
    """SolcContract"""

    abi: ABI
    bin: str
    metadata: str


class SolcJson(TypedDict):
    """SolcJson"""

    contracts: dict[str, SolcContract]
    version: str
