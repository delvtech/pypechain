"""A web3.py Contract class for the ContractC contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.46.
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

# methods are overridden with specific arguments instead of generic *args, **kwargs
# pylint: disable=arguments-differ

# consumers have too many opinions on line length
# pylint: disable=line-too-long

# We use protected classes within pypechain
# pylint: disable=protected-access

# We sometimes define a variable that might not be returned in `call`,
# but we still may want to call the function
# pylint: disable=unused-variable


from __future__ import annotations

import copy
from typing import Any, Type, cast, overload

from eth_account.signers.local import LocalAccount
from eth_typing import ABI, ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunctions
from web3.types import BlockIdentifier, StateOverride, TxParams

from pypechain.core import (
    PypechainBaseContractErrors,
    PypechainContractFunction,
    dataclass_to_tuple,
    expand_struct_type_str,
    get_arg_type_names,
    rename_returned_types,
)

from ..ContractA import ContractATypes as ContractA
from ..ContractB import ContractBTypes as ContractB

structs = {
    "ContractA.StructsA": ContractA.StructsA,
    "ContractB.InnerStruct": ContractB.InnerStruct,
    "ContractB.StructsB": ContractB.StructsB,
}

contractc_abi: ABI = cast(
    ABI,
    [
        {
            "type": "function",
            "name": "buildStruct",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple",
                    "internalType": "struct ContractB.StructsB",
                    "components": [
                        {
                            "name": "structA",
                            "type": "tuple",
                            "internalType": "struct ContractA.StructsA",
                            "components": [
                                {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                                {"name": "strVal", "type": "string", "internalType": "string"},
                            ],
                        },
                        {
                            "name": "structB",
                            "type": "tuple",
                            "internalType": "struct ContractB.InnerStruct",
                            "components": [
                                {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                                {"name": "strVal", "type": "string", "internalType": "string"},
                            ],
                        },
                    ],
                }
            ],
            "stateMutability": "pure",
        }
    ],
)


class ContractCContractErrors(PypechainBaseContractErrors):
    """ContractErrors for the ContractC contract."""

    def __init__(
        self,
    ) -> None:

        self._all = []


class ContractCBuildStructContractFunction0(PypechainContractFunction):
    """ContractFunction for the buildStruct() method."""

    _function_name = "buildStruct"
    _type_signature = expand_struct_type_str(tuple([]), structs)
    _error_class = ContractCContractErrors

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> ContractB.StructsB:
        """returns ContractB.StructsB."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = ContractB.StructsB

        # Call the function
        raw_values = self._call(transaction, block_identifier, state_override, ccip_read_enabled)

        return cast(ContractB.StructsB, rename_returned_types(structs, return_types, raw_values))


class ContractCBuildStructContractFunction(PypechainContractFunction):
    """ContractFunction for the buildStruct method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "buildStruct"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self) -> ContractCBuildStructContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> ContractCBuildStructContractFunction:  # type: ignore
        clone = super().__call__(
            *(dataclass_to_tuple(arg) for arg in args), **{key: dataclass_to_tuple(arg) for key, arg in kwargs.items()}
        )

        # Arguments is the flattened set of arguments from args and kwargs, ordered by the abi
        # We get the python types of the args passed in, but remapped from tuples -> dataclasses
        arg_types = get_arg_type_names(clone.arguments)

        # Look up the function class based on arg types.
        # We ensure we use a copy of the original object.
        function_obj = copy.copy(self._functions[arg_types])

        function_obj.args = clone.args
        function_obj.kwargs = clone.kwargs

        # The `@overload` of `__call__` takes care of setting the type of this object correctly
        return function_obj  # type: ignore

    @classmethod
    def factory(cls, class_name: str, **kwargs: Any) -> Self:
        out = super().factory(class_name, **kwargs)

        # We initialize our overridden functions here.
        # Note that we use the initialized object to ensure each function
        # is attached to the instanciated object
        # (attached to a specific web3 and contract address)
        out._functions = {
            ContractCBuildStructContractFunction0._type_signature: ContractCBuildStructContractFunction0.factory(
                "ContractCBuildStructContractFunction0", **kwargs
            ),
        }
        return out


class ContractCContractFunctions(ContractFunctions):
    """ContractFunctions for the ContractC contract."""

    buildStruct: ContractCBuildStructContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.buildStruct = ContractCBuildStructContractFunction.factory(
            "buildStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="buildStruct",
        )


class ContractCContract(Contract):
    """A web3.py Contract class for the ContractC contract."""

    abi: ABI = contractc_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b506101e2806100206000396000f3fe608060405234801561001057600080fd5b506004361061002b5760003560e01c8063a80476c814610030575b600080fd5b61003861004e565b604051610045919061016a565b60405180910390f35b6100566100cc565b6040518060400160405280604051806040016040528060018152602001604051806040016040528060018152602001606160f81b8152508152508152602001604051806040016040528060028152602001604051806040016040528060018152602001603160f91b815250815250815250905090565b6040805160808101825260009181019182526060808201529081908152602001610109604051806040016040528060008152602001606081525090565b905290565b80518252600060208083015160406020860152805180604087015260005b818110156101485782810184015187820160600152830161012c565b506000606082880101526060601f19601f830116870101935050505092915050565b602081526000825160406020840152610186606084018261010e565b90506020840151601f198483030160408501526101a3828261010e565b9594505050505056fea264697066735822122008df8170b2c76e5c63907987a567db4b097987ade9d37c5e5ffeabefcb313f9f64736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = ContractCContractFunctions(contractc_abi, self.w3, address)  # type: ignore

    functions: ContractCContractFunctions

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
        contract.functions = ContractCContractFunctions(contractc_abi, w3, None)

        return contract
