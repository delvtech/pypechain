"""A web3.py Contract class for the Events contract.

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
from typing import Any, Iterable, NamedTuple, Sequence, Tuple, Type, TypeVar, cast

from eth_account.signers.local import LocalAccount
from eth_typing import ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3._utils.filters import LogFilter
from web3.contract.contract import (
    Contract,
    ContractConstructor,
    ContractEvent,
    ContractEvents,
    ContractFunction,
    ContractFunctions,
)
from web3.exceptions import FallbackNotFound
from web3.types import ABI, BlockIdentifier, CallOverride, EventData, TxParams

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


class EventsEmitNoEventsContractFunction(ContractFunction):
    """ContractFunction for the emitNoEvents method."""

    def __call__(self, x: int, y: int) -> EventsEmitNoEventsContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(x), dataclass_to_tuple(y))
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
        return cast(int, rename_returned_types(return_types, raw_values))


class EventsEmitOneEventContractFunction(ContractFunction):
    """ContractFunction for the emitOneEvent method."""

    def __call__(self, value: int, who: str) -> EventsEmitOneEventContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(value), dataclass_to_tuple(who))
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


class EventsEmitTwoEventsContractFunction(ContractFunction):
    """ContractFunction for the emitTwoEvents method."""

    def __call__(self, value: int, who: str) -> EventsEmitTwoEventsContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(value), dataclass_to_tuple(who))
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


class EventsContractFunctions(ContractFunctions):
    """ContractFunctions for the Events contract."""

    emitNoEvents: EventsEmitNoEventsContractFunction

    emitOneEvent: EventsEmitOneEventContractFunction

    emitTwoEvents: EventsEmitTwoEventsContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.emitNoEvents = EventsEmitNoEventsContractFunction.factory(
            "emitNoEvents",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="emitNoEvents",
        )
        self.emitOneEvent = EventsEmitOneEventContractFunction.factory(
            "emitOneEvent",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="emitOneEvent",
        )
        self.emitTwoEvents = EventsEmitTwoEventsContractFunction.factory(
            "emitTwoEvents",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="emitTwoEvents",
        )


class EventsEventAContractEvent(ContractEvent):
    """ContractEvent for EventA."""

    # super() get_logs and create_filter methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ

    # @combomethod destroys return types, so we are redefining functions as both class and instance
    # pylint: disable=function-redefined

    # pylint: disable=useless-parent-delegation
    def __init__(self, *argument_names: tuple[str]) -> None:
        super().__init__(*argument_names)

    def get_logs(  # type: ignore
        self: "EventsEventAContractEvent",
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier | None = None,
        block_hash: HexBytes | None = None,
    ) -> Iterable[EventData]:
        return cast(
            Iterable[EventData],
            super().get_logs(
                argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, block_hash=block_hash
            ),
        )

    @classmethod
    def get_logs(  # type: ignore
        cls: Type["EventsEventAContractEvent"],
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier | None = None,
        block_hash: HexBytes | None = None,
    ) -> Iterable[EventData]:
        return cast(
            Iterable[EventData],
            super().get_logs(
                argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, block_hash=block_hash
            ),
        )

    def create_filter(  # type: ignore
        self: "EventsEventAContractEvent",
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return cast(
            LogFilter,
            super().create_filter(
                argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, address=address, topics=topics
            ),
        )

    @classmethod
    def create_filter(  # type: ignore
        cls: Type["EventsEventAContractEvent"],
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return cast(
            LogFilter,
            super().create_filter(
                argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, address=address, topics=topics
            ),
        )


class EventsEventBContractEvent(ContractEvent):
    """ContractEvent for EventB."""

    # super() get_logs and create_filter methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ

    # @combomethod destroys return types, so we are redefining functions as both class and instance
    # pylint: disable=function-redefined

    # pylint: disable=useless-parent-delegation
    def __init__(self, *argument_names: tuple[str]) -> None:
        super().__init__(*argument_names)

    def get_logs(  # type: ignore
        self: "EventsEventBContractEvent",
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier | None = None,
        block_hash: HexBytes | None = None,
    ) -> Iterable[EventData]:
        return cast(
            Iterable[EventData],
            super().get_logs(
                argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, block_hash=block_hash
            ),
        )

    @classmethod
    def get_logs(  # type: ignore
        cls: Type["EventsEventBContractEvent"],
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier | None = None,
        block_hash: HexBytes | None = None,
    ) -> Iterable[EventData]:
        return cast(
            Iterable[EventData],
            super().get_logs(
                argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, block_hash=block_hash
            ),
        )

    def create_filter(  # type: ignore
        self: "EventsEventBContractEvent",
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return cast(
            LogFilter,
            super().create_filter(
                argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, address=address, topics=topics
            ),
        )

    @classmethod
    def create_filter(  # type: ignore
        cls: Type["EventsEventBContractEvent"],
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return cast(
            LogFilter,
            super().create_filter(
                argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, address=address, topics=topics
            ),
        )


class EventsContractEvents(ContractEvents):
    """ContractEvents for the Events contract."""

    EventA: EventsEventAContractEvent

    EventB: EventsEventBContractEvent

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
    ) -> None:
        super().__init__(abi, w3, address)
        self.EventA = cast(
            EventsEventAContractEvent,
            EventsEventAContractEvent.factory("EventA", w3=w3, contract_abi=abi, address=address, event_name="EventA"),
        )
        self.EventB = cast(
            EventsEventBContractEvent,
            EventsEventBContractEvent.factory("EventB", w3=w3, contract_abi=abi, address=address, event_name="EventB"),
        )


events_abi: ABI = cast(
    ABI,
    [
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "internalType": "address", "name": "who", "type": "address"},
                {"indexed": False, "internalType": "uint256", "name": "value", "type": "uint256"},
            ],
            "name": "EventA",
            "type": "event",
        },
        {"anonymous": False, "inputs": [], "name": "EventB", "type": "event"},
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
            ],
            "name": "emitNoEvents",
            "outputs": [{"internalType": "uint256", "name": "added", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "value", "type": "uint256"},
                {"internalType": "address", "name": "who", "type": "address"},
            ],
            "name": "emitOneEvent",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "value", "type": "uint256"},
                {"internalType": "address", "name": "who", "type": "address"},
            ],
            "name": "emitTwoEvents",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ],
)
# pylint: disable=line-too-long
events_bytecode = HexStr(
    "0x608060405234801561000f575f80fd5b5061035b8061001d5f395ff3fe608060405234801561000f575f80fd5b506004361061003f575f3560e01c8063307324fd14610043578063b517b0d81461005f578063c79ba18b1461007b575b5f80fd5b61005d60048036038101906100589190610221565b6100ab565b005b61007960048036038101906100749190610221565b6100fd565b005b6100956004803603810190610090919061025f565b61017b565b6040516100a291906102ac565b60405180910390f35b8073ffffffffffffffffffffffffffffffffffffffff167f9796ec8d639e8a8082085b1912b0c782def636bb8e5bde841892baff0f925433836040516100f191906102ac565b60405180910390a25050565b8073ffffffffffffffffffffffffffffffffffffffff167f9796ec8d639e8a8082085b1912b0c782def636bb8e5bde841892baff0f9254338360405161014391906102ac565b60405180910390a27f72c635b4ade595df848fdc26063ba6c3f276cd7121dadbacb0064e1e3a61961460405160405180910390a15050565b5f818361018891906102f2565b905092915050565b5f80fd5b5f819050919050565b6101a681610194565b81146101b0575f80fd5b50565b5f813590506101c18161019d565b92915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6101f0826101c7565b9050919050565b610200816101e6565b811461020a575f80fd5b50565b5f8135905061021b816101f7565b92915050565b5f806040838503121561023757610236610190565b5b5f610244858286016101b3565b92505060206102558582860161020d565b9150509250929050565b5f806040838503121561027557610274610190565b5b5f610282858286016101b3565b9250506020610293858286016101b3565b9150509250929050565b6102a681610194565b82525050565b5f6020820190506102bf5f83018461029d565b92915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6102fc82610194565b915061030783610194565b925082820190508082111561031f5761031e6102c5565b5b9291505056fea2646970667358221220b383644ab18d548fe7afe30be32478f77f7e0db56970ec5447b2d4a0a79fa05d64736f6c63430008170033"
)


class EventsContract(Contract):
    """A web3.py Contract class for the Events contract."""

    abi: ABI = events_abi
    bytecode: bytes = HexBytes(events_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = EventsContractFunctions(events_abi, self.w3, address)  # type: ignore
            self.events = EventsContractEvents(events_abi, self.w3, address)  # type: ignore

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    events: EventsContractEvents

    functions: EventsContractFunctions

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
        contract.functions = EventsContractFunctions(events_abi, w3, None)

        return contract
