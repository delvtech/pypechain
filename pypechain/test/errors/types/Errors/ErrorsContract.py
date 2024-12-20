"""A web3.py Contract class for the Errors contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.49.
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
    PypechainBaseError,
    PypechainContractFunction,
    PypechainOverloadedFunctions,
    dataclass_to_tuple,
    expand_struct_type_str,
    get_arg_type_names,
)

from ..Errors import ErrorsTypes as Errors

structs = {
    "Errors.Ages": Errors.Ages,
}

errors_abi: ABI = cast(
    ABI,
    [
        {"type": "function", "name": "revertWithErrorOne", "inputs": [], "outputs": [], "stateMutability": "pure"},
        {
            "type": "function",
            "name": "revertWithErrorThree",
            "inputs": [
                {
                    "name": "ages",
                    "type": "tuple",
                    "internalType": "struct Errors.Ages",
                    "components": [
                        {"name": "bart", "type": "uint256", "internalType": "uint256"},
                        {"name": "lisa", "type": "uint256", "internalType": "uint256"},
                        {"name": "homer", "type": "uint256", "internalType": "uint256"},
                        {"name": "marge", "type": "uint256", "internalType": "uint256"},
                    ],
                }
            ],
            "outputs": [],
            "stateMutability": "pure",
        },
        {"type": "function", "name": "revertWithErrorTwo", "inputs": [], "outputs": [], "stateMutability": "pure"},
        {"type": "error", "name": "One", "inputs": []},
        {
            "type": "error",
            "name": "Three",
            "inputs": [
                {"name": "trueOrFalse", "type": "bool", "internalType": "bool"},
                {
                    "name": "theSimpsons",
                    "type": "tuple",
                    "internalType": "struct Errors.Ages",
                    "components": [
                        {"name": "bart", "type": "uint256", "internalType": "uint256"},
                        {"name": "lisa", "type": "uint256", "internalType": "uint256"},
                        {"name": "homer", "type": "uint256", "internalType": "uint256"},
                        {"name": "marge", "type": "uint256", "internalType": "uint256"},
                    ],
                },
                {"name": "who", "type": "uint8", "internalType": "enum Errors.Simpsons"},
            ],
        },
        {
            "type": "error",
            "name": "Two",
            "inputs": [
                {"name": "message", "type": "string", "internalType": "string"},
                {"name": "who", "type": "address", "internalType": "address"},
                {"name": "value", "type": "uint8", "internalType": "uint8"},
            ],
        },
    ],
)


class ErrorsOneContractError(PypechainBaseError):
    """ContractError for One."""

    # Error name
    name: str = "One"
    # 4 byte error selector
    selector: str = "0xbe0c2110"
    # error signature, i.e. CustomError(uint256,bool)
    signature: str = "One()"
    # Error input types
    abi: ABI = errors_abi


class ErrorsThreeContractError(PypechainBaseError):
    """ContractError for Three."""

    # Error name
    name: str = "Three"
    # 4 byte error selector
    selector: str = "0x09b8b989"
    # error signature, i.e. CustomError(uint256,bool)
    signature: str = "Three(bool,(uint256,uint256,uint256,uint256),uint8)"
    # Error input types
    abi: ABI = errors_abi


class ErrorsTwoContractError(PypechainBaseError):
    """ContractError for Two."""

    # Error name
    name: str = "Two"
    # 4 byte error selector
    selector: str = "0x01e3e2f6"
    # error signature, i.e. CustomError(uint256,bool)
    signature: str = "Two(string,address,uint8)"
    # Error input types
    abi: ABI = errors_abi


class ErrorsContractErrors(PypechainBaseContractErrors):
    """ContractErrors for the Errors contract."""

    One: ErrorsOneContractError

    Three: ErrorsThreeContractError

    Two: ErrorsTwoContractError

    def __init__(
        self,
    ) -> None:
        self.One = ErrorsOneContractError()
        self.Three = ErrorsThreeContractError()
        self.Two = ErrorsTwoContractError()

        self._all = [
            self.One,
            self.Three,
            self.Two,
        ]


class ErrorsRevertWithErrorOneContractFunction0(PypechainContractFunction):
    """ContractFunction for the revertWithErrorOne() method."""

    _function_name = "revertWithErrorOne"
    _type_signature = expand_struct_type_str(tuple([]), structs)
    _error_class = ErrorsContractErrors

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> None:
        """returns None."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Call the function
        raw_values = self._call(transaction, block_identifier, state_override, ccip_read_enabled)


class ErrorsRevertWithErrorOneContractFunction(PypechainOverloadedFunctions):
    """ContractFunction for the revertWithErrorOne method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "revertWithErrorOne"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self) -> ErrorsRevertWithErrorOneContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> ErrorsRevertWithErrorOneContractFunction:  # type: ignore
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
            ErrorsRevertWithErrorOneContractFunction0._type_signature: ErrorsRevertWithErrorOneContractFunction0,
        }
        return out


class ErrorsRevertWithErrorThreeContractFunction0(PypechainContractFunction):
    """ContractFunction for the revertWithErrorThree(Errors.Ages) method."""

    _function_name = "revertWithErrorThree"
    _type_signature = expand_struct_type_str(tuple(["Errors.Ages"]), structs)
    _error_class = ErrorsContractErrors

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> None:
        """returns None."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Call the function
        raw_values = self._call(transaction, block_identifier, state_override, ccip_read_enabled)


class ErrorsRevertWithErrorThreeContractFunction(PypechainOverloadedFunctions):
    """ContractFunction for the revertWithErrorThree method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "revertWithErrorThree"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self, ages: Errors.Ages) -> ErrorsRevertWithErrorThreeContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> ErrorsRevertWithErrorThreeContractFunction:  # type: ignore
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
            ErrorsRevertWithErrorThreeContractFunction0._type_signature: ErrorsRevertWithErrorThreeContractFunction0,
        }
        return out


class ErrorsRevertWithErrorTwoContractFunction0(PypechainContractFunction):
    """ContractFunction for the revertWithErrorTwo() method."""

    _function_name = "revertWithErrorTwo"
    _type_signature = expand_struct_type_str(tuple([]), structs)
    _error_class = ErrorsContractErrors

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> None:
        """returns None."""
        # We handle the block identifier = None case here for typing.
        if block_identifier is None:
            block_identifier = self.w3.eth.default_block

        # Call the function
        raw_values = self._call(transaction, block_identifier, state_override, ccip_read_enabled)


class ErrorsRevertWithErrorTwoContractFunction(PypechainOverloadedFunctions):
    """ContractFunction for the revertWithErrorTwo method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    _function_name = "revertWithErrorTwo"

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self) -> ErrorsRevertWithErrorTwoContractFunction0:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> ErrorsRevertWithErrorTwoContractFunction:  # type: ignore
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
            ErrorsRevertWithErrorTwoContractFunction0._type_signature: ErrorsRevertWithErrorTwoContractFunction0,
        }
        return out


class ErrorsContractFunctions(ContractFunctions):
    """ContractFunctions for the Errors contract."""

    revertWithErrorOne: ErrorsRevertWithErrorOneContractFunction

    revertWithErrorThree: ErrorsRevertWithErrorThreeContractFunction

    revertWithErrorTwo: ErrorsRevertWithErrorTwoContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.revertWithErrorOne = ErrorsRevertWithErrorOneContractFunction.factory(
            "revertWithErrorOne",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="revertWithErrorOne",
        )
        self.revertWithErrorThree = ErrorsRevertWithErrorThreeContractFunction.factory(
            "revertWithErrorThree",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="revertWithErrorThree",
        )
        self.revertWithErrorTwo = ErrorsRevertWithErrorTwoContractFunction.factory(
            "revertWithErrorTwo",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="revertWithErrorTwo",
        )


class ErrorsContract(Contract):
    """A web3.py Contract class for the Errors contract."""

    abi: ABI = errors_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b5061021a806100206000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c8063987daa8214610046578063a13e7b711461005b578063dc785aeb14610063575b600080fd5b610059610054366004610112565b61006b565b005b610059610095565b6100596100ae565b60008160006040516309b8b98960e01b815260040161008c93929190610186565b60405180910390fd5b604051630be0c21160e41b815260040160405180910390fd5b60405162f1f17b60e11b815260606004820152602560648201527f492077696c6c206e6f7420706c6564676520616c6c656769616e636520746f206084820152642130b93a1760d91b60a48201526000602482015260ff604482015260c40161008c565b60006080828403121561012457600080fd5b6040516080810181811067ffffffffffffffff8211171561015557634e487b7160e01b600052604160045260246000fd5b8060405250823581526020830135602082015260408301356040820152606083013560608201528091505092915050565b600060c082019050841515825283516020830152602084015160408301526040840151606083015260608401516080830152600483106101d657634e487b7160e01b600052602160045260246000fd5b8260a083015294935050505056fea2646970667358221220acb78cc98c38846ebf51fc20c2b9cddfb4d5b3c3486feea68dcc9b46f1e292b064736f6c63430008180033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = ErrorsContractFunctions(errors_abi, self.w3, address)  # type: ignore

        self.errors = ErrorsContractErrors()

    errors: ErrorsContractErrors = ErrorsContractErrors()

    functions: ErrorsContractFunctions

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
        contract.functions = ErrorsContractFunctions(errors_abi, w3, None)
        contract.errors = ErrorsContractErrors()

        return contract
