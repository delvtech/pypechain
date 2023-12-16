"""A web3.py Contract class for the ConstructorWithStructArgs contract.

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

from .ConstructorWithStructArgsTypes import Config, Items
from .utilities import dataclass_to_tuple, rename_returned_types

structs = {
    "Items": Items,
    "Config": Config,
}


class ConstructorWithStructArgsNameContractFunction(ContractFunction):
    """ContractFunction for the name method."""

    def __call__(self) -> ConstructorWithStructArgsNameContractFunction:  # type: ignore
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
        return cast(str, rename_returned_types(structs, return_types, raw_values))


class ConstructorWithStructArgsSetNameContractFunction(ContractFunction):
    """ContractFunction for the setName method."""

    def __call__(self, name: str) -> ConstructorWithStructArgsSetNameContractFunction:  # type: ignore
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


class ConstructorWithStructArgsThingContractFunction(ContractFunction):
    """ContractFunction for the thing method."""

    def __call__(self) -> ConstructorWithStructArgsThingContractFunction:  # type: ignore
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
        return cast(str, rename_returned_types(structs, return_types, raw_values))


class ConstructorWithStructArgsContractFunctions(ContractFunctions):
    """ContractFunctions for the ConstructorWithStructArgs contract."""

    name: ConstructorWithStructArgsNameContractFunction

    setName: ConstructorWithStructArgsSetNameContractFunction

    thing: ConstructorWithStructArgsThingContractFunction

    def __init__(
        self,
        abi: ABI,
        w3: "Web3",
        address: ChecksumAddress | None = None,
        decode_tuples: bool | None = False,
    ) -> None:
        super().__init__(abi, w3, address, decode_tuples)
        self.name = ConstructorWithStructArgsNameContractFunction.factory(
            "name",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="name",
        )
        self.setName = ConstructorWithStructArgsSetNameContractFunction.factory(
            "setName",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="setName",
        )
        self.thing = ConstructorWithStructArgsThingContractFunction.factory(
            "thing",
            w3=w3,
            contract_abi=abi,
            address=address,
            decode_tuples=decode_tuples,
            function_identifier="thing",
        )


constructorwithstructargs_abi: ABI = cast(
    ABI,
    [
        {
            "inputs": [
                {
                    "components": [
                        {"internalType": "string", "name": "name", "type": "string"},
                        {
                            "components": [
                                {"internalType": "string", "name": "thing", "type": "string"},
                                {"internalType": "bool", "name": "yesOrNo", "type": "bool"},
                            ],
                            "internalType": "struct ConstructorNoArgs.Items",
                            "name": "items",
                            "type": "tuple",
                        },
                    ],
                    "internalType": "struct ConstructorNoArgs.Config",
                    "name": "config",
                    "type": "tuple",
                }
            ],
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
        {
            "inputs": [],
            "name": "thing",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
    ],
)
# pylint: disable=line-too-long
constructorwithstructargs_bytecode = HexStr(
    "0x60806040525f60025f6101000a81548160ff02191690831515021790555034801562000029575f80fd5b5060405162000de638038062000de683398181016040528101906200004f919062000374565b805f01515f9081620000629190620005fa565b5080602001515f0151600190816200007b9190620005fa565b5080602001516020015160025f6101000a81548160ff02191690831515021790555050620006de565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6200010182620000b9565b810181811067ffffffffffffffff82111715620001235762000122620000c9565b5b80604052505050565b5f62000137620000a4565b9050620001458282620000f6565b919050565b5f80fd5b5f80fd5b5f80fd5b5f67ffffffffffffffff821115620001735762000172620000c9565b5b6200017e82620000b9565b9050602081019050919050565b5f5b83811015620001aa5780820151818401526020810190506200018d565b5f8484015250505050565b5f620001cb620001c58462000156565b6200012c565b905082815260208101848484011115620001ea57620001e962000152565b5b620001f78482856200018b565b509392505050565b5f82601f8301126200021657620002156200014e565b5b815162000228848260208601620001b5565b91505092915050565b5f8115159050919050565b620002478162000231565b811462000252575f80fd5b50565b5f8151905062000265816200023c565b92915050565b5f60408284031215620002835762000282620000b5565b5b6200028f60406200012c565b90505f82015167ffffffffffffffff811115620002b157620002b06200014a565b5b620002bf84828501620001ff565b5f830152506020620002d48482850162000255565b60208301525092915050565b5f60408284031215620002f857620002f7620000b5565b5b6200030460406200012c565b90505f82015167ffffffffffffffff8111156200032657620003256200014a565b5b6200033484828501620001ff565b5f83015250602082015167ffffffffffffffff8111156200035a57620003596200014a565b5b62000368848285016200026b565b60208301525092915050565b5f602082840312156200038c576200038b620000ad565b5b5f82015167ffffffffffffffff811115620003ac57620003ab620000b1565b5b620003ba84828501620002e0565b91505092915050565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806200041257607f821691505b602082108103620004285762000427620003cd565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026200048c7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826200044f565b6200049886836200044f565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f620004e2620004dc620004d684620004b0565b620004b9565b620004b0565b9050919050565b5f819050919050565b620004fd83620004c2565b620005156200050c82620004e9565b8484546200045b565b825550505050565b5f90565b6200052b6200051d565b62000538818484620004f2565b505050565b5b818110156200055f57620005535f8262000521565b6001810190506200053e565b5050565b601f821115620005ae5762000578816200042e565b620005838462000440565b8101602085101562000593578190505b620005ab620005a28562000440565b8301826200053d565b50505b505050565b5f82821c905092915050565b5f620005d05f1984600802620005b3565b1980831691505092915050565b5f620005ea8383620005bf565b9150826002028217905092915050565b6200060582620003c3565b67ffffffffffffffff811115620006215762000620620000c9565b5b6200062d8254620003fa565b6200063a82828562000563565b5f60209050601f83116001811462000670575f84156200065b578287015190505b620006678582620005dd565b865550620006d6565b601f19841662000680866200042e565b5f5b82811015620006a95784890151825560018201915060208501945060208101905062000682565b86831015620006c95784890151620006c5601f891682620005bf565b8355505b6001600288020188555050505b505050505050565b6106fa80620006ec5f395ff3fe608060405234801561000f575f80fd5b506004361061003f575f3560e01c806306fdde0314610043578063c47f002714610061578063c55e90fe1461007d575b5f80fd5b61004b61009b565b604051610058919061024e565b60405180910390f35b61007b600480360381019061007691906103ab565b610126565b005b610085610138565b604051610092919061024e565b60405180910390f35b5f80546100a79061041f565b80601f01602080910402602001604051908101604052809291908181526020018280546100d39061041f565b801561011e5780601f106100f55761010080835404028352916020019161011e565b820191905f5260205f20905b81548152906001019060200180831161010157829003601f168201915b505050505081565b805f908161013491906105f5565b5050565b600180546101459061041f565b80601f01602080910402602001604051908101604052809291908181526020018280546101719061041f565b80156101bc5780601f10610193576101008083540402835291602001916101bc565b820191905f5260205f20905b81548152906001019060200180831161019f57829003601f168201915b505050505081565b5f81519050919050565b5f82825260208201905092915050565b5f5b838110156101fb5780820151818401526020810190506101e0565b5f8484015250505050565b5f601f19601f8301169050919050565b5f610220826101c4565b61022a81856101ce565b935061023a8185602086016101de565b61024381610206565b840191505092915050565b5f6020820190508181035f8301526102668184610216565b905092915050565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f80fd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6102bd82610206565b810181811067ffffffffffffffff821117156102dc576102db610287565b5b80604052505050565b5f6102ee61026e565b90506102fa82826102b4565b919050565b5f67ffffffffffffffff82111561031957610318610287565b5b61032282610206565b9050602081019050919050565b828183375f83830152505050565b5f61034f61034a846102ff565b6102e5565b90508281526020810184848401111561036b5761036a610283565b5b61037684828561032f565b509392505050565b5f82601f8301126103925761039161027f565b5b81356103a284826020860161033d565b91505092915050565b5f602082840312156103c0576103bf610277565b5b5f82013567ffffffffffffffff8111156103dd576103dc61027b565b5b6103e98482850161037e565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061043657607f821691505b602082108103610449576104486103f2565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026104ab7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610470565b6104b58683610470565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6104f96104f46104ef846104cd565b6104d6565b6104cd565b9050919050565b5f819050919050565b610512836104df565b61052661051e82610500565b84845461047c565b825550505050565b5f90565b61053a61052e565b610545818484610509565b505050565b5b818110156105685761055d5f82610532565b60018101905061054b565b5050565b601f8211156105ad5761057e8161044f565b61058784610461565b81016020851015610596578190505b6105aa6105a285610461565b83018261054a565b50505b505050565b5f82821c905092915050565b5f6105cd5f19846008026105b2565b1980831691505092915050565b5f6105e583836105be565b9150826002028217905092915050565b6105fe826101c4565b67ffffffffffffffff81111561061757610616610287565b5b610621825461041f565b61062c82828561056c565b5f60209050601f83116001811461065d575f841561064b578287015190505b61065585826105da565b8655506106bc565b601f19841661066b8661044f565b5f5b828110156106925784890151825560018201915060208501945060208101905061066d565b868310156106af57848901516106ab601f8916826105be565b8355505b6001600288020188555050505b50505050505056fea2646970667358221220fb393bea68b9fa7b0cbec3901624c1b26ae0d6a54f73e40f5bd84de4ee4b58b564736f6c63430008170033"
)


class ConstructorWithStructArgsContract(Contract):
    """A web3.py Contract class for the ConstructorWithStructArgs contract."""

    abi: ABI = constructorwithstructargs_abi
    bytecode: bytes = HexBytes(constructorwithstructargs_bytecode)

    def __init__(self, address: ChecksumAddress | None = None) -> None:
        try:
            # Initialize parent Contract class
            super().__init__(address=address)
            self.functions = ConstructorWithStructArgsContractFunctions(constructorwithstructargs_abi, self.w3, address)  # type: ignore

        except FallbackNotFound:
            print("Fallback function not found. Continuing...")

    functions: ConstructorWithStructArgsContractFunctions

    class ConstructorArgs(NamedTuple):
        """Arguments to pass the contract's constructor function."""

        config: Config

    @classmethod
    def constructor(cls, config: Config) -> ContractConstructor:  # type: ignore
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

        return super().constructor(dataclass_to_tuple(config))

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
        contract.functions = ConstructorWithStructArgsContractFunctions(constructorwithstructargs_abi, w3, None)

        return contract
