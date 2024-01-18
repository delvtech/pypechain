"""Tests recursive json discovery."""

import os

import pytest

from pypechain import pypechain_cli

# tests fixtures require passing the same name
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.fixture
def temp_dir_structure(tmpdir):
    """
    Creates a temporary directory structure with sample Solidity ABIs.
    """
    # Root directory
    root = tmpdir.mkdir("test_directory")

    # Subdirectories
    sub1 = root.mkdir("sub1")
    sub2 = root.mkdir("sub2")

    # Sample Solidity ABI JSONs
    abi1 = """
    {
        "abi":
            [
                {
                    "constant": true,
                    "inputs": [],
                    "name": "name",
                    "outputs": [{"name": "", "type": "string"}],
                    "payable": false,
                    "stateMutability": "view",
                    "type": "function"
                }
            ]
    }
    """

    abi2 = """
    {
        "abi":
            [
                {
                    "constant": true,
                    "inputs": [],
                    "name": "symbol",
                    "outputs": [{"name": "", "type": "string"}],
                    "payable": false,
                    "stateMutability": "view",
                    "type": "function"
                }
            ]
    }
    """

    abi3 = """
    {
        "abi":
            [
                {
                    "constant": true,
                    "inputs": [],
                    "name": "decimals",
                    "outputs": [{"name": "", "type": "uint8"}],
                    "payable": false,
                    "stateMutability": "view",
                    "type": "function"
                }
            ]
    }
    """

    # Write the ABIs to JSON files
    root.join("file1.json").write(abi1)
    sub1.join("file2.json").write(abi2)
    sub2.join("file3.json").write(abi3)

    return root


@pytest.mark.skip(reason="broken")
def test_recursive_json_discovery(temp_dir_structure):
    """
    Tests that the main() function recursively discovers JSON files and processes them.
    """
    # Output directory
    output_dir = temp_dir_structure.join("output")

    # Call main function
    pypechain_cli(argv=[str(temp_dir_structure), "--output-dir", str(output_dir)])

    # # Assertions
    assert os.path.exists(os.path.join(output_dir, "file1Contract.py"))
    assert os.path.exists(os.path.join(output_dir, "file1Types.py"))

    assert os.path.exists(os.path.join(output_dir, "file2Contract.py"))
    assert os.path.exists(os.path.join(output_dir, "file2Types.py"))

    assert os.path.exists(os.path.join(output_dir, "file3Contract.py"))
    assert os.path.exists(os.path.join(output_dir, "file3Types.py"))
