"""Script to generate typed web3.py classes for solidity contracts."""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import NamedTuple

from pypechain.render.main import render_files


def main() -> None:
    """Generates class files for a given abi.

    Arguments
    ---------
    abi_file_path : str
        Path to the abi JSON file.
    output_dr: str
        Path to the directory where files will be generated.
    line_length : int
        Optional argument for the output file's maximum line length. Defaults to 80.
    """
    parser = argparse.ArgumentParser(
        description="Generates class files for a given abi."
    )
    parser.add_argument(
        "abi_file_path",
        help="Path to the abi JSON file or directory containing multiple JSON files.",
    )

    parser.add_argument(
        "--output_dir",
        default="pypechain_types",
        help="Path to the directory where files will be generated. Defaults to pypechain_types.",
    )
    parser.add_argument(
        "--line_length",
        type=int,
        default=80,
        help="Optional argument for the output file's maximum line length. Defaults to 80.",
    )

    # If no arguments were passed, display the help message and exit
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args: Args = namespace_to_args(parser.parse_args())
    abi_file_path, output_dir, line_length = args

    # Set up the output directory
    setup_directory(output_dir)

    # Check if provided path is a directory or file
    if os.path.isdir(abi_file_path):
        # If directory, process all JSON files in the directory
        for json_file in Path(abi_file_path).glob("*.json"):
            render_files(str(json_file), output_dir, line_length)
    else:
        # Otherwise, process the single file
        render_files(abi_file_path, output_dir, line_length)


def setup_directory(directory: str) -> None:
    """Set up the output directory. If it exists, clear it. Otherwise, create it."""

    # If the directory exists, remove it
    if os.path.exists(directory):
        shutil.rmtree(directory)

    # Create the directory
    os.makedirs(directory)


class Args(NamedTuple):
    """Command line arguments for pypechain."""

    abi_file_path: str
    output_dir: str
    line_length: int


def namespace_to_args(namespace: argparse.Namespace) -> Args:
    """Converts argprase.Namespace to Args."""
    return Args(
        abi_file_path=namespace.abi_file_path,
        output_dir=namespace.output_dir,
        line_length=namespace.line_length,
    )


if __name__ == "__main__":
    main()
