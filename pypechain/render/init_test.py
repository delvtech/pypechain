"""Tests for rendering the init file."""

import os

from pypechain.utilities.templates import get_jinja_env
from pypechain.utilities.types import RenderOutput

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

        file_outputs = [
            RenderOutput(filename="ContractFile1", definitions=["ContractFile1Contract"]),
            RenderOutput(filename="ContractFile2", definitions=["ContractFile2Contract"]),
            RenderOutput(filename="TypesFile", definitions=["Struct1"]),
            RenderOutput(filename="TypesFile", definitions=["Struct2"]),
        ]

        # To avoid having to regenerate snapshots per version bump, we hard code the test version to 0.0.0 here
        init_code = init_template.render(
            pypechain_version="_version_ignored",
            file_outputs=file_outputs,
        )

        snapshot.snapshot_dir = "snapshots"  # This line is optional.
        snapshot.assert_match(init_code, "expected_init.py")
