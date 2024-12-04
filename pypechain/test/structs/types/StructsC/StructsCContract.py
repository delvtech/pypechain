"""A web3.py Contract class for the StructsC contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.48.
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
    PypechainOverloadedFunctions,
    dataclass_to_tuple,
    expand_struct_type_str,
    get_arg_type_names,
    rename_returned_types,
)

from ..IStructs import IStructsTypes as IStructs
from ..StructsC import StructsCTypes as StructsC

structs = {
    "StructsC.InnyStruct": StructsC.InnyStruct,
    "StructsC.NestedStruct": StructsC.NestedStruct,
    "StructsC.OuterStruct": StructsC.OuterStruct,
    "IStructs.InnerStruct": IStructs.InnerStruct,
    "StructsC.CStruct": StructsC.CStruct,
}

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


class StructsCAllStructsInternalContractFunction0(PypechainContractFunction):
    """ContractFunction for the allStructsInternal() method."""

    _function_name = "allStructsInternal"
    _type_signature = expand_struct_type_str(tuple([]), structs)
    _error_class = StructsCContractErrors

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
        raw_values = self._call(transaction, block_identifier, state_override, ccip_read_enabled)

        return cast(StructsC.OuterStruct, rename_returned_types(structs, return_types, raw_values))


class StructsCAllStructsInternalContractFunction(PypechainOverloadedFunctions):
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
        # Special case when there are no args or kwargs
        if len(args) == 0 and len(kwargs) == 0:
            # We need to specify the element identifier as the function call without arguments.
            # Despite this setting the member variable `abi_element_identifier`
            # that's shared across this object, this field gets overwritten in the
            # clone if arguments are provided.
            self.abi_element_identifier = self._function_name + "()"
            clone = super().__call__()
        else:
            clone = super().__call__(
                *(dataclass_to_tuple(arg) for arg in args),
                **{key: dataclass_to_tuple(arg) for key, arg in kwargs.items()},
            )

        # Arguments is the flattened set of arguments from args and kwargs, ordered by the abi
        # We get the python types of the args passed in, but remapped from tuples -> dataclasses
        arg_types = get_arg_type_names(clone.arguments)

        # Grab the relevant kwargs when factory was called.
        factory_kwargs = self._factory_kwargs
        factory_kwargs["abi_element_identifier"] = clone.abi_element_identifier

        function_obj = self._overloaded_functions[arg_types].factory(self._function_name, **factory_kwargs)

        function_obj.args = clone.args
        function_obj.kwargs = clone.kwargs

        # The `@overload` of `__call__` takes care of setting the type of this object correctly
        return function_obj  # type: ignore

    @classmethod
    def factory(cls, class_name: str, **kwargs: Any) -> Self:
        out = super().factory(class_name, **kwargs)
        # Store the factory args for downstream consumption
        out._factory_kwargs = kwargs

        # We initialize our overridden functions here.
        # Note that we use the initialized object to ensure each function
        # is attached to the instantiated object
        # (attached to a specific web3 and contract address)
        out._overloaded_functions = {
            StructsCAllStructsInternalContractFunction0._type_signature: StructsCAllStructsInternalContractFunction0,
        }
        return out


class StructsCInnerStructIsExternalContractFunction0(PypechainContractFunction):
    """ContractFunction for the innerStructIsExternal() method."""

    _function_name = "innerStructIsExternal"
    _type_signature = expand_struct_type_str(tuple([]), structs)
    _error_class = StructsCContractErrors

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
        raw_values = self._call(transaction, block_identifier, state_override, ccip_read_enabled)

        return cast(StructsC.CStruct, rename_returned_types(structs, return_types, raw_values))


class StructsCInnerStructIsExternalContractFunction(PypechainOverloadedFunctions):
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
        # Special case when there are no args or kwargs
        if len(args) == 0 and len(kwargs) == 0:
            # We need to specify the element identifier as the function call without arguments.
            # Despite this setting the member variable `abi_element_identifier`
            # that's shared across this object, this field gets overwritten in the
            # clone if arguments are provided.
            self.abi_element_identifier = self._function_name + "()"
            clone = super().__call__()
        else:
            clone = super().__call__(
                *(dataclass_to_tuple(arg) for arg in args),
                **{key: dataclass_to_tuple(arg) for key, arg in kwargs.items()},
            )

        # Arguments is the flattened set of arguments from args and kwargs, ordered by the abi
        # We get the python types of the args passed in, but remapped from tuples -> dataclasses
        arg_types = get_arg_type_names(clone.arguments)

        # Grab the relevant kwargs when factory was called.
        factory_kwargs = self._factory_kwargs
        factory_kwargs["abi_element_identifier"] = clone.abi_element_identifier

        function_obj = self._overloaded_functions[arg_types].factory(self._function_name, **factory_kwargs)

        function_obj.args = clone.args
        function_obj.kwargs = clone.kwargs

        # The `@overload` of `__call__` takes care of setting the type of this object correctly
        return function_obj  # type: ignore

    @classmethod
    def factory(cls, class_name: str, **kwargs: Any) -> Self:
        out = super().factory(class_name, **kwargs)
        # Store the factory args for downstream consumption
        out._factory_kwargs = kwargs

        # We initialize our overridden functions here.
        # Note that we use the initialized object to ensure each function
        # is attached to the instantiated object
        # (attached to a specific web3 and contract address)
        out._overloaded_functions = {
            StructsCInnerStructIsExternalContractFunction0._type_signature: StructsCInnerStructIsExternalContractFunction0,
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


class StructsCContract(Contract):
    """A web3.py Contract class for the StructsC contract."""

    abi: ABI = structsc_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b5060f48061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c80638012d826146037578063fc0db1de14606c575b600080fd5b604080518082018252600060208083018281529092528251808401845280830182815290529151918252015b60405180910390f35b608e60408051606081018252600091810191825260208101918252908152609e565b6040519051515181526020016063565b50604080516060810182526001918101918252602081019182529081529056fea26469706673582212205900f00372304faa9ba1e2d1953ca8b18c52e723f21a6a744e0559f4590a61e464736f6c63430008180033"
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
