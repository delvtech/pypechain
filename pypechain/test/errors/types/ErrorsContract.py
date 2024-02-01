"""A web3.py Contract class for the Errors contract.

DO NOT EDIT.  This file was generated by pypechain.  See documentation at
https://github.com/delvtech/pypechain"""

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

from __future__ import annotations

from typing import Any, Type, cast

from eth_abi.codec import ABICodec
from eth_abi.registry import registry as default_registry
from eth_account.signers.local import LocalAccount
from eth_typing import ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunction, ContractFunctions
from web3.exceptions import FallbackNotFound
from web3.types import ABI, ABIFunction, BlockIdentifier, CallOverride, TxParams

from .utilities import get_abi_input_types

structs = {}


class ErrorsRevertWithErrorOneContractFunction(ContractFunction):
    """ContractFunction for the revertWithErrorOne method."""

    def __call__(self) -> ErrorsRevertWithErrorOneContractFunction:  # type: ignore
        clone = super().__call__()
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> None:
        """returns None."""
        # Define the expected return types from the smart contract call

        # Call the function


class ErrorsRevertWithErrorThreeContractFunction(ContractFunction):
    """ContractFunction for the revertWithErrorThree method."""

    def __call__(self) -> ErrorsRevertWithErrorThreeContractFunction:  # type: ignore
        clone = super().__call__()
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> None:
        """returns None."""
        # Define the expected return types from the smart contract call

        # Call the function


class ErrorsRevertWithErrorTwoContractFunction(ContractFunction):
    """ContractFunction for the revertWithErrorTwo method."""

    def __call__(self) -> ErrorsRevertWithErrorTwoContractFunction:  # type: ignore
        clone = super().__call__()
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> None:
        """returns None."""
        # Define the expected return types from the smart contract call

        # Call the function


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
            function_identifier="revertWithErrorOne",
        )
        self.revertWithErrorThree = ErrorsRevertWithErrorThreeContractFunction.factory(
            "revertWithErrorThree",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="revertWithErrorThree",
        )
        self.revertWithErrorTwo = ErrorsRevertWithErrorTwoContractFunction.factory(
            "revertWithErrorTwo",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="revertWithErrorTwo",
        )


class ErrorsOneContractError:
    """ContractError for One."""

    # @combomethod destroys return types, so we are redefining functions as both class and instance
    # pylint: disable=function-redefined

    # 4 byte error selector
    selector: str
    # error signature, i.e. CustomError(uint256,bool)
    signature: str

    # pylint: disable=useless-parent-delegation
    def __init__(
        self: "ErrorsOneContractError",
    ) -> None:
        self.selector = "0xbe0c2110"
        self.signature = "One()"

    def decode_error_data(  # type: ignore
        self: "ErrorsOneContractError",
        data: HexBytes,
        # TODO: instead of returning a tuple, return a dataclass with the input names and types just like we do for functions
    ) -> tuple[Any, ...]:
        """Decodes error data returns from a smart contract."""
        error_abi = cast(
            ABIFunction,
            [item for item in errors_abi if item.get("name") == "One" and item.get("type") == "error"][0],
        )
        types = get_abi_input_types(error_abi)
        abi_codec = ABICodec(default_registry)
        decoded = abi_codec.decode(types, HexBytes(data))
        return decoded

    @classmethod
    def decode_error_data(  # type: ignore
        cls: Type["ErrorsOneContractError"],
        data: HexBytes,
    ) -> tuple[Any, ...]:
        """Decodes error data returns from a smart contract."""
        error_abi = cast(
            ABIFunction,
            [item for item in errors_abi if item.get("name") == "One" and item.get("type") == "error"][0],
        )
        types = get_abi_input_types(error_abi)
        abi_codec = ABICodec(default_registry)
        decoded = abi_codec.decode(types, HexBytes(data))
        return decoded


class ErrorsThreeContractError:
    """ContractError for Three."""

    # @combomethod destroys return types, so we are redefining functions as both class and instance
    # pylint: disable=function-redefined

    # 4 byte error selector
    selector: str
    # error signature, i.e. CustomError(uint256,bool)
    signature: str

    # pylint: disable=useless-parent-delegation
    def __init__(
        self: "ErrorsThreeContractError",
    ) -> None:
        self.selector = "0x09b8b989"
        self.signature = "Three(bool,(uint256,uint256,uint256,uint256),uint8)"

    def decode_error_data(  # type: ignore
        self: "ErrorsThreeContractError",
        data: HexBytes,
        # TODO: instead of returning a tuple, return a dataclass with the input names and types just like we do for functions
    ) -> tuple[Any, ...]:
        """Decodes error data returns from a smart contract."""
        error_abi = cast(
            ABIFunction,
            [item for item in errors_abi if item.get("name") == "Three" and item.get("type") == "error"][0],
        )
        types = get_abi_input_types(error_abi)
        abi_codec = ABICodec(default_registry)
        decoded = abi_codec.decode(types, HexBytes(data))
        return decoded

    @classmethod
    def decode_error_data(  # type: ignore
        cls: Type["ErrorsThreeContractError"],
        data: HexBytes,
    ) -> tuple[Any, ...]:
        """Decodes error data returns from a smart contract."""
        error_abi = cast(
            ABIFunction,
            [item for item in errors_abi if item.get("name") == "Three" and item.get("type") == "error"][0],
        )
        types = get_abi_input_types(error_abi)
        abi_codec = ABICodec(default_registry)
        decoded = abi_codec.decode(types, HexBytes(data))
        return decoded


class ErrorsTwoContractError:
    """ContractError for Two."""

    # @combomethod destroys return types, so we are redefining functions as both class and instance
    # pylint: disable=function-redefined

    # 4 byte error selector
    selector: str
    # error signature, i.e. CustomError(uint256,bool)
    signature: str

    # pylint: disable=useless-parent-delegation
    def __init__(
        self: "ErrorsTwoContractError",
    ) -> None:
        self.selector = "0x01e3e2f6"
        self.signature = "Two(string,address,uint8)"

    def decode_error_data(  # type: ignore
        self: "ErrorsTwoContractError",
        data: HexBytes,
        # TODO: instead of returning a tuple, return a dataclass with the input names and types just like we do for functions
    ) -> tuple[Any, ...]:
        """Decodes error data returns from a smart contract."""
        error_abi = cast(
            ABIFunction,
            [item for item in errors_abi if item.get("name") == "Two" and item.get("type") == "error"][0],
        )
        types = get_abi_input_types(error_abi)
        abi_codec = ABICodec(default_registry)
        decoded = abi_codec.decode(types, HexBytes(data))
        return decoded

    @classmethod
    def decode_error_data(  # type: ignore
        cls: Type["ErrorsTwoContractError"],
        data: HexBytes,
    ) -> tuple[Any, ...]:
        """Decodes error data returns from a smart contract."""
        error_abi = cast(
            ABIFunction,
            [item for item in errors_abi if item.get("name") == "Two" and item.get("type") == "error"][0],
        )
        types = get_abi_input_types(error_abi)
        abi_codec = ABICodec(default_registry)
        decoded = abi_codec.decode(types, HexBytes(data))
        return decoded


class ErrorsContractErrors:
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


errors_abi: ABI = cast(
    ABI,
    [
        {"inputs": [], "name": "One", "type": "error"},
        {
            "inputs": [
                {"internalType": "bool", "name": "trueOrFalse", "type": "bool"},
                {
                    "components": [
                        {"internalType": "uint256", "name": "bart", "type": "uint256"},
                        {"internalType": "uint256", "name": "lisa", "type": "uint256"},
                        {"internalType": "uint256", "name": "homer", "type": "uint256"},
                        {"internalType": "uint256", "name": "marge", "type": "uint256"},
                    ],
                    "internalType": "struct Errors.Ages",
                    "name": "theSimpsons",
                    "type": "tuple",
                },
                {"internalType": "enum Errors.Simpsons", "name": "who", "type": "uint8"},
            ],
            "name": "Three",
            "type": "error",
        },
        {
            "inputs": [
                {"internalType": "string", "name": "message", "type": "string"},
                {"internalType": "address", "name": "who", "type": "address"},
                {"internalType": "uint8", "name": "value", "type": "uint8"},
            ],
            "name": "Two",
            "type": "error",
        },
        {"inputs": [], "name": "revertWithErrorOne", "outputs": [], "stateMutability": "pure", "type": "function"},
        {"inputs": [], "name": "revertWithErrorThree", "outputs": [], "stateMutability": "pure", "type": "function"},
        {"inputs": [], "name": "revertWithErrorTwo", "outputs": [], "stateMutability": "pure", "type": "function"},
    ],
)
# pylint: disable=line-too-long
errors_bytecode = HexStr(
    "0x608060405234801561000f575f80fd5b506104328061001d5f395ff3fe608060405234801561000f575f80fd5b506004361061003f575f3560e01c806349cbdbf514610043578063a13e7b711461004d578063dc785aeb14610057575b5f80fd5b61004b610061565b005b6100556100ca565b005b61005f6100fc565b005b5f6040518060800160405280600181526020016002815260200160038152602001600481525090505f815f6040517f09b8b9890000000000000000000000000000000000000000000000000000000081526004016100c193929190610234565b60405180910390fd5b6040517fbe0c211000000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b5f60ff6040517f01e3e2f60000000000000000000000000000000000000000000000000000000081526004016101339291906103c2565b60405180910390fd5b5f8115159050919050565b6101508161013c565b82525050565b5f819050919050565b61016881610156565b82525050565b608082015f8201516101825f85018261015f565b506020820151610195602085018261015f565b5060408201516101a8604085018261015f565b5060608201516101bb606085018261015f565b50505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602160045260245ffd5b600481106101ff576101fe6101c1565b5b50565b5f81905061020f826101ee565b919050565b5f61021e82610202565b9050919050565b61022e81610214565b82525050565b5f60c0820190506102475f830186610147565b610254602083018561016e565b61026160a0830184610225565b949350505050565b5f82825260208201905092915050565b7f492077696c6c206e6f7420706c6564676520616c6c656769616e636520746f205f8201527f426172742e20492077696c6c206e6f7420706c6564676520616c6c656769616e60208201527f636520746f20426172742e20492077696c6c206e6f7420706c6564676520616c60408201527f6c656769616e636520746f20426172742e000000000000000000000000000000606082015250565b5f61031f607183610269565b915061032a82610279565b608082019050919050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61035e82610335565b9050919050565b61036e81610354565b82525050565b5f819050919050565b5f60ff82169050919050565b5f819050919050565b5f6103ac6103a76103a284610374565b610389565b61037d565b9050919050565b6103bc81610392565b82525050565b5f6060820190508181035f8301526103d981610313565b90506103e86020830185610365565b6103f560408301846103b3565b939250505056fea2646970667358221220d2ccb335b1907f8c97ee5b43958fd13ff523a48524e48710094939c1728f158b64736f6c63430008170033"
)


class ErrorsContract(Contract):
    """A web3.py Contract class for the Errors contract."""

    abi: ABI = errors_abi
    bytecode: bytes = HexBytes(errors_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = ErrorsContractFunctions(errors_abi, self.w3, address)  # type: ignore

            self.errors = ErrorsContractErrors()

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

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

        return super().constructor()

    @classmethod
    def deploy(cls, w3: Web3, account: LocalAccount | ChecksumAddress) -> Self:
        """Deploys and instance of the contract.

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
        current_nonce = w3.eth.get_transaction_count(account.address)
        deployment_tx.update({"nonce": current_nonce})

        # Sign the transaction with local account private key
        signed_tx = account.sign_transaction(deployment_tx)

        # Send the signed transaction and wait for receipt
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        deployed_contract = deployer(address=tx_receipt.contractAddress)  # type: ignore
        return deployed_contract

    @classmethod
    def factory(cls, w3: Web3, class_name: str | None = None, **kwargs: Any) -> Type[Self]:
        """Deploys and instance of the contract.

        Parameters
        ----------
        w3 : Web3
            A web3 instance.
        class_name: str | None
            The instance class name.

        Returns
        -------
        Self
            A deployed instance of the contract.
        """
        contract = super().factory(w3, class_name, **kwargs)
        contract.functions = ErrorsContractFunctions(errors_abi, w3, None)

        return contract
