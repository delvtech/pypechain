"""Defines the base event class for all subclasses of events."""

from dataclasses import dataclass

from eth_typing import ABIEvent, ChecksumAddress
from hexbytes import HexBytes


@dataclass(kw_only=True)
class BaseEvent:
    # Base event arguments
    log_index: int
    transaction_index: int
    transaction_hash: HexBytes
    address: ChecksumAddress
    block_hash: HexBytes
    block_number: int
    # We keep the original abi event here as well
    abi_event: ABIEvent
    __name__: str = "BaseEvent"
