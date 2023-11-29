



class OverloadedBalanceOfContractFunction0(ContractFunction):
    """ContractFunction for the balanceOf method."""

    def __call__(self) -> OverloadedBalanceOfContractFunction: #type: ignore
        super().__call__()
        return cast(OverloadedBalanceOfContractFunction, self)

    
    
    

    

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
        

class OverloadedBalanceOfContractFunction1(ContractFunction):
    """ContractFunction for the balanceOf method."""

    def __call__(self, who: str) -> OverloadedBalanceOfContractFunction: #type: ignore
        super().__call__(who)
        return cast(OverloadedBalanceOfContractFunction, self)

    
    
    

    

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
        

class OverloadedBalanceOfContractFunction(ContractFunction):
    """ContractFunction for the balanceOf method."""
    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined



    @overload
    def __call__(self) -> OverloadedBalanceOfContractFunction0:  # type: ignore
        ...

    @overload
    def __call__(self, who: str) -> OverloadedBalanceOfContractFunction1:  # type: ignore
        ...


    def __call__(self, *args) -> OverloadedBalanceOfContractFunction:  # type: ignore
        clone = super().__call__(*args)
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self  # type: ignore
 



class OverloadedContractFunctions(ContractFunctions):
    """ContractFunctions for the Overloaded contract."""

    balanceOf: OverloadedBalanceOfContractFunction

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
         
 