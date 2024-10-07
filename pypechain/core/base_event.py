"""Defines the base event class for all subclasses of events."""

from __future__ import annotations

from dataclasses import dataclass

from eth_typing import ChecksumAddress
from hexbytes import HexBytes


@dataclass(kw_only=True)
class BaseEventArgs:
    """The base event argument class for all subclasses of event args."""


@dataclass(kw_only=True)
class BaseEvent:
    """The base event class for all subclasses of events."""

    # pylint: disable=too-many-instance-attributes

    # Base event arguments
    log_index: int
    transaction_index: int
    transaction_hash: HexBytes
    address: ChecksumAddress
    block_hash: HexBytes
    block_number: int
    args: BaseEventArgs
    __name__: str = "BaseEvent"
