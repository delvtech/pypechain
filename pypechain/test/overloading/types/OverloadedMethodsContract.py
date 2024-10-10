"""A web3.py Contract class for the OverloadedMethods contract.

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
    rename_returned_types,
)

from . import OverloadedMethodsTypes as OverloadedMethods

structs = {
    "OverloadedMethods.SimpleStruct": OverloadedMethods.SimpleStruct,
}


class OverloadedMethodsDoSomethingContractFunction0(PypechainContractFunction):
    """ContractFunction for the doSomething(OverloadedMethods.SimpleStruct) method."""

    _type_signature = expand_struct_type_str(tuple(["OverloadedMethods.SimpleStruct"]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> OverloadedMethods.SimpleStruct:
        """returns OverloadedMethods.SimpleStruct."""
        # Define the expected return types from the smart contract call

        return_types = OverloadedMethods.SimpleStruct

        # Call the function
        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)

        return cast(OverloadedMethods.SimpleStruct, rename_returned_types(structs, return_types, raw_values))


class OverloadedMethodsDoSomethingContractFunction1(PypechainContractFunction):
    """ContractFunction for the doSomething(int,str) method."""

    _type_signature = expand_struct_type_str(tuple(["int", "str"]), structs)

    class ReturnValues(NamedTuple):
        """The return named tuple for DoSomething."""

        int_input: int
        arg2: str

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> ReturnValues:
        """returns ReturnValues."""
        # Define the expected return types from the smart contract call

        return_types = [int, str]

        # Call the function
        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)

        return self.ReturnValues(*rename_returned_types(structs, return_types, raw_values))


class OverloadedMethodsDoSomethingContractFunction2(PypechainContractFunction):
    """ContractFunction for the doSomething(list[OverloadedMethods.SimpleStruct]) method."""

    _type_signature = expand_struct_type_str(tuple(["list[OverloadedMethods.SimpleStruct]"]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> list[OverloadedMethods.SimpleStruct]:
        """returns list[OverloadedMethods.SimpleStruct]."""
        # Define the expected return types from the smart contract call

        return_types = list[OverloadedMethods.SimpleStruct]

        # Call the function
        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)

        return cast(list[OverloadedMethods.SimpleStruct], rename_returned_types(structs, return_types, raw_values))


class OverloadedMethodsDoSomethingContractFunction3(PypechainContractFunction):
    """ContractFunction for the doSomething() method."""

    _type_signature = expand_struct_type_str(tuple([]), structs)

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


class OverloadedMethodsDoSomethingContractFunction4(PypechainContractFunction):
    """ContractFunction for the doSomething(str) method."""

    _type_signature = expand_struct_type_str(tuple(["str"]), structs)

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: StateOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> str:
        """returns str."""
        # Define the expected return types from the smart contract call

        return_types = str

        # Call the function
        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)

        return cast(str, rename_returned_types(structs, return_types, raw_values))


class OverloadedMethodsDoSomethingContractFunction5(PypechainContractFunction):
    """ContractFunction for the doSomething(int) method."""

    _type_signature = expand_struct_type_str(tuple(["int"]), structs)

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


class OverloadedMethodsDoSomethingContractFunction6(PypechainContractFunction):
    """ContractFunction for the doSomething(int,int) method."""

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
        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)

        return cast(int, rename_returned_types(structs, return_types, raw_values))


class OverloadedMethodsDoSomethingContractFunction(PypechainContractFunction):
    """ContractFunction for the doSomething method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined

    # Make lookup for function signature -> overloaded function
    # The function signatures are python types, as we need to do a
    # lookup of arguments passed in to contract function
    _functions: dict[str, PypechainContractFunction]

    @overload
    def __call__(self, simpleStruct: OverloadedMethods.SimpleStruct) -> OverloadedMethodsDoSomethingContractFunction0:  # type: ignore
        ...

    @overload
    def __call__(self, x: int, s: str) -> OverloadedMethodsDoSomethingContractFunction1:  # type: ignore
        ...

    @overload
    def __call__(self, simpleStructVec: list[OverloadedMethods.SimpleStruct]) -> OverloadedMethodsDoSomethingContractFunction2:  # type: ignore
        ...

    @overload
    def __call__(self) -> OverloadedMethodsDoSomethingContractFunction3:  # type: ignore
        ...

    @overload
    def __call__(self, s: str) -> OverloadedMethodsDoSomethingContractFunction4:  # type: ignore
        ...

    @overload
    def __call__(self, x: int) -> OverloadedMethodsDoSomethingContractFunction5:  # type: ignore
        ...

    @overload
    def __call__(self, x: int, y: int) -> OverloadedMethodsDoSomethingContractFunction6:  # type: ignore
        ...

    def __call__(self, *args, **kwargs) -> OverloadedMethodsDoSomethingContractFunction:  # type: ignore
        clone = super().__call__(
            *(dataclass_to_tuple(arg) for arg in args), **{key: dataclass_to_tuple(arg) for key, arg in kwargs.items()}
        )

        # Arguments is the flattened set of arguments from args and kwargs, ordered by the abi
        # We get the python types of the args passed in, but remapped from tuples -> dataclasses
        arg_types = get_arg_type_names(clone.arguments)

        # Look up the function class based on arg types
        function_obj = self._functions[arg_types]

        function_obj.args = clone.args
        function_obj.kwargs = clone.kwargs

        # The `@overload` of `__call__` takes care of setting the type of this object correctly
        return function_obj  # type: ignore

    @classmethod
    def factory(cls, class_name: str, **kwargs: Any) -> Self:
        out = super().factory(class_name, **kwargs)

        # We initialize our overridden functions here
        cls._functions = {
            OverloadedMethodsDoSomethingContractFunction0._type_signature: OverloadedMethodsDoSomethingContractFunction0.factory(
                "OverloadedMethodsDoSomethingContractFunction0", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction1._type_signature: OverloadedMethodsDoSomethingContractFunction1.factory(
                "OverloadedMethodsDoSomethingContractFunction1", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction2._type_signature: OverloadedMethodsDoSomethingContractFunction2.factory(
                "OverloadedMethodsDoSomethingContractFunction2", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction3._type_signature: OverloadedMethodsDoSomethingContractFunction3.factory(
                "OverloadedMethodsDoSomethingContractFunction3", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction4._type_signature: OverloadedMethodsDoSomethingContractFunction4.factory(
                "OverloadedMethodsDoSomethingContractFunction4", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction5._type_signature: OverloadedMethodsDoSomethingContractFunction5.factory(
                "OverloadedMethodsDoSomethingContractFunction5", **kwargs
            ),
            OverloadedMethodsDoSomethingContractFunction6._type_signature: OverloadedMethodsDoSomethingContractFunction6.factory(
                "OverloadedMethodsDoSomethingContractFunction6", **kwargs
            ),
        }
        return out


class OverloadedMethodsContractFunctions(ContractFunctions):
    """ContractFunctions for the OverloadedMethods contract."""

    doSomething: OverloadedMethodsDoSomethingContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.doSomething = OverloadedMethodsDoSomethingContractFunction.factory(
            "doSomething",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="doSomething",
        )


overloadedmethods_abi: ABI = cast(
    ABI,
    [
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [
                {
                    "name": "simpleStruct",
                    "type": "tuple",
                    "internalType": "struct OverloadedMethods.SimpleStruct",
                    "components": [
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                    ],
                }
            ],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple",
                    "internalType": "struct OverloadedMethods.SimpleStruct",
                    "components": [
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                    ],
                }
            ],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [
                {"name": "x", "type": "uint256", "internalType": "uint256"},
                {"name": "s", "type": "string", "internalType": "string"},
            ],
            "outputs": [
                {"name": "int_input", "type": "uint256", "internalType": "uint256"},
                {"name": "", "type": "string", "internalType": "string"},
            ],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [
                {
                    "name": "simpleStructVec",
                    "type": "tuple[]",
                    "internalType": "struct OverloadedMethods.SimpleStruct[]",
                    "components": [
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                    ],
                }
            ],
            "outputs": [
                {
                    "name": "",
                    "type": "tuple[]",
                    "internalType": "struct OverloadedMethods.SimpleStruct[]",
                    "components": [
                        {"name": "strVal", "type": "string", "internalType": "string"},
                        {"name": "intVal", "type": "uint256", "internalType": "uint256"},
                    ],
                }
            ],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [],
            "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [{"name": "s", "type": "string", "internalType": "string"}],
            "outputs": [{"name": "", "type": "string", "internalType": "string"}],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [{"name": "x", "type": "uint256", "internalType": "uint256"}],
            "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}],
            "stateMutability": "pure",
        },
        {
            "type": "function",
            "name": "doSomething",
            "inputs": [
                {"name": "x", "type": "uint256", "internalType": "uint256"},
                {"name": "y", "type": "uint256", "internalType": "uint256"},
            ],
            "outputs": [{"name": "added", "type": "uint256", "internalType": "uint256"}],
            "stateMutability": "pure",
        },
    ],
)


class OverloadedMethodsContract(Contract):
    """A web3.py Contract class for the OverloadedMethods contract."""

    abi: ABI = overloadedmethods_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b506105f7806100206000396000f3fe608060405234801561001057600080fd5b506004361061007d5760003560e01c8063826926791161005b57806382692679146101135780638ae3048e14610124578063a6b206bf1461013f578063b2dd1d791461015257600080fd5b80631d37834b146100825780633b6c27c4146100d55780634a4c53e9146100f5575b600080fd5b6100bf6100903660046102b1565b604080518082018252606081526000602091820152815180830190925282518252918201519181019190915290565b6040516100cc919061035d565b60405180910390f35b6100e76100e3366004610370565b9091565b6040516100cc9291906103b7565b6101066101033660046103d0565b90565b6040516100cc9190610493565b60025b6040519081526020016100cc565b6101326101033660046104f7565b6040516100cc919061052c565b61011661014d36600461053f565b610165565b610116610160366004610558565b610178565b600061017282600261057a565b92915050565b6000610184828461059f565b9392505050565b634e487b7160e01b600052604160045260246000fd5b604051601f8201601f1916810167ffffffffffffffff811182821017156101ca576101ca61018b565b604052919050565b600082601f8301126101e357600080fd5b813567ffffffffffffffff8111156101fd576101fd61018b565b610210601f8201601f19166020016101a1565b81815284602083860101111561022557600080fd5b816020850160208301376000918101602001919091529392505050565b60006040828403121561025457600080fd5b6040516040810167ffffffffffffffff82821081831117156102785761027861018b565b81604052829350843591508082111561029057600080fd5b5061029d858286016101d2565b825250602083013560208201525092915050565b6000602082840312156102c357600080fd5b813567ffffffffffffffff8111156102da57600080fd5b6102e684828501610242565b949350505050565b6000815180845260005b81811015610314576020818501810151868301820152016102f8565b506000602082860101526020601f19601f83011685010191505092915050565b600081516040845261034960408501826102ee565b602093840151949093019390935250919050565b6020815260006101846020830184610334565b6000806040838503121561038357600080fd5b82359150602083013567ffffffffffffffff8111156103a157600080fd5b6103ad858286016101d2565b9150509250929050565b8281526040602082015260006102e660408301846102ee565b600060208083850312156103e357600080fd5b823567ffffffffffffffff808211156103fb57600080fd5b818501915085601f83011261040f57600080fd5b8135818111156104215761042161018b565b8060051b6104308582016101a1565b918252838101850191858101908984111561044a57600080fd5b86860192505b83831015610486578235858111156104685760008081fd5b6104768b89838a0101610242565b8352509186019190860190610450565b9998505050505050505050565b600060208083016020845280855180835260408601915060408160051b87010192506020870160005b828110156104ea57603f198886030184526104d8858351610334565b945092850192908501906001016104bc565b5092979650505050505050565b60006020828403121561050957600080fd5b813567ffffffffffffffff81111561052057600080fd5b6102e6848285016101d2565b60208152600061018460208301846102ee565b60006020828403121561055157600080fd5b5035919050565b6000806040838503121561056b57600080fd5b50508035926020909101359150565b808202811582820484141761017257634e487b7160e01b600052601160045260246000fd5b6000826105bc57634e487b7160e01b600052601260045260246000fd5b50049056fea2646970667358221220fbb67c256adf4df798aa96e09c7826472fcd082baac0e33935ae8ea94457a89764736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = OverloadedMethodsContractFunctions(overloadedmethods_abi, self.w3, address)  # type: ignore

    functions: OverloadedMethodsContractFunctions

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
        contract.functions = OverloadedMethodsContractFunctions(overloadedmethods_abi, w3, None)

        return contract
