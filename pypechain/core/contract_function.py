"""The contract function base class for pypechain."""

from web3.contract.contract import ContractFunction


class PypechainContractFunction(ContractFunction):
    """The contract function base class for pypechain."""

    # The function name for the contract function
    _function_name: str

    # The python type signatures for the contract function
    _type_signature: str
