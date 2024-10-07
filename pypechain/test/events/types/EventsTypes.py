"""Dataclasses for all structs in the Events contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.41.
See documentation at https://github.com/delvtech/pypechain """

# super() call methods are generic, while our version adds values & types
# pylint: disable=arguments-differ

# contracts have PascalCase names
# pylint: disable=invalid-name
# contracts control how many attributes and arguments we have in generated code
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# unable to determine which imports will be used in the generated code
# pylint: disable=unused-import
# we don't need else statement if the other conditionals all have return,
# but it's easier to generate
# pylint: disable=no-else-return
from __future__ import annotations

from dataclasses import dataclass

from pypechain.core import BaseEvent, BaseEventArgs


@dataclass(kw_only=True, frozen=True)
class EventAEvent(BaseEvent):
    """The event type for event EventA"""

    @dataclass(kw_only=True, frozen=True)
    class EventAEventArgs(BaseEventArgs):
        """The args to the event EventA"""

        who: str
        value: int

    args: EventAEventArgs

    __name__: str = "EventA"


@dataclass(kw_only=True, frozen=True)
class EventBEvent(BaseEvent):
    """The event type for event EventB"""

    __name__: str = "EventB"
