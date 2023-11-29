"""A web3.py Contract class for the OverloadedMethods contract.

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

from __future__ import annotations

from dataclasses import fields, is_dataclass
from typing import Any, NamedTuple, Tuple, Type, TypeVar, cast, overload

from eth_typing import ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractFunction, ContractFunctions
from web3.exceptions import FallbackNotFound
from web3.types import ABI, BlockIdentifier, CallOverride, TxParams


T = TypeVar("T")

structs = {}


def tuple_to_dataclass(cls: type[T], tuple_data: Any | Tuple[Any, ...]) -> T:
    """
    Converts a tuple (including nested tuples) to a dataclass instance.  If cls is not a dataclass,
    then the data will just be passed through this function.

    Arguments
    ---------
    cls: type[T]
        The dataclass type to which the tuple data is to be converted.
    tuple_data: Any | Tuple[Any, ...]
        A tuple (or nested tuple) of values to convert into a dataclass instance.

    Returns
    -------
    T
        Either an instance of cls populated with data from tuple_data or tuple_data itself.
    """
    if not is_dataclass(cls):
        return cast(T, tuple_data)

    field_types = {field.name: field.type for field in fields(cls)}
    field_values = {}

    for (field_name, field_type), value in zip(field_types.items(), tuple_data):
        field_type = structs.get(field_type, field_type)
        if is_dataclass(field_type):
            # Recursively convert nested tuples to nested dataclasses
            field_values[field_name] = tuple_to_dataclass(field_type, value)
        elif (
            isinstance(value, tuple)
            and not getattr(field_type, "_name", None) == "Tuple"
        ):
            # If it's a tuple and the field is not intended to be a tuple, assume it's a nested dataclass
            field_values[field_name] = tuple_to_dataclass(field_type, value)
        else:
            # Otherwise, set the primitive value directly
            field_values[field_name] = value

    return cls(**field_values)


def rename_returned_types(return_types, raw_values) -> Any:
    """_summary_

    Parameters
    ----------
    return_types : _type_
        _description_
    raw_values : _type_
        _description_

    Returns
    -------
    tuple
        _description_
    """
    # cover case of multiple return values
    if isinstance(return_types, list):
        # Ensure raw_values is a tuple for consistency
        if not isinstance(raw_values, list):
            raw_values = (raw_values,)

        # Convert the tuple to the dataclass instance using the utility function
        converted_values = tuple(
            (
                tuple_to_dataclass(return_type, value)
                for return_type, value in zip(return_types, raw_values)
            )
        )

        return converted_values


class OverloadedMethodsDoSomethingContractFunction0(ContractFunction):
    """ContractFunction for the doSomething method."""

    def __call__(self, x: int, s: str) -> "OverloadedMethodsDoSomethingContractFunction":  # type: ignore
        super().__call__(x, s)
        return self

    class ReturnValues(NamedTuple):
        """The return named tuple for DoSomething."""

        added: int
        arg2: str

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> ReturnValues:
        """returns ReturnValues."""
        # Define the expected return types from the smart contract call

        return_types = self.ReturnValues

        # Call the function
        raw_values = super().call(
            transaction, block_identifier, state_override, ccip_read_enabled
        )

        return self.ReturnValues(
            rename_returned_types(return_types, raw_values)
        )


class OverloadedMethodsDoSomethingContractFunction1(ContractFunction):
    """ContractFunction for the doSomething method."""

    def __call__(self, s: str) -> "OverloadedMethodsDoSomethingContractFunction":  # type: ignore
        super().__call__(s)
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> str:
        """returns str."""
        # Define the expected return types from the smart contract call

        return_types = str

        # Call the function
        raw_values = super().call(
            transaction, block_identifier, state_override, ccip_read_enabled
        )

        return rename_returned_types(return_types, raw_values)


class OverloadedMethodsDoSomethingContractFunction2(ContractFunction):
    """ContractFunction for the doSomething method."""

    def __call__(self, x: int) -> "OverloadedMethodsDoSomethingContractFunction":  # type: ignore
        super().__call__(x)
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
        raw_values = super().call(
            transaction, block_identifier, state_override, ccip_read_enabled
        )

        return rename_returned_types(return_types, raw_values)


class OverloadedMethodsDoSomethingContractFunction3(ContractFunction):
    """ContractFunction for the doSomething method."""

    def __call__(self, x: int, y: int) -> "OverloadedMethodsDoSomethingContractFunction":  # type: ignore
        super().__call__(x, y)
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
        raw_values = super().call(
            transaction, block_identifier, state_override, ccip_read_enabled
        )

        return rename_returned_types(return_types, raw_values)


class OverloadedMethodsDoSomethingContractFunction(ContractFunction):
    """ContractFunction for the doSomething method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    @overload
    def __call__(self, x: int, s: str) -> OverloadedMethodsDoSomethingContractFunction0:  # type: ignore
        ...

    @overload
    def __call__(self, s: str) -> OverloadedMethodsDoSomethingContractFunction1:  # type: ignore
        ...

    @overload
    def __call__(self, x: int) -> OverloadedMethodsDoSomethingContractFunction2:  # type: ignore
        ...

    @overload
    def __call__(self, x: int, y: int) -> OverloadedMethodsDoSomethingContractFunction3:  # type: ignore
        ...

    def __call__(self, *args) -> OverloadedMethodsDoSomethingContractFunction:  # type: ignore
        clone = super().__call__(*args)
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self  # type: ignore


class OverloadedMethodsContractFunctions(ContractFunctions):
    """ContractFunctions for the OverloadedMethods contract."""

    doSomething: OverloadedMethodsDoSomethingContractFunction


overloadedmethods_abi: ABI = cast(
    ABI,
    [
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "string", "name": "s", "type": "string"},
            ],
            "name": "doSomething",
            "outputs": [
                {"internalType": "uint256", "name": "added", "type": "uint256"},
                {"internalType": "string", "name": "", "type": "string"},
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "string", "name": "s", "type": "string"}
            ],
            "name": "doSomething",
            "outputs": [
                {"internalType": "string", "name": "", "type": "string"}
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"}
            ],
            "name": "doSomething",
            "outputs": [
                {"internalType": "uint256", "name": "", "type": "uint256"}
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
            ],
            "name": "doSomething",
            "outputs": [
                {"internalType": "uint256", "name": "added", "type": "uint256"}
            ],
            "stateMutability": "pure",
            "type": "function",
        },
    ],
)
# pylint: disable=line-too-long
overloadedmethods_bytecode = HexStr(
    "0x608060405234801561000f575f80fd5b506105a48061001d5f395ff3fe608060405234801561000f575f80fd5b506004361061004a575f3560e01c80633b6c27c41461004e5780638ae3048e1461007f578063a6b206bf146100af578063b2dd1d79146100df575b5f80fd5b610068600480360381019061006391906102d3565b61010f565b6040516100769291906103b6565b60405180910390f35b610099600480360381019061009491906103e4565b61011f565b6040516100a6919061042b565b60405180910390f35b6100c960048036038101906100c4919061044b565b610129565b6040516100d69190610476565b60405180910390f35b6100f960048036038101906100f4919061048f565b61013e565b6040516101069190610476565b60405180910390f35b5f60608383915091509250929050565b6060819050919050565b5f60028261013791906104fa565b9050919050565b5f818361014b919061053b565b905092915050565b5f604051905090565b5f80fd5b5f80fd5b5f819050919050565b61017681610164565b8114610180575f80fd5b50565b5f813590506101918161016d565b92915050565b5f80fd5b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101e58261019f565b810181811067ffffffffffffffff82111715610204576102036101af565b5b80604052505050565b5f610216610153565b905061022282826101dc565b919050565b5f67ffffffffffffffff821115610241576102406101af565b5b61024a8261019f565b9050602081019050919050565b828183375f83830152505050565b5f61027761027284610227565b61020d565b9050828152602081018484840111156102935761029261019b565b5b61029e848285610257565b509392505050565b5f82601f8301126102ba576102b9610197565b5b81356102ca848260208601610265565b91505092915050565b5f80604083850312156102e9576102e861015c565b5b5f6102f685828601610183565b925050602083013567ffffffffffffffff81111561031757610316610160565b5b610323858286016102a6565b9150509250929050565b61033681610164565b82525050565b5f81519050919050565b5f82825260208201905092915050565b5f5b83811015610373578082015181840152602081019050610358565b5f8484015250505050565b5f6103888261033c565b6103928185610346565b93506103a2818560208601610356565b6103ab8161019f565b840191505092915050565b5f6040820190506103c95f83018561032d565b81810360208301526103db818461037e565b90509392505050565b5f602082840312156103f9576103f861015c565b5b5f82013567ffffffffffffffff81111561041657610415610160565b5b610422848285016102a6565b91505092915050565b5f6020820190508181035f830152610443818461037e565b905092915050565b5f602082840312156104605761045f61015c565b5b5f61046d84828501610183565b91505092915050565b5f6020820190506104895f83018461032d565b92915050565b5f80604083850312156104a5576104a461015c565b5b5f6104b285828601610183565b92505060206104c385828601610183565b9150509250929050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f61050482610164565b915061050f83610164565b925082820261051d81610164565b91508282048414831517610534576105336104cd565b5b5092915050565b5f61054582610164565b915061055083610164565b9250828201905080821115610568576105676104cd565b5b9291505056fea264697066735822122078825cb5ad9e448f88e15b30baf7ce6082e7974758a1a6d316643df618e8a17b64736f6c63430008170033"
)


class OverloadedMethodsContract(Contract):
    """A web3.py Contract class for the OverloadedMethods contract."""

    abi: ABI = overloadedmethods_abi
    bytecode: bytes = HexBytes(overloadedmethods_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = OverloadedMethodsContractFunctions(
                overloadedmethods_abi, self.w3, address
            )

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    # TODO: add events
    # events: ERC20ContractEvents

    functions: OverloadedMethodsContractFunctions

    @classmethod
    def factory(
        cls, w3: Web3, class_name: str | None = None, **kwargs: Any
    ) -> Type[Self]:
        contract = super().factory(w3, class_name, **kwargs)
        contract.functions = OverloadedMethodsContractFunctions(
            overloadedmethods_abi, w3, None
        )

        return contract
