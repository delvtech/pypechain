"""Tests for rendering the init file."""

import importlib.metadata
import os

from pypechain.utilities.templates import get_jinja_env

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


class TestRenderInit:
    """Tests rendering for the init file using snapshots"""

    def test_render_init(self, snapshot):
        """
        Tests the code gen init file using snapshots
        """

        env = get_jinja_env()
        init_template = env.get_template("init.py.jinja2")

        # TODO: add return types to function calls

        file_names = [
            "ContractFile1",
            "ContractFile2",
            "ContractFile3",
        ]

        init_code = init_template.render(
            pypechain_version=importlib.metadata.version("pypechain"),
            file_names=file_names,
        )

        snapshot.snapshot_dir = "snapshots"  # This line is optional.
        snapshot.assert_match(init_code, "expected_init.py")
