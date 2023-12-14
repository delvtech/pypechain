"""A web3.py Contract class for the NoConstructor contract.

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
from typing import Any, Tuple, Type, TypeVar, cast

from eth_typing import ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunction, ContractFunctions
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
        elif isinstance(value, tuple) and not getattr(field_type, "_name", None) == "Tuple":
            # If it's a tuple and the field is not intended to be a tuple, assume it's a nested dataclass
            field_values[field_name] = tuple_to_dataclass(field_type, value)
        else:
            # Otherwise, set the primitive value directly
            field_values[field_name] = value

    return cls(**field_values)


def dataclass_to_tuple(instance: Any) -> Any:
    """Convert a dataclass instance to a tuple, handling nested dataclasses.
    If the input is not a dataclass, return the original value.
    """
    if not is_dataclass(instance):
        return instance

    def convert_value(value: Any) -> Any:
        """Convert nested dataclasses to tuples recursively, or return the original value."""
        if is_dataclass(value):
            return dataclass_to_tuple(value)
        return value

    return tuple(convert_value(getattr(instance, field.name)) for field in fields(instance))


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
            tuple_to_dataclass(return_type, value) for return_type, value in zip(return_types, raw_values)
        )

        return converted_values

    # cover case of single return value
    converted_value = tuple_to_dataclass(return_types, raw_values)
    return converted_value


class NoConstructorSetNameContractFunction(ContractFunction):
    """ContractFunction for the setName method."""

    def __call__(self, name: str) -> NoConstructorSetNameContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(name))
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> None:
        """returns None."""
        # Define the expected return types from the smart contract call

        # Call the function


class NoConstructorContractFunctions(ContractFunctions):
    """ContractFunctions for the NoConstructor contract."""

    setName: NoConstructorSetNameContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.setName = NoConstructorSetNameContractFunction.factory(
            "setName",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="setName",
        )


noconstructor_abi: ABI = cast(
    ABI,
    [
        {
            "inputs": [{"internalType": "string", "name": "_name", "type": "string"}],
            "name": "setName",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        }
    ],
)
# pylint: disable=line-too-long
noconstructor_bytecode = HexStr(
    "0x608060405234801561000f575f80fd5b506105018061001d5f395ff3fe608060405234801561000f575f80fd5b5060043610610029575f3560e01c8063c47f00271461002d575b5f80fd5b610047600480360381019061004291906101a8565b610049565b005b805f908161005791906103fc565b5050565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100ba82610074565b810181811067ffffffffffffffff821117156100d9576100d8610084565b5b80604052505050565b5f6100eb61005b565b90506100f782826100b1565b919050565b5f67ffffffffffffffff82111561011657610115610084565b5b61011f82610074565b9050602081019050919050565b828183375f83830152505050565b5f61014c610147846100fc565b6100e2565b90508281526020810184848401111561016857610167610070565b5b61017384828561012c565b509392505050565b5f82601f83011261018f5761018e61006c565b5b813561019f84826020860161013a565b91505092915050565b5f602082840312156101bd576101bc610064565b5b5f82013567ffffffffffffffff8111156101da576101d9610068565b5b6101e68482850161017b565b91505092915050565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061023d57607f821691505b6020821081036102505761024f6101f9565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026102b27fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610277565b6102bc8683610277565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6103006102fb6102f6846102d4565b6102dd565b6102d4565b9050919050565b5f819050919050565b610319836102e6565b61032d61032582610307565b848454610283565b825550505050565b5f90565b610341610335565b61034c818484610310565b505050565b5b8181101561036f576103645f82610339565b600181019050610352565b5050565b601f8211156103b45761038581610256565b61038e84610268565b8101602085101561039d578190505b6103b16103a985610268565b830182610351565b50505b505050565b5f82821c905092915050565b5f6103d45f19846008026103b9565b1980831691505092915050565b5f6103ec83836103c5565b9150826002028217905092915050565b610405826101ef565b67ffffffffffffffff81111561041e5761041d610084565b5b6104288254610226565b610433828285610373565b5f60209050601f831160018114610464575f8415610452578287015190505b61045c85826103e1565b8655506104c3565b601f19841661047286610256565b5f5b8281101561049957848901518255600182019150602085019450602081019050610474565b868310156104b657848901516104b2601f8916826103c5565b8355505b6001600288020188555050505b50505050505056fea26469706673582212207ed84ab8768ed6efc3e454c359b719b54494d5f5dbfce2f004052cb806844d7d64736f6c63430008170033"
)


class NoConstructorContract(Contract):
    """A web3.py Contract class for the NoConstructor contract."""

    abi: ABI = noconstructor_abi
    bytecode: bytes = HexBytes(noconstructor_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = NoConstructorContractFunctions(noconstructor_abi, self.w3, address)  # type: ignore

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    functions: NoConstructorContractFunctions

    @classmethod
    def constructor(cls) -> ContractConstructor:
        return super().constructor()

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
        contract.functions = NoConstructorContractFunctions(noconstructor_abi, w3, None)

        return contract
