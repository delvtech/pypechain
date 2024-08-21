"""A web3.py Contract class for the StructsB contract.

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
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunction, ContractFunctions
from web3.exceptions import FallbackNotFound
from web3.types import ABI, BlockIdentifier, CallOverride, TxParams

from .IStructsTypes import SimpleStruct
from .utilities import dataclass_to_tuple, rename_returned_types, try_bytecode_hexbytes

structs = {
    "SimpleStruct": SimpleStruct,
}


class StructsBNoNameSingleValueContractFunction(ContractFunction):
    """ContractFunction for the noNameSingleValue method."""

    def __call__(self, x: int) -> StructsBNoNameSingleValueContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(x))
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


class StructsBSingleSimpleStructContractFunction(ContractFunction):
    """ContractFunction for the singleSimpleStruct method."""

    def __call__(self) -> StructsBSingleSimpleStructContractFunction:  # type: ignore
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
    ) -> SimpleStruct:
        """returns SimpleStruct."""
        # Define the expected return types from the smart contract call

        return_types = SimpleStruct

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(SimpleStruct, rename_returned_types(structs, return_types, raw_values))


class StructsBContractFunctions(ContractFunctions):
    """ContractFunctions for the StructsB contract."""

    noNameSingleValue: StructsBNoNameSingleValueContractFunction

    singleSimpleStruct: StructsBSingleSimpleStructContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.noNameSingleValue = StructsBNoNameSingleValueContractFunction.factory(
            "noNameSingleValue",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="noNameSingleValue",
        )
        self.singleSimpleStruct = StructsBSingleSimpleStructContractFunction.factory(
            "singleSimpleStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="singleSimpleStruct",
        )


structsb_abi: ABI = cast(
    ABI,
    [
        {
            "inputs": [{"internalType": "uint256", "name": "x", "type": "uint256"}],
            "name": "noNameSingleValue",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "singleSimpleStruct",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct IStructs.SimpleStruct",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "pure",
            "type": "function",
        },
    ],
)
# pylint: disable=line-too-long
structsb_bytecode = HexStr(
    "0x608060405234801561000f575f80fd5b506102b38061001d5f395ff3fe608060405234801561000f575f80fd5b5060043610610034575f3560e01c8063389e9102146100385780636456bc7914610068575b5f80fd5b610052600480360381019061004d9190610137565b610086565b60405161005f9190610171565b60405180910390f35b61007061008f565b60405161007d919061025d565b60405180910390f35b5f819050919050565b6100976100e7565b6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d626572203100000000000000000000000000000000815250815250905090565b60405180604001604052805f8152602001606081525090565b5f80fd5b5f819050919050565b61011681610104565b8114610120575f80fd5b50565b5f813590506101318161010d565b92915050565b5f6020828403121561014c5761014b610100565b5b5f61015984828501610123565b91505092915050565b61016b81610104565b82525050565b5f6020820190506101845f830184610162565b92915050565b61019381610104565b82525050565b5f81519050919050565b5f82825260208201905092915050565b5f5b838110156101d05780820151818401526020810190506101b5565b5f8484015250505050565b5f601f19601f8301169050919050565b5f6101f582610199565b6101ff81856101a3565b935061020f8185602086016101b3565b610218816101db565b840191505092915050565b5f604083015f8301516102385f86018261018a565b506020830151848203602086015261025082826101eb565b9150508091505092915050565b5f6020820190508181035f8301526102758184610223565b90509291505056fea2646970667358221220352d075827d41fbea731eb01becf07d37fe207c4d0380dc5e6cc1d12d810ec4864736f6c63430008170033"
)


class StructsBContract(Contract):
    """A web3.py Contract class for the StructsB contract."""

    abi: ABI = structsb_abi
    bytecode: bytes | None = try_bytecode_hexbytes(structsb_bytecode, "structsb")

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = StructsBContractFunctions(structsb_abi, self.w3, address)  # type: ignore

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    functions: StructsBContractFunctions

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

        return super().constructor()

    @classmethod
    def deploy(cls, w3: Web3, account: LocalAccount | ChecksumAddress) -> Self:
        """Deploys and instance of the contract.

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
        """Deploys and instance of the contract.

        Parameters
        ----------
        w3 : Web3
            A web3 instance.
        class_name: str | None
            The instance class name.

        Returns
        -------
        Self
            A deployed instance of the contract.
        """
        contract = super().factory(w3, class_name, **kwargs)
        contract.functions = StructsBContractFunctions(structsb_abi, w3, None)

        return contract
