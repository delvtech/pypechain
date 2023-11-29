"""Tests for overloading methods."""
from __future__ import annotations

import os

import pytest

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.mark.usefixtures("process_contracts")
class TestEvents:
    """Tests events emitted from the contracts."""

    def test_event_filters(self, w3):
        """Test that we can use event filters."""
