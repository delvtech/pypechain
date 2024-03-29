"""A web3.py Contract class for the ReturnTypes contract.

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

# consumers have too many opinions on line length
# pylint: disable=line-too-long


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

from .ReturnTypesTypes import InnerStruct, NestedStruct, SimpleStruct
from .utilities import dataclass_to_tuple, rename_returned_types

structs = {
    "SimpleStruct": SimpleStruct,
    "InnerStruct": InnerStruct,
    "NestedStruct": NestedStruct,
}


class ReturnTypesMixStructsAndPrimitivesContractFunction(ContractFunction):
    """ContractFunction for the mixStructsAndPrimitives method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for MixStructsAndPrimitives."""

        simpleStruct: SimpleStruct
        arg2: NestedStruct
        arg3: int
        name: str
        YesOrNo: bool

    def __call__(self) -> ReturnTypesMixStructsAndPrimitivesContractFunction:  # type: ignore
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


class ReturnTypesNamedSingleStructContractFunction(ContractFunction):
    """ContractFunction for the namedSingleStruct method."""

    def __call__(self) -> ReturnTypesNamedSingleStructContractFunction:  # type: ignore
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


class ReturnTypesNamedSingleValueContractFunction(ContractFunction):
    """ContractFunction for the namedSingleValue method."""

    def __call__(self, x: int, y: int) -> ReturnTypesNamedSingleValueContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(x), dataclass_to_tuple(y))
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> int:
        """returns int."""
        # Define the expected return types from the smart contract call

        return_types = int

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(int, rename_returned_types(structs, return_types, raw_values))


class ReturnTypesNamedTwoMixedStructsContractFunction(ContractFunction):
    """ContractFunction for the namedTwoMixedStructs method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for NamedTwoMixedStructs."""

        simpleStruct: SimpleStruct
        nestedStruct: NestedStruct

    def __call__(self) -> ReturnTypesNamedTwoMixedStructsContractFunction:  # type: ignore
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


class ReturnTypesNamedTwoValuesContractFunction(ContractFunction):
    """ContractFunction for the namedTwoValues method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for NamedTwoValues."""

        flip: int
        flop: int

    def __call__(self, x: int, y: int) -> ReturnTypesNamedTwoValuesContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(x), dataclass_to_tuple(y))
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


class ReturnTypesNoNameSingleValueContractFunction(ContractFunction):
    """ContractFunction for the noNameSingleValue method."""

    def __call__(self, x: int) -> ReturnTypesNoNameSingleValueContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(x))
        self.kwargs = clone.kwargs
        self.args = clone.args
        return self

    def call(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier = "latest",
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> int:
        """returns int."""
        # Define the expected return types from the smart contract call

        return_types = int

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(int, rename_returned_types(structs, return_types, raw_values))


class ReturnTypesNoNameTwoValuesContractFunction(ContractFunction):
    """ContractFunction for the noNameTwoValues method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for NoNameTwoValues."""

        arg1: str
        arg2: int

    def __call__(self, s: str) -> ReturnTypesNoNameTwoValuesContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(s))
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

        return_types = [str, int]

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return self.ReturnValues(*rename_returned_types(structs, return_types, raw_values))


class ReturnTypesSingleNestedStructContractFunction(ContractFunction):
    """ContractFunction for the singleNestedStruct method."""

    def __call__(self) -> ReturnTypesSingleNestedStructContractFunction:  # type: ignore
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
    ) -> NestedStruct:
        """returns NestedStruct."""
        # Define the expected return types from the smart contract call

        return_types = NestedStruct

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(NestedStruct, rename_returned_types(structs, return_types, raw_values))


class ReturnTypesSingleSimpleStructContractFunction(ContractFunction):
    """ContractFunction for the singleSimpleStruct method."""

    def __call__(self) -> ReturnTypesSingleSimpleStructContractFunction:  # type: ignore
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


class ReturnTypesTwoMixedStructsContractFunction(ContractFunction):
    """ContractFunction for the twoMixedStructs method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for TwoMixedStructs."""

        arg1: SimpleStruct
        arg2: NestedStruct

    def __call__(self) -> ReturnTypesTwoMixedStructsContractFunction:  # type: ignore
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


class ReturnTypesTwoSimpleStructsContractFunction(ContractFunction):
    """ContractFunction for the twoSimpleStructs method."""

    class ReturnValues(NamedTuple):
        """The return named tuple for TwoSimpleStructs."""

        arg1: SimpleStruct
        arg2: SimpleStruct

    def __call__(self) -> ReturnTypesTwoSimpleStructsContractFunction:  # type: ignore
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


class ReturnTypesContractFunctions(ContractFunctions):
    """ContractFunctions for the ReturnTypes contract."""

    mixStructsAndPrimitives: ReturnTypesMixStructsAndPrimitivesContractFunction

    namedSingleStruct: ReturnTypesNamedSingleStructContractFunction

    namedSingleValue: ReturnTypesNamedSingleValueContractFunction

    namedTwoMixedStructs: ReturnTypesNamedTwoMixedStructsContractFunction

    namedTwoValues: ReturnTypesNamedTwoValuesContractFunction

    noNameSingleValue: ReturnTypesNoNameSingleValueContractFunction

    noNameTwoValues: ReturnTypesNoNameTwoValuesContractFunction

    singleNestedStruct: ReturnTypesSingleNestedStructContractFunction

    singleSimpleStruct: ReturnTypesSingleSimpleStructContractFunction

    twoMixedStructs: ReturnTypesTwoMixedStructsContractFunction

    twoSimpleStructs: ReturnTypesTwoSimpleStructsContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.mixStructsAndPrimitives = ReturnTypesMixStructsAndPrimitivesContractFunction.factory(
            "mixStructsAndPrimitives",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="mixStructsAndPrimitives",
        )
        self.namedSingleStruct = ReturnTypesNamedSingleStructContractFunction.factory(
            "namedSingleStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="namedSingleStruct",
        )
        self.namedSingleValue = ReturnTypesNamedSingleValueContractFunction.factory(
            "namedSingleValue",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="namedSingleValue",
        )
        self.namedTwoMixedStructs = ReturnTypesNamedTwoMixedStructsContractFunction.factory(
            "namedTwoMixedStructs",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="namedTwoMixedStructs",
        )
        self.namedTwoValues = ReturnTypesNamedTwoValuesContractFunction.factory(
            "namedTwoValues",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="namedTwoValues",
        )
        self.noNameSingleValue = ReturnTypesNoNameSingleValueContractFunction.factory(
            "noNameSingleValue",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="noNameSingleValue",
        )
        self.noNameTwoValues = ReturnTypesNoNameTwoValuesContractFunction.factory(
            "noNameTwoValues",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="noNameTwoValues",
        )
        self.singleNestedStruct = ReturnTypesSingleNestedStructContractFunction.factory(
            "singleNestedStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="singleNestedStruct",
        )
        self.singleSimpleStruct = ReturnTypesSingleSimpleStructContractFunction.factory(
            "singleSimpleStruct",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="singleSimpleStruct",
        )
        self.twoMixedStructs = ReturnTypesTwoMixedStructsContractFunction.factory(
            "twoMixedStructs",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="twoMixedStructs",
        )
        self.twoSimpleStructs = ReturnTypesTwoSimpleStructsContractFunction.factory(
            "twoSimpleStructs",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="twoSimpleStructs",
        )


returntypes_abi: ABI = cast(
    ABI,
    [
        {
            "inputs": [],
            "name": "mixStructsAndPrimitives",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct ReturnTypes.SimpleStruct",
                    "name": "simpleStruct",
                    "type": "tuple",
                },
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                        {
                            "components": [{"internalType": "bool", "name": "boolVal", "type": "bool"}],
                            "internalType": "struct ReturnTypes.InnerStruct",
                            "name": "innerStruct",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct ReturnTypes.NestedStruct",
                    "name": "",
                    "type": "tuple",
                },
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "string", "name": "name", "type": "string"},
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
                    "internalType": "struct ReturnTypes.SimpleStruct",
                    "name": "struct1",
                    "type": "tuple",
                }
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
            ],
            "name": "namedSingleValue",
            "outputs": [{"internalType": "uint256", "name": "added", "type": "uint256"}],
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
                    "internalType": "struct ReturnTypes.SimpleStruct",
                    "name": "simpleStruct",
                    "type": "tuple",
                },
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                        {
                            "components": [{"internalType": "bool", "name": "boolVal", "type": "bool"}],
                            "internalType": "struct ReturnTypes.InnerStruct",
                            "name": "innerStruct",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct ReturnTypes.NestedStruct",
                    "name": "nestedStruct",
                    "type": "tuple",
                },
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
            ],
            "name": "namedTwoValues",
            "outputs": [
                {"internalType": "uint256", "name": "flip", "type": "uint256"},
                {"internalType": "uint256", "name": "flop", "type": "uint256"},
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "x", "type": "uint256"}],
            "name": "noNameSingleValue",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "string", "name": "s", "type": "string"}],
            "name": "noNameTwoValues",
            "outputs": [
                {"internalType": "string", "name": "", "type": "string"},
                {"internalType": "uint256", "name": "", "type": "uint256"},
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "singleNestedStruct",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                        {
                            "components": [{"internalType": "bool", "name": "boolVal", "type": "bool"}],
                            "internalType": "struct ReturnTypes.InnerStruct",
                            "name": "innerStruct",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct ReturnTypes.NestedStruct",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "singleSimpleStruct",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct ReturnTypes.SimpleStruct",
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
                    "internalType": "struct ReturnTypes.SimpleStruct",
                    "name": "",
                    "type": "tuple",
                },
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                        {
                            "components": [{"internalType": "bool", "name": "boolVal", "type": "bool"}],
                            "internalType": "struct ReturnTypes.InnerStruct",
                            "name": "innerStruct",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct ReturnTypes.NestedStruct",
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
                    "internalType": "struct ReturnTypes.SimpleStruct",
                    "name": "",
                    "type": "tuple",
                },
                {
                    "components": [
                        {"internalType": "uint256", "name": "intVal", "type": "uint256"},
                        {"internalType": "string", "name": "strVal", "type": "string"},
                    ],
                    "internalType": "struct ReturnTypes.SimpleStruct",
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
returntypes_bytecode = HexStr(
    "0x608060405234801561000f575f80fd5b50610d428061001d5f395ff3fe608060405234801561000f575f80fd5b50600436106100a7575f3560e01c806373b10c0f1161006f57806373b10c0f14610167578063811d9aa314610189578063879896af146101a7578063c567c2f3146101d8578063d6c1a03e146101f6578063e0f7c60414610227576100a7565b8063389e9102146100ab57806340e27b10146100db57806353fd1043146100fa5780636456bc7914610119578063730fe90e14610137575b5f80fd5b6100c560048036038101906100c09190610798565b610246565b6040516100d291906107d2565b60405180910390f35b6100e361024f565b6040516100f19291906108be565b60405180910390f35b610102610307565b604051610110929190610974565b60405180910390f35b6101216103d6565b60405161012e91906109a9565b60405180910390f35b610151600480360381019061014c91906109c9565b61042e565b60405161015e91906107d2565b60405180910390f35b61016f610443565b604051610180959493929190610a5e565b60405180910390f35b610191610557565b60405161019e91906109a9565b60405180910390f35b6101c160048036038101906101bc9190610bf0565b6105af565b6040516101cf929190610c37565b60405180910390f35b6101e06105be565b6040516101ed9190610c65565b60405180910390f35b610210600480360381019061020b91906109c9565b61062d565b60405161021e929190610c85565b60405180910390f35b61022f61063c565b60405161023d929190610974565b60405180910390f35b5f819050919050565b610257610701565b61025f610701565b5f6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525090505f6040518060400160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d626572203200000000000000000000000000000000815250815250905081819350935050509091565b61030f610701565b61031761071a565b5f6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525090505f6040518060600160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d6265722032000000000000000000000000000000008152508152602001604051806020016040528060011515815250815250905081819350935050509091565b6103de610701565b6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d626572203100000000000000000000000000000000815250815250905090565b5f818361043b9190610cd9565b905092915050565b61044b610701565b61045361071a565b5f60605f6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525094505f6040518060600160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d62657220320000000000000000000000000000000081525081526020016040518060200160405280600115158152508152509050858160015f6040518060400160405280601381526020017f52657475726e5479706573436f6e7472616374000000000000000000000000008152509095509550955095509550509091929394565b61055f610701565b6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d626572203100000000000000000000000000000000815250815250905090565b60605f82600291509150915091565b6105c661071a565b6040518060600160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d6265722031000000000000000000000000000000008152508152602001604051806020016040528060011515815250815250905090565b5f808284915091509250929050565b610644610701565b61064c61071a565b6040518060400160405280600181526020016040518060400160405280601081526020017f596f7520617265206e756d62657220310000000000000000000000000000000081525081525091506040518060600160405280600281526020016040518060400160405280601081526020017f596f7520617265206e756d626572203200000000000000000000000000000000815250815260200160405180602001604052806001151581525081525090509091565b60405180604001604052805f8152602001606081525090565b60405180606001604052805f81526020016060815260200161073a610740565b81525090565b60405180602001604052805f151581525090565b5f604051905090565b5f80fd5b5f80fd5b5f819050919050565b61077781610765565b8114610781575f80fd5b50565b5f813590506107928161076e565b92915050565b5f602082840312156107ad576107ac61075d565b5b5f6107ba84828501610784565b91505092915050565b6107cc81610765565b82525050565b5f6020820190506107e55f8301846107c3565b92915050565b6107f481610765565b82525050565b5f81519050919050565b5f82825260208201905092915050565b5f5b83811015610831578082015181840152602081019050610816565b5f8484015250505050565b5f601f19601f8301169050919050565b5f610856826107fa565b6108608185610804565b9350610870818560208601610814565b6108798161083c565b840191505092915050565b5f604083015f8301516108995f8601826107eb565b50602083015184820360208601526108b1828261084c565b9150508091505092915050565b5f6040820190508181035f8301526108d68185610884565b905081810360208301526108ea8184610884565b90509392505050565b5f8115159050919050565b610907816108f3565b82525050565b602082015f8201516109215f8501826108fe565b50505050565b5f606083015f83015161093c5f8601826107eb565b5060208301518482036020860152610954828261084c565b9150506040830151610969604086018261090d565b508091505092915050565b5f6040820190508181035f83015261098c8185610884565b905081810360208301526109a08184610927565b90509392505050565b5f6020820190508181035f8301526109c18184610884565b905092915050565b5f80604083850312156109df576109de61075d565b5b5f6109ec85828601610784565b92505060206109fd85828601610784565b9150509250929050565b5f82825260208201905092915050565b5f610a21826107fa565b610a2b8185610a07565b9350610a3b818560208601610814565b610a448161083c565b840191505092915050565b610a58816108f3565b82525050565b5f60a0820190508181035f830152610a768188610884565b90508181036020830152610a8a8187610927565b9050610a9960408301866107c3565b8181036060830152610aab8185610a17565b9050610aba6080830184610a4f565b9695505050505050565b5f80fd5b5f80fd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610b028261083c565b810181811067ffffffffffffffff82111715610b2157610b20610acc565b5b80604052505050565b5f610b33610754565b9050610b3f8282610af9565b919050565b5f67ffffffffffffffff821115610b5e57610b5d610acc565b5b610b678261083c565b9050602081019050919050565b828183375f83830152505050565b5f610b94610b8f84610b44565b610b2a565b905082815260208101848484011115610bb057610baf610ac8565b5b610bbb848285610b74565b509392505050565b5f82601f830112610bd757610bd6610ac4565b5b8135610be7848260208601610b82565b91505092915050565b5f60208284031215610c0557610c0461075d565b5b5f82013567ffffffffffffffff811115610c2257610c21610761565b5b610c2e84828501610bc3565b91505092915050565b5f6040820190508181035f830152610c4f8185610a17565b9050610c5e60208301846107c3565b9392505050565b5f6020820190508181035f830152610c7d8184610927565b905092915050565b5f604082019050610c985f8301856107c3565b610ca560208301846107c3565b9392505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f610ce382610765565b9150610cee83610765565b9250828201905080821115610d0657610d05610cac565b5b9291505056fea2646970667358221220e3889d05f9a166b91391574ab82b4dac305987a0962eb279cd01f524cb7ded2464736f6c63430008170033"
)


class ReturnTypesContract(Contract):
    """A web3.py Contract class for the ReturnTypes contract."""

    abi: ABI = returntypes_abi
    bytecode: bytes = HexBytes(returntypes_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = ReturnTypesContractFunctions(returntypes_abi, self.w3, address)  # type: ignore

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    functions: ReturnTypesContractFunctions

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
        contract.functions = ReturnTypesContractFunctions(returntypes_abi, w3, None)

        return contract
