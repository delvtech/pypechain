




class OverloadedBalanceOfContractFunction0(PypechainContractFunction):
    """ContractFunction for the balanceOf() method."""

    _function_name = "balanceOf"
    _type_signature = expand_struct_type_str(
        tuple([]),
        structs
    )

    
    
    

    

    def call(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None,
        state_override: Optional[StateOverride] = None,
        ccip_read_enabled: Optional[bool] = None,
    ) -> int:
        """returns int."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        
        # Define the expected return types from the smart contract call
        return_types = int
        

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err: # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err
        

        
        return cast(int, rename_returned_types(structs, return_types, raw_values))
        

    def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err: # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending", # race condition here, best effort to get block of txn.
            ) from err




class OverloadedBalanceOfContractFunction1(PypechainContractFunction):
    """ContractFunction for the balanceOf(str) method."""

    _function_name = "balanceOf"
    _type_signature = expand_struct_type_str(
        tuple(['str']),
        structs
    )

    
    
    

    

    def call(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None,
        state_override: Optional[StateOverride] = None,
        ccip_read_enabled: Optional[bool] = None,
    ) -> int:
        """returns int."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        
        # Define the expected return types from the smart contract call
        return_types = int
        

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err: # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err
        

        
        return cast(int, rename_returned_types(structs, return_types, raw_values))
        

    def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err: # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending", # race condition here, best effort to get block of txn.
            ) from err



class OverloadedBalanceOfContractFunction(PypechainContractFunction):
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
        
            OverloadedBalanceOfContractFunction1._type_signature: OverloadedBalanceOfContractFunction1.factory(
                "OverloadedBalanceOfContractFunction1",
                **kwargs
            ),
        
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
         