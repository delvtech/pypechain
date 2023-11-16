"""A web3.py Contract class for the OverloadedMethods contract."""

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

from __future__ import annotations
from typing import cast

from eth_typing import ChecksumAddress, HexStr
from hexbytes import HexBytes
from web3.types import ABI
from web3.contract.contract import Contract, ContractFunction, ContractFunctions
from web3.exceptions import FallbackNotFound

from multimethod import multimethod


class OverloadedMethodsDoSomethingContractFunction(ContractFunction):
    """ContractFunction for the doSomething method."""

    # super() call methods are generic, while our version adds values & types
    # pylint: disable=arguments-differ# disable this warning when there is overloading
    # pylint: disable=function-redefined
    @multimethod
    def __call__(self, s: str) -> "OverloadedMethodsDoSomethingContractFunction":  # type: ignore
        super().__call__(s)
        return self

    @multimethod
    def __call__(self, x: int) -> "OverloadedMethodsDoSomethingContractFunction":  # type: ignore
        super().__call__(x)
        return self

    @multimethod
    def __call__(self, x: int, y: int) -> "OverloadedMethodsDoSomethingContractFunction":  # type: ignore
        super().__call__(x, y)
        return self


class OverloadedMethodsContractFunctions(ContractFunctions):
    """ContractFunctions for the OverloadedMethods contract."""

    doSomething: OverloadedMethodsDoSomethingContractFunction


overloadedmethods_abi: ABI = cast(
    ABI,
    [
        {
            "inputs": [{"internalType": "string", "name": "s", "type": "string"}],
            "name": "doSomething",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "x", "type": "uint256"}],
            "name": "doSomething",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "x", "type": "uint256"},
                {"internalType": "uint256", "name": "y", "type": "uint256"},
            ],
            "name": "doSomething",
            "outputs": [{"internalType": "uint256", "name": "added", "type": "uint256"}],
            "stateMutability": "pure",
            "type": "function",
        },
    ],
)
# pylint: disable=line-too-long
overloadedmethods_bytecode = HexStr(
    "0x608060405234801561000f575f80fd5b506104d08061001d5f395ff3fe608060405234801561000f575f80fd5b506004361061003f575f3560e01c80638ae3048e14610043578063a6b206bf14610073578063b2dd1d79146100a3575b5f80fd5b61005d60048036038101906100589190610254565b6100d3565b60405161006a9190610315565b60405180910390f35b61008d60048036038101906100889190610368565b6100dd565b60405161009a91906103a2565b60405180910390f35b6100bd60048036038101906100b891906103bb565b6100f2565b6040516100ca91906103a2565b60405180910390f35b6060819050919050565b5f6002826100eb9190610426565b9050919050565b5f81836100ff9190610467565b905092915050565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b61016682610120565b810181811067ffffffffffffffff8211171561018557610184610130565b5b80604052505050565b5f610197610107565b90506101a3828261015d565b919050565b5f67ffffffffffffffff8211156101c2576101c1610130565b5b6101cb82610120565b9050602081019050919050565b828183375f83830152505050565b5f6101f86101f3846101a8565b61018e565b9050828152602081018484840111156102145761021361011c565b5b61021f8482856101d8565b509392505050565b5f82601f83011261023b5761023a610118565b5b813561024b8482602086016101e6565b91505092915050565b5f6020828403121561026957610268610110565b5b5f82013567ffffffffffffffff81111561028657610285610114565b5b61029284828501610227565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f5b838110156102d25780820151818401526020810190506102b7565b5f8484015250505050565b5f6102e78261029b565b6102f181856102a5565b93506103018185602086016102b5565b61030a81610120565b840191505092915050565b5f6020820190508181035f83015261032d81846102dd565b905092915050565b5f819050919050565b61034781610335565b8114610351575f80fd5b50565b5f813590506103628161033e565b92915050565b5f6020828403121561037d5761037c610110565b5b5f61038a84828501610354565b91505092915050565b61039c81610335565b82525050565b5f6020820190506103b55f830184610393565b92915050565b5f80604083850312156103d1576103d0610110565b5b5f6103de85828601610354565b92505060206103ef85828601610354565b9150509250929050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f61043082610335565b915061043b83610335565b925082820261044981610335565b915082820484148315176104605761045f6103f9565b5b5092915050565b5f61047182610335565b915061047c83610335565b9250828201905080821115610494576104936103f9565b5b9291505056fea2646970667358221220302a4cdc1dfb754065d06f51532b94876e677fac92e5bc7cf8488748219e851564736f6c63430008170033"
)


class OverloadedMethodsContract(Contract):
    """A web3.py Contract class for the OverloadedMethods contract."""

    abi: ABI = overloadedmethods_abi
    bytecode: bytes = HexBytes(overloadedmethods_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    # TODO: add events
    # events: ERC20ContractEvents

    functions: OverloadedMethodsContractFunctions
