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

from __future__ import annotations

from dataclasses import fields, is_dataclass
from typing import Any, NamedTuple, Tuple, Type, TypeVar, cast

from eth_account.signers.local import LocalAccount
from eth_typing import ChecksumAddress, HexStr
from hexbytes import HexBytes
from typing_extensions import Self
from web3 import Web3
from web3.contract.contract import Contract, ContractConstructor, ContractFunction, ContractFunctions
from web3.exceptions import FallbackNotFound
from web3.types import ABI, BlockIdentifier, CallOverride, TxParams

T = TypeVar("T")

structs = {}


def tuple_to_dataclass(cls: type[T], tuple_data: Any | Tuple[Any, ...]) -> T:
    """
    Converts a tuple (including nested tuples) to a dataclass instance.  If cls is not a dataclass,
    then the data will just be passed through this function.

    Arguments
    ---------
    cls: type[T]
        The dataclass type to which the tuple data is to be converted.
    tuple_data: Any | Tuple[Any, ...]
        A tuple (or nested tuple) of values to convert into a dataclass instance.

    Returns
    -------
    T
        Either an instance of cls populated with data from tuple_data or tuple_data itself.
    """
    if not is_dataclass(cls):
        return cast(T, tuple_data)

    field_types = {field.name: field.type for field in fields(cls)}
    field_values = {}

    for (field_name, field_type), value in zip(field_types.items(), tuple_data):
        field_type = structs.get(field_type, field_type)
        if is_dataclass(field_type):
            # Recursively convert nested tuples to nested dataclasses
            field_values[field_name] = tuple_to_dataclass(field_type, value)
        elif isinstance(value, tuple) and not getattr(field_type, "_name", None) == "Tuple":
            # If it's a tuple and the field is not intended to be a tuple, assume it's a nested dataclass
            field_values[field_name] = tuple_to_dataclass(field_type, value)
        else:
            # Otherwise, set the primitive value directly
            field_values[field_name] = value

    return cls(**field_values)


def dataclass_to_tuple(instance: Any) -> Any:
    """Convert a dataclass instance to a tuple, handling nested dataclasses.
    If the input is not a dataclass, return the original value.
    """
    if not is_dataclass(instance):
        return instance

    def convert_value(value: Any) -> Any:
        """Convert nested dataclasses to tuples recursively, or return the original value."""
        if is_dataclass(value):
            return dataclass_to_tuple(value)
        return value

    return tuple(convert_value(getattr(instance, field.name)) for field in fields(instance))


def rename_returned_types(return_types, raw_values) -> Any:
    """_summary_

    Parameters
    ----------
    return_types : _type_
        _description_
    raw_values : _type_
        _description_

    Returns
    -------
    tuple
        _description_
    """
    # cover case of multiple return values
    if isinstance(return_types, list):
        # Ensure raw_values is a tuple for consistency
        if not isinstance(raw_values, list):
            raw_values = (raw_values,)

        # Convert the tuple to the dataclass instance using the utility function
        converted_values = tuple(
            tuple_to_dataclass(return_type, value) for return_type, value in zip(return_types, raw_values)
        )

        return converted_values

    # cover case of single return value
    converted_value = tuple_to_dataclass(return_types, raw_values)
    return converted_value


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
        state_override: CallOverride | None = None,
        ccip_read_enabled: bool | None = None,
    ) -> str:
        """returns str."""
        # Define the expected return types from the smart contract call

        return_types = str

        # Call the function

        raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        return cast(str, rename_returned_types(return_types, raw_values))


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
        state_override: CallOverride | None = None,
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
            function_identifier="name",
        )
        self.setName = ConstructorWithArgsSetNameContractFunction.factory(
            "setName",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="setName",
        )


constructorwithargs_abi: ABI = cast(
    ABI,
    [
        {
            "inputs": [{"internalType": "string", "name": "_name", "type": "string"}],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "inputs": [],
            "name": "name",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "string", "name": "_name", "type": "string"}],
            "name": "setName",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ],
)
# pylint: disable=line-too-long
constructorwithargs_bytecode = HexStr(
    "0x608060405234801562000010575f80fd5b5060405162000b9038038062000b908339818101604052810190620000369190620001d3565b805f908162000046919062000459565b50506200053d565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b620000af8262000067565b810181811067ffffffffffffffff82111715620000d157620000d062000077565b5b80604052505050565b5f620000e56200004e565b9050620000f38282620000a4565b919050565b5f67ffffffffffffffff82111562000115576200011462000077565b5b620001208262000067565b9050602081019050919050565b5f5b838110156200014c5780820151818401526020810190506200012f565b5f8484015250505050565b5f6200016d6200016784620000f8565b620000da565b9050828152602081018484840111156200018c576200018b62000063565b5b620001998482856200012d565b509392505050565b5f82601f830112620001b857620001b76200005f565b5b8151620001ca84826020860162000157565b91505092915050565b5f60208284031215620001eb57620001ea62000057565b5b5f82015167ffffffffffffffff8111156200020b576200020a6200005b565b5b6200021984828501620001a1565b91505092915050565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806200027157607f821691505b6020821081036200028757620002866200022c565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f60088302620002eb7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82620002ae565b620002f78683620002ae565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f620003416200033b62000335846200030f565b62000318565b6200030f565b9050919050565b5f819050919050565b6200035c8362000321565b620003746200036b8262000348565b848454620002ba565b825550505050565b5f90565b6200038a6200037c565b6200039781848462000351565b505050565b5b81811015620003be57620003b25f8262000380565b6001810190506200039d565b5050565b601f8211156200040d57620003d7816200028d565b620003e2846200029f565b81016020851015620003f2578190505b6200040a62000401856200029f565b8301826200039c565b50505b505050565b5f82821c905092915050565b5f6200042f5f198460080262000412565b1980831691505092915050565b5f6200044983836200041e565b9150826002028217905092915050565b620004648262000222565b67ffffffffffffffff81111562000480576200047f62000077565b5b6200048c825462000259565b62000499828285620003c2565b5f60209050601f831160018114620004cf575f8415620004ba578287015190505b620004c685826200043c565b86555062000535565b601f198416620004df866200028d565b5f5b828110156200050857848901518255600182019150602085019450602081019050620004e1565b8683101562000528578489015162000524601f8916826200041e565b8355505b6001600288020188555050505b505050505050565b610645806200054b5f395ff3fe608060405234801561000f575f80fd5b5060043610610034575f3560e01c806306fdde0314610038578063c47f002714610056575b5f80fd5b610040610072565b60405161004d9190610199565b60405180910390f35b610070600480360381019061006b91906102f6565b6100fd565b005b5f805461007e9061036a565b80601f01602080910402602001604051908101604052809291908181526020018280546100aa9061036a565b80156100f55780601f106100cc576101008083540402835291602001916100f5565b820191905f5260205f20905b8154815290600101906020018083116100d857829003601f168201915b505050505081565b805f908161010b9190610540565b5050565b5f81519050919050565b5f82825260208201905092915050565b5f5b8381101561014657808201518184015260208101905061012b565b5f8484015250505050565b5f601f19601f8301169050919050565b5f61016b8261010f565b6101758185610119565b9350610185818560208601610129565b61018e81610151565b840191505092915050565b5f6020820190508181035f8301526101b18184610161565b905092915050565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f80fd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b61020882610151565b810181811067ffffffffffffffff82111715610227576102266101d2565b5b80604052505050565b5f6102396101b9565b905061024582826101ff565b919050565b5f67ffffffffffffffff821115610264576102636101d2565b5b61026d82610151565b9050602081019050919050565b828183375f83830152505050565b5f61029a6102958461024a565b610230565b9050828152602081018484840111156102b6576102b56101ce565b5b6102c184828561027a565b509392505050565b5f82601f8301126102dd576102dc6101ca565b5b81356102ed848260208601610288565b91505092915050565b5f6020828403121561030b5761030a6101c2565b5b5f82013567ffffffffffffffff811115610328576103276101c6565b5b610334848285016102c9565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061038157607f821691505b6020821081036103945761039361033d565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026103f67fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826103bb565b61040086836103bb565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61044461043f61043a84610418565b610421565b610418565b9050919050565b5f819050919050565b61045d8361042a565b6104716104698261044b565b8484546103c7565b825550505050565b5f90565b610485610479565b610490818484610454565b505050565b5b818110156104b3576104a85f8261047d565b600181019050610496565b5050565b601f8211156104f8576104c98161039a565b6104d2846103ac565b810160208510156104e1578190505b6104f56104ed856103ac565b830182610495565b50505b505050565b5f82821c905092915050565b5f6105185f19846008026104fd565b1980831691505092915050565b5f6105308383610509565b9150826002028217905092915050565b6105498261010f565b67ffffffffffffffff811115610562576105616101d2565b5b61056c825461036a565b6105778282856104b7565b5f60209050601f8311600181146105a8575f8415610596578287015190505b6105a08582610525565b865550610607565b601f1984166105b68661039a565b5f5b828110156105dd578489015182556001820191506020850194506020810190506105b8565b868310156105fa57848901516105f6601f891682610509565b8355505b6001600288020188555050505b50505050505056fea2646970667358221220b87bbfbecccce3bdbf545805121127addb336182e62dc59415dd90ed789d49aa64736f6c63430008170033"
)


class ConstructorWithArgsContract(Contract):
    """A web3.py Contract class for the ConstructorWithArgs contract."""

    abi: ABI = constructorwithargs_abi
    bytecode: bytes = HexBytes(constructorwithargs_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = ConstructorWithArgsContractFunctions(constructorwithargs_abi, self.w3, address)  # type: ignore

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    functions: ConstructorWithArgsContractFunctions

    class ConstructorArgs(NamedTuple):
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
        contract.functions = ConstructorWithArgsContractFunctions(constructorwithargs_abi, w3, None)

        return contract
