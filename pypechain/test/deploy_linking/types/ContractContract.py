"""A web3.py Contract class for the Contract contract.

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

# methods are overriden with specific arguments instead of generic *args, **kwargs
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
from typing import Any, NamedTuple, Type, cast, overload

from eth_account.signers.local import LocalAccount
from eth_typing import ABI, ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunctions
from web3.types import BlockIdentifier, StateOverride, TxParams

from pypechain.core import (
    PypechainContractFunction,
    dataclass_to_tuple,
    expand_struct_type_str,
    get_arg_type_names,
    handle_contract_logic_error,
    rename_returned_types,
)

from .MyLibraryContract import MyLibraryContract

structs = {}


class ContractAddContractFunction0(PypechainContractFunction):
    """ContractFunction for the add(int,int) method."""

    _function_name = "add"
    _type_signature = expand_struct_type_str(tuple(["int", "int"]), structs)

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
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=ContractContractErrors,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err

        return cast(int, rename_returned_types(structs, return_types, raw_values))


class ContractAddContractFunction(PypechainContractFunction):
    """ContractFunction for the add method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "add"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self, a: int, b: int) -> ContractAddContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> ContractAddContractFunction:  # type: ignore
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
            ContractAddContractFunction0._type_signature: ContractAddContractFunction0.factory(
                "ContractAddContractFunction0", **kwargs
            ),
        }
        return out


class ContractContractFunctions(ContractFunctions):
    """ContractFunctions for the Contract contract."""

    add: ContractAddContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.add = ContractAddContractFunction.factory(
            "add",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="add",
        )


contract_abi: ABI = cast(
    ABI,
    [
        {"type": "constructor", "inputs": [], "stateMutability": "nonpayable"},
        {
            "type": "function",
            "name": "add",
            "inputs": [
                {"name": "a", "type": "int256", "internalType": "int256"},
                {"name": "b", "type": "int256", "internalType": "int256"},
            ],
            "outputs": [{"name": "", "type": "int256", "internalType": "int256"}],
            "stateMutability": "pure",
        },
    ],
)


class ContractContract(Contract):
    """A web3.py Contract class for the Contract contract."""

    abi: ABI = contract_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b5061014b806100206000396000f3fe608060405234801561001057600080fd5b506004361061002b5760003560e01c8063a5f3c23b14610030575b600080fd5b61004361003e3660046100da565b610055565b60405190815260200160405180910390f35b60405163a5f3c23b60e01b8152600481018390526024810182905260009073__$81c732ea87169659ae18eec7be97daeb59$__9063a5f3c23b90604401602060405180830381865af41580156100af573d6000803e3d6000fd5b505050506040513d601f19601f820116820180604052508101906100d391906100fc565b9392505050565b600080604083850312156100ed57600080fd5b50508035926020909101359150565b60006020828403121561010e57600080fd5b505191905056fea26469706673582212203e385201b901c32fa0479ef9dd1325389f0f2975f8a784d655f0e38b1b98e6e064736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = ContractContractFunctions(contract_abi, self.w3, address)  # type: ignore

    functions: ContractContractFunctions

    class LinkReferences(NamedTuple):
        """Link references required when deploying."""

        MyLibrary: MyLibraryContract

    link_references_placeholder_lookup: dict[str, str] = {
        "MyLibrary": "__$81c732ea87169659ae18eec7be97daeb59$__",
    }

    @classmethod
    def constructor(cls, link_references: LinkReferences) -> ContractConstructor:  # type: ignore
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

            cls.bytecode = cls.bytecode.replace(
                cls.link_references_placeholder_lookup["MyLibrary"], link_references.MyLibrary.address[2:].lower()
            )

            # bytecode needs to be in hex for web3
            cls.bytecode = HexBytes(cls.bytecode)

        return super().constructor()

    @classmethod
    def deploy(cls, w3: Web3, account: LocalAccount | ChecksumAddress, link_references: LinkReferences) -> Self:
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
        constructor_fn = deployer.constructor(link_references)

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
        contract.functions = ContractContractFunctions(contract_abi, w3, None)

        return contract
