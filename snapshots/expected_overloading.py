




class OverloadedBalanceOfContractFunction0(PypechainContractFunction):
    """ContractFunction for the balanceOf() method."""

    _function_name = "balanceOf"
    _type_signature = expand_struct_type_str(
        tuple([]),
        structs
    )
    _error_class = OverloadedContractErrors

    
    
    

    

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> int:
        """returns int."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        
        # Define the expected return types from the smart contract call
        return_types = int
        

        # Call the function
        raw_values = self._call(transaction, block_identifier, state_override, ccip_read_enabled)

        
        return cast(int, rename_returned_types(structs, return_types, raw_values))
        



class OverloadedBalanceOfContractFunction1(PypechainContractFunction):
    """ContractFunction for the balanceOf(str) method."""

    _function_name = "balanceOf"
    _type_signature = expand_struct_type_str(
        tuple(['str']),
        structs
    )
    _error_class = OverloadedContractErrors

    
    
    

    

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> int:
        """returns int."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        
        # Define the expected return types from the smart contract call
        return_types = int
        

        # Call the function
        raw_values = self._call(transaction, block_identifier, state_override, ccip_read_enabled)

        
        return cast(int, rename_returned_types(structs, return_types, raw_values))
        


class OverloadedBalanceOfContractFunction(PypechainOverloadedFunctions):
    """ContractFunction for the balanceOf method."""
    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "balanceOf"


    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]



    @overload
    def __call__(self) -> OverloadedBalanceOfContractFunction0:  # type: ignore
        ...

    @overload
    def __call__(self, who: str) -> OverloadedBalanceOfContractFunction1:  # type: ignore
        ...


    def __call__(self, *args, **kwargs) -> OverloadedBalanceOfContractFunction:  # type: ignore
        # Special case when there are no args or kwargs
        if len(args) == 0 and len(kwargs) == 0:
            # We need to specify the element identifier as the function call without arguments.
            # Despite this setting the member variable `abi_element_identifier`
            # that's shared across this object, this field gets overwritten in the
            # clone if arguments are provided.
            self.abi_element_identifier = self._function_name + "()"
            clone = super().__call__()
        else:
            clone = super().__call__(*(dataclass_to_tuple(arg) for arg in args), **{key: dataclass_to_tuple(arg) for key, arg in kwargs.items()})

        # Arguments is the flattened set of arguments from args and kwargs, ordered by the abi
        # We get the python types of the args passed in, but remapped from tuples -> dataclasses
        arg_types = get_arg_type_names(clone.arguments)

        # Grab the relevant kwargs when factory was called.
        factory_kwargs = self._factory_kwargs
        factory_kwargs["abi_element_identifier"] = clone.abi_element_identifier

        function_obj = self._overloaded_functions[arg_types].factory(
            self._function_name,
            **factory_kwargs
        )

        function_obj.args = clone.args
        function_obj.kwargs = clone.kwargs

        # The `@overload` of `__call__` takes care of setting the type of this object correctly
        return function_obj # type: ignore
    
    @classmethod
    def factory(
        cls, class_name: str, **kwargs: Any
    ) -> Self:
        out = super().factory(class_name, **kwargs)
        # Store the factory args for downstream consumption
        out._factory_kwargs = kwargs

        # We initialize our overridden functions here.
        # Note that we use the initialized object to ensure each function
        # is attached to the instantiated object 
        # (attached to a specific web3 and contract address)
        out._overloaded_functions = {
        
            OverloadedBalanceOfContractFunction0._type_signature: OverloadedBalanceOfContractFunction0,
        
            OverloadedBalanceOfContractFunction1._type_signature: OverloadedBalanceOfContractFunction1,
        
        }
        return out





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
             abi_element_identifier="balanceOf",
         )
         