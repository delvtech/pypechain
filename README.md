<p align="center">
  <img src="/docs/images/python-vaporwave.png" width="300" alt="Pypechain"><br>
  <img src="/docs/images/pypechain.svg" width="600" alt="Pypechain"><br>
  Type-safe Python bindings for Ethereum smart contracts!<br><br>
  <i>Used by</i> <br>
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/delvtech/agent0/blob/main/icons/agent0-dark.svg">
  <img alt="Delv" src="https://github.com/delvtech/agent0/blob/main/icons/agent0-light.svg">
  </picture>

  <!-- Badges -->
  <p align="center">
      <a href="https://app.codecov.io/gh/delvtech/pypechain?displayType=list"><img src="https://codecov.io/gh/delvtech/pypechain/branch/main/graph/badge.svg?token=1S60MD42ZP" alt="Codecov"></a>
      <a href="https://githb.com/delvtech/pypechain/LICENSE"><img src="https://img.shields.io/badge/license-Apache-brightgreen.svg" alt="License"></a>
      <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style: Black"></a>
      <a href="https://docs.pytest.org/en/latest/contents.html"><img src="https://img.shields.io/badge/testing-pytest-blue.svg" alt="Testing: Pytest"></a><br>
      <a href="https://app.codecov.io/gh/delvtech/pypechain?displayType=list"><img height="50px" src="https://codecov.io/gh/delvtech/pypechain/graphs/tree.svg?token=A3BTPZ02E6" alt="Codecov Tree"></a>
  </p>
</p>

## Features

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

## Packages 📦

| Package Name | Version                                                                                  | Description                                        |
| ------------ | ---------------------------------------------------------------------------------------- | -------------------------------------------------- |
| pypechain    | [![](https://img.shields.io/pypi/v/pypechain.svg)](<(https://pypi.org/pypi/pypechain/)>) | Codegen python interfaces for web3.py contracts.   |
| autoflake    | [![](https://img.shields.io/pypi/v/autoflake.svg)](<(https://pypi.org/pypi/autoflake/)>) | Removes unused imports and unused variables        |
| black        | [![](https://img.shields.io/pypi/v/black.svg)](<(https://pypi.org/pypi/black/)>)         | The uncompromising code formatter.                 |
| isort        | [![](https://img.shields.io/pypi/v/isort.svg)](<(https://pypi.org/pypi/isort/)>)         | A Python utility / library to sort Python imports. |
| jinja2       | [![](https://img.shields.io/pypi/v/jinja2.svg)](<(https://pypi.org/pypi/jinja2/)>)       | A very fast and expressive template engine.        |
| web3         | [![](https://img.shields.io/pypi/v/web3.svg)](<(https://pypi.org/pypi/web3/)>)           | web3.py                                            |

## Usage

Pypechain is primarily to be used via the CLI:

```
❯❯ pypechain -h

usage: pypechain [-h] [--output-dir OUTPUT_DIR] [--line-length LINE_LENGTH] abi_file_path

Generates class files for a given abi.

positional arguments:
  abi_file_path         Path to the abi JSON file or directory containing multiple JSON files.

options:
  -h, --help            show this help message and exit
  --output-dir OUTPUT_DIR
                        Path to the directory where files will be generated. Defaults to pypechain_types.
  --line-length LINE_LENGTH
                        Optional argument for the output file's maximum line length. Defaults to 80.
```

However, you can also run the `main` script directly from Python:

```python
from pypechain import pypechain

abi_dir = "some/abi/dir"
output_dir = "some/output/dir"

pypechain(abi_dir, output_dir)
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
user_address = "0xUserAddress"

# Contract construction takes an ABI filepath string
base_token_contract = web3.eth.contract(
    abi=base_contract_abi, address=web3.to_checksum_address(base_token_address)
)

# Arbitrary function arguments and names forces one to examine the ABI JSON to know the values & types
# Additionally, the types are not specified as Python types in the ABI
fn_args = [user_address]
fn_kwargs = {}

# HARD TO DISCOVER ALL FUNCTIONS AND THEIR ARGUMENTS
contract_function = base_token_contract.get_function_by_name("balanceOf")(*fn_args, **fn_kwargs)

# The function call also takes arbitrary args and kwargs
call_args = []
call_kwargs = {}

# UNTYPED RETURN VALUE!!
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
    base_token_contract: ERC20MintableContract = ERC20MintableContract.deploy(w3=web3, signer=user_address)

    # balanceOf is a class function, enabling IDE tab-completion, intuitive inspection, typed inputs and typed outputs
    user_base_balance: int = base_token_contract.functions.balanceOf(user_address).call()
```

### Understanding contracts

Solidity files can be difficult to read for native Python programmers that have little exposure to smart contract code.

```typescript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReturnTypes {

    struct SimpleStruct {
        uint intVal;
        string strVal;
    }

    struct InnerStruct {
        bool boolVal;
    }

    struct NestedStruct {
        uint intVal;
        string strVal;
        InnerStruct innerStruct;
    }

    function mixStructsAndPrimitives() public pure returns (SimpleStruct memory simpleStruct, NestedStruct memory, uint, string memory name, bool YesOrNo) {
        simpleStruct = SimpleStruct({
            intVal: 1,
            strVal: "You are number 1"
        });
        NestedStruct memory nestedStruct = NestedStruct({
            intVal: 2,
            strVal: "You are number 2",
            innerStruct: InnerStruct({boolVal: true})
        });

        return (simpleStruct, nestedStruct, 1, "ReturnTypesContract", false);
    }
}
```

Running pypechain on the compiled ABI from this contract produces code that is more intuitive for Python programmers.

```python
... # imports


@dataclass
class SimpleStruct:
    """SimpleStruct struct."""
    intVal: int
    strVal: str


@dataclass
class InnerStruct:
    """InnerStruct struct."""
    boolVal: bool


@dataclass
class NestedStruct:
    """NestedStruct struct."""
    intVal: int
    strVal: str
    innerStruct: InnerStruct

class ReturnTypesMixStructsAndPrimitivesContractFunction(ContractFunction):
    """ContractFunction for the mixStructsAndPrimitives method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for MixStructsAndPrimitives."""

        simpleStruct: SimpleStruct
        arg2: NestedStruct
        arg3: int
        name: str
        YesOrNo: bool

    def __call__(self) -> ReturnTypesMixStructsAndPrimitivesContractFunction:
        clone = super().__call__()
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> ReturnValues:
        """returns ReturnValues."""
        # Define the expected return types from the smart contract call
        return_types = [SimpleStruct, NestedStruct, int, str, bool]
        # Call the function
        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return self.ReturnValues(*rename_returned_types(return_types, raw_values))


class ReturnTypesContractFunctions(ContractFunctions):
    """ContractFunctions for the ReturnTypes contract."""

    mixStructsAndPrimitives: ReturnTypesMixStructsAndPrimitivesContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.mixStructsAndPrimitives = ReturnTypesMixStructsAndPrimitivesContractFunction.factory(
            "mixStructsAndPrimitives",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="mixStructsAndPrimitives",
        )


class ReturnTypesContract(Contract):
    """A web3.py Contract class for the ReturnTypes contract."""

    abi: ABI = returntypes_abi
    bytecode: bytes = HexBytes(returntypes_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = ReturnTypesContractFunctions(returntypes_abi, self.w3, address)
        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    functions: ReturnTypesContractFunctions

    @classmethod
    def deploy(cls, w3: Web3, signer: ChecksumAddress) -> Self:
        """Deploys and instance of the contract.

        Parameters
        ----------
        w3 : Web3
            A web3 instance.
        signer : ChecksumAddress
            The address to deploy the contract from.

        Returns
        -------
        Self
            A deployed instance of the contract.
        """
        deployer = cls.factory(w3=w3)
        tx_hash = deployer.constructor().transact({"from": signer})
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        deployed_contract = deployer(address=tx_receipt.contractAddress)  # type: ignore
        return deployed_contract

    @classmethod
    def factory(cls, w3: Web3, class_name: str | None = None, **kwargs: Any) -> Type[Self]:
        contract = super().factory(w3, class_name, **kwargs)
        contract.functions = ReturnTypesContractFunctions(returntypes_abi, w3, None)
        return contract
```

## Tests
We use pytest in our pypechain tests. Pytest, when ran locally, automatically compiles Solidity 
using [Foundry](https://book.getfoundry.sh/getting-started/installation), as well as running 
pypechain on the output abis.

If you run into issues during pytest, run `make clean; make build-test` to rebuild all solidity
and pypechain types in tests.

We also use [`pytest-snapshot`](https://pypi.org/project/pytest-snapshot/) for some tests to ensure
rendered files are as expected. If any changes are made to rendering that results in failures in snapshots, 
run `pytest --snapshot-update`, ensure the generated files in `snapshots/` are as expected, and commit the new
snapshots in `snapshots/` as part of the update.

TODO also add in tests compiled via solc. See `conftest.py` for more information.
