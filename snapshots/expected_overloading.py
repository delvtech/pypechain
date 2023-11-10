class OverloadedBalanceOfContractFunction(ContractFunction):
    """ContractFunction for the balanceOf method."""
    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ

    @multimethod
    def __call__(self) -> "OverloadedBalanceOfContractFunction":
        super().__call__()
        return self

    @multimethod
    def __call__(self, who: str) -> "OverloadedBalanceOfContractFunction":
        super().__call__(who)
        return self


class OverloadedContractFunctions(ContractFunctions):
    """ContractFunctions for the Overloaded contract."""

    balanceOf: OverloadedBalanceOfContractFunction
