"""The contract function base class for pypechain."""

from __future__ import annotations

from typing import Any, Optional, Type

from eth_account.signers.local import LocalAccount
from eth_typing import ABIFunction
from hexbytes import HexBytes
from web3._utils.abi import get_name_from_abi_element_identifier
from web3.contract.contract import ContractFunction
from web3.types import BlockIdentifier, StateOverride, TxParams, TxReceipt

from .contract_call_exception import check_txn_receipt, handle_contract_logic_error
from .error import PypechainBaseContractErrors


class PypechainOverloadedFunctions(ContractFunction):
    """The contract functions object that wraps a collection of overloaded functions."""

    _factory_kwargs: dict[str, Any]
    _overloaded_functions: dict[str, Type[PypechainContractFunction]]

    def __init__(self, abi: Optional[ABIFunction] = None) -> None:
        # We overload the init function here to not do anything to avoid
        # setting the member variables that are not used by the overloaded functions
        # wrapper. This avoids a check against the abi for this function name.

        # pylint: disable=super-init-not-called

        if not self.abi_element_identifier:
            self.abi_element_identifier = type(self).__name__

        self.fn_name = get_name_from_abi_element_identifier(self.abi_element_identifier)


class PypechainContractFunction(ContractFunction):
    """The contract function base class for pypechain."""

    # The function name for the contract function
    _function_name: str

    # The python type signatures for the contract function
    _type_signature: str

    # The error class for this function
    _error_class: Type[PypechainBaseContractErrors]

    # TODO abstract out `call`
    # We still need to codegen the return types of call, but we want to handle errors
    # here, so we use a private function
    def _call(
        self,
        transaction: TxParams | None,
        block_identifier: BlockIdentifier,
        state_override: StateOverride | None,
        ccip_read_enabled: bool | None,
    ) -> Any:
        try:
            raw_values = super().call(transaction, block_identifier, state_override, ccip_read_enabled)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=self._error_class,
                err=err,
                contract_call_type="call",
                transaction=transaction,
                block_identifier=block_identifier,
            ) from err
        return raw_values

    def transact(self, transaction: TxParams | None = None) -> HexBytes:
        try:
            return super().transact(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=self._error_class,
                err=err,
                contract_call_type="transact",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def estimate_gas(
        self,
        transaction: TxParams | None = None,
        block_identifier: BlockIdentifier | None = None,
        state_override: StateOverride | None = None,
    ) -> int:
        try:
            return super().estimate_gas(transaction, block_identifier, state_override)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=self._error_class,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def build_transaction(self, transaction: TxParams | None = None) -> TxParams:
        try:
            return super().build_transaction(transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=self._error_class,
                err=err,
                contract_call_type="build",
                transaction=transaction,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def sign_and_transact(self, account: LocalAccount, transaction: TxParams | None = None) -> HexBytes:
        """Convenience method for signing and sending a transaction using the provided account.

        Arguments
        ---------
        account : LocalAccount
            The account to use for signing and sending the transaction.
        transaction : TxParams | None, optional
            The transaction parameters to use for sending the transaction.

        Returns
        -------
        HexBytes
            The transaction hash.
        """
        if transaction is None:
            transaction_params: TxParams = {}
        else:
            transaction_params: TxParams = transaction

        if "from" in transaction_params:
            # Ensure if transaction is set, it matches
            assert (
                transaction_params["from"] == account.address
            ), f"Transaction from {transaction_params['from']} does not match account {account.address}"
        else:
            transaction_params["from"] = account.address

        if "gas" not in transaction_params:
            # Web3 default gas estimate seems to be underestimating gas, likely due to
            # not looking at pending block. Here, we explicitly call estimate gas
            # if gas isn't passed in.
            transaction_params["gas"] = self.estimate_gas(transaction_params, block_identifier="pending")

        # Build the raw transaction
        raw_transaction = self.build_transaction(transaction_params)

        if "nonce" not in raw_transaction:
            raw_transaction["nonce"] = self.w3.eth.get_transaction_count(account.address, block_identifier="pending")

        # Sign the raw transaction
        # Mismatched types between account and web3py
        signed_transaction = account.sign_transaction(raw_transaction)  # type: ignore

        # Send the signed transaction
        try:
            return self.w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
        except Exception as err:  # pylint disable=broad-except
            raise handle_contract_logic_error(
                contract_function=self,
                errors_class=self._error_class,
                err=err,
                contract_call_type="transact",
                transaction=transaction_params,
                block_identifier="pending",  # race condition here, best effort to get block of txn.
            ) from err

    def sign_transact_and_wait(
        self,
        account: LocalAccount,
        transaction: TxParams | None = None,
        timeout: float | None = None,
        poll_latency: float | None = None,
        validate_transaction: bool = False,
    ) -> TxReceipt:
        """Convenience method for signing and sending a transaction using the provided account.

        Arguments
        ---------
        account : LocalAccount
            The account to use for signing and sending the transaction.
        transaction : TxParams | None, optional
            The transaction parameters to use for sending the transaction.
        timeout: float, optional
            The number of seconds to wait for the transaction to be mined. Defaults to 120.
        poll_latency: float, optional
            The number of seconds to wait between polling for the transaction receipt. Defaults to 0.1.
        validate_transaction: bool, optional
            Whether to validate the transaction. If True, will throw an exception if the resulting
            tx_receipt returned a failure status.

        Returns
        -------
        HexBytes
            The transaction hash.
        """

        # pylint: disable=too-many-arguments
        # pylint: disable=too-many-positional-arguments

        if timeout is None:
            timeout = 120
        if poll_latency is None:
            poll_latency = 0.1

        tx_hash = self.sign_and_transact(account, transaction)
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=timeout, poll_latency=poll_latency)
        # Check the receipt, throwing an error if status == 0
        if validate_transaction:
            return check_txn_receipt(self, tx_hash, tx_receipt)
        return tx_receipt
