"""A web3.py Contract class for the StructsA contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.41.
See documentation at https://github.com/delvtech/pypechain """

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
from eth_typing import ABI, ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunction, ContractFunctions
from web3.types import BlockIdentifier, StateOverride, TxParams

from pypechain.core import rename_returned_types

from .IStructsTypes import InnerStruct, NestedStruct, SimpleStruct
from .StructsATypes import AStruct

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
        state_override: StateOverride | None = None,
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
        state_override: StateOverride | None = None,
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
        state_override: StateOverride | None = None,
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
            abi_element_identifier="singleNestedStruct",
        )
        self.singleSimpleStruct = StructsASingleSimpleStructContractFunction.factory(
            "singleSimpleStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="singleSimpleStruct",
        )
        self.structA = StructsAStructAContractFunction.factory(
            "structA",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="structA",
        )


structsa_abi: ABI = cast(
    ABI,
    [
        {
            "type": "function",
            "name": "singleNestedStruct",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple",
                    "internalType": "struct IStructs.NestedStruct",
                    "components": [
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {
                            "name": "innerStruct",
                            "type": "tuple",
                            "internalType": "struct IStructs.InnerStruct",
                            "components": [{"name": "boolVal", "type": "bool", "internalType": "bool"}],
                        },
                    ],
                }
            ],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "singleSimpleStruct",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple",
                    "internalType": "struct IStructs.SimpleStruct",
                    "components": [
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                        {"name": "strVal", "type": "string", "internalType": "string"},
                    ],
                }
            ],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "structA",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple",
                    "internalType": "struct StructsA.AStruct",
                    "components": [
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                        {"name": "strVal", "type": "string", "internalType": "string"},
                    ],
                }
            ],
            "stateMutability": "pure",
        },
    ],
)


class StructsAContract(Contract):
    """A web3.py Contract class for the StructsA contract."""

    abi: ABI = structsa_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b5061024e806100206000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c806311ba731f146100465780636456bc7914610046578063c567c2f3146100a5575b600080fd5b604080518082018252600081526060602091820152815180830183526001815282518084018452601081526f596f7520617265206e756d626572203160801b8184015291810191909152905161009c91906101bf565b60405180910390f35b6100ad6100ba565b60405161009c91906101d9565b6100c261011c565b6040518060600160405280600181526020016040518060400160405280601081526020016f596f7520617265206e756d626572203160801b8152508152602001604051806020016040528060011515815250815250905090565b6040518060600160405280600081526020016060815260200161014d60405180602001604052806000151581525090565b905290565b6000815180845260005b818110156101785760208185018101518683018201520161015c565b506000602082860101526020601f19601f83011685010191505092915050565b8051825260006020820151604060208501526101b76040850182610152565b949350505050565b6020815260006101d26020830184610198565b9392505050565b602081528151602082015260006020830151606060408401526101ff6080840182610152565b905060408401515115156060840152809150509291505056fea2646970667358221220bc1b4d24faa73bb69c7c733cb49b490e847da06a9083c0d28e077d44105cf11564736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = StructsAContractFunctions(structsa_abi, self.w3, address)  # type: ignore

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
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
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
        contract.functions = StructsAContractFunctions(structsa_abi, w3, None)

        return contract
