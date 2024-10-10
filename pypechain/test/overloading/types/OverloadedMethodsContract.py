"""A web3.py Contract class for the OverloadedMethods contract.

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

from . import OverloadedMethodsTypes as OverloadedMethods

structs = {
    "OverloadedMethods.SimpleStruct": OverloadedMethods.SimpleStruct,
    "OverloadedMethods.NestedStruct": OverloadedMethods.NestedStruct,
}


class OverloadedMethodsDoSomethingContractFunction0(PypechainContractFunction):
    """ContractFunction for the doSomething(list[OverloadedMethods.NestedStruct]) method."""

    _function_name = "doSomething"
    _type_signature = expand_struct_type_str(tuple(["list[OverloadedMethods.NestedStruct]"]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> list[OverloadedMethods.NestedStruct]:
        """returns list[OverloadedMethods.NestedStruct]."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = list[OverloadedMethods.NestedStruct]

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(list[OverloadedMethods.NestedStruct], rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class OverloadedMethodsDoSomethingContractFunction1(PypechainContractFunction):
    """ContractFunction for the doSomething(OverloadedMethods.SimpleStruct) method."""

    _function_name = "doSomething"
    _type_signature = expand_struct_type_str(tuple(["OverloadedMethods.SimpleStruct"]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> OverloadedMethods.SimpleStruct:
        """returns OverloadedMethods.SimpleStruct."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = OverloadedMethods.SimpleStruct

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(OverloadedMethods.SimpleStruct, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class OverloadedMethodsDoSomethingContractFunction2(PypechainContractFunction):
    """ContractFunction for the doSomething(int,str) method."""

    _function_name = "doSomething"
    _type_signature = expand_struct_type_str(tuple(["int", "str"]), structs)

    class ReturnValues(NamedTuple):
        """The return named tuple for DoSomething."""

        int_input: int
        arg2: str

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> ReturnValues:
        """returns ReturnValues."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = [int, str]

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return self.ReturnValues(*rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class OverloadedMethodsDoSomethingContractFunction3(PypechainContractFunction):
    """ContractFunction for the doSomething(list[OverloadedMethods.SimpleStruct]) method."""

    _function_name = "doSomething"
    _type_signature = expand_struct_type_str(tuple(["list[OverloadedMethods.SimpleStruct]"]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> list[OverloadedMethods.SimpleStruct]:
        """returns list[OverloadedMethods.SimpleStruct]."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = list[OverloadedMethods.SimpleStruct]

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(list[OverloadedMethods.SimpleStruct], rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class OverloadedMethodsDoSomethingContractFunction4(PypechainContractFunction):
    """ContractFunction for the doSomething() method."""

    _function_name = "doSomething"
    _type_signature = expand_struct_type_str(tuple([]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> int:
        """returns int."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = int

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(int, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class OverloadedMethodsDoSomethingContractFunction5(PypechainContractFunction):
    """ContractFunction for the doSomething(str) method."""

    _function_name = "doSomething"
    _type_signature = expand_struct_type_str(tuple(["str"]), structs)

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
                errors_class=OverloadedMethodsContractErrors,
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
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class OverloadedMethodsDoSomethingContractFunction6(PypechainContractFunction):
    """ContractFunction for the doSomething(int) method."""

    _function_name = "doSomething"
    _type_signature = expand_struct_type_str(tuple(["int"]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> int:
        """returns int."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = int

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(int, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class OverloadedMethodsDoSomethingContractFunction7(PypechainContractFunction):
    """ContractFunction for the doSomething(int,int) method."""

    _function_name = "doSomething"
    _type_signature = expand_struct_type_str(tuple(["int", "int"]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> int:
        """returns int."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = int

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(int, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedMethodsContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class OverloadedMethodsDoSomethingContractFunction(PypechainContractFunction):
    """ContractFunction for the doSomething method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "doSomething"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self, nestedStructVec: list[OverloadedMethods.NestedStruct]) -> OverloadedMethodsDoSomethingContractFunction0:  # type: ignore
        ...

    @overload
    def __call__(self, simpleStruct: OverloadedMethods.SimpleStruct) -> OverloadedMethodsDoSomethingContractFunction1:  # type: ignore
        ...

    @overload
    def __call__(self, x: int, s: str) -> OverloadedMethodsDoSomethingContractFunction2:  # type: ignore
        ...

    @overload
    def __call__(self, simpleStructVec: list[OverloadedMethods.SimpleStruct]) -> OverloadedMethodsDoSomethingContractFunction3:  # type: ignore
        ...

    @overload
    def __call__(self) -> OverloadedMethodsDoSomethingContractFunction4:  # type: ignore
        ...

    @overload
    def __call__(self, s: str) -> OverloadedMethodsDoSomethingContractFunction5:  # type: ignore
        ...

    @overload
    def __call__(self, x: int) -> OverloadedMethodsDoSomethingContractFunction6:  # type: ignore
        ...

    @overload
    def __call__(self, x: int, y: int) -> OverloadedMethodsDoSomethingContractFunction7:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> OverloadedMethodsDoSomethingContractFunction:  # type: ignore
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
            OverloadedMethodsDoSomethingContractFunction0._type_signature: OverloadedMethodsDoSomethingContractFunction0.factory(
                "OverloadedMethodsDoSomethingContractFunction0", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction1._type_signature: OverloadedMethodsDoSomethingContractFunction1.factory(
                "OverloadedMethodsDoSomethingContractFunction1", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction2._type_signature: OverloadedMethodsDoSomethingContractFunction2.factory(
                "OverloadedMethodsDoSomethingContractFunction2", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction3._type_signature: OverloadedMethodsDoSomethingContractFunction3.factory(
                "OverloadedMethodsDoSomethingContractFunction3", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction4._type_signature: OverloadedMethodsDoSomethingContractFunction4.factory(
                "OverloadedMethodsDoSomethingContractFunction4", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction5._type_signature: OverloadedMethodsDoSomethingContractFunction5.factory(
                "OverloadedMethodsDoSomethingContractFunction5", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction6._type_signature: OverloadedMethodsDoSomethingContractFunction6.factory(
                "OverloadedMethodsDoSomethingContractFunction6", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction7._type_signature: OverloadedMethodsDoSomethingContractFunction7.factory(
                "OverloadedMethodsDoSomethingContractFunction7", **kwargs
            ),
        }
        return out


class OverloadedMethodsContractFunctions(ContractFunctions):
    """ContractFunctions for the OverloadedMethods contract."""

    doSomething: OverloadedMethodsDoSomethingContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.doSomething = OverloadedMethodsDoSomethingContractFunction.factory(
            "doSomething",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="doSomething",
        )


overloadedmethods_abi: ABI = cast(
    ABI,
    [
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [
                {
                    "name": "nestedStructVec",
                    "type": "tuple[]",
                    "internalType": "struct OverloadedMethods.NestedStruct[]",
                    "components": [
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {
                            "name": "simpleStruct",
                            "type": "tuple",
                            "internalType": "struct OverloadedMethods.SimpleStruct",
                            "components": [
                                {"name": "strVal", "type": "string", "internalType": "string"},
                                {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                            ],
                        },
                    ],
                }
            ],
            "outputs": [
                {
                    "name": "outNestedStructVec",
                    "type": "tuple[]",
                    "internalType": "struct OverloadedMethods.NestedStruct[]",
                    "components": [
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {
                            "name": "simpleStruct",
                            "type": "tuple",
                            "internalType": "struct OverloadedMethods.SimpleStruct",
                            "components": [
                                {"name": "strVal", "type": "string", "internalType": "string"},
                                {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                            ],
                        },
                    ],
                }
            ],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [
                {
                    "name": "simpleStruct",
                    "type": "tuple",
                    "internalType": "struct OverloadedMethods.SimpleStruct",
                    "components": [
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                    ],
                }
            ],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple",
                    "internalType": "struct OverloadedMethods.SimpleStruct",
                    "components": [
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                    ],
                }
            ],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [
                {"name": "x", "type": "uint256", "internalType": "uint256"},
                {"name": "s", "type": "string", "internalType": "string"},
            ],
            "outputs": [
                {"name": "int_input", "type": "uint256", "internalType": "uint256"},
                {"name": "", "type": "string", "internalType": "string"},
            ],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [
                {
                    "name": "simpleStructVec",
                    "type": "tuple[]",
                    "internalType": "struct OverloadedMethods.SimpleStruct[]",
                    "components": [
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                    ],
                }
            ],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple[]",
                    "internalType": "struct OverloadedMethods.SimpleStruct[]",
                    "components": [
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                    ],
                }
            ],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [],
            "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [{"name": "s", "type": "string", "internalType": "string"}],
            "outputs": [{"name": "", "type": "string", "internalType": "string"}],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [{"name": "x", "type": "uint256", "internalType": "uint256"}],
            "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [
                {"name": "x", "type": "uint256", "internalType": "uint256"},
                {"name": "y", "type": "uint256", "internalType": "uint256"},
            ],
            "outputs": [{"name": "added", "type": "uint256", "internalType": "uint256"}],
            "stateMutability": "pure",
        },
    ],
)


class OverloadedMethodsContractErrors(PypechainBaseContractErrors):
    """ContractErrors for the OverloadedMethods contract."""

    def __init__(
        self,
    ) -> None:

        self._all = []


class OverloadedMethodsContract(Contract):
    """A web3.py Contract class for the OverloadedMethods contract."""

    abi: ABI = overloadedmethods_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b506107f9806100206000396000f3fe608060405234801561001057600080fd5b50600436106100885760003560e01c8063826926791161005b57806382692679146101395780638ae3048e1461014a578063a6b206bf14610165578063b2dd1d791461017857600080fd5b8063146c7dea1461008d5780631d37834b146100b45780633b6c27c4146100fe5780634a4c53e91461011e575b600080fd5b61009e61009b366004610324565b90565b6040516100ab91906104ae565b60405180910390f35b6100f16100c2366004610541565b604080518082018252606081526000602091820152815180830190925282518252918201519181019190915290565b6040516100ab919061057e565b61011061010c366004610591565b9091565b6040516100ab9291906105d8565b61012c61009b3660046105f1565b6040516100ab9190610695565b60025b6040519081526020016100ab565b61015861009b3660046106f9565b6040516100ab919061072e565b61013c610173366004610741565b61018b565b61013c61018636600461075a565b61019e565b600061019882600261077c565b92915050565b60006101aa82846107a1565b9392505050565b634e487b7160e01b600052604160045260246000fd5b6040516060810167ffffffffffffffff811182821017156101ea576101ea6101b1565b60405290565b604051601f8201601f1916810167ffffffffffffffff81118282101715610219576102196101b1565b604052919050565b600067ffffffffffffffff82111561023b5761023b6101b1565b5060051b60200190565b600082601f83011261025657600080fd5b813567ffffffffffffffff811115610270576102706101b1565b610283601f8201601f19166020016101f0565b81815284602083860101111561029857600080fd5b816020850160208301376000918101602001919091529392505050565b6000604082840312156102c757600080fd5b6040516040810167ffffffffffffffff82821081831117156102eb576102eb6101b1565b81604052829350843591508082111561030357600080fd5b5061031085828601610245565b825250602083013560208201525092915050565b6000602080838503121561033757600080fd5b823567ffffffffffffffff8082111561034f57600080fd5b818501915085601f83011261036357600080fd5b813561037661037182610221565b6101f0565b81815260059190911b8301840190848101908883111561039557600080fd5b8585015b83811015610432578035858111156103b15760008081fd5b86016060818c03601f19018113156103c95760008081fd5b6103d16101c7565b898301358152604080840135898111156103eb5760008081fd5b6103f98f8d83880101610245565b838d0152509183013591888311156104115760008081fd5b61041f8e8c858701016102b5565b9082015285525050918601918601610399565b5098975050505050505050565b6000815180845260005b8181101561046557602081850181015186830182015201610449565b506000602082860101526020601f19601f83011685010191505092915050565b600081516040845261049a604085018261043f565b602093840151949093019390935250919050565b600060208083018184528085518083526040925060408601915060408160051b87010184880160005b8381101561053357603f19898403018552815160608151855288820151818a8701526105058287018261043f565b9150508782015191508481038886015261051f8183610485565b9689019694505050908601906001016104d7565b509098975050505050505050565b60006020828403121561055357600080fd5b813567ffffffffffffffff81111561056a57600080fd5b610576848285016102b5565b949350505050565b6020815260006101aa6020830184610485565b600080604083850312156105a457600080fd5b82359150602083013567ffffffffffffffff8111156105c257600080fd5b6105ce85828601610245565b9150509250929050565b828152604060208201526000610576604083018461043f565b6000602080838503121561060457600080fd5b823567ffffffffffffffff8082111561061c57600080fd5b818501915085601f83011261063057600080fd5b813561063e61037182610221565b81815260059190911b8301840190848101908883111561065d57600080fd5b8585015b83811015610432578035858111156106795760008081fd5b6106878b89838a01016102b5565b845250918601918601610661565b600060208083016020845280855180835260408601915060408160051b87010192506020870160005b828110156106ec57603f198886030184526106da858351610485565b945092850192908501906001016106be565b5092979650505050505050565b60006020828403121561070b57600080fd5b813567ffffffffffffffff81111561072257600080fd5b61057684828501610245565b6020815260006101aa602083018461043f565b60006020828403121561075357600080fd5b5035919050565b6000806040838503121561076d57600080fd5b50508035926020909101359150565b808202811582820484141761019857634e487b7160e01b600052601160045260246000fd5b6000826107be57634e487b7160e01b600052601260045260246000fd5b50049056fea2646970667358221220bda866931d31d56519d7f24e2a69ea362471a83fcb4bd41e5fc750dac61ea0fb64736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = OverloadedMethodsContractFunctions(overloadedmethods_abi, self.w3, address)  # type: ignore

    functions: OverloadedMethodsContractFunctions

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
        contract.functions = OverloadedMethodsContractFunctions(overloadedmethods_abi, w3, None)

        return contract
