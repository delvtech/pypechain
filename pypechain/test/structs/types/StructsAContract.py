"""A web3.py Contract class for the StructsA contract.

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

from .IStructsTypes import InnerStruct, NestedStruct, SimpleStruct
from .StructsATypes import AStruct
from .utilities import rename_returned_types

structs = {
    "InnerStruct": InnerStruct,
    "NestedStruct": NestedStruct,
    "SimpleStruct": SimpleStruct,
    "AStruct": AStruct,
}


class StructsASingleNestedStructContractFunction(ContractFunction):
    """ContractFunction for the singleNestedStruct method."""

    def __call__(self) -> StructsASingleNestedStructContractFunction:  # type: ignore
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
    ) -> NestedStruct:
        """returns NestedStruct."""
        # Define the expected return types from the smart contract call

        return_types = NestedStruct

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(NestedStruct, rename_returned_types(structs, return_types, raw_values))


class StructsASingleSimpleStructContractFunction(ContractFunction):
    """ContractFunction for the singleSimpleStruct method."""

    def __call__(self) -> StructsASingleSimpleStructContractFunction:  # type: ignore
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


class StructsAStructAContractFunction(ContractFunction):
    """ContractFunction for the structA method."""

    def __call__(self) -> StructsAStructAContractFunction:  # type: ignore
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
    ) -> AStruct:
        """returns AStruct."""
        # Define the expected return types from the smart contract call

        return_types = AStruct

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(AStruct, rename_returned_types(structs, return_types, raw_values))


class StructsAContractFunctions(ContractFunctions):
    """ContractFunctions for the StructsA contract."""

    singleNestedStruct: StructsASingleNestedStructContractFunction

    singleSimpleStruct: StructsASingleSimpleStructContractFunction

    structA: StructsAStructAContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.singleNestedStruct = StructsASingleNestedStructContractFunction.factory(
            "singleNestedStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="singleNestedStruct",
        )
        self.singleSimpleStruct = StructsASingleSimpleStructContractFunction.factory(
            "singleSimpleStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="singleSimpleStruct",
        )
        self.structA = StructsAStructAContractFunction.factory(
            "structA",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="structA",
        )


structsa_abi: ABI = cast(
    ABI,
    [
        {
            "inputs": [],
            "name": "singleNestedStruct",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                        {
                            "components": [{"internalType": "bool", "name": "boolVal", "type": "bool"}],
                            "internalType": "struct IStructs.InnerStruct",
                            "name": "innerStruct",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct IStructs.NestedStruct",
                    "name": "",
                    "type": "tuple",
                }
            ],
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
        {
            "inputs": [],
            "name": "structA",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct StructsA.AStruct",
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
structsa_bytecode = HexStr(
    "0x608060405234801561000f575f80fd5b506104558061001d5f395ff3fe608060405234801561000f575f80fd5b506004361061003f575f3560e01c806311ba731f146100435780636456bc7914610061578063c567c2f31461007f575b5f80fd5b61004b61009d565b6040516100589190610304565b60405180910390f35b6100696100f5565b604051610076919061035e565b60405180910390f35b61008761014d565b60405161009491906103ff565b60405180910390f35b6100a56101bc565b6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d626572203100000000000000000000000000000000815250815250905090565b6100fd6101d5565b6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d626572203100000000000000000000000000000000815250815250905090565b6101556101ee565b6040518060600160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d6265722031000000000000000000000000000000008152508152602001604051806020016040528060011515815250815250905090565b60405180604001604052805f8152602001606081525090565b60405180604001604052805f8152602001606081525090565b60405180606001604052805f81526020016060815260200161020e610214565b81525090565b60405180602001604052805f151581525090565b5f819050919050565b61023a81610228565b82525050565b5f81519050919050565b5f82825260208201905092915050565b5f5b8381101561027757808201518184015260208101905061025c565b5f8484015250505050565b5f601f19601f8301169050919050565b5f61029c82610240565b6102a6818561024a565b93506102b681856020860161025a565b6102bf81610282565b840191505092915050565b5f604083015f8301516102df5f860182610231565b50602083015184820360208601526102f78282610292565b9150508091505092915050565b5f6020820190508181035f83015261031c81846102ca565b905092915050565b5f604083015f8301516103395f860182610231565b50602083015184820360208601526103518282610292565b9150508091505092915050565b5f6020820190508181035f8301526103768184610324565b905092915050565b5f8115159050919050565b6103928161037e565b82525050565b602082015f8201516103ac5f850182610389565b50505050565b5f606083015f8301516103c75f860182610231565b50602083015184820360208601526103df8282610292565b91505060408301516103f46040860182610398565b508091505092915050565b5f6020820190508181035f83015261041781846103b2565b90509291505056fea264697066735822122083246da06bca51bffc4bf245d9e0f6c1c617d3e52709030d0f1f175dbc881b5a64736f6c63430008170033"
)


class StructsAContract(Contract):
    """A web3.py Contract class for the StructsA contract."""

    abi: ABI = structsa_abi
    bytecode: bytes = HexBytes(structsa_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = StructsAContractFunctions(structsa_abi, self.w3, address)  # type: ignore

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    functions: StructsAContractFunctions

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
        current_nonce = w3.eth.get_transaction_count(account.address)
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
        contract.functions = StructsAContractFunctions(structsa_abi, w3, None)

        return contract
