"""Script to generate typed web3.py classes for solidity contracts."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from shutil import copy2
from typing import NamedTuple, Sequence

from pypechain.render.init import render_init_file
from pypechain.render.main import render_files
from pypechain.utilities.abi import AbiInfo, load_abi_infos_from_file


def main(argv: Sequence[str] | None = None) -> None:
    """Main entrypoint for pypechain cli.

    Parameters
    ----------
    argv : Sequence[str] | None, optional
        Command line arguments
    """
    abi_file_path, output_dir, line_length, apply_formatting = parse_arguments(argv)
    pypechain(abi_file_path, output_dir, line_length, apply_formatting)


def pypechain(
    abi_file_path: str, output_dir: str = "pypechain_types", line_length: int = 120, apply_formatting: bool = True
):
    """Generates class files for a given abi.

    Parameters
    ----------
    abi_file_path : str
        Path to the abi JSON file.
    output_dir: str, optional
        Path to the directory where files will be generated. Defaults to 'pypechain_types'.
    line_length : int, optional
        Optional argument for the output file's maximum line length. Defaults to 120.
    apply_formatting : bool, optional
        If True, autoflake, isort and black will be applied to the file in that order, by default True.
    """

    # TODO: move to end of main() so that files aren't cleared if something breaks during script
    # execution. Create/clear the output directory
    setup_directory(output_dir)

    # List to store all JSON ABI files to be processed
    json_files_to_process: list[Path] = []

    # Check if provided path is a directory or file
    if os.path.isdir(abi_file_path):
        # If directory, gather all JSON files recursively in the directory
        json_files_to_process.extend(gather_json_files(abi_file_path))
    else:
        # Otherwise, add the single file to the list
        json_files_to_process.append(Path(abi_file_path))

    # parse the files and gather AbiInfos.
    abi_infos: list[AbiInfo] = []
    for json_file in json_files_to_process:
        infos = load_abi_infos_from_file(json_file)
        abi_infos.extend(infos)

    file_names: list[str] = []

    # Now process all gathered files
    file_names = render_files(abi_infos, output_dir, line_length, apply_formatting)

    # Render the __init__.py file
    render_init_file(output_dir, file_names, line_length)

    # Copy utilities.py to the output_dir
    # Get the path to `utilities.py` (assuming it's in the same directory as your script)
    utilities_path = Path(__file__).parent / "templates/utilities.py"
    # Copy the file to the output directory
    copy2(utilities_path, output_dir)


def gather_json_files(directory: str) -> list:
    """Gathers all JSON files in the specified directory and its subdirectories."""
    return list(Path(directory).rglob("*.json"))


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
    apply_formatting: bool


def namespace_to_args(namespace: argparse.Namespace) -> Args:
    """Converts argprase.Namespace to Args."""
    return Args(
        abi_file_path=namespace.abi_file_path,
        output_dir=namespace.output_dir,
        line_length=namespace.line_length,
        apply_formatting=namespace.apply_formatting,
    )


def parse_arguments(argv: Sequence[str] | None = None) -> Args:
    """Parses input arguments"""
    parser = argparse.ArgumentParser(description="Generates class files for a given abi.")
    parser.add_argument(
        "abi_file_path",
        help="Path to the abi JSON file or directory containing multiple JSON files.",
    )

    parser.add_argument(
        "--output-dir",
        default="pypechain_types",
        help="Path to the directory where files will be generated. Defaults to pypechain_types.",
    )
    parser.add_argument(
        "--line-length",
        type=int,
        default=120,
        help="Optional argument for the output file's maximum line length. Defaults to 120.",
    )
    parser.add_argument(
        "--apply-formatting",
        type=bool,
        default=True,
        help="Optional argument to apply formatting to each file. Defaults to True.",
    )

    # Use system arguments if none were passed
    if argv is None:
        argv = sys.argv

    # If no arguments were passed, display the help message and exit
    if len(argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return namespace_to_args(parser.parse_args())


if __name__ == "__main__":
    main()
