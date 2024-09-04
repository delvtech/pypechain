
 
class OverloadedBalanceOfContractFunction(ContractFunction):
    """ContractFunction for the balanceOf method."""

    
    
    
    
    

    def __call__(self) -> OverloadedBalanceOfContractFunction: #type: ignore
        clone = super().__call__()
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
        
 


 
class OverloadedBalanceOfWhoContractFunction(ContractFunction):
    """ContractFunction for the balanceOfWho method."""

    
    
    
    
    

    def __call__(self, who: str) -> OverloadedBalanceOfWhoContractFunction: #type: ignore
        clone = super().__call__(dataclass_to_tuple(who))
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> bool:
        """returns bool."""
        # Define the expected return types from the smart contract call
        
        return_types = bool
        
        # Call the function
        
        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(bool, rename_returned_types(structs, return_types, raw_values))
        
 



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
             abi_element_identifier="balanceOf",
         )
         self.balanceOfWho = OverloadedBalanceOfWhoContractFunction.factory(
             "balanceOfWho",
             w3=w3,
             contract_abi=abi,
             address=address,
             decode_tuples=decode_tuples,
             abi_element_identifier="balanceOfWho",
         )
         