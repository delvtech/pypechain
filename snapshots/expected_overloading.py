class OverloadedBalanceOfContractFunction(ContractFunction):
    """ContractFunction for the balanceOf method."""
    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined
    @multimethod
    def __call__(self) -> "OverloadedBalanceOfContractFunction": #type: ignore
        super().__call__()
        return self
    @multimethod
    def call( #type: ignore
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = 'latest',
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None) -> int:
            """returns int"""
            return super().call(transaction, block_identifier, state_override, ccip_read_enabled)



    @multimethod
    def __call__(self, who: str) -> "OverloadedBalanceOfContractFunction": #type: ignore
        super().__call__(who)
        return self
    @multimethod
    def call( #type: ignore
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = 'latest',
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None) -> int:
            """returns int"""
            return super().call(transaction, block_identifier, state_override, ccip_read_enabled)




class OverloadedContractFunctions(ContractFunctions):
    """ContractFunctions for the Overloaded contract."""

    balanceOf: OverloadedBalanceOfContractFunction
