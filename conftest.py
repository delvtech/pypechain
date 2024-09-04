"""Pypechain test fixtures."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
from typing import Iterator

import pytest
from eth_typing import URI
from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware
from web3.types import RPCEndpoint

from pypechain import pypechain

# pylint: disable=redefined-outer-name

# IMPORTANT NOTE!!!!!
# If you end up using this debugging method, this will catch exceptions before teardown of fixtures

# Use this in conjunction with the following launch.json configuration:
#      {
#        "name": "Debug Current Test",
#        "type": "python",
#        "request": "launch",
#        "module": "pytest",
#        "args": ["${file}", "-vs"],
#        "console": "integratedTerminal",
#        "justMyCode": true,
#        "env": {
#            "_PYTEST_RAISE": "1"
#        },
#      },
if os.getenv("_PYTEST_RAISE", "0") != "0":

    @pytest.hookimpl(tryfirst=True)
    def pytest_exception_interact(call):
        """Allows you to set breakpoints in pytest."""
        raise call.excinfo.value

    @pytest.hookimpl(tryfirst=True)
    def pytest_internalerror(excinfo):
        """Allows you to set breakpoints in pytest."""
        raise excinfo.value


@pytest.fixture(scope="session")
def local_chain() -> Iterator[str]:
    """Launch a local anvil chain for testing and kill the anvil chain after.

    Returns
    -------
    Iterator[str]
        Yields the local anvil chain URI
    """
    anvil_port = 9999
    host = "127.0.0.1"  # localhost

    # Assuming anvil command is accessible in path
    # running into issue with contract size without --code-size-limit arg

    # Using context manager here seems to make CI hang, so explicitly killing process at the end of yield
    # pylint: disable=consider-using-with
    anvil_process = subprocess.Popen(
        ["anvil", "--silent", "--host", "127.0.0.1", "--port", str(anvil_port), "--code-size-limit", "9999999999"]
    )

    local_chain_ = "http://" + host + ":" + str(anvil_port)

    # wait for anvil chain to initialize
    time.sleep(1)

    yield local_chain_

    # Kill anvil process at end
    anvil_process.kill()


@pytest.fixture(scope="session")
def w3_init(local_chain: str) -> Web3:
    """Get a Web3 instance connected to the local chain.

    Parameters
    ----------
    local_chain : str
        A local anvil chain.

    Returns
    -------
    tuple[Web3, Callable]
        A web3.py instance and a reset function.
    """

    w3_init = initialize_web3_with_http_provider(local_chain)

    return w3_init


@pytest.fixture(scope="function")
def w3(w3_init: Web3) -> Iterator[Web3]:
    """Reset the anvil instance at the function level so each test gets a fresh chain.

    Parameters
    ----------
    w3_init : tuple[Web3, Callable]
        A web3.py instance and a reset function.

    Returns
    -------
    Web3
        A web3.py instance.
    """
    response = w3_init.provider.make_request(method=RPCEndpoint("evm_snapshot"), params=[])
    snapshot_id: str | None = response.get("result")

    yield w3_init

    w3_init.provider.make_request(method=RPCEndpoint("evm_revert"), params=[snapshot_id])


def initialize_web3_with_http_provider(
    ethereum_node: URI | str, request_kwargs: dict | None = None, reset_provider: bool = False
) -> Web3:
    """Initialize a Web3 instance using an HTTP provider and inject a geth Proof of Authority (poa) middleware.

    Parameters
    ----------
    ethereum_node: URI | str
        Address of the http provider
    request_kwargs: dict
        The HTTPProvider uses the python requests library for making requests.
        If you would like to modify how requests are made,
        you can use the request_kwargs to do so.

    Notes
    -----
    The ExtraataToPOAMiddleware is required to connect to geth --dev or the Goerli public network.
    It may also be needed for other EVM compatible blockchains like Polygon or BNB Chain (Binance Smart Chain).
    See more `here <https://web3py.readthedocs.io/en/stable/middleware.html#proof-of-authority>`_.
    """
    if request_kwargs is None:
        request_kwargs = {}
    provider = Web3.HTTPProvider(ethereum_node, request_kwargs)
    web3 = Web3(provider)
    web3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)
    if reset_provider:
        # TODO: Check that the user is running on anvil, raise error if not
        _ = web3.provider.make_request(method=RPCEndpoint("anvil_reset"), params=[])
    return web3


def _format_json_dir(json_dir):
    for root, dirs, files in os.walk(json_dir):
        # Format any outer json files
        for file in files:
            if file.endswith(".json"):
                json_file = os.path.join(root, file)
                # Format the JSON file
                with open(json_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                with open(json_file, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=2)

        for d in dirs:
            _format_json_dir(d)


@pytest.fixture(scope="class")
def process_contracts(request):
    """Generate ABIs for all contracts and pypechain types from those abis."""

    # Don't regenerate files in CI, it can cause things to break in weird ways.
    if os.environ.get("IN_CI"):
        return

    # Define the contracts and abis directories
    test_dir = os.path.dirname(os.path.abspath(request.fspath))
    contracts_dir = os.path.join(test_dir, "contracts")
    abis_dir = os.path.join(test_dir, "abis")

    # Clear out the abis/ directory
    if os.path.exists(abis_dir):
        shutil.rmtree(abis_dir)
    os.makedirs(abis_dir, exist_ok=True)

    # Build the abis/ directory with forge
    command = f"forge build {contracts_dir} -o {abis_dir}"
    subprocess.run(command, shell=True, check=True)

    # TODO also test when building with solc
    # # Process each .sol file in the contracts directory and its subdirectories
    # for root, _, files in os.walk(contracts_dir):
    #     for file in files:
    #         if file.endswith(".sol"):
    #             contract_file = os.path.join(root, file)
    #             contract_name = os.path.basename(contract_file).replace(".sol", "")
    #             # output_file = os.path.join(abis_dir, f"{contract_name}.json")

    #             # Run the solc command
    #             # command = f"solc {contract_file} --combined-json abi,bin,metadata > {output_file}"
    #             # Run the forge command
    #             command = f"forge build {contract_file} -o {abis_dir}"
    #             subprocess.run(command, shell=True, check=True)

    # Format the output json files
    _format_json_dir(abis_dir)

    # Run the pypechain module after processing all contracts
    pypechain(f"{test_dir}/abis", f"{test_dir}/types")
