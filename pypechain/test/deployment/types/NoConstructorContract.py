"""A web3.py Contract class for the NoConstructor contract.

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
from typing import Any, Optional, Type, cast, overload

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

structs = {}


class NoConstructorNameContractFunction0(PypechainContractFunction):
    """ContractFunction for the name() method."""

    _function_name = "name"
    _type_signature = expand_struct_type_str(tuple([]), structs)

    def call(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None,
        state_override: Optional[StateOverride] = None,
        ccip_read_enabled: Optional[bool] = None,
    ) -> str:
        """returns str."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Define the expected return types from the smart contract call
        return_types = str

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=NoConstructorContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(str, rename_returned_types(structs, return_types, raw_values))

    def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=NoConstructorContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class NoConstructorNameContractFunction(PypechainContractFunction):
    """ContractFunction for the name method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "name"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self) -> NoConstructorNameContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> NoConstructorNameContractFunction:  # type: ignore
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
            NoConstructorNameContractFunction0._type_signature: NoConstructorNameContractFunction0.factory(
                "NoConstructorNameContractFunction0", **kwargs
            ),
        }
        return out


class NoConstructorSetNameContractFunction0(PypechainContractFunction):
    """ContractFunction for the setName(str) method."""

    _function_name = "setName"
    _type_signature = expand_struct_type_str(tuple(["str"]), structs)

    def call(
        self,
        transaction: Optional[TxParams] = None,
        block_identifier: Optional[BlockIdentifier] = None,
        state_override: Optional[StateOverride] = None,
        ccip_read_enabled: Optional[bool] = None,
    ) -> None:
        """returns None."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Call the function
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=NoConstructorContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

    def transact(self, transaction: Optional[TxParams] = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=NoConstructorContractErrors,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err


class NoConstructorSetNameContractFunction(PypechainContractFunction):
    """ContractFunction for the setName method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "setName"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self, name: str) -> NoConstructorSetNameContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> NoConstructorSetNameContractFunction:  # type: ignore
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
            NoConstructorSetNameContractFunction0._type_signature: NoConstructorSetNameContractFunction0.factory(
                "NoConstructorSetNameContractFunction0", **kwargs
            ),
        }
        return out


class NoConstructorContractFunctions(ContractFunctions):
    """ContractFunctions for the NoConstructor contract."""

    name: NoConstructorNameContractFunction

    setName: NoConstructorSetNameContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.name = NoConstructorNameContractFunction.factory(
            "name",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="name",
        )
        self.setName = NoConstructorSetNameContractFunction.factory(
            "setName",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="setName",
        )


class NoConstructorContractErrors(PypechainBaseContractErrors):
    """ContractErrors for the NoConstructor contract."""

    def __init__(
        self,
    ) -> None:

        self._all = []


noconstructor_abi: ABI = cast(
    ABI,
    [
        {
            "type": "function",
            "name": "name",
            "inputs": [],
            "outputs": [{"name": "", "type": "string", "internalType": "string"}],
            "stateMutability": "view",
        },
        {
            "type": "function",
            "name": "setName",
            "inputs": [{"name": "_name", "type": "string", "internalType": "string"}],
            "outputs": [],
            "stateMutability": "nonpayable",
        },
    ],
)


class NoConstructorContract(Contract):
    """A web3.py Contract class for the NoConstructor contract."""

    abi: ABI = noconstructor_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x60c06040526007608090815266191959985d5b1d60ca1b60a05260009061002690826100da565b5034801561003357600080fd5b50610199565b634e487b7160e01b600052604160045260246000fd5b600181811c9082168061006357607f821691505b60208210810361008357634e487b7160e01b600052602260045260246000fd5b50919050565b601f8211156100d5576000816000526020600020601f850160051c810160208610156100b25750805b601f850160051c820191505b818110156100d1578281556001016100be565b5050505b505050565b81516001600160401b038111156100f3576100f3610039565b61010781610101845461004f565b84610089565b602080601f83116001811461013c57600084156101245750858301515b600019600386901b1c1916600185901b1785556100d1565b600085815260208120601f198616915b8281101561016b5788860151825594840194600190910190840161014c565b50858210156101895787850151600019600388901b60f8161c191681555b5050505050600190811b01905550565b6103a3806101a86000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c806306fdde031461003b578063c47f002714610059575b600080fd5b61004361006e565b604051610050919061010c565b60405180910390f35b61006c610067366004610171565b6100fc565b005b6000805461007b90610222565b80601f01602080910402602001604051908101604052809291908181526020018280546100a790610222565b80156100f45780601f106100c9576101008083540402835291602001916100f4565b820191906000526020600020905b8154815290600101906020018083116100d757829003601f168201915b505050505081565b600061010882826102ad565b5050565b60006020808352835180602085015260005b8181101561013a5785810183015185820160400152820161011e565b506000604082860101526040601f19601f8301168501019250505092915050565b634e487b7160e01b600052604160045260246000fd5b60006020828403121561018357600080fd5b813567ffffffffffffffff8082111561019b57600080fd5b818401915084601f8301126101af57600080fd5b8135818111156101c1576101c161015b565b604051601f8201601f19908116603f011681019083821181831017156101e9576101e961015b565b8160405282815287602084870101111561020257600080fd5b826020860160208301376000928101602001929092525095945050505050565b600181811c9082168061023657607f821691505b60208210810361025657634e487b7160e01b600052602260045260246000fd5b50919050565b601f8211156102a8576000816000526020600020601f850160051c810160208610156102855750805b601f850160051c820191505b818110156102a457828155600101610291565b5050505b505050565b815167ffffffffffffffff8111156102c7576102c761015b565b6102db816102d58454610222565b8461025c565b602080601f83116001811461031057600084156102f85750858301515b600019600386901b1c1916600185901b1785556102a4565b600085815260208120601f198616915b8281101561033f57888601518255948401946001909101908401610320565b508582101561035d5787850151600019600388901b60f8161c191681555b5050505050600190811b0190555056fea26469706673582212203df9d86aa6f2c45f9e29458168dddac1ca445f8f2409ce94f667aebe984bc1fa64736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = NoConstructorContractFunctions(noconstructor_abi, self.w3, address)  # type: ignore

    functions: NoConstructorContractFunctions

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
        contract.functions = NoConstructorContractFunctions(noconstructor_abi, w3, None)

        return contract
