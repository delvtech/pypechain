"""Test fixture for deploying local anvil chain."""
from __future__ import annotations

import subprocess
import time
from typing import Iterator

import pytest
from eth_typing import URI
from web3 import Web3
from web3.middleware import geth_poa
from web3.types import RPCEndpoint

# pylint: disable=redefined-outer-name


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
def w3_init(local_chain) -> Web3:
    """gets a Web3 instance connected to the local chain.

    Parameters
    ----------
    local_chain : str
        A local anvil chain.

    Returns
    -------
    Web3
        A web3.py instance.
    """

    return initialize_web3_with_http_provider(local_chain)


@pytest.fixture(scope="function")
def w3(w3_init) -> Web3:  # type: ignore
    """resets the anvil instance at the function level so each test gets a fresh chain.

    Parameters
    ----------
    w3_init : Web3
        A web3.py instance.

    Returns
    -------
    Web3
        A web3.py instance.
    """
    w3_init.provider.make_request(method=RPCEndpoint("anvil_reset"), params=[])
    return w3_init


def initialize_web3_with_http_provider(
    ethereum_node: URI | str, request_kwargs: dict | None = None, reset_provider: bool = False
) -> Web3:
    """Initialize a Web3 instance using an HTTP provider and inject a geth Proof of Authority (poa) middleware.

    Arguments
    ---------
    ethereum_node: URI | str
        Address of the http provider
    request_kwargs: dict
        The HTTPProvider uses the python requests library for making requests.
        If you would like to modify how requests are made,
        you can use the request_kwargs to do so.

    Notes
    -----
    The geth_poa_middleware is required to connect to geth --dev or the Goerli public network.
    It may also be needed for other EVM compatible blockchains like Polygon or BNB Chain (Binance Smart Chain).
    See more `here <https://web3py.readthedocs.io/en/stable/middleware.html#proof-of-authority>`_.
    """
    if request_kwargs is None:
        request_kwargs = {}
    provider = Web3.HTTPProvider(ethereum_node, request_kwargs)
    web3 = Web3(provider)
    web3.middleware_onion.inject(geth_poa.geth_poa_middleware, layer=0)
    if reset_provider:
        # TODO: Check that the user is running on anvil, raise error if not
        _ = web3.provider.make_request(method=RPCEndpoint("anvil_reset"), params=[])
    return web3
