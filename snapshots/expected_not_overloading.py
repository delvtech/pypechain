class OverloadedBalanceOfContractFunction(ContractFunction):
    """ContractFunction for the balanceOf method."""
    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ

    def __call__(self) -> "OverloadedBalanceOfContractFunction":
        super().__call__()
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = 'latest',
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None) -> int:
            """returns int"""
            return super().call(transaction, block_identifier, state_override, ccip_read_enabled)



class OverloadedBalanceOfWhoContractFunction(ContractFunction):
    """ContractFunction for the balanceOfWho method."""
    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ

    def __call__(self, who: str) -> "OverloadedBalanceOfWhoContractFunction":
        super().__call__(who)
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = 'latest',
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None) -> bool:
            """returns bool"""
            return super().call(transaction, block_identifier, state_override, ccip_read_enabled)




class OverloadedContractFunctions(ContractFunctions):
    """ContractFunctions for the Overloaded contract."""

    balanceOf: OverloadedBalanceOfContractFunction

    balanceOfWho: OverloadedBalanceOfWhoContractFunction
