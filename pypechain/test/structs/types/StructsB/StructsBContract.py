"""A web3.py Contract class for the StructsB contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.44.
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
from web3.types import BlockIdentifier, Nonce, StateOverride, TxParams

from pypechain.core import (
    PypechainBaseContractErrors,
    PypechainContractFunction,
    dataclass_to_tuple,
    expand_struct_type_str,
    get_arg_type_names,
    handle_contract_logic_error,
    rename_returned_types,
)

from ..IStructs import IStructsTypes as IStructs

structs = {
    "IStructs.SimpleStruct": IStructs.SimpleStruct,
}


class StructsBNoNameSingleValueContractFunction0(PypechainContractFunction):
    """ContractFunction for the noNameSingleValue(int) method."""

    _function_name = "noNameSingleValue"
    _type_signature = expand_struct_type_str(tuple(["int"]), structs)

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
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsBContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(int, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsBContractErrors,
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
                errors_class=StructsBContractErrors,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def sign_and_transact(
        self, account: LocalAccount, transaction: TxParams | None = None, nonce: Nonce | None = None
    ) -> HexBytes:
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

        if "gas" not in transaction_params:
            # Web3 default gas estimate seems to be underestimating gas, likely due to
            # not looking at pending block. Here, we explicitly call estimate gas
            # if gas isn't passed in.
            transaction_params["gas"] = self.estimate_gas(transaction_params, block_identifier="pending")

        # Build the raw transaction
        raw_transaction = self.build_transaction(transaction_params)

        if nonce is None:
            raw_transaction["nonce"] = self.w3.eth.get_transaction_count(account.address)
        else:
            raw_transaction["nonce"] = nonce

        # Sign the raw transaction
        # Mismatched types between account and web3py
        signed_transaction = account.sign_transaction(raw_transaction)  # type: ignore

        # Send the signed transaction
        try:
            return self.w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsBContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction_params,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class StructsBNoNameSingleValueContractFunction(PypechainContractFunction):
    """ContractFunction for the noNameSingleValue method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "noNameSingleValue"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self, x: int) -> StructsBNoNameSingleValueContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> StructsBNoNameSingleValueContractFunction:  # type: ignore
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
            StructsBNoNameSingleValueContractFunction0._type_signature: StructsBNoNameSingleValueContractFunction0.factory(
                "StructsBNoNameSingleValueContractFunction0", **kwargs
            ),
        }
        return out


class StructsBSingleSimpleStructContractFunction0(PypechainContractFunction):
    """ContractFunction for the singleSimpleStruct() method."""

    _function_name = "singleSimpleStruct"
    _type_signature = expand_struct_type_str(tuple([]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> IStructs.SimpleStruct:
        """returns IStructs.SimpleStruct."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = IStructs.SimpleStruct

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsBContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(IStructs.SimpleStruct, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsBContractErrors,
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
                errors_class=StructsBContractErrors,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def sign_and_transact(
        self, account: LocalAccount, transaction: TxParams | None = None, nonce: Nonce | None = None
    ) -> HexBytes:
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

        if "gas" not in transaction_params:
            # Web3 default gas estimate seems to be underestimating gas, likely due to
            # not looking at pending block. Here, we explicitly call estimate gas
            # if gas isn't passed in.
            transaction_params["gas"] = self.estimate_gas(transaction_params, block_identifier="pending")

        # Build the raw transaction
        raw_transaction = self.build_transaction(transaction_params)

        if nonce is None:
            raw_transaction["nonce"] = self.w3.eth.get_transaction_count(account.address)
        else:
            raw_transaction["nonce"] = nonce

        # Sign the raw transaction
        # Mismatched types between account and web3py
        signed_transaction = account.sign_transaction(raw_transaction)  # type: ignore

        # Send the signed transaction
        try:
            return self.w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=StructsBContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction_params,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class StructsBSingleSimpleStructContractFunction(PypechainContractFunction):
    """ContractFunction for the singleSimpleStruct method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "singleSimpleStruct"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self) -> StructsBSingleSimpleStructContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> StructsBSingleSimpleStructContractFunction:  # type: ignore
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
            StructsBSingleSimpleStructContractFunction0._type_signature: StructsBSingleSimpleStructContractFunction0.factory(
                "StructsBSingleSimpleStructContractFunction0", **kwargs
            ),
        }
        return out


class StructsBContractFunctions(ContractFunctions):
    """ContractFunctions for the StructsB contract."""

    noNameSingleValue: StructsBNoNameSingleValueContractFunction

    singleSimpleStruct: StructsBSingleSimpleStructContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.noNameSingleValue = StructsBNoNameSingleValueContractFunction.factory(
            "noNameSingleValue",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="noNameSingleValue",
        )
        self.singleSimpleStruct = StructsBSingleSimpleStructContractFunction.factory(
            "singleSimpleStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="singleSimpleStruct",
        )


structsb_abi: ABI = cast(
    ABI,
    [
        {
            "type": "function",
            "name": "noNameSingleValue",
            "inputs": [{"name": "x", "type": "uint256", "internalType": "uint256"}],
            "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "singleSimpleStruct",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple",
                    "internalType": "struct IStructs.SimpleStruct",
                    "components": [
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                        {"name": "strVal", "type": "string", "internalType": "string"},
                    ],
                }
            ],
            "stateMutability": "pure",
        },
    ],
)


class StructsBContractErrors(PypechainBaseContractErrors):
    """ContractErrors for the StructsB contract."""

    def __init__(
        self,
    ) -> None:

        self._all = []


class StructsBContract(Contract):
    """A web3.py Contract class for the StructsB contract."""

    abi: ABI = structsb_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b50610166806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063389e91021461003b5780636456bc791461005f575b600080fd5b61004c6100493660046100b5565b90565b6040519081526020015b60405180910390f35b604080518082018252600081526060602091820152815180830183526001815282518084018452601081526f596f7520617265206e756d626572203160801b8184015291810191909152905161005691906100ce565b6000602082840312156100c757600080fd5b5035919050565b60006020808352835160208401526020840151604080850152805180606086015260005b8181101561010e578281018401518682016080015283016100f2565b506000608082870101526080601f19601f83011686010193505050509291505056fea2646970667358221220ad88b65d8d939f33e6b0c7fb080cedf1622d450c939626245098b934f5f8dcc164736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = StructsBContractFunctions(structsb_abi, self.w3, address)  # type: ignore

    functions: StructsBContractFunctions

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
        contract.functions = StructsBContractFunctions(structsb_abi, w3, None)

        return contract
