"""A web3.py Contract class for the ConstructorWithStructArgs contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.43.
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
from typing import Any, NamedTuple, Type, cast, overload

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
    handle_contract_logic_error,
    rename_returned_types,
)

from ..ConstructorWithStructArgs import ConstructorWithStructArgsTypes as ConstructorWithStructArgs

structs = {
    "ConstructorWithStructArgs.Items": ConstructorWithStructArgs.Items,
    "ConstructorWithStructArgs.Config": ConstructorWithStructArgs.Config,
}


class ConstructorWithStructArgsNameContractFunction0(PypechainContractFunction):
    """ContractFunction for the name() method."""

    _function_name = "name"
    _type_signature = expand_struct_type_str(tuple([]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> str:
        """returns str."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = str

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(str, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def build_transaction(self, transaction: TxParams | None = None) -> TxParams:
        try:
            return super().build_transaction(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def sign_and_transact(self, account: LocalAccount, transaction: TxParams | None = None) -> HexBytes:
        """Convenience method for signing and sending a transaction using the provided account.

        Arguments
        ---------
        account : LocalAccount
            The account to use for signing and sending the transaction.
        transaction : TxParams | None, optional
            The transaction parameters to use for sending the transaction.

        Returns
        -------
        HexBytes
            The transaction hash.
        """
        if transaction is None:
            transaction_params: TxParams = {}
        else:
            transaction_params: TxParams = transaction

        if "from" in transaction_params:
            # Ensure if transaction is set, it matches
            assert (
                transaction_params["from"] == account.address
            ), f"Transaction from {transaction_params['from']} does not match account {account.address}"
        else:
            transaction_params["from"] = account.address

        # Build the raw transaction
        raw_transaction = self.build_transaction(transaction_params)

        if "nonce" not in raw_transaction:
            raw_transaction["nonce"] = self.w3.eth.get_transaction_count(account.address)

        # Sign the raw transaction
        # Mismatched types between account and web3py
        signed_transaction = account.sign_transaction(raw_transaction)  # type: ignore

        # Send the signed transaction
        try:
            return self.w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction_params,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class ConstructorWithStructArgsNameContractFunction(PypechainContractFunction):
    """ContractFunction for the name method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "name"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self) -> ConstructorWithStructArgsNameContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> ConstructorWithStructArgsNameContractFunction:  # type: ignore
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

        # We initialize our overridden functions here
        cls._functions = {
            ConstructorWithStructArgsNameContractFunction0._type_signature: ConstructorWithStructArgsNameContractFunction0.factory(
                "ConstructorWithStructArgsNameContractFunction0", **kwargs
            ),
        }
        return out


class ConstructorWithStructArgsSetNameContractFunction0(PypechainContractFunction):
    """ContractFunction for the setName(str) method."""

    _function_name = "setName"
    _type_signature = expand_struct_type_str(tuple(["str"]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> None:
        """returns None."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def build_transaction(self, transaction: TxParams | None = None) -> TxParams:
        try:
            return super().build_transaction(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def sign_and_transact(self, account: LocalAccount, transaction: TxParams | None = None) -> HexBytes:
        """Convenience method for signing and sending a transaction using the provided account.

        Arguments
        ---------
        account : LocalAccount
            The account to use for signing and sending the transaction.
        transaction : TxParams | None, optional
            The transaction parameters to use for sending the transaction.

        Returns
        -------
        HexBytes
            The transaction hash.
        """
        if transaction is None:
            transaction_params: TxParams = {}
        else:
            transaction_params: TxParams = transaction

        if "from" in transaction_params:
            # Ensure if transaction is set, it matches
            assert (
                transaction_params["from"] == account.address
            ), f"Transaction from {transaction_params['from']} does not match account {account.address}"
        else:
            transaction_params["from"] = account.address

        # Build the raw transaction
        raw_transaction = self.build_transaction(transaction_params)

        if "nonce" not in raw_transaction:
            raw_transaction["nonce"] = self.w3.eth.get_transaction_count(account.address)

        # Sign the raw transaction
        # Mismatched types between account and web3py
        signed_transaction = account.sign_transaction(raw_transaction)  # type: ignore

        # Send the signed transaction
        try:
            return self.w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction_params,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class ConstructorWithStructArgsSetNameContractFunction(PypechainContractFunction):
    """ContractFunction for the setName method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "setName"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self, name: str) -> ConstructorWithStructArgsSetNameContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> ConstructorWithStructArgsSetNameContractFunction:  # type: ignore
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

        # We initialize our overridden functions here
        cls._functions = {
            ConstructorWithStructArgsSetNameContractFunction0._type_signature: ConstructorWithStructArgsSetNameContractFunction0.factory(
                "ConstructorWithStructArgsSetNameContractFunction0", **kwargs
            ),
        }
        return out


class ConstructorWithStructArgsThingContractFunction0(PypechainContractFunction):
    """ContractFunction for the thing() method."""

    _function_name = "thing"
    _type_signature = expand_struct_type_str(tuple([]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> str:
        """returns str."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = str

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(str, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def build_transaction(self, transaction: TxParams | None = None) -> TxParams:
        try:
            return super().build_transaction(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def sign_and_transact(self, account: LocalAccount, transaction: TxParams | None = None) -> HexBytes:
        """Convenience method for signing and sending a transaction using the provided account.

        Arguments
        ---------
        account : LocalAccount
            The account to use for signing and sending the transaction.
        transaction : TxParams | None, optional
            The transaction parameters to use for sending the transaction.

        Returns
        -------
        HexBytes
            The transaction hash.
        """
        if transaction is None:
            transaction_params: TxParams = {}
        else:
            transaction_params: TxParams = transaction

        if "from" in transaction_params:
            # Ensure if transaction is set, it matches
            assert (
                transaction_params["from"] == account.address
            ), f"Transaction from {transaction_params['from']} does not match account {account.address}"
        else:
            transaction_params["from"] = account.address

        # Build the raw transaction
        raw_transaction = self.build_transaction(transaction_params)

        if "nonce" not in raw_transaction:
            raw_transaction["nonce"] = self.w3.eth.get_transaction_count(account.address)

        # Sign the raw transaction
        # Mismatched types between account and web3py
        signed_transaction = account.sign_transaction(raw_transaction)  # type: ignore

        # Send the signed transaction
        try:
            return self.w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ConstructorWithStructArgsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction_params,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class ConstructorWithStructArgsThingContractFunction(PypechainContractFunction):
    """ContractFunction for the thing method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "thing"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self) -> ConstructorWithStructArgsThingContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> ConstructorWithStructArgsThingContractFunction:  # type: ignore
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

        # We initialize our overridden functions here
        cls._functions = {
            ConstructorWithStructArgsThingContractFunction0._type_signature: ConstructorWithStructArgsThingContractFunction0.factory(
                "ConstructorWithStructArgsThingContractFunction0", **kwargs
            ),
        }
        return out


class ConstructorWithStructArgsContractFunctions(ContractFunctions):
    """ContractFunctions for the ConstructorWithStructArgs contract."""

    name: ConstructorWithStructArgsNameContractFunction

    setName: ConstructorWithStructArgsSetNameContractFunction

    thing: ConstructorWithStructArgsThingContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.name = ConstructorWithStructArgsNameContractFunction.factory(
            "name",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="name",
        )
        self.setName = ConstructorWithStructArgsSetNameContractFunction.factory(
            "setName",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="setName",
        )
        self.thing = ConstructorWithStructArgsThingContractFunction.factory(
            "thing",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="thing",
        )


constructorwithstructargs_abi: ABI = cast(
    ABI,
    [
        {
            "type": "constructor",
            "inputs": [
                {
                    "name": "config",
                    "type": "tuple",
                    "internalType": "struct ConstructorWithStructArgs.Config",
                    "components": [
                        {"name": "name", "type": "string", "internalType": "string"},
                        {
                            "name": "items",
                            "type": "tuple",
                            "internalType": "struct ConstructorWithStructArgs.Items",
                            "components": [
                                {"name": "thing", "type": "string", "internalType": "string"},
                                {"name": "yesOrNo", "type": "bool", "internalType": "bool"},
                            ],
                        },
                    ],
                }
            ],
            "stateMutability": "nonpayable",
        },
        {
            "type": "function",
            "name": "name",
            "inputs": [],
            "outputs": [{"name": "", "type": "string", "internalType": "string"}],
            "stateMutability": "view",
        },
        {
            "type": "function",
            "name": "setName",
            "inputs": [{"name": "_name", "type": "string", "internalType": "string"}],
            "outputs": [],
            "stateMutability": "nonpayable",
        },
        {
            "type": "function",
            "name": "thing",
            "inputs": [],
            "outputs": [{"name": "", "type": "string", "internalType": "string"}],
            "stateMutability": "view",
        },
    ],
)


class ConstructorWithStructArgsContractErrors(PypechainBaseContractErrors):
    """ContractErrors for the ConstructorWithStructArgs contract."""

    def __init__(
        self,
    ) -> None:

        self._all = []


class ConstructorWithStructArgsContract(Contract):
    """A web3.py Contract class for the ConstructorWithStructArgs contract."""

    abi: ABI = constructorwithstructargs_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x60806040526002805460ff1916905534801561001a57600080fd5b506040516107673803806107678339810160408190526100399161016d565b805160009061004890826102d6565b5060208101515160019061005c90826102d6565b5060209081015101516002805460ff1916911515919091179055610395565b634e487b7160e01b600052604160045260246000fd5b604080519081016001600160401b03811182821017156100b3576100b361007b565b60405290565b604051601f8201601f191681016001600160401b03811182821017156100e1576100e161007b565b604052919050565b600082601f8301126100fa57600080fd5b81516001600160401b038111156101135761011361007b565b6020610127601f8301601f191682016100b9565b828152858284870101111561013b57600080fd5b60005b8381101561015957858101830151828201840152820161013e565b506000928101909101919091529392505050565b60006020828403121561017f57600080fd5b81516001600160401b038082111561019657600080fd5b90830190604082860312156101aa57600080fd5b6101b2610091565b8251828111156101c157600080fd5b6101cd878286016100e9565b8252506020830151828111156101e257600080fd5b9290920191604083870312156101f757600080fd5b6101ff610091565b83518381111561020e57600080fd5b61021a888287016100e9565b82525060208401519350831515841461023257600080fd5b8360208201528060208301525080935050505092915050565b600181811c9082168061025f57607f821691505b60208210810361027f57634e487b7160e01b600052602260045260246000fd5b50919050565b601f8211156102d1576000816000526020600020601f850160051c810160208610156102ae5750805b601f850160051c820191505b818110156102cd578281556001016102ba565b5050505b505050565b81516001600160401b038111156102ef576102ef61007b565b610303816102fd845461024b565b84610285565b602080601f83116001811461033857600084156103205750858301515b600019600386901b1c1916600185901b1785556102cd565b600085815260208120601f198616915b8281101561036757888601518255948401946001909101908401610348565b50858210156103855787850151600019600388901b60f8161c191681555b5050505050600190811b01905550565b6103c3806103a46000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c806306fdde0314610046578063c47f002714610064578063c55e90fe14610079575b600080fd5b61004e610081565b60405161005b919061012c565b60405180910390f35b610077610072366004610191565b61010f565b005b61004e61011f565b6000805461008e90610242565b80601f01602080910402602001604051908101604052809291908181526020018280546100ba90610242565b80156101075780601f106100dc57610100808354040283529160200191610107565b820191906000526020600020905b8154815290600101906020018083116100ea57829003601f168201915b505050505081565b600061011b82826102cd565b5050565b6001805461008e90610242565b60006020808352835180602085015260005b8181101561015a5785810183015185820160400152820161013e565b506000604082860101526040601f19601f8301168501019250505092915050565b634e487b7160e01b600052604160045260246000fd5b6000602082840312156101a357600080fd5b813567ffffffffffffffff808211156101bb57600080fd5b818401915084601f8301126101cf57600080fd5b8135818111156101e1576101e161017b565b604051601f8201601f19908116603f011681019083821181831017156102095761020961017b565b8160405282815287602084870101111561022257600080fd5b826020860160208301376000928101602001929092525095945050505050565b600181811c9082168061025657607f821691505b60208210810361027657634e487b7160e01b600052602260045260246000fd5b50919050565b601f8211156102c8576000816000526020600020601f850160051c810160208610156102a55750805b601f850160051c820191505b818110156102c4578281556001016102b1565b5050505b505050565b815167ffffffffffffffff8111156102e7576102e761017b565b6102fb816102f58454610242565b8461027c565b602080601f83116001811461033057600084156103185750858301515b600019600386901b1c1916600185901b1785556102c4565b600085815260208120601f198616915b8281101561035f57888601518255948401946001909101908401610340565b508582101561037d5787850151600019600388901b60f8161c191681555b5050505050600190811b0190555056fea2646970667358221220fb50b7afb6125dd2706f2243bf1b2b3f463ade0f1235b0bc5839d97b95a021c764736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = ConstructorWithStructArgsContractFunctions(constructorwithstructargs_abi, self.w3, address)  # type: ignore

    functions: ConstructorWithStructArgsContractFunctions

    class ConstructorArgs(NamedTuple):
        """Arguments to pass the contract's constructor function."""

        config: ConstructorWithStructArgs.Config

    @classmethod
    def constructor(cls, config: ConstructorWithStructArgs.Config) -> ContractConstructor:  # type: ignore
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

        return super().constructor(dataclass_to_tuple(config))

    @classmethod
    def deploy(cls, w3: Web3, account: LocalAccount | ChecksumAddress, constructor_args: ConstructorArgs) -> Self:
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
        constructor_fn = deployer.constructor(
            *constructor_args,
        )

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
        contract.functions = ConstructorWithStructArgsContractFunctions(constructorwithstructargs_abi, w3, None)

        return contract
