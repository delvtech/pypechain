"""Types for foundry-rs."""

from typing import Any, Literal, TypedDict

from web3.types import ABI


class FoundryByteCode(TypedDict):
    """Foundry"""

    object: str
    sourceMap: str
    linkReference: Any


class FoundryDeployedByteCode(TypedDict):
    """Foundry"""

    object: str
    sourceMap: str
    linkReference: Any


class FoundryCompiler(TypedDict):
    """Foundry"""

    version: str


class FoundryMetadata(TypedDict, total=False):
    """Foundry"""

    compiler: FoundryCompiler
    language: Literal["Solidity", "Vyper"]


class FoundryJson(TypedDict):
    """Foundry"""

    abi: ABI
    bytecode: FoundryByteCode
    deployedBytecode: FoundryDeployedByteCode
    methodIdentifiers: dict[str, str]
    rawMetadata: str
    metadata: FoundryMetadata
    ast: Any
    id: int
