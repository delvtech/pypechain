

class OverloadedTransferContractEvent(ContractEvent):
    """ContractEvent for Transfer."""
    # super() get_logs and create_filter methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ

    # @combomethod destroys return types, so we are redefining functions as both class and instance
    # pylint: disable=function-redefined

    
    
    # pylint: disable=useless-parent-delegation
    def __init__(self, *argument_names: tuple[str]) -> None:
        super().__init__(*argument_names)

    # We ignore types here for function redefinition
    def get_typed_logs( # type: ignore
        self: "OverloadedTransferContractEvent",
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

                args = TransferEventArgs(
                    _from = abi_event.args["_from"],
                    to = abi_event.args["to"],
                    value = abi_event.args["value"],
                ),

            ) for abi_event in abi_events
        ]

    @classmethod
    # We ignore types here for function redefinition
    def get_typed_logs( # type: ignore
        cls: Type["OverloadedTransferContractEvent"],
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

                args = TransferEventArgs(
                    _from = abi_event.args["_from"],
                    to = abi_event.args["to"],
                    value = abi_event.args["value"],
                ),

            ) for abi_event in abi_events
        ]

    def create_filter( # type: ignore
        self: "OverloadedTransferContractEvent",
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        from_block: BlockIdentifier | None = None,
        to_block: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return cast(LogFilter, super().create_filter(argument_filters=argument_filters, from_block=from_block, to_block=to_block, address=address, topics=topics))

    @classmethod
    def create_filter( # type: ignore
        cls: Type["OverloadedTransferContractEvent"],
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

    # @combomethod destroys return types, so we are redefining functions as both class and instance
    # pylint: disable=function-redefined

    
    
    # pylint: disable=useless-parent-delegation
    def __init__(self, *argument_names: tuple[str]) -> None:
        super().__init__(*argument_names)

    # We ignore types here for function redefinition
    def get_typed_logs( # type: ignore
        self: "OverloadedApprovalContractEvent",
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

                args = ApprovalEventArgs(
                    owner = abi_event.args["owner"],
                    spender = abi_event.args["spender"],
                    value = abi_event.args["value"],
                ),

            ) for abi_event in abi_events
        ]

    @classmethod
    # We ignore types here for function redefinition
    def get_typed_logs( # type: ignore
        cls: Type["OverloadedApprovalContractEvent"],
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

                args = ApprovalEventArgs(
                    owner = abi_event.args["owner"],
                    spender = abi_event.args["spender"],
                    value = abi_event.args["value"],
                ),

            ) for abi_event in abi_events
        ]

    def create_filter( # type: ignore
        self: "OverloadedApprovalContractEvent",
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        from_block: BlockIdentifier | None = None,
        to_block: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return cast(LogFilter, super().create_filter(argument_filters=argument_filters, from_block=from_block, to_block=to_block, address=address, topics=topics))

    @classmethod
    def create_filter( # type: ignore
        cls: Type["OverloadedApprovalContractEvent"],
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

    Transfer: OverloadedTransferContractEvent

    Approval: OverloadedApprovalContractEvent


    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
    ) -> None:
        super().__init__(abi, w3, address)
        self.Transfer = cast(OverloadedTransferContractEvent, OverloadedTransferContractEvent.factory(
            "Transfer",
            w3=w3,
            contract_abi=abi,
            address=address,
            event_name="Transfer"
        ))
        self.Approval = cast(OverloadedApprovalContractEvent, OverloadedApprovalContractEvent.factory(
            "Approval",
            w3=w3,
            contract_abi=abi,
            address=address,
            event_name="Approval"
        ))
        