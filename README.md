[![](https://codecov.io/gh/delvtech/pypechain/branch/main/graph/badge.svg?token=1S60MD42ZP)](https://app.codecov.io/gh/delvtech/pypechain?displayType=list)
[![](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![](https://img.shields.io/badge/testing-pytest-blue.svg)](https://docs.pytest.org/en/latest/contents.html)
<br><a href="https://app.codecov.io/gh/delvtech/pypechain?displayType=list"><img height="50px" src="https://codecov.io/gh/delvtech/pypechain/graphs/tree.svg?token=A3BTPZ02E6"><a>

# Pypechain

Static Python bindings for ethereum smart contracts.

- Parses JSON ABIs to create typesafe web3.py contract instances
- Functions have typesafe function parameters and return values
- Smart Contract internal types are exposed as dataclasses
- Contract event interfaces are exposed as typesafe classes

This project is a work-in-progress. All code is provided as is and without guarantee.

## Install

```bash
pip install --upgrade pypechain
```

For development install instructions, see toplevel [INSTALL.md](https://github.com/delvtech/pypechain/blob/main/INSTALL.md)

## Usage

```bash
#  pypechain <OUT_DIR>          <ABI_FILE>
❯❯ pypechain --out_dir=./build/ ./abis/ERC20.json
```

## Examples

Pypechain generates a Python module from compiled Solidity code in ABI format.
This enables access to typesafe contract, struct, and event objects, which greatly improves
the developer experience.

### Accessing contract balances

Using web3:
```python
from web3 import Web3
web3 = Web3()
base_token_address = "0xSomeAddress"
# Contract construction takes an ABI filepath string
base_token_contract = web3.eth.contract(
    abi=base_contract_abi, address=web3.to_checksum_address(base_token_address)
)
# Arbitrary function arguments and names forces one to examine the ABI JSON to know the values & types
# Additionally, the types are not specified as Python types in the ABI
fn_args = [user_address]
fn_kwargs = {}
# Get the contract function, which could then be evoked by e.g. `call()` or `transact()`
contract_function = base_token_contract.get_function_by_name("balanceOf")(*fn_args, **fn_kwargs)
# The function call also takes arbitrary args and kwargs
call_args = []
call_kwargs = {}
# return values is a dict with string keys, which minimizes discoverability & has no type assurances
return_values: dict[str, Any] = contract_function.call(*call_args, **call_kwargs)
```

Using Pypechain generated objects:

```python
    from web3 import Web3
    from pypechain_types import ERC20MintableContract
    
    web3 = Web3()
    base_token_address = "0xSomeAddress"
    user_address = "0xUserAddress"
    # Contracts include a factory function to initialize with your given web3 provider
    base_token_contract: ERC20MintableContract = ERC20MintableContract.factory(w3=web3)(base_token_address)
    # balanceOf is a class function, enabling IDE tab-completion, intuitive inspection, and typed outputs
    user_base_balance: int = base_token_contract.functions.balanceOf(user_address).call()
```

### Retrieving events
This example will demonstrate how to Retrieve events

### Understanding contracts
This example will demonstrate how a Python developer can use pypechain to translate and understand smart contracts.