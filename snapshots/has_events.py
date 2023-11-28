class OverloadedTransferContractEvent(ContractEvent):
    """ContractEvent for Transfer."""
    # super() get_logs and create_filter methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ
    
    # TODO: remove pylint disable when we add a type-hint for argument_names
    # pylint: disable=useless-parent-delegation
    def __init__(self, *argument_names: tuple[str]) -> None:
        super().__init__(*argument_names)

    @combomethod
    def get_logs(
        self,
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier | None = None,
        block_hash: HexBytes | None = None,
    ) -> Iterable[EventData]:
        return super().get_logs(argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, block_hash=block_hash)

    @combomethod
    def create_filter(
        self,
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return super().create_filter(argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, address=address, topics=topics)

class OverloadedApprovalContractEvent(ContractEvent):
    """ContractEvent for Approval."""
    # super() get_logs and create_filter methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ
    
    # TODO: remove pylint disable when we add a type-hint for argument_names
    # pylint: disable=useless-parent-delegation
    def __init__(self, *argument_names: tuple[str]) -> None:
        super().__init__(*argument_names)

    @combomethod
    def get_logs(
        self,
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier | None = None,
        block_hash: HexBytes | None = None,
    ) -> Iterable[EventData]:
        return super().get_logs(argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, block_hash=block_hash)

    @combomethod
    def create_filter(
        self,
        *,  # PEP 3102
        argument_filters: dict[str, Any] | None = None,
        fromBlock: BlockIdentifier | None = None,
        toBlock: BlockIdentifier = "latest",
        address: ChecksumAddress | None = None,
        topics: Sequence[Any] | None = None,
    ) -> LogFilter:
        return super().create_filter(argument_filters=argument_filters, fromBlock=fromBlock, toBlock=toBlock, address=address, topics=topics)



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
        