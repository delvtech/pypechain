"""The contract function base class for pypechain."""

from web3.contract.contract import ContractFunction


class PypechainContractFunction(ContractFunction):
    """The contract function base class for pypechain."""

    # The python type signatures for the contract function
    _type_signature: str
