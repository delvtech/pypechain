

class OverloadedTransferContractEvent(ContractEvent):
    """ContractEvent for Transfer."""
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
    ) -> Iterable[TransferEvent]:
        """Extension of `get_logs` that return a typed dataclass of the event."""
        abi_events = super().get_logs(argument_filters=argument_filters, from_block=from_block, to_block=to_block, block_hash=block_hash)
        # TODO there may be issues with this function if the user uses a middleware that changes event structure.
        return [
            TransferEvent(
                log_index = abi_event.logIndex,
                transaction_index = abi_event.transactionIndex,
                transaction_hash = abi_event.transactionHash,
                address = abi_event.address,
                block_hash = abi_event.blockHash,
                block_number = abi_event.blockNumber,

                args = TransferEvent.TransferEventArgs(
                    _from = abi_event.args["_from"],
                    to = abi_event.args["to"],
                    value = abi_event.args["value"],
                ),

            ) for abi_event in abi_events
        ]
    
    @combomethod_typed
    def process_receipt_typed(
        self, txn_receipt: TxReceipt, errors: EventLogErrorFlags = WARN
    ) -> Iterable[TransferEvent]:
        """Extension of `process_receipt` that return a typed dataclass of the event."""
        abi_events = super().process_receipt(txn_receipt, errors)
        # TODO there may be issues with this function if the user uses a middleware that changes event structure.
        return [
            TransferEvent(
                log_index = abi_event.logIndex,
                transaction_index = abi_event.transactionIndex,
                transaction_hash = abi_event.transactionHash,
                address = abi_event.address,
                block_hash = abi_event.blockHash,
                block_number = abi_event.blockNumber,

                args = TransferEvent.TransferEventArgs(
                    _from = abi_event.args["_from"],
                    to = abi_event.args["to"],
                    value = abi_event.args["value"],
                ),

            ) for abi_event in abi_events
        ]

    @combomethod_typed
    def create_filter( # type: ignore
        self,
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        from_block: BlockIdentifier | None = None,
        to_block: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return cast(LogFilter, super().create_filter(argument_filters=argument_filters, from_block=from_block, to_block=to_block, address=address, topics=topics))



class OverloadedApprovalContractEvent(ContractEvent):
    """ContractEvent for Approval."""
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
    ) -> Iterable[ApprovalEvent]:
        """Extension of `get_logs` that return a typed dataclass of the event."""
        abi_events = super().get_logs(argument_filters=argument_filters, from_block=from_block, to_block=to_block, block_hash=block_hash)
        # TODO there may be issues with this function if the user uses a middleware that changes event structure.
        return [
            ApprovalEvent(
                log_index = abi_event.logIndex,
                transaction_index = abi_event.transactionIndex,
                transaction_hash = abi_event.transactionHash,
                address = abi_event.address,
                block_hash = abi_event.blockHash,
                block_number = abi_event.blockNumber,

                args = ApprovalEvent.ApprovalEventArgs(
                    owner = abi_event.args["owner"],
                    spender = abi_event.args["spender"],
                    value = abi_event.args["value"],
                ),

            ) for abi_event in abi_events
        ]
    
    @combomethod_typed
    def process_receipt_typed(
        self, txn_receipt: TxReceipt, errors: EventLogErrorFlags = WARN
    ) -> Iterable[ApprovalEvent]:
        """Extension of `process_receipt` that return a typed dataclass of the event."""
        abi_events = super().process_receipt(txn_receipt, errors)
        # TODO there may be issues with this function if the user uses a middleware that changes event structure.
        return [
            ApprovalEvent(
                log_index = abi_event.logIndex,
                transaction_index = abi_event.transactionIndex,
                transaction_hash = abi_event.transactionHash,
                address = abi_event.address,
                block_hash = abi_event.blockHash,
                block_number = abi_event.blockNumber,

                args = ApprovalEvent.ApprovalEventArgs(
                    owner = abi_event.args["owner"],
                    spender = abi_event.args["spender"],
                    value = abi_event.args["value"],
                ),

            ) for abi_event in abi_events
        ]

    @combomethod_typed
    def create_filter( # type: ignore
        self,
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        from_block: BlockIdentifier | None = None,
        to_block: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return cast(LogFilter, super().create_filter(argument_filters=argument_filters, from_block=from_block, to_block=to_block, address=address, topics=topics))



class OverloadedContractEvents(ContractEvents):
    """ContractEvents for the Overloaded contract."""

    Transfer: Type[OverloadedTransferContractEvent]

    Approval: Type[OverloadedApprovalContractEvent]


    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
    ) -> None:
        super().__init__(abi, w3, address)
        self.Transfer = cast(Type[OverloadedTransferContractEvent], OverloadedTransferContractEvent.factory(
            "Transfer",
            w3=w3,
            contract_abi=abi,
            address=address,
            event_name="Transfer"
        ))
        self.Approval = cast(Type[OverloadedApprovalContractEvent], OverloadedApprovalContractEvent.factory(
            "Approval",
            w3=w3,
            contract_abi=abi,
            address=address,
            event_name="Approval"
        ))
        