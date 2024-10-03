"""A web3.py Contract class for the ConstructorWithArgs contract.

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
from eth_typing import ABI, ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunction, ContractFunctions
from web3.types import BlockIdentifier, StateOverride, TxParams

from pypechain.core import dataclass_to_tuple, rename_returned_types

structs = {}


class ConstructorWithArgsNameContractFunction(ContractFunction):
    """ContractFunction for the name method."""

    def __call__(self) -> ConstructorWithArgsNameContractFunction:  # type: ignore
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
    ) -> str:
        """returns str."""
        # Define the expected return types from the smart contract call

        return_types = str

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(str, rename_returned_types(structs, return_types, raw_values))


class ConstructorWithArgsSetNameContractFunction(ContractFunction):
    """ContractFunction for the setName method."""

    def __call__(self, name: str) -> ConstructorWithArgsSetNameContractFunction:  # type: ignore
        clone = super().__call__(dataclass_to_tuple(name))
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


class ConstructorWithArgsContractFunctions(ContractFunctions):
    """ContractFunctions for the ConstructorWithArgs contract."""

    name: ConstructorWithArgsNameContractFunction

    setName: ConstructorWithArgsSetNameContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.name = ConstructorWithArgsNameContractFunction.factory(
            "name",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="name",
        )
        self.setName = ConstructorWithArgsSetNameContractFunction.factory(
            "setName",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            abi_element_identifier="setName",
        )


constructorwithargs_abi: ABI = cast(
    ABI,
    [
        {
            "type": "constructor",
            "inputs": [{"name": "_name", "type": "string", "internalType": "string"}],
            "stateMutability": "nonpayable",
        },
        {
            "type": "function",
            "name": "name",
            "inputs": [],
            "outputs": [{"name": "", "type": "string", "internalType": "string"}],
            "stateMutability": "view",
        },
        {
            "type": "function",
            "name": "setName",
            "inputs": [{"name": "_name", "type": "string", "internalType": "string"}],
            "outputs": [],
            "stateMutability": "nonpayable",
        },
    ],
)


class ConstructorWithArgsContract(Contract):
    """A web3.py Contract class for the ConstructorWithArgs contract."""

    abi: ABI = constructorwithargs_abi
    # We change `bytecode` as needed for linking, but keep
    # `_raw_bytecode` unchanged as an original copy.
    # pylint: disable=line-too-long
    _raw_bytecode: HexStr | None = HexStr(
        "0x608060405234801561001057600080fd5b5060405161061d38038061061d83398101604081905261002f91610058565b600061003b82826101ac565b505061026b565b634e487b7160e01b600052604160045260246000fd5b6000602080838503121561006b57600080fd5b82516001600160401b038082111561008257600080fd5b818501915085601f83011261009657600080fd5b8151818111156100a8576100a8610042565b604051601f8201601f19908116603f011681019083821181831017156100d0576100d0610042565b8160405282815288868487010111156100e857600080fd5b600093505b8284101561010a57848401860151818501870152928501926100ed565b600086848301015280965050505050505092915050565b600181811c9082168061013557607f821691505b60208210810361015557634e487b7160e01b600052602260045260246000fd5b50919050565b601f8211156101a7576000816000526020600020601f850160051c810160208610156101845750805b601f850160051c820191505b818110156101a357828155600101610190565b5050505b505050565b81516001600160401b038111156101c5576101c5610042565b6101d9816101d38454610121565b8461015b565b602080601f83116001811461020e57600084156101f65750858301515b600019600386901b1c1916600185901b1785556101a3565b600085815260208120601f198616915b8281101561023d5788860151825594840194600190910190840161021e565b508582101561025b5787850151600019600388901b60f8161c191681555b5050505050600190811b01905550565b6103a38061027a6000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c806306fdde031461003b578063c47f002714610059575b600080fd5b61004361006e565b604051610050919061010c565b60405180910390f35b61006c610067366004610171565b6100fc565b005b6000805461007b90610222565b80601f01602080910402602001604051908101604052809291908181526020018280546100a790610222565b80156100f45780601f106100c9576101008083540402835291602001916100f4565b820191906000526020600020905b8154815290600101906020018083116100d757829003601f168201915b505050505081565b600061010882826102ad565b5050565b60006020808352835180602085015260005b8181101561013a5785810183015185820160400152820161011e565b506000604082860101526040601f19601f8301168501019250505092915050565b634e487b7160e01b600052604160045260246000fd5b60006020828403121561018357600080fd5b813567ffffffffffffffff8082111561019b57600080fd5b818401915084601f8301126101af57600080fd5b8135818111156101c1576101c161015b565b604051601f8201601f19908116603f011681019083821181831017156101e9576101e961015b565b8160405282815287602084870101111561020257600080fd5b826020860160208301376000928101602001929092525095945050505050565b600181811c9082168061023657607f821691505b60208210810361025657634e487b7160e01b600052602260045260246000fd5b50919050565b601f8211156102a8576000816000526020600020601f850160051c810160208610156102855750805b601f850160051c820191505b818110156102a457828155600101610291565b5050505b505050565b815167ffffffffffffffff8111156102c7576102c761015b565b6102db816102d58454610222565b8461025c565b602080601f83116001811461031057600084156102f85750858301515b600019600386901b1c1916600185901b1785556102a4565b600085815260208120601f198616915b8281101561033f57888601518255948401946001909101908401610320565b508582101561035d5787850151600019600388901b60f8161c191681555b5050505050600190811b0190555056fea26469706673582212206522acd864bbfb39c5173d520e85f497a3c7e924876166bf1e7ee26db5b20e2264736f6c63430008160033"
    )

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        # Initialize parent Contract class
        super().__init__(address=address)
        self.functions = ConstructorWithArgsContractFunctions(constructorwithargs_abi, self.w3, address)  # type: ignore

    functions: ConstructorWithArgsContractFunctions

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
        cls.bytecode = cls._raw_bytecode
        if cls.bytecode is not None:

            # bytecode needs to be in hex for web3
            cls.bytecode = HexBytes(cls.bytecode)

        return super().constructor(dataclass_to_tuple(name))

    @classmethod
    def deploy(cls, w3: Web3, account: LocalAccount | ChecksumAddress, constructor_args: ConstructorArgs) -> Self:
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
        constructor_fn = deployer.constructor(
            *constructor_args,
        )

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
        contract.functions = ConstructorWithArgsContractFunctions(constructorwithargs_abi, w3, None)

        return contract
