"""Tests for overloading methods."""

from __future__ import annotations

import os

from web3 import Web3
from web3.logs import DISCARD

from .types.Events import EventAEvent, EventBEvent, EventsContract

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


class TestEvents:
    """Tests events emitted from the contracts."""

    def test_process_receipt_typed(self, w3: Web3):
        """Test that we can use event filters."""
        deployed_contract = EventsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        hash_a = deployed_contract.functions.emitOneEvent(0, "0x0000000000000000000000000000000000000000").transact()
        receipt_a = w3.eth.get_transaction_receipt(hash_a)
        hash_b = deployed_contract.functions.emitTwoEvents(1, "0x0000000000000000000000000000000000000001").transact()
        receipt_b = w3.eth.get_transaction_receipt(hash_b)

        # Web3 requires instantiated events (i.e., `EventA()`) for process_receipts
        # NOTE uses of `process_receipts` with an actual event will throw warnings
        # if the receipt has multiple events. This is expected, as web3 under the hood
        # loops through all events, regardless of the event attached. Hence, we discard
        # any events, as we handle looping over known events here.
        event_aa = list(deployed_contract.events.EventA().process_receipt_typed(receipt_a, errors=DISCARD))
        event_ab = list(deployed_contract.events.EventA().process_receipt_typed(receipt_b, errors=DISCARD))
        event_ba = list(deployed_contract.events.EventB().process_receipt_typed(receipt_a, errors=DISCARD))
        event_bb = list(deployed_contract.events.EventB().process_receipt_typed(receipt_b, errors=DISCARD))

        assert len(event_aa) == 1
        assert isinstance(event_aa[0], EventAEvent)
        assert event_aa[0].args.who == "0x0000000000000000000000000000000000000000"
        assert event_aa[0].args.value == 0

        assert len(event_ab) == 1
        assert isinstance(event_ab[0], EventAEvent)
        assert event_ab[0].args.who == "0x0000000000000000000000000000000000000001"
        assert event_ab[0].args.value == 1

        assert len(event_ba) == 0

        assert len(event_bb) == 1
        assert isinstance(event_bb[0], EventBEvent)

    def test_get_logs_typed(self, w3):
        """Test that we can get logs and the return is the type we expect."""
        deployed_contract = EventsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        deployed_contract.functions.emitOneEvent(0, "0x0000000000000000000000000000000000000000").transact()
        deployed_contract.functions.emitTwoEvents(1, "0x0000000000000000000000000000000000000000").transact()

        event_a_logs = list(
            deployed_contract.events.EventA.get_logs_typed(
                argument_filters={"who": "0x0000000000000000000000000000000000000000"},
                from_block=0,
            )
        )
        event_b_logs = list(
            deployed_contract.events.EventB.get_logs_typed(
                from_block=0,
            )
        )

        assert len(event_a_logs) == 2
        assert isinstance(event_a_logs[0], EventAEvent)
        assert event_a_logs[0].args.who == "0x0000000000000000000000000000000000000000"
        assert event_a_logs[0].args.value == 0
        assert isinstance(event_a_logs[1], EventAEvent)
        assert event_a_logs[1].args.who == "0x0000000000000000000000000000000000000000"
        assert event_a_logs[1].args.value == 1

        assert len(list(event_b_logs)) == 1
        assert isinstance(event_b_logs[0], EventBEvent)

    def test_create_filter(self, w3):
        """Test that we can use event filters."""
        deployed_contract = EventsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        tx_hash = deployed_contract.functions.emitOneEvent(0, "0x0000000000000000000000000000000000000000").transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)

        event_a_filter = deployed_contract.events.EventA.create_filter(
            argument_filters={"who": "0x0000000000000000000000000000000000000000"},
            from_block=0,
        )
        event_b_filter = deployed_contract.events.EventB.create_filter(
            from_block=0,
        )

        a_events = event_a_filter.get_new_entries()
        b_events = event_b_filter.get_new_entries()

        assert len(a_events) == 1
        assert len(b_events) == 0

        tx_hash = deployed_contract.functions.emitTwoEvents(0, "0x0000000000000000000000000000000000000000").transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)

        a_events = event_a_filter.get_new_entries()
        b_events = event_b_filter.get_new_entries()

        assert len(a_events) == 1
        assert len(b_events) == 1
