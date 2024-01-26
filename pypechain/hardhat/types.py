"""Types for Hardhat."""

from typing import Any, TypedDict

from web3.types import ABI


class HardhatJson(TypedDict):
    """Hardhat"""

    _format: str
    contractName: str
    sourceName: str
    abi: ABI
    bytecode: str
    deployedBytecode: str
    linkReferences: Any
    deployedLinkReferences: Any
