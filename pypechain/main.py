"""Script to generate typed web3.py classes for solidity contracts."""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from shutil import copy2
from typing import NamedTuple, Sequence

from web3.exceptions import NoABIFunctionsFound

from pypechain.render.init import render_init_file
from pypechain.render.main import render_files


def main(argv: Sequence[str] | None = None) -> None:
    """Generates class files for a given abi.

    Arguments
    ---------
    abi_file_path : str
        Path to the abi JSON file.
    output_dir: str
        Path to the directory where files will be generated.
    line_length : int
        Optional argument for the output file's maximum line length. Defaults to 80.
    """

    abi_file_path, output_dir, line_length = parse_arguments(argv)

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

    file_names: list[str] = []

    # Now process all gathered files
    for json_file in json_files_to_process:
        try:
            rendered_file_names = render_files(str(json_file), output_dir, line_length)
            file_names.extend(rendered_file_names)
        except NoABIFunctionsFound:
            # TODO: use logging
            print(f"No ABI Functions found in {json_file}, skipping...")
        except BaseException as err:
            print(f"Error creating types for {json_file}")
            raise err

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


def namespace_to_args(namespace: argparse.Namespace) -> Args:
    """Converts argprase.Namespace to Args."""
    return Args(
        abi_file_path=namespace.abi_file_path,
        output_dir=namespace.output_dir,
        line_length=namespace.line_length,
    )


def parse_arguments(argv: Sequence[str] | None = None) -> Args:
    """Parses input arguments"""
    parser = argparse.ArgumentParser(description="Generates class files for a given abi.")
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
        default=120,
        help="Optional argument for the output file's maximum line length. Defaults to 120.",
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
