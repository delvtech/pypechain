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
    "0x608060405234801562000010575f80fd5b5060405162001267380380620012678339818101604052810190620000369190620001d3565b805f908162000046919062000459565b50506200053d565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b620000af8262000067565b810181811067ffffffffffffffff82111715620000d157620000d062000077565b5b80604052505050565b5f620000e56200004e565b9050620000f38282620000a4565b919050565b5f67ffffffffffffffff82111562000115576200011462000077565b5b620001208262000067565b9050602081019050919050565b5f5b838110156200014c5780820151818401526020810190506200012f565b5f8484015250505050565b5f6200016d6200016784620000f8565b620000da565b9050828152602081018484840111156200018c576200018b62000063565b5b620001998482856200012d565b509392505050565b5f82601f830112620001b857620001b76200005f565b5b8151620001ca84826020860162000157565b91505092915050565b5f60208284031215620001eb57620001ea62000057565b5b5f82015167ffffffffffffffff8111156200020b576200020a6200005b565b5b6200021984828501620001a1565b91505092915050565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806200027157607f821691505b6020821081036200028757620002866200022c565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f60088302620002eb7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82620002ae565b620002f78683620002ae565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f620003416200033b62000335846200030f565b62000318565b6200030f565b9050919050565b5f819050919050565b6200035c8362000321565b620003746200036b8262000348565b848454620002ba565b825550505050565b5f90565b6200038a6200037c565b6200039781848462000351565b505050565b5b81811015620003be57620003b25f8262000380565b6001810190506200039d565b5050565b601f8211156200040d57620003d7816200028d565b620003e2846200029f565b81016020851015620003f2578190505b6200040a62000401856200029f565b8301826200039c565b50505b505050565b5f82821c905092915050565b5f6200042f5f198460080262000412565b1980831691505092915050565b5f6200044983836200041e565b9150826002028217905092915050565b620004648262000222565b67ffffffffffffffff81111562000480576200047f62000077565b5b6200048c825462000259565b62000499828285620003c2565b5f60209050601f831160018114620004cf575f8415620004ba578287015190505b620004c685826200043c565b86555062000535565b601f198416620004df866200028d565b5f5b828110156200050857848901518255600182019150602085019450602081019050620004e1565b8683101562000528578489015162000524601f8916826200041e565b8355505b6001600288020188555050505b505050505050565b610d1c806200054b5f395ff3fe608060405234801561000f575f80fd5b5060043610610086575f3560e01c806386a5a4c31161005957806386a5a4c314610108578063cf71512c14610138578063d332644614610169578063e0f7c6041461019957610086565b806340e27b101461008a57806353fd1043146100a957806373b10c0f146100c8578063811d9aa3146100ea575b5f80fd5b6100926101b8565b6040516100a09291906106e0565b60405180910390f35b6100b1610270565b6040516100bf929190610796565b60405180910390f35b6100d061033f565b6040516100e1959493929190610831565b60405180910390f35b6100f2610453565b6040516100ff9190610897565b60405180910390f35b610122600480360381019061011d91906108ea565b6104ab565b60405161012f9190610897565b60405180910390f35b610152600480360381019061014d919061095b565b6104c4565b604051610160929190610999565b60405180910390f35b610183600480360381019061017e91906109de565b6104d3565b6040516101909190610a25565b60405180910390f35b6101a16104ec565b6040516101af929190610796565b60405180910390f35b6101c06105b1565b6101c86105b1565b5f6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525090505f6040518060400160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d626572203200000000000000000000000000000000815250815250905081819350935050509091565b6102786105b1565b6102806105ca565b5f6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525090505f6040518060600160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d6265722032000000000000000000000000000000008152508152602001604051806020016040528060011515815250815250905081819350935050509091565b6103476105b1565b61034f6105ca565b5f60605f6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525094505f6040518060600160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d62657220320000000000000000000000000000000081525081526020016040518060200160405280600115158152508152509050858160015f6040518060400160405280601381526020017f52657475726e5479706573436f6e7472616374000000000000000000000000008152509095509550955095509550509091929394565b61045b6105b1565b6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d626572203100000000000000000000000000000000815250815250905090565b6104b36105b1565b816104bd90610be2565b9050919050565b5f808284915091509250929050565b6104db6105ca565b816104e590610cd4565b9050919050565b6104f46105b1565b6104fc6105ca565b6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525091506040518060600160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d626572203200000000000000000000000000000000815250815260200160405180602001604052806001151581525081525090509091565b60405180604001604052805f8152602001606081525090565b60405180606001604052805f8152602001606081526020016105ea6105f0565b81525090565b60405180602001604052805f151581525090565b5f819050919050565b61061681610604565b82525050565b5f81519050919050565b5f82825260208201905092915050565b5f5b83811015610653578082015181840152602081019050610638565b5f8484015250505050565b5f601f19601f8301169050919050565b5f6106788261061c565b6106828185610626565b9350610692818560208601610636565b61069b8161065e565b840191505092915050565b5f604083015f8301516106bb5f86018261060d565b50602083015184820360208601526106d3828261066e565b9150508091505092915050565b5f6040820190508181035f8301526106f881856106a6565b9050818103602083015261070c81846106a6565b90509392505050565b5f8115159050919050565b61072981610715565b82525050565b602082015f8201516107435f850182610720565b50505050565b5f606083015f83015161075e5f86018261060d565b5060208301518482036020860152610776828261066e565b915050604083015161078b604086018261072f565b508091505092915050565b5f6040820190508181035f8301526107ae81856106a6565b905081810360208301526107c28184610749565b90509392505050565b6107d481610604565b82525050565b5f82825260208201905092915050565b5f6107f48261061c565b6107fe81856107da565b935061080e818560208601610636565b6108178161065e565b840191505092915050565b61082b81610715565b82525050565b5f60a0820190508181035f83015261084981886106a6565b9050818103602083015261085d8187610749565b905061086c60408301866107cb565b818103606083015261087e81856107ea565b905061088d6080830184610822565b9695505050505050565b5f6020820190508181035f8301526108af81846106a6565b905092915050565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f604082840312156108e1576108e06108c8565b5b81905092915050565b5f602082840312156108ff576108fe6108c0565b5b5f82013567ffffffffffffffff81111561091c5761091b6108c4565b5b610928848285016108cc565b91505092915050565b61093a81610604565b8114610944575f80fd5b50565b5f8135905061095581610931565b92915050565b5f8060408385031215610971576109706108c0565b5b5f61097e85828601610947565b925050602061098f85828601610947565b9150509250929050565b5f6040820190506109ac5f8301856107cb565b6109b960208301846107cb565b9392505050565b5f606082840312156109d5576109d46108c8565b5b81905092915050565b5f602082840312156109f3576109f26108c0565b5b5f82013567ffffffffffffffff811115610a1057610a0f6108c4565b5b610a1c848285016109c0565b91505092915050565b5f6020820190508181035f830152610a3d8184610749565b905092915050565b5f80fd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610a7f8261065e565b810181811067ffffffffffffffff82111715610a9e57610a9d610a49565b5b80604052505050565b5f610ab06108b7565b9050610abc8282610a76565b919050565b5f80fd5b5f80fd5b5f80fd5b5f67ffffffffffffffff821115610ae757610ae6610a49565b5b610af08261065e565b9050602081019050919050565b828183375f83830152505050565b5f610b1d610b1884610acd565b610aa7565b905082815260208101848484011115610b3957610b38610ac9565b5b610b44848285610afd565b509392505050565b5f82601f830112610b6057610b5f610ac5565b5b8135610b70848260208601610b0b565b91505092915050565b5f60408284031215610b8e57610b8d610a45565b5b610b986040610aa7565b90505f610ba784828501610947565b5f83015250602082013567ffffffffffffffff811115610bca57610bc9610ac1565b5b610bd684828501610b4c565b60208301525092915050565b5f610bed3683610b79565b9050919050565b610bfd81610715565b8114610c07575f80fd5b50565b5f81359050610c1881610bf4565b92915050565b5f60208284031215610c3357610c32610a45565b5b610c3d6020610aa7565b90505f610c4c84828501610c0a565b5f8301525092915050565b5f60608284031215610c6c57610c6b610a45565b5b610c766060610aa7565b90505f610c8584828501610947565b5f83015250602082013567ffffffffffffffff811115610ca857610ca7610ac1565b5b610cb484828501610b4c565b6020830152506040610cc884828501610c1e565b60408301525092915050565b5f610cdf3683610c57565b905091905056fea2646970667358221220a1bf0f774ea805d3ee3e4f8a8f6ce66ed5d2e29a68674bceb93b23e89939db3364736f6c63430008170033"
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

        return super().constructor(name)

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
