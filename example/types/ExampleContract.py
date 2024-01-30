"""A web3.py Contract class for the Example contract.

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

from typing import Any, NamedTuple, Type, cast

from eth_account.signers.local import LocalAccount
from eth_typing import ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunction, ContractFunctions
from web3.exceptions import FallbackNotFound
from web3.types import ABI, BlockIdentifier, CallOverride, TxParams

from .ExampleTypes import InnerStruct, NestedStruct, SimpleStruct
from .utilities import dataclass_to_tuple, rename_returned_types

structs = {
    "SimpleStruct": SimpleStruct,
    "InnerStruct": InnerStruct,
    "NestedStruct": NestedStruct,
}


class ExampleFlipFlopContractFunction(ContractFunction):
    """ContractFunction for the flipFlop method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for FlipFlop."""

        flop: int
        flip: int

    def __call__(self, flip: int, flop: int) -> ExampleFlipFlopContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(flip), dataclass_to_tuple(flop))
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> ReturnValues:
        """returns ReturnValues."""
        # Define the expected return types from the smart contract call

        return_types = [int, int]

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return self.ReturnValues(*rename_returned_types(structs, return_types, raw_values))


class ExampleGuessALetterContractFunction(ContractFunction):
    """ContractFunction for the guessALetter method."""

    def __call__(self, guess: int) -> ExampleGuessALetterContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(guess))
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


class ExampleMixStructsAndPrimitivesContractFunction(ContractFunction):
    """ContractFunction for the mixStructsAndPrimitives method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for MixStructsAndPrimitives."""

        simpleStruct: SimpleStruct
        arg2: NestedStruct
        arg3: int
        name: str
        YesOrNo: bool

    def __call__(self) -> ExampleMixStructsAndPrimitivesContractFunction:  # type: ignore
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
    ) -> ReturnValues:
        """returns ReturnValues."""
        # Define the expected return types from the smart contract call

        return_types = [SimpleStruct, NestedStruct, int, str, bool]

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return self.ReturnValues(*rename_returned_types(structs, return_types, raw_values))


class ExampleNamedSingleStructContractFunction(ContractFunction):
    """ContractFunction for the namedSingleStruct method."""

    def __call__(self) -> ExampleNamedSingleStructContractFunction:  # type: ignore
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
    ) -> SimpleStruct:
        """returns SimpleStruct."""
        # Define the expected return types from the smart contract call

        return_types = SimpleStruct

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(SimpleStruct, rename_returned_types(structs, return_types, raw_values))


class ExampleNamedTwoMixedStructsContractFunction(ContractFunction):
    """ContractFunction for the namedTwoMixedStructs method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for NamedTwoMixedStructs."""

        simpleStruct: SimpleStruct
        nestedStruct: NestedStruct

    def __call__(self) -> ExampleNamedTwoMixedStructsContractFunction:  # type: ignore
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
    ) -> ReturnValues:
        """returns ReturnValues."""
        # Define the expected return types from the smart contract call

        return_types = [SimpleStruct, NestedStruct]

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return self.ReturnValues(*rename_returned_types(structs, return_types, raw_values))


class ExampleSingleNestedStructContractFunction(ContractFunction):
    """ContractFunction for the singleNestedStruct method."""

    def __call__(self, nestedStruct: NestedStruct) -> ExampleSingleNestedStructContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(nestedStruct))
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> NestedStruct:
        """returns NestedStruct."""
        # Define the expected return types from the smart contract call

        return_types = NestedStruct

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(NestedStruct, rename_returned_types(structs, return_types, raw_values))


class ExampleSingleSimpleStructContractFunction(ContractFunction):
    """ContractFunction for the singleSimpleStruct method."""

    def __call__(self, simpleStruct: SimpleStruct) -> ExampleSingleSimpleStructContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(simpleStruct))
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> SimpleStruct:
        """returns SimpleStruct."""
        # Define the expected return types from the smart contract call

        return_types = SimpleStruct

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(SimpleStruct, rename_returned_types(structs, return_types, raw_values))


class ExampleTwoMixedStructsContractFunction(ContractFunction):
    """ContractFunction for the twoMixedStructs method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for TwoMixedStructs."""

        arg1: SimpleStruct
        arg2: NestedStruct

    def __call__(self) -> ExampleTwoMixedStructsContractFunction:  # type: ignore
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
    ) -> ReturnValues:
        """returns ReturnValues."""
        # Define the expected return types from the smart contract call

        return_types = [SimpleStruct, NestedStruct]

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return self.ReturnValues(*rename_returned_types(structs, return_types, raw_values))


class ExampleTwoSimpleStructsContractFunction(ContractFunction):
    """ContractFunction for the twoSimpleStructs method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for TwoSimpleStructs."""

        arg1: SimpleStruct
        arg2: SimpleStruct

    def __call__(self) -> ExampleTwoSimpleStructsContractFunction:  # type: ignore
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
    ) -> ReturnValues:
        """returns ReturnValues."""
        # Define the expected return types from the smart contract call

        return_types = [SimpleStruct, SimpleStruct]

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return self.ReturnValues(*rename_returned_types(structs, return_types, raw_values))


class ExampleContractFunctions(ContractFunctions):
    """ContractFunctions for the Example contract."""

    flipFlop: ExampleFlipFlopContractFunction

    guessALetter: ExampleGuessALetterContractFunction

    mixStructsAndPrimitives: ExampleMixStructsAndPrimitivesContractFunction

    namedSingleStruct: ExampleNamedSingleStructContractFunction

    namedTwoMixedStructs: ExampleNamedTwoMixedStructsContractFunction

    singleNestedStruct: ExampleSingleNestedStructContractFunction

    singleSimpleStruct: ExampleSingleSimpleStructContractFunction

    twoMixedStructs: ExampleTwoMixedStructsContractFunction

    twoSimpleStructs: ExampleTwoSimpleStructsContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.flipFlop = ExampleFlipFlopContractFunction.factory(
            "flipFlop",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="flipFlop",
        )
        self.guessALetter = ExampleGuessALetterContractFunction.factory(
            "guessALetter",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="guessALetter",
        )
        self.mixStructsAndPrimitives = ExampleMixStructsAndPrimitivesContractFunction.factory(
            "mixStructsAndPrimitives",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="mixStructsAndPrimitives",
        )
        self.namedSingleStruct = ExampleNamedSingleStructContractFunction.factory(
            "namedSingleStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="namedSingleStruct",
        )
        self.namedTwoMixedStructs = ExampleNamedTwoMixedStructsContractFunction.factory(
            "namedTwoMixedStructs",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="namedTwoMixedStructs",
        )
        self.singleNestedStruct = ExampleSingleNestedStructContractFunction.factory(
            "singleNestedStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="singleNestedStruct",
        )
        self.singleSimpleStruct = ExampleSingleSimpleStructContractFunction.factory(
            "singleSimpleStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="singleSimpleStruct",
        )
        self.twoMixedStructs = ExampleTwoMixedStructsContractFunction.factory(
            "twoMixedStructs",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="twoMixedStructs",
        )
        self.twoSimpleStructs = ExampleTwoSimpleStructsContractFunction.factory(
            "twoSimpleStructs",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="twoSimpleStructs",
        )


example_abi: ABI = cast(
    ABI,
    [
        {
            "inputs": [{"internalType": "string", "name": "name", "type": "string"}],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "inputs": [
                {"internalType": "enum Example.Letters", "name": "answer", "type": "uint8"},
                {"internalType": "string", "name": "errorMessage", "type": "string"},
            ],
            "name": "WrongChoice",
            "type": "error",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "flip", "type": "uint256"},
                {"internalType": "uint256", "name": "flop", "type": "uint256"},
            ],
            "name": "flipFlop",
            "outputs": [
                {"internalType": "uint256", "name": "_flop", "type": "uint256"},
                {"internalType": "uint256", "name": "_flip", "type": "uint256"},
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "enum Example.Letters", "name": "guess", "type": "uint8"}],
            "name": "guessALetter",
            "outputs": [],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "mixStructsAndPrimitives",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct Example.SimpleStruct",
                    "name": "simpleStruct",
                    "type": "tuple",
                },
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                        {
                            "components": [{"internalType": "bool", "name": "boolVal", "type": "bool"}],
                            "internalType": "struct Example.InnerStruct",
                            "name": "innerStruct",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct Example.NestedStruct",
                    "name": "",
                    "type": "tuple",
                },
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "string", "name": "_name", "type": "string"},
                {"internalType": "bool", "name": "YesOrNo", "type": "bool"},
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "namedSingleStruct",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct Example.SimpleStruct",
                    "name": "struct1",
                    "type": "tuple",
                }
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "namedTwoMixedStructs",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct Example.SimpleStruct",
                    "name": "simpleStruct",
                    "type": "tuple",
                },
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                        {
                            "components": [{"internalType": "bool", "name": "boolVal", "type": "bool"}],
                            "internalType": "struct Example.InnerStruct",
                            "name": "innerStruct",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct Example.NestedStruct",
                    "name": "nestedStruct",
                    "type": "tuple",
                },
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                        {
                            "components": [{"internalType": "bool", "name": "boolVal", "type": "bool"}],
                            "internalType": "struct Example.InnerStruct",
                            "name": "innerStruct",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct Example.NestedStruct",
                    "name": "nestedStruct",
                    "type": "tuple",
                }
            ],
            "name": "singleNestedStruct",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                        {
                            "components": [{"internalType": "bool", "name": "boolVal", "type": "bool"}],
                            "internalType": "struct Example.InnerStruct",
                            "name": "innerStruct",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct Example.NestedStruct",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct Example.SimpleStruct",
                    "name": "simpleStruct",
                    "type": "tuple",
                }
            ],
            "name": "singleSimpleStruct",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct Example.SimpleStruct",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "twoMixedStructs",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct Example.SimpleStruct",
                    "name": "",
                    "type": "tuple",
                },
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                        {
                            "components": [{"internalType": "bool", "name": "boolVal", "type": "bool"}],
                            "internalType": "struct Example.InnerStruct",
                            "name": "innerStruct",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct Example.NestedStruct",
                    "name": "",
                    "type": "tuple",
                },
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "twoSimpleStructs",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct Example.SimpleStruct",
                    "name": "",
                    "type": "tuple",
                },
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct Example.SimpleStruct",
                    "name": "",
                    "type": "tuple",
                },
            ],
            "stateMutability": "pure",
            "type": "function",
        },
    ],
)
# pylint: disable=line-too-long
example_bytecode = HexStr(
    "0x608060405234801562000010575f80fd5b5060405162001535380380620015358339818101604052810190620000369190620001d3565b805f908162000046919062000459565b50506200053d565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b620000af8262000067565b810181811067ffffffffffffffff82111715620000d157620000d062000077565b5b80604052505050565b5f620000e56200004e565b9050620000f38282620000a4565b919050565b5f67ffffffffffffffff82111562000115576200011462000077565b5b620001208262000067565b9050602081019050919050565b5f5b838110156200014c5780820151818401526020810190506200012f565b5f8484015250505050565b5f6200016d6200016784620000f8565b620000da565b9050828152602081018484840111156200018c576200018b62000063565b5b620001998482856200012d565b509392505050565b5f82601f830112620001b857620001b76200005f565b5b8151620001ca84826020860162000157565b91505092915050565b5f60208284031215620001eb57620001ea62000057565b5b5f82015167ffffffffffffffff8111156200020b576200020a6200005b565b5b6200021984828501620001a1565b91505092915050565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806200027157607f821691505b6020821081036200028757620002866200022c565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f60088302620002eb7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82620002ae565b620002f78683620002ae565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f620003416200033b62000335846200030f565b62000318565b6200030f565b9050919050565b5f819050919050565b6200035c8362000321565b620003746200036b8262000348565b848454620002ba565b825550505050565b5f90565b6200038a6200037c565b6200039781848462000351565b505050565b5b81811015620003be57620003b25f8262000380565b6001810190506200039d565b5050565b601f8211156200040d57620003d7816200028d565b620003e2846200029f565b81016020851015620003f2578190505b6200040a62000401856200029f565b8301826200039c565b50505b505050565b5f82821c905092915050565b5f6200042f5f198460080262000412565b1980831691505092915050565b5f6200044983836200041e565b9150826002028217905092915050565b620004648262000222565b67ffffffffffffffff81111562000480576200047f62000077565b5b6200048c825462000259565b62000499828285620003c2565b5f60209050601f831160018114620004cf575f8415620004ba578287015190505b620004c685826200043c565b86555062000535565b601f198416620004df866200028d565b5f5b828110156200050857848901518255600182019150602085019450602081019050620004e1565b8683101562000528578489015162000524601f8916826200041e565b8355505b6001600288020188555050505b505050505050565b610fea806200054b5f395ff3fe608060405234801561000f575f80fd5b5060043610610091575f3560e01c8063811d9aa311610064578063811d9aa31461011157806386a5a4c31461012f578063cf71512c1461015f578063d332644614610190578063e0f7c604146101c057610091565b806326da1c9e1461009557806340e27b10146100b157806353fd1043146100d057806373b10c0f146100ef575b5f80fd5b6100af60048036038101906100aa91906106df565b6101df565b005b6100b961025f565b6040516100c79291906107e6565b60405180910390f35b6100d8610317565b6040516100e692919061089c565b60405180910390f35b6100f76103e6565b604051610108959493929190610937565b60405180910390f35b6101196104fa565b604051610126919061099d565b60405180910390f35b610149600480360381019061014491906109df565b610552565b604051610156919061099d565b60405180910390f35b61017960048036038101906101749190610a50565b61056b565b604051610187929190610a8e565b60405180910390f35b6101aa60048036038101906101a59190610ad3565b61057a565b6040516101b79190610b1a565b60405180910390f35b6101c8610593565b6040516101d692919061089c565b60405180910390f35b5f600360018360028111156101f7576101f6610b3a565b5b6102019190610ba0565b61020b9190610c01565b60ff1660028111156102205761021f610b3a565b5b9050806040517fc13b30d40000000000000000000000000000000000000000000000000000000081526004016102569190610ce7565b60405180910390fd5b610267610658565b61026f610658565b5f6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525090505f6040518060400160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d626572203200000000000000000000000000000000815250815250905081819350935050509091565b61031f610658565b610327610671565b5f6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525090505f6040518060600160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d6265722032000000000000000000000000000000008152508152602001604051806020016040528060011515815250815250905081819350935050509091565b6103ee610658565b6103f6610671565b5f60605f6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525094505f6040518060600160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d62657220320000000000000000000000000000000081525081526020016040518060200160405280600115158152508152509050858160015f6040518060400160405280601381526020017f52657475726e5479706573436f6e7472616374000000000000000000000000008152509095509550955095509550509091929394565b610502610658565b6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d626572203100000000000000000000000000000000815250815250905090565b61055a610658565b8161056490610eb0565b9050919050565b5f808284915091509250929050565b610582610671565b8161058c90610fa2565b9050919050565b61059b610658565b6105a3610671565b6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525091506040518060600160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d626572203200000000000000000000000000000000815250815260200160405180602001604052806001151581525081525090509091565b60405180604001604052805f8152602001606081525090565b60405180606001604052805f815260200160608152602001610691610697565b81525090565b60405180602001604052805f151581525090565b5f604051905090565b5f80fd5b5f80fd5b600381106106c8575f80fd5b50565b5f813590506106d9816106bc565b92915050565b5f602082840312156106f4576106f36106b4565b5b5f610701848285016106cb565b91505092915050565b5f819050919050565b61071c8161070a565b82525050565b5f81519050919050565b5f82825260208201905092915050565b5f5b8381101561075957808201518184015260208101905061073e565b5f8484015250505050565b5f601f19601f8301169050919050565b5f61077e82610722565b610788818561072c565b935061079881856020860161073c565b6107a181610764565b840191505092915050565b5f604083015f8301516107c15f860182610713565b50602083015184820360208601526107d98282610774565b9150508091505092915050565b5f6040820190508181035f8301526107fe81856107ac565b9050818103602083015261081281846107ac565b90509392505050565b5f8115159050919050565b61082f8161081b565b82525050565b602082015f8201516108495f850182610826565b50505050565b5f606083015f8301516108645f860182610713565b506020830151848203602086015261087c8282610774565b91505060408301516108916040860182610835565b508091505092915050565b5f6040820190508181035f8301526108b481856107ac565b905081810360208301526108c8818461084f565b90509392505050565b6108da8161070a565b82525050565b5f82825260208201905092915050565b5f6108fa82610722565b61090481856108e0565b935061091481856020860161073c565b61091d81610764565b840191505092915050565b6109318161081b565b82525050565b5f60a0820190508181035f83015261094f81886107ac565b90508181036020830152610963818761084f565b905061097260408301866108d1565b818103606083015261098481856108f0565b90506109936080830184610928565b9695505050505050565b5f6020820190508181035f8301526109b581846107ac565b905092915050565b5f80fd5b5f604082840312156109d6576109d56109bd565b5b81905092915050565b5f602082840312156109f4576109f36106b4565b5b5f82013567ffffffffffffffff811115610a1157610a106106b8565b5b610a1d848285016109c1565b91505092915050565b610a2f8161070a565b8114610a39575f80fd5b50565b5f81359050610a4a81610a26565b92915050565b5f8060408385031215610a6657610a656106b4565b5b5f610a7385828601610a3c565b9250506020610a8485828601610a3c565b9150509250929050565b5f604082019050610aa15f8301856108d1565b610aae60208301846108d1565b9392505050565b5f60608284031215610aca57610ac96109bd565b5b81905092915050565b5f60208284031215610ae857610ae76106b4565b5b5f82013567ffffffffffffffff811115610b0557610b046106b8565b5b610b1184828501610ab5565b91505092915050565b5f6020820190508181035f830152610b32818461084f565b905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602160045260245ffd5b5f60ff82169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f610baa82610b67565b9150610bb583610b67565b9250828201905060ff811115610bce57610bcd610b73565b5b92915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601260045260245ffd5b5f610c0b82610b67565b9150610c1683610b67565b925082610c2657610c25610bd4565b5b828206905092915050565b60038110610c4257610c41610b3a565b5b50565b5f819050610c5282610c31565b919050565b5f610c6182610c45565b9050919050565b610c7181610c57565b82525050565b7f5468616e6b20796f7520666f7220706c6179696e672c2062757420796f7520635f8201527f686f7365207468652077726f6e67206c65747465720000000000000000000000602082015250565b5f610cd16035836108e0565b9150610cdc82610c77565b604082019050919050565b5f604082019050610cfa5f830184610c68565b8181036020830152610d0b81610cc5565b905092915050565b5f80fd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610d4d82610764565b810181811067ffffffffffffffff82111715610d6c57610d6b610d17565b5b80604052505050565b5f610d7e6106ab565b9050610d8a8282610d44565b919050565b5f80fd5b5f80fd5b5f80fd5b5f67ffffffffffffffff821115610db557610db4610d17565b5b610dbe82610764565b9050602081019050919050565b828183375f83830152505050565b5f610deb610de684610d9b565b610d75565b905082815260208101848484011115610e0757610e06610d97565b5b610e12848285610dcb565b509392505050565b5f82601f830112610e2e57610e2d610d93565b5b8135610e3e848260208601610dd9565b91505092915050565b5f60408284031215610e5c57610e5b610d13565b5b610e666040610d75565b90505f610e7584828501610a3c565b5f83015250602082013567ffffffffffffffff811115610e9857610e97610d8f565b5b610ea484828501610e1a565b60208301525092915050565b5f610ebb3683610e47565b9050919050565b610ecb8161081b565b8114610ed5575f80fd5b50565b5f81359050610ee681610ec2565b92915050565b5f60208284031215610f0157610f00610d13565b5b610f0b6020610d75565b90505f610f1a84828501610ed8565b5f8301525092915050565b5f60608284031215610f3a57610f39610d13565b5b610f446060610d75565b90505f610f5384828501610a3c565b5f83015250602082013567ffffffffffffffff811115610f7657610f75610d8f565b5b610f8284828501610e1a565b6020830152506040610f9684828501610eec565b60408301525092915050565b5f610fad3683610f25565b905091905056fea264697066735822122062992a1f0d910c18b3e4158e6a13a45fecfa4e04259349bd3f28b56da17dcf2664736f6c63430008170033"
)


class ExampleContract(Contract):
    """A web3.py Contract class for the Example contract."""

    abi: ABI = example_abi
    bytecode: bytes = HexBytes(example_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = ExampleContractFunctions(example_abi, self.w3, address)  # type: ignore

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    functions: ExampleContractFunctions

    class ConstructorArgs(NamedTuple):
        """Arguments to pass the contract's constructor function."""

        name: str

    @classmethod
    def constructor(cls, name: str) -> ContractConstructor:  # type: ignore
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

        return super().constructor(dataclass_to_tuple(name))

    @classmethod
    def deploy(cls, w3: Web3, account: LocalAccount | ChecksumAddress, constructorArgs: ConstructorArgs) -> Self:
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
        constructor_fn = deployer.constructor(*constructorArgs)

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
        contract.functions = ExampleContractFunctions(example_abi, w3, None)

        return contract
