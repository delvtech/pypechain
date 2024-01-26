"""Tests for overloading methods."""

from __future__ import annotations

import os

import pytest
from web3 import Web3
from web3.logs import WARN

from pypechain.test.events.types import EventsContract

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.mark.usefixtures("process_contracts")
class TestEvents:
    """Tests events emitted from the contracts."""

    @pytest.mark.skip()
    def test_process_receipt(self, w3: Web3):
        """Test that we can use event filters."""
        deployed_contract = EventsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        hash_a = deployed_contract.functions.emitOneEvent(0, "0x0000000000000000000000000000000000000000").transact()
        receipt_a = w3.eth.get_transaction_receipt(hash_a)
        hash_b = deployed_contract.functions.emitTwoEvents(0, "0x0000000000000000000000000000000000000000").transact()
        receipt_b = w3.eth.get_transaction_receipt(hash_b)

        deployed_contract.events.EventA.process_receipt(receipt_a, WARN)
        deployed_contract.events.EventB.process_receipt(receipt_b, WARN)

    def test_get_logs(self, w3):
        """Test that we can use event filters."""
        deployed_contract = EventsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        deployed_contract.functions.emitOneEvent(0, "0x0000000000000000000000000000000000000000").transact()
        deployed_contract.functions.emitTwoEvents(0, "0x0000000000000000000000000000000000000000").transact()

        event_a_logs = deployed_contract.events.EventA.get_logs(
            argument_filters={"who": "0x0000000000000000000000000000000000000000"},
            fromBlock=0,
        )
        event_b_logs = deployed_contract.events.EventB.get_logs(
            fromBlock=0,
        )
        assert len(list(event_a_logs)) == 2
        assert len(list(event_b_logs)) == 1

    def test_create_filter(self, w3):
        """Test that we can use event filters."""
        deployed_contract = EventsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        tx_hash = deployed_contract.functions.emitOneEvent(0, "0x0000000000000000000000000000000000000000").transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)

        event_a_filter = deployed_contract.events.EventA.create_filter(
            argument_filters={"who": "0x0000000000000000000000000000000000000000"},
            fromBlock=0,
        )
        event_b_filter = deployed_contract.events.EventB.create_filter(
            fromBlock=0,
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
