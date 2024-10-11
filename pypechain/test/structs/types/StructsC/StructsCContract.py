"""A web3.py Contract class for the StructsC contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.43.
See documentation at https://github.com/delvtech/pypechain """

# contracts have PascalCase names
# pylint: disable=invalid-name

# contracts control how many attributes and arguments we have in generated code
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments

# we don't need else statement if the other conditionals all have return,
# but it's easier to generate
# pylint: disable=no-else-return

# This file is bound to get very long depending on contract sizes.
# pylint: disable=too-many-lines

# methods are overridden with specific arguments instead of generic *args, **kwargs
# pylint: disable=arguments-differ

# consumers have too many opinions on line length
# pylint: disable=line-too-long

# We use protected classes within pypechain
# pylint: disable=protected-access

# We sometimes define a variable that might not be returned in `call`,
# but we still may want to call the function
# pylint: disable=unused-variable


from __future__ import annotations

import copy
from typing import Any, Type, cast, overload

from eth_account.signers.local import LocalAccount
from eth_typing import ABI, ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunctions
from web3.types import BlockIdentifier, StateOverride, TxParams

from pypechain.core import (
    PypechainBaseContractErrors,
    PypechainContractFunction,
    dataclass_to_tuple,
    expand_struct_type_str,
    get_arg_type_names,
    handle_contract_logic_error,
    rename_returned_types,
)

from .. import IStructs, StructsC

structs = {
    "StructsC.InnyStruct": StructsC.InnyStruct,
    "StructsC.NestedStruct": StructsC.NestedStruct,
    "StructsC.OuterStruct": StructsC.OuterStruct,
    "IStructs.InnerStruct": IStructs.InnerStruct,
    "StructsC.CStruct": StructsC.CStruct,
}


class StructsCAllStructsInternalContractFunction0(PypechainContractFunction):
    """ContractFunction for the allStructsInternal() method."""

    _function_name = "allStructsInternal"
    _type_signature = expand_struct_type_str(tuple([]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> StructsC.OuterStruct:
        """returns StructsC.OuterStruct."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = StructsC.OuterStruct

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsCContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(StructsC.OuterStruct, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsCContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def build_transaction(self, transaction: TxParams | None = None) -> TxParams:
        try:
            return super().build_transaction(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsCContractErrors,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
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
            assert (
                transaction_params["from"] == account.address
            ), f"Transaction from {transaction_params['from']} does not match account {account.address}"
        else:
            transaction_params["from"] = account.address

        # Build the raw transaction
        raw_transaction = self.build_transaction(transaction_params)

        if "nonce" not in raw_transaction:
            raw_transaction["nonce"] = self.w3.eth.get_transaction_count(account.address)

        # Sign the raw transaction
        # Mismatched types between account and web3py
        signed_transaction = account.sign_transaction(raw_transaction)  # type: ignore

        # Send the signed transaction
        try:
            return self.w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsCContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction_params,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class StructsCAllStructsInternalContractFunction(PypechainContractFunction):
    """ContractFunction for the allStructsInternal method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "allStructsInternal"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self) -> StructsCAllStructsInternalContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> StructsCAllStructsInternalContractFunction:  # type: ignore
        clone = super().__call__(
            *(dataclass_to_tuple(arg) for arg in args), **{key: dataclass_to_tuple(arg) for key, arg in kwargs.items()}
        )

        # Arguments is the flattened set of arguments from args and kwargs, ordered by the abi
        # We get the python types of the args passed in, but remapped from tuples -> dataclasses
        arg_types = get_arg_type_names(clone.arguments)

        # Look up the function class based on arg types.
        # We ensure we use a copy of the original object.
        function_obj = copy.copy(self._functions[arg_types])

        function_obj.args = clone.args
        function_obj.kwargs = clone.kwargs

        # The `@overload` of `__call__` takes care of setting the type of this object correctly
        return function_obj  # type: ignore

    @classmethod
    def factory(cls, class_name: str, **kwargs: Any) -> Self:
        out = super().factory(class_name, **kwargs)

        # We initialize our overridden functions here
        cls._functions = {
            StructsCAllStructsInternalContractFunction0._type_signature: StructsCAllStructsInternalContractFunction0.factory(
                "StructsCAllStructsInternalContractFunction0", **kwargs
            ),
        }
        return out


class StructsCInnerStructIsExternalContractFunction0(PypechainContractFunction):
    """ContractFunction for the innerStructIsExternal() method."""

    _function_name = "innerStructIsExternal"
    _type_signature = expand_struct_type_str(tuple([]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> StructsC.CStruct:
        """returns StructsC.CStruct."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = StructsC.CStruct

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsCContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(StructsC.CStruct, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsCContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def build_transaction(self, transaction: TxParams | None = None) -> TxParams:
        try:
            return super().build_transaction(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsCContractErrors,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
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
            assert (
                transaction_params["from"] == account.address
            ), f"Transaction from {transaction_params['from']} does not match account {account.address}"
        else:
            transaction_params["from"] = account.address

        # Build the raw transaction
        raw_transaction = self.build_transaction(transaction_params)

        if "nonce" not in raw_transaction:
            raw_transaction["nonce"] = self.w3.eth.get_transaction_count(account.address)

        # Sign the raw transaction
        # Mismatched types between account and web3py
        signed_transaction = account.sign_transaction(raw_transaction)  # type: ignore

        # Send the signed transaction
        try:
            return self.w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsCContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction_params,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class StructsCInnerStructIsExternalContractFunction(PypechainContractFunction):
    """ContractFunction for the innerStructIsExternal method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "innerStructIsExternal"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self) -> StructsCInnerStructIsExternalContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> StructsCInnerStructIsExternalContractFunction:  # type: ignore
        clone = super().__call__(
            *(dataclass_to_tuple(arg) for arg in args), **{key: dataclass_to_tuple(arg) for key, arg in kwargs.items()}
        )

        # Arguments is the flattened set of arguments from args and kwargs, ordered by the abi
        # We get the python types of the args passed in, but remapped from tuples -> dataclasses
        arg_types = get_arg_type_names(clone.arguments)

        # Look up the function class based on arg types.
        # We ensure we use a copy of the original object.
        function_obj = copy.copy(self._functions[arg_types])

        function_obj.args = clone.args
        function_obj.kwargs = clone.kwargs

        # The `@overload` of `__call__` takes care of setting the type of this object correctly
        return function_obj  # type: ignore

    @classmethod
    def factory(cls, class_name: str, **kwargs: Any) -> Self:
        out = super().factory(class_name, **kwargs)

        # We initialize our overridden functions here
        cls._functions = {
            StructsCInnerStructIsExternalContractFunction0._type_signature: StructsCInnerStructIsExternalContractFunction0.factory(
                "StructsCInnerStructIsExternalContractFunction0", **kwargs
            ),
        }
        return out


class StructsCContractFunctions(ContractFunctions):
    """ContractFunctions for the StructsC contract."""

    allStructsInternal: StructsCAllStructsInternalContractFunction

    innerStructIsExternal: StructsCInnerStructIsExternalContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.allStructsInternal = StructsCAllStructsInternalContractFunction.factory(
            "allStructsInternal",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="allStructsInternal",
        )
        self.innerStructIsExternal = StructsCInnerStructIsExternalContractFunction.factory(
            "innerStructIsExternal",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="innerStructIsExternal",
        )


structsc_abi: ABI = cast(
    ABI,
    [
        {
            "type": "function",
            "name": "allStructsInternal",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple",
                    "internalType": "struct StructsC.OuterStruct",
                    "components": [
                        {
                            "name": "nested",
                            "type": "tuple",
                            "internalType": "struct StructsC.NestedStruct",
                            "components": [
                                {
                                    "name": "inner",
                                    "type": "tuple",
                                    "internalType": "struct StructsC.InnyStruct",
                                    "components": [{"name": "innerVal", "type": "uint256", "internalType": "uint256"}],
                                }
                            ],
                        }
                    ],
                }
            ],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "innerStructIsExternal",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple",
                    "internalType": "struct StructsC.CStruct",
                    "components": [
                        {
                            "name": "inner",
                            "type": "tuple",
                            "internalType": "struct IStructs.InnerStruct",
                            "components": [{"name": "boolVal", "type": "bool", "internalType": "bool"}],
                        }
                    ],
                }
            ],
            "stateMutability": "pure",
        },
    ],
)


class StructsCContractErrors(PypechainBaseContractErrors):
    """ContractErrors for the StructsC contract."""

    def __init__(
        self,
    ) -> None:

        self._all = []


class StructsCContract(Contract):
    """A web3.py Contract class for the StructsC contract."""

    abi: ABI = structsc_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b5060f48061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c80638012d826146037578063fc0db1de14606c575b600080fd5b604080518082018252600060208083018281529092528251808401845280830182815290529151918252015b60405180910390f35b608e60408051606081018252600091810191825260208101918252908152609e565b6040519051515181526020016063565b50604080516060810182526001918101918252602081019182529081529056fea2646970667358221220a897fe982f8c33895641b65745ff946b07724c9d9115b63b8c097c9d855b260464736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = StructsCContractFunctions(structsc_abi, self.w3, address)  # type: ignore

    functions: StructsCContractFunctions

    @classmethod
    def constructor(cls) -> ContractConstructor:  # type: ignore
        """Creates a transaction with the contract's constructor function.

        Parameters
        ----------

        w3 : Web3
            A web3 instance.
        account : LocalAccount
            The account to use to deploy the contract.

        Returns
        -------
        Self
            A deployed instance of the contract.

        """
        cls.bytecode = cls._raw_bytecode
        if cls.bytecode is not None:

            # bytecode needs to be in hex for web3
            cls.bytecode = HexBytes(cls.bytecode)

        return super().constructor()

    @classmethod
    def deploy(cls, w3: Web3, account: LocalAccount | ChecksumAddress) -> Self:
        """Deploys an instance of the contract.

        Parameters
        ----------
        w3 : Web3
            A web3 instance.
        account : LocalAccount
            The account to use to deploy the contract.

        Returns
        -------
        Self
            A deployed instance of the contract.
        """
        deployer = cls.factory(w3=w3)
        constructor_fn = deployer.constructor()

        # if an address is supplied, try to use a web3 default account
        if isinstance(account, str):
            tx_hash = constructor_fn.transact({"from": account})
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            deployed_contract = deployer(address=tx_receipt.contractAddress)  # type: ignore
            return deployed_contract

        # otherwise use the account provided.
        deployment_tx = constructor_fn.build_transaction()
        current_nonce = w3.eth.get_transaction_count(account.address, "pending")
        deployment_tx.update({"nonce": current_nonce})

        # Sign the transaction with local account private key
        signed_tx = account.sign_transaction(deployment_tx)

        # Send the signed transaction and wait for receipt
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        deployed_contract = deployer(address=tx_receipt.contractAddress)  # type: ignore
        return deployed_contract

    @classmethod
    def factory(cls, w3: Web3, class_name: str | None = None, **kwargs: Any) -> Type[Self]:
        """Initializes the contract object.

        Parameters
        ----------
        w3 : Web3
            A web3 instance.
        class_name: str | None
            The instance class name.

        Returns
        -------
        Self
            An instance of the contract class.
        """
        contract = super().factory(w3, class_name, **kwargs)
        contract.functions = StructsCContractFunctions(structsc_abi, w3, None)

        return contract