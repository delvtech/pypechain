"""A web3.py Contract class for the Errors contract.

DO NOT EDIT.  This file was generated by pypechain v0.0.40.
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


from __future__ import annotations

from typing import Any, Type, cast

from eth_abi.codec import ABICodec
from eth_abi.registry import registry as default_registry
from eth_account.signers.local import LocalAccount
from eth_typing import ABI, ABIFunction, ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunction, ContractFunctions
from web3.types import BlockIdentifier, StateOverride, TxParams

from pypechain.core import combomethod_typed, get_abi_input_types

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
        state_override: StateOverride | None = None,
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
        state_override: StateOverride | None = None,
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
        state_override: StateOverride | None = None,
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


class ErrorsOneContractError:
    """ContractError for One."""

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

    @combomethod_typed
    def decode_error_data(
        self,
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
        decoded = abi_codec.decode(types, data)
        return decoded


class ErrorsThreeContractError:
    """ContractError for Three."""

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

    @combomethod_typed
    def decode_error_data(
        self,
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
        decoded = abi_codec.decode(types, data)
        return decoded


class ErrorsTwoContractError:
    """ContractError for Two."""

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

    @combomethod_typed
    def decode_error_data(
        self,
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
        decoded = abi_codec.decode(types, data)
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

        self._all = [
            self.One,
            self.Three,
            self.Two,
        ]

    def decode_custom_error(self, data: str) -> tuple[Any, ...]:
        """Decodes a custom contract error."""
        selector = data[:10]
        for err in self._all:
            if err.selector == selector:
                return err.decode_error_data(HexBytes(data[10:]))

        raise ValueError(f"Errors does not have a selector matching {selector}")


errors_abi: ABI = cast(
    ABI,
    [
        {"type": "function", "name": "revertWithErrorOne", "inputs": [], "outputs": [], "stateMutability": "pure"},
        {"type": "function", "name": "revertWithErrorThree", "inputs": [], "outputs": [], "stateMutability": "pure"},
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


class ErrorsContract(Contract):
    """A web3.py Contract class for the Errors contract."""

    abi: ABI = errors_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b50610216806100206000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c806349cbdbf514610046578063a13e7b7114610050578063dc785aeb14610058575b600080fd5b61004e610060565b005b61004e6100ac565b61004e6100c5565b60408051608081018252600181526002602082015260038183015260046060820181905291516309b8b98960e01b815290916100a3916000918491839101610182565b60405180910390fd5b604051630be0c21160e41b815260040160405180910390fd5b60405162f1f17b60e11b815260606004820152607160648201527f492077696c6c206e6f7420706c6564676520616c6c656769616e636520746f2060848201527f426172742e20492077696c6c206e6f7420706c6564676520616c6c656769616e60a48201527f636520746f20426172742e20492077696c6c206e6f7420706c6564676520616c60c4820152703632b3b4b0b731b2903a37902130b93a1760791b60e48201526000602482015260ff6044820152610104016100a3565b600060c082019050841515825283516020830152602084015160408301526040840151606083015260608401516080830152600483106101d257634e487b7160e01b600052602160045260246000fd5b8260a083015294935050505056fea2646970667358221220296623bdd3b38f3766971b76f4c245b8f5a41426d160fc493f0bfc894995e25e64736f6c63430008160033"
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
