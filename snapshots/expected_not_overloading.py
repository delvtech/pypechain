class OverloadedBalanceOfContractFunction(ContractFunction):
    """ContractFunction for the balanceOf method."""
    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ

    def __call__(self) -> "OverloadedBalanceOfContractFunction":
        clone = super().__call__()
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self


    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = 'latest',
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None) -> int:
            """returns int"""
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
            # Define the expected return types from the smart contract call
            return_types = int
            
            return cast(int, self._call(return_types, raw_values))
            
    def _call(self, return_types, raw_values):
        # cover case of multiple return values
        if isinstance(return_types, list):
            # Ensure raw_values is a tuple for consistency
            if not isinstance(raw_values, list):
                raw_values = (raw_values,)

            # Convert the tuple to the dataclass instance using the utility function
            converted_values = tuple(
                (tuple_to_dataclass(return_type, value) for return_type, value in zip(return_types, raw_values))
            )

            return converted_values

        # cover case of single return value
        converted_value = tuple_to_dataclass(return_types, raw_values)
        return converted_value
class OverloadedBalanceOfWhoContractFunction(ContractFunction):
    """ContractFunction for the balanceOfWho method."""
    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ

    def __call__(self, who: str) -> "OverloadedBalanceOfWhoContractFunction":
        clone = super().__call__(who)
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self


    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = 'latest',
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None) -> bool:
            """returns bool"""
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
            # Define the expected return types from the smart contract call
            return_types = bool
            
            return cast(bool, self._call(return_types, raw_values))
            
    def _call(self, return_types, raw_values):
        # cover case of multiple return values
        if isinstance(return_types, list):
            # Ensure raw_values is a tuple for consistency
            if not isinstance(raw_values, list):
                raw_values = (raw_values,)

            # Convert the tuple to the dataclass instance using the utility function
            converted_values = tuple(
                (tuple_to_dataclass(return_type, value) for return_type, value in zip(return_types, raw_values))
            )

            return converted_values

        # cover case of single return value
        converted_value = tuple_to_dataclass(return_types, raw_values)
        return converted_value


class OverloadedContractFunctions(ContractFunctions):
    """ContractFunctions for the Overloaded contract."""

    balanceOf: OverloadedBalanceOfContractFunction

    balanceOfWho: OverloadedBalanceOfWhoContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.balanceOf = OverloadedBalanceOfContractFunction.factory(
            "balanceOf",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="balanceOf",
        )
        self.balanceOfWho = OverloadedBalanceOfWhoContractFunction.factory(
            "balanceOfWho",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="balanceOfWho",
        )
        