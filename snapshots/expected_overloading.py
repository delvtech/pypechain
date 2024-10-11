




class OverloadedBalanceOfContractFunction0(PypechainContractFunction):
    """ContractFunction for the balanceOf() method."""

    _function_name = "balanceOf"
    _type_signature = expand_struct_type_str(
        tuple([]),
        structs
    )

    
    
    

    

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
        

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
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
    
    def build_transaction(self, transaction: TxParams | None = None) -> TxParams:
        try:
            return super().build_transaction(transaction)
        except Exception as err: # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedContractErrors,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending", # race condition here, best effort to get block of txn.
            ) from err
    
    def sign_and_transact(self, account: LocalAccount, transaction: TxParams | None = None) -> HexBytes:
        """Convenience method for signing and sending a transaction using the provided account.

        Arguments
        ---------
        account : LocalAccount
            The account to use for signing and sending the transaction.
        transaction : TxParams | None, optional
            The transaction parameters to use for sending the transaction.
        
        Returns
        -------
        HexBytes
            The transaction hash.
        """
        if transaction is None:
            transaction_params: TxParams = {}
        else:
            transaction_params: TxParams = transaction

        if "from" in transaction_params:
            # Ensure if transaction is set, it matches
            assert transaction_params["from"] == account.address, f"Transaction from {transaction_params['from']} does not match account {account.address}"
        else:
            transaction_params["from"] = account.address

        if "gas" not in transaction_params:
            # Web3 default gas estimate seems to be underestimating gas, likely due to
            # not looking at pending block. Here, we explicitly call estimate gas
            # if gas isn't passed in.
            transaction_params["gas"] = self.estimate_gas(transaction_params, block_identifier="pending")
        
        # Build the raw transaction
        raw_transaction = self.build_transaction(transaction_params)

        if "nonce" not in raw_transaction:
            raw_transaction["nonce"] = self.w3.eth.get_transaction_count(account.address, block_identifier="pending")

        # Sign the raw transaction
        # Mismatched types between account and web3py
        signed_transaction = account.sign_transaction(raw_transaction) # type: ignore

        # Send the signed transaction
        try:
            return self.w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        except Exception as err: # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction_params,
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
        

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
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
    
    def build_transaction(self, transaction: TxParams | None = None) -> TxParams:
        try:
            return super().build_transaction(transaction)
        except Exception as err: # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedContractErrors,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending", # race condition here, best effort to get block of txn.
            ) from err
    
    def sign_and_transact(self, account: LocalAccount, transaction: TxParams | None = None) -> HexBytes:
        """Convenience method for signing and sending a transaction using the provided account.

        Arguments
        ---------
        account : LocalAccount
            The account to use for signing and sending the transaction.
        transaction : TxParams | None, optional
            The transaction parameters to use for sending the transaction.
        
        Returns
        -------
        HexBytes
            The transaction hash.
        """
        if transaction is None:
            transaction_params: TxParams = {}
        else:
            transaction_params: TxParams = transaction

        if "from" in transaction_params:
            # Ensure if transaction is set, it matches
            assert transaction_params["from"] == account.address, f"Transaction from {transaction_params['from']} does not match account {account.address}"
        else:
            transaction_params["from"] = account.address

        if "gas" not in transaction_params:
            # Web3 default gas estimate seems to be underestimating gas, likely due to
            # not looking at pending block. Here, we explicitly call estimate gas
            # if gas isn't passed in.
            transaction_params["gas"] = self.estimate_gas(transaction_params, block_identifier="pending")
        
        # Build the raw transaction
        raw_transaction = self.build_transaction(transaction_params)

        if "nonce" not in raw_transaction:
            raw_transaction["nonce"] = self.w3.eth.get_transaction_count(account.address, block_identifier="pending")

        # Sign the raw transaction
        # Mismatched types between account and web3py
        signed_transaction = account.sign_transaction(raw_transaction) # type: ignore

        # Send the signed transaction
        try:
            return self.w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        except Exception as err: # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=OverloadedContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction_params,
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
         