
 
class OverloadedBalanceOfContractFunction(ContractFunction):
    """ContractFunction for the balanceOf method."""

    
    
    
    
    

    def __call__(self) -> OverloadedBalanceOfContractFunction:
        clone = super().__call__()
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
        
        return rename_returned_types(return_types, raw_values)
        
 


 
class OverloadedBalanceOfWhoContractFunction(ContractFunction):
    """ContractFunction for the balanceOfWho method."""

    
    
    
    
    

    def __call__(self, who: str) -> OverloadedBalanceOfWhoContractFunction:
        clone = super().__call__(who)
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self
    
    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> bool: 
        """returns bool."""
        # Define the expected return types from the smart contract call
        
        return_types = bool
        
        # Call the function
        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        
        return rename_returned_types(return_types, raw_values)
        
 



class OverloadedContractFunctions(ContractFunctions):
    """ContractFunctions for the Overloaded contract."""

    balanceOf: OverloadedBalanceOfContractFunction

    balanceOfWho: OverloadedBalanceOfWhoContractFunction
