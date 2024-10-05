"""A web3.py Contract class for the Events contract.

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

from typing import Any, Iterable, Sequence, Type, cast

from eth_account.signers.local import LocalAccount
from eth_typing import ABI, ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3._utils.events import EventLogErrorFlags
from web3._utils.filters import LogFilter
from web3.contract.contract import (
    Contract,
    ContractConstructor,
    ContractEvent,
    ContractEvents,
    ContractFunction,
    ContractFunctions,
)
from web3.logs import WARN
from web3.types import BlockIdentifier, StateOverride, TxParams, TxReceipt

from pypechain.core import combomethod_typed, dataclass_to_tuple, rename_returned_types

from .EventsTypes import EventAEvent, EventBEvent

structs = {}


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
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> int:
        """returns int."""
        # Define the expected return types from the smart contract call

        return_types = int

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(int, rename_returned_types(structs, return_types, raw_values))


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
        state_override: StateOverride | None = None,
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
        state_override: StateOverride | None = None,
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
            abi_element_identifier="emitNoEvents",
        )
        self.emitOneEvent = EventsEmitOneEventContractFunction.factory(
            "emitOneEvent",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="emitOneEvent",
        )
        self.emitTwoEvents = EventsEmitTwoEventsContractFunction.factory(
            "emitTwoEvents",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="emitTwoEvents",
        )


class EventsEventAContractEvent(ContractEvent):
    """ContractEvent for EventA."""

    # super() get_logs and create_filter methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ

    # pylint: disable=useless-parent-delegation
    def __init__(self, *argument_names: tuple[str]) -> None:
        super().__init__(*argument_names)

    @combomethod_typed
    def get_logs_typed(
        self,
        argument_filters: dict[str, Any] | None = None,
        from_block: BlockIdentifier | None = None,
        to_block: BlockIdentifier | None = None,
        block_hash: HexBytes | None = None,
    ) -> Iterable[EventAEvent]:
        """Extension of `get_logs` that return a typed dataclass of the event."""
        abi_events = super().get_logs(
            argument_filters=argument_filters, from_block=from_block, to_block=to_block, block_hash=block_hash
        )
        # TODO there may be issues with this function if the user uses a middleware that changes event structure.
        return [
            EventAEvent(
                log_index=abi_event.logIndex,
                transaction_index=abi_event.transactionIndex,
                transaction_hash=abi_event.transactionHash,
                address=abi_event.address,
                block_hash=abi_event.blockHash,
                block_number=abi_event.blockNumber,
                args=EventAEvent.EventAEventArgs(
                    who=abi_event.args["who"],
                    value=abi_event.args["value"],
                ),
            )
            for abi_event in abi_events
        ]

    @combomethod_typed
    def process_receipt_typed(self, txn_receipt: TxReceipt, errors: EventLogErrorFlags = WARN) -> Iterable[EventAEvent]:
        """Extension of `process_receipt` that return a typed dataclass of the event."""
        abi_events = super().process_receipt(txn_receipt, errors)
        # TODO there may be issues with this function if the user uses a middleware that changes event structure.
        return [
            EventAEvent(
                log_index=abi_event.logIndex,
                transaction_index=abi_event.transactionIndex,
                transaction_hash=abi_event.transactionHash,
                address=abi_event.address,
                block_hash=abi_event.blockHash,
                block_number=abi_event.blockNumber,
                args=EventAEvent.EventAEventArgs(
                    who=abi_event.args["who"],
                    value=abi_event.args["value"],
                ),
            )
            for abi_event in abi_events
        ]

    @combomethod_typed
    def create_filter(  # type: ignore
        self,
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        from_block: BlockIdentifier | None = None,
        to_block: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return cast(
            LogFilter,
            super().create_filter(
                argument_filters=argument_filters,
                from_block=from_block,
                to_block=to_block,
                address=address,
                topics=topics,
            ),
        )


class EventsEventBContractEvent(ContractEvent):
    """ContractEvent for EventB."""

    # super() get_logs and create_filter methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ

    # pylint: disable=useless-parent-delegation
    def __init__(self, *argument_names: tuple[str]) -> None:
        super().__init__(*argument_names)

    @combomethod_typed
    def get_logs_typed(
        self,
        argument_filters: dict[str, Any] | None = None,
        from_block: BlockIdentifier | None = None,
        to_block: BlockIdentifier | None = None,
        block_hash: HexBytes | None = None,
    ) -> Iterable[EventBEvent]:
        """Extension of `get_logs` that return a typed dataclass of the event."""
        abi_events = super().get_logs(
            argument_filters=argument_filters, from_block=from_block, to_block=to_block, block_hash=block_hash
        )
        # TODO there may be issues with this function if the user uses a middleware that changes event structure.
        return [
            EventBEvent(
                log_index=abi_event.logIndex,
                transaction_index=abi_event.transactionIndex,
                transaction_hash=abi_event.transactionHash,
                address=abi_event.address,
                block_hash=abi_event.blockHash,
                block_number=abi_event.blockNumber,
            )
            for abi_event in abi_events
        ]

    @combomethod_typed
    def process_receipt_typed(self, txn_receipt: TxReceipt, errors: EventLogErrorFlags = WARN) -> Iterable[EventBEvent]:
        """Extension of `process_receipt` that return a typed dataclass of the event."""
        abi_events = super().process_receipt(txn_receipt, errors)
        # TODO there may be issues with this function if the user uses a middleware that changes event structure.
        return [
            EventBEvent(
                log_index=abi_event.logIndex,
                transaction_index=abi_event.transactionIndex,
                transaction_hash=abi_event.transactionHash,
                address=abi_event.address,
                block_hash=abi_event.blockHash,
                block_number=abi_event.blockNumber,
            )
            for abi_event in abi_events
        ]

    @combomethod_typed
    def create_filter(  # type: ignore
        self,
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        from_block: BlockIdentifier | None = None,
        to_block: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return cast(
            LogFilter,
            super().create_filter(
                argument_filters=argument_filters,
                from_block=from_block,
                to_block=to_block,
                address=address,
                topics=topics,
            ),
        )


class EventsContractEvents(ContractEvents):
    """ContractEvents for the Events contract."""

    EventA: Type[EventsEventAContractEvent]

    EventB: Type[EventsEventBContractEvent]

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
    ) -> None:
        super().__init__(abi, w3, address)
        self.EventA = cast(
            Type[EventsEventAContractEvent],
            EventsEventAContractEvent.factory("EventA", w3=w3, contract_abi=abi, address=address, event_name="EventA"),
        )
        self.EventB = cast(
            Type[EventsEventBContractEvent],
            EventsEventBContractEvent.factory("EventB", w3=w3, contract_abi=abi, address=address, event_name="EventB"),
        )


events_abi: ABI = cast(
    ABI,
    [
        {
            "type": "function",
            "name": "emitNoEvents",
            "inputs": [
                {"name": "x", "type": "uint256", "internalType": "uint256"},
                {"name": "y", "type": "uint256", "internalType": "uint256"},
            ],
            "outputs": [{"name": "added", "type": "uint256", "internalType": "uint256"}],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "emitOneEvent",
            "inputs": [
                {"name": "value", "type": "uint256", "internalType": "uint256"},
                {"name": "who", "type": "address", "internalType": "address"},
            ],
            "outputs": [],
            "stateMutability": "nonpayable",
        },
        {
            "type": "function",
            "name": "emitTwoEvents",
            "inputs": [
                {"name": "value", "type": "uint256", "internalType": "uint256"},
                {"name": "who", "type": "address", "internalType": "address"},
            ],
            "outputs": [],
            "stateMutability": "nonpayable",
        },
        {
            "type": "event",
            "name": "EventA",
            "inputs": [
                {"name": "who", "type": "address", "indexed": True, "internalType": "address"},
                {"name": "value", "type": "uint256", "indexed": False, "internalType": "uint256"},
            ],
            "anonymous": False,
        },
        {"type": "event", "name": "EventB", "inputs": [], "anonymous": False},
    ],
)


class EventsContract(Contract):
    """A web3.py Contract class for the Events contract."""

    abi: ABI = events_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b50610214806100206000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c8063307324fd14610046578063b517b0d81461005b578063c79ba18b1461006e575b600080fd5b61005961005436600461015f565b610093565b005b61005961006936600461015f565b6100da565b61008161007c36600461019b565b61014a565b60405190815260200160405180910390f35b806001600160a01b03167f9796ec8d639e8a8082085b1912b0c782def636bb8e5bde841892baff0f925433836040516100ce91815260200190565b60405180910390a25050565b806001600160a01b03167f9796ec8d639e8a8082085b1912b0c782def636bb8e5bde841892baff0f9254338360405161011591815260200190565b60405180910390a26040517f72c635b4ade595df848fdc26063ba6c3f276cd7121dadbacb0064e1e3a61961490600090a15050565b600061015682846101bd565b90505b92915050565b6000806040838503121561017257600080fd5b8235915060208301356001600160a01b038116811461019057600080fd5b809150509250929050565b600080604083850312156101ae57600080fd5b50508035926020909101359150565b8082018082111561015957634e487b7160e01b600052601160045260246000fdfea2646970667358221220f4fc44b59a7d7fc9f695214dbacf39738bcfb36286157033034ece49be233d7564736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = EventsContractFunctions(events_abi, self.w3, address)  # type: ignore
        self.events = EventsContractEvents(events_abi, self.w3, address)  # type: ignore

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
        contract.functions = EventsContractFunctions(events_abi, w3, None)

        return contract
