




class OverloadedBalanceOfContractFunction0(PypechainContractFunction):
    """ContractFunction for the balanceOf() method."""

    _type_signature = expand_struct_type_str(
        tuple([]),
        structs
    )

    
    
    

    

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
        

class OverloadedBalanceOfContractFunction(PypechainContractFunction):
    """ContractFunction for the balanceOf method."""
    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined


    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]



    @overload
    def __call__(self) -> OverloadedBalanceOfContractFunction0:  # type: ignore
        ...


    def __call__(self, *args, **kwargs) -> OverloadedBalanceOfContractFunction:  # type: ignore
        clone = super().__call__(*(dataclass_to_tuple(arg) for arg in args), **{key: dataclass_to_tuple(arg) for key, arg in kwargs.items()})

        # Arguments is the flattened set of arguments from args and kwargs, ordered by the abi
        # We get the python types of the args passed in, but remapped from tuples -> dataclasses
        arg_types = get_arg_type_names(clone.arguments)

        # Look up the function class based on arg types.
        # We ensure we use a copy of the original object.
        function_obj = copy.copy(self._functions[arg_types])

        function_obj.args = clone.args
        function_obj.kwargs = clone.kwargs

        # The `@overload` of `__call__` takes care of setting the type of this object correctly
        return function_obj # type: ignore
    
    @classmethod
    def factory(
        cls, class_name: str, **kwargs: Any
    ) -> Self:
        out = super().factory(class_name, **kwargs)

        # We initialize our overridden functions here
        cls._functions = {
        
            OverloadedBalanceOfContractFunction0._type_signature: OverloadedBalanceOfContractFunction0.factory(
                "OverloadedBalanceOfContractFunction0",
                **kwargs
            ),
        
        }
        return out








class OverloadedBalanceOfWhoContractFunction0(PypechainContractFunction):
    """ContractFunction for the balanceOfWho(str) method."""

    _type_signature = expand_struct_type_str(
        tuple(['str']),
        structs
    )

    
    
    

    

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
        

class OverloadedBalanceOfWhoContractFunction(PypechainContractFunction):
    """ContractFunction for the balanceOfWho method."""
    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined


    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]



    @overload
    def __call__(self, who: str) -> OverloadedBalanceOfWhoContractFunction0:  # type: ignore
        ...


    def __call__(self, *args, **kwargs) -> OverloadedBalanceOfWhoContractFunction:  # type: ignore
        clone = super().__call__(*(dataclass_to_tuple(arg) for arg in args), **{key: dataclass_to_tuple(arg) for key, arg in kwargs.items()})

        # Arguments is the flattened set of arguments from args and kwargs, ordered by the abi
        # We get the python types of the args passed in, but remapped from tuples -> dataclasses
        arg_types = get_arg_type_names(clone.arguments)

        # Look up the function class based on arg types.
        # We ensure we use a copy of the original object.
        function_obj = copy.copy(self._functions[arg_types])

        function_obj.args = clone.args
        function_obj.kwargs = clone.kwargs

        # The `@overload` of `__call__` takes care of setting the type of this object correctly
        return function_obj # type: ignore
    
    @classmethod
    def factory(
        cls, class_name: str, **kwargs: Any
    ) -> Self:
        out = super().factory(class_name, **kwargs)

        # We initialize our overridden functions here
        cls._functions = {
        
            OverloadedBalanceOfWhoContractFunction0._type_signature: OverloadedBalanceOfWhoContractFunction0.factory(
                "OverloadedBalanceOfWhoContractFunction0",
                **kwargs
            ),
        
        }
        return out





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
         