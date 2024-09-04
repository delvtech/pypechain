"""A web3.py Contract class for the MyLibrary contract.

DO NOT EDIT.  This file was generated by pypechain.  See documentation at
https://github.com/delvtech/pypechain"""

# contracts have PascalCase names
# pylint: disable=invalid-name

# contracts control how many attributes and arguments we have in generated code
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments

# we don't need else statement if the other conditionals all have return,
# but it's easier to generate
# pylint: disable=no-else-return

# This file is bound to get very long depending on contract sizes.
# pylint: disable=too-many-lines

# methods are overriden with specific arguments instead of generic *args, **kwargs
# pylint: disable=arguments-differ

# consumers have too many opinions on line length
# pylint: disable=line-too-long


from __future__ import annotations

from typing import Any, Type, cast

from eth_account.signers.local import LocalAccount
from eth_typing import ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunction, ContractFunctions
from web3.exceptions import FallbackNotFound
from web3.types import ABI, BlockIdentifier, CallOverride, TxParams

from .utilities import dataclass_to_tuple, rename_returned_types

structs = {}


class MyLibraryAddContractFunction(ContractFunction):
    """ContractFunction for the add method."""

    def __call__(self, a: int, b: int) -> MyLibraryAddContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(a), dataclass_to_tuple(b))
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> int:
        """returns int."""
        # Define the expected return types from the smart contract call

        return_types = int

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(int, rename_returned_types(structs, return_types, raw_values))


class MyLibraryContractFunctions(ContractFunctions):
    """ContractFunctions for the MyLibrary contract."""

    add: MyLibraryAddContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.add = MyLibraryAddContractFunction.factory(
            "add",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="add",
        )


mylibrary_abi: ABI = cast(
    ABI,
    [
        {
            "type": "function",
            "name": "add",
            "inputs": [
                {"name": "a", "type": "int256", "internalType": "int256"},
                {"name": "b", "type": "int256", "internalType": "int256"},
            ],
            "outputs": [{"name": "", "type": "int256", "internalType": "int256"}],
            "stateMutability": "pure",
        }
    ],
)


class MyLibraryContract(Contract):
    """A web3.py Contract class for the MyLibrary contract."""

    abi: ABI = mylibrary_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x60f6610039600b82828239805160001a60731461002c57634e487b7160e01b600052600060045260246000fd5b30600052607381538281f3fe730000000000000000000000000000000000000000301460806040526004361060335760003560e01c8063a5f3c23b146038575b600080fd5b60476043366004606a565b6059565b60405190815260200160405180910390f35b600060638284608b565b9392505050565b60008060408385031215607c57600080fd5b50508035926020909101359150565b808201828112600083128015821682158216171560b857634e487b7160e01b600052601160045260246000fd5b50509291505056fea264697066735822122005a4ed8899d0d0b37e2e1469b5fa9e841609aeb03530a92c9c31c0993e8364b864736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = MyLibraryContractFunctions(mylibrary_abi, self.w3, address)  # type: ignore

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    functions: MyLibraryContractFunctions

    @classmethod
    def constructor(cls) -> ContractConstructor:  # type: ignore
        """Creates a transaction with the contract's constructor function.

        Parameters
        ----------

        w3 : Web3
            A web3 instance.
        account : LocalAccount
            The account to use to deploy the contract.

        Returns
        -------
        Self
            A deployed instance of the contract.

        """
        cls.bytecode = cls._raw_bytecode
        if cls.bytecode is not None:

            # bytecode needs to be in hex for web3
            cls.bytecode = HexBytes(cls.bytecode)

        return super().constructor()

    @classmethod
    def deploy(cls, w3: Web3, account: LocalAccount | ChecksumAddress) -> Self:
        """Deploys an instance of the contract.

        Parameters
        ----------
        w3 : Web3
            A web3 instance.
        account : LocalAccount
            The account to use to deploy the contract.

        Returns
        -------
        Self
            A deployed instance of the contract.
        """
        deployer = cls.factory(w3=w3)
        constructor_fn = deployer.constructor()

        # if an address is supplied, try to use a web3 default account
        if isinstance(account, str):
            tx_hash = constructor_fn.transact({"from": account})
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            deployed_contract = deployer(address=tx_receipt.contractAddress)  # type: ignore
            return deployed_contract

        # otherwise use the account provided.
        deployment_tx = constructor_fn.build_transaction()
        current_nonce = w3.eth.get_transaction_count(account.address, "pending")
        deployment_tx.update({"nonce": current_nonce})

        # Sign the transaction with local account private key
        signed_tx = account.sign_transaction(deployment_tx)

        # Send the signed transaction and wait for receipt
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        deployed_contract = deployer(address=tx_receipt.contractAddress)  # type: ignore
        return deployed_contract

    @classmethod
    def factory(cls, w3: Web3, class_name: str | None = None, **kwargs: Any) -> Type[Self]:
        """Initializes the contract object.

        Parameters
        ----------
        w3 : Web3
            A web3 instance.
        class_name: str | None
            The instance class name.

        Returns
        -------
        Self
            An instance of the contract class.
        """
        contract = super().factory(w3, class_name, **kwargs)
        contract.functions = MyLibraryContractFunctions(mylibrary_abi, w3, None)

        return contract
