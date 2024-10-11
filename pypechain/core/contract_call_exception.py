"""Wrapped web3 exceptions that add additional information."""

from __future__ import annotations

from typing import Any, Generic, Literal, Type, TypeVar, Union

from eth_typing import BlockNumber
from web3.exceptions import ContractCustomError, ContractLogicError, ContractPanicError, OffchainLookup
from web3.types import BlockIdentifier, TxParams

from .contract_function import PypechainContractFunction
from .error import PypechainBaseContractErrors

# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-ancestors

ContractCallType = Union[Literal["call"], Literal["transact"], Literal["build"]]


class PypechainCallException(Exception):
    """Custom contract call exception wrapper that contains additional information on the function call"""

    def __init__(
        self,
        *args,
        # Explicitly passing these arguments as kwargs to allow for multiple `args` to be passed in
        # similar for other types of exceptions
        orig_exception: BaseException,
        decoded_error: str | None = None,
        decoded_error_name: str | None = None,
        decoded_error_args: tuple[Any, ...] | None = None,
        contract_call_type: ContractCallType | None = None,
        function_name: str | None = None,
        fn_args: tuple | None = None,
        fn_kwargs: dict[str, Any] | None = None,
        raw_txn: TxParams | None = None,
        block_number: BlockNumber | None = None,
    ):
        super().__init__(*args)
        self.orig_exception = orig_exception
        self.decoded_error = decoded_error
        self.decoded_error_name = decoded_error_name
        self.decoded_error_args = decoded_error_args
        self.contract_call_type = contract_call_type
        self.function_name = function_name
        self.fn_args = fn_args
        self.fn_kwargs = fn_kwargs
        self.block_number: BlockNumber | None = block_number
        self.raw_txn = raw_txn

    def __repr__(self):
        # We overwrite repr here to ensure the orig exception gets printed for
        # repr(ContractCallException)
        return (
            f"{type(self).__name__}("
            f"{', '.join(self.args)}{', ' if self.args else ''}"
            f"decoded_error={self.decoded_error}, "
            f"orig_exception={repr(self.orig_exception)})"
        )


# Subclasses of these exceptions for all 4 types of exceptions

T = TypeVar("T", bound=ContractLogicError)


class PypechainGenericError(PypechainCallException, Generic[T]):
    """Wrapper of a generic web3 exception that also contains additional information on the function call.
    This inherits from both `PypechainCallException` and subclasses of `BaseException`,
    so that this exception is caught from whatever generic type is defined and
    `PypechainCallException`.
    """

    def __init__(
        self,
        *args,
        # Explicitly passing these arguments as kwargs to allow for multiple `args` to be passed in
        # similar for other types of exceptions
        orig_exception: T,
        decoded_error: str | None = None,
        decoded_error_name: str | None = None,
        decoded_error_args: tuple[Any, ...] | None = None,
        contract_call_type: ContractCallType | None = None,
        function_name: str | None = None,
        fn_args: tuple | None = None,
        fn_kwargs: dict[str, Any] | None = None,
        raw_txn: TxParams | None = None,
        block_number: BlockNumber | None = None,
    ):
        super().__init__(
            *args,
            orig_exception=orig_exception,
            decoded_error=decoded_error,
            decoded_error_name=decoded_error_name,
            decoded_error_args=decoded_error_args,
            contract_call_type=contract_call_type,
            function_name=function_name,
            fn_args=fn_args,
            fn_kwargs=fn_kwargs,
            raw_txn=raw_txn,
            block_number=block_number,
        )

        # Set `ContractLogicError` fields through `orig_exception`
        self.message = orig_exception.message
        self.data = orig_exception.data


class PypechainContractCustomError(PypechainGenericError[ContractCustomError], ContractCustomError):
    """Instance of `PypechainGenericError` for `ContractCustomError`."""


class PypechainContractPanicError(PypechainGenericError[ContractPanicError], ContractPanicError):
    """Instance of `PypechainGenericError` for `ContractPanicError`."""


class PypechainOffchainLookup(PypechainGenericError[OffchainLookup], OffchainLookup):
    """Instance of `PypechainGenericError` for `OffchainLookup`."""


class PypechainContractLogicError(PypechainGenericError[ContractLogicError], ContractLogicError):
    """Instance of `PypechainGenericError` for `ContractLogicError`."""


def handle_contract_logic_error(
    contract_function: PypechainContractFunction,
    errors_class: Type[PypechainBaseContractErrors],
    err: BaseException,
    contract_call_type: ContractCallType,
    transaction: TxParams | None,
    block_identifier: BlockIdentifier,
) -> PypechainGenericError | PypechainCallException:
    """Handles an exception thrown by a contract call."""
    # We first handle the base `ContractLogicError`
    if isinstance(err, ContractLogicError):
        # We decode the error here
        (decoded_error_name, decoded_error_args) = errors_class().decode_custom_error(err.message)
        decoded_error = f"{decoded_error_name}({', '.join([str(e) for e in decoded_error_args])})"
    else:
        decoded_error_name = None
        decoded_error_args = None
        decoded_error = None

    raw_txn = None
    # Best effort to get raw transaction
    # Avoid rebuilding the transaction if the error itself is in build transaction
    if contract_call_type != "build":
        try:
            raw_txn = contract_function.build_transaction(transaction=transaction)
        except Exception:  # pylint: disable=broad-except
            pass

    # Get the block number that the call was attempted on.
    block_number = contract_function.w3.eth.get_block(block_identifier=block_identifier).get("number", None)

    # We create the contract logic error tied to the specific class of the original error
    match err:
        case ContractCustomError():
            return PypechainContractCustomError(
                decoded_error=decoded_error,
                decoded_error_name=decoded_error_name,
                decoded_error_args=decoded_error_args,
                orig_exception=err,
                contract_call_type=contract_call_type,
                function_name=contract_function._function_name,  # pylint: disable=protected-access
                fn_args=contract_function.args,
                fn_kwargs=contract_function.kwargs,
                raw_txn=raw_txn,
                block_number=block_number,
            )
        case ContractPanicError():
            return PypechainContractPanicError(
                decoded_error=decoded_error,
                decoded_error_name=decoded_error_name,
                decoded_error_args=decoded_error_args,
                orig_exception=err,
                contract_call_type=contract_call_type,
                function_name=contract_function._function_name,  # pylint: disable=protected-access
                fn_args=contract_function.args,
                fn_kwargs=contract_function.kwargs,
                raw_txn=raw_txn,
                block_number=block_number,
            )
        case OffchainLookup():
            return PypechainOffchainLookup(
                decoded_error=decoded_error,
                decoded_error_name=decoded_error_name,
                decoded_error_args=decoded_error_args,
                orig_exception=err,
                contract_call_type=contract_call_type,
                function_name=contract_function._function_name,  # pylint: disable=protected-access
                fn_args=contract_function.args,
                fn_kwargs=contract_function.kwargs,
                raw_txn=raw_txn,
                block_number=block_number,
            )
        # Handle base class
        case ContractLogicError():
            return PypechainContractLogicError(
                decoded_error=decoded_error,
                decoded_error_name=decoded_error_name,
                decoded_error_args=decoded_error_args,
                orig_exception=err,
                contract_call_type=contract_call_type,
                function_name=contract_function._function_name,  # pylint: disable=protected-access
                fn_args=contract_function.args,
                fn_kwargs=contract_function.kwargs,
                raw_txn=raw_txn,
                block_number=block_number,
            )
        case BaseException():
            # If none of the above, we don't use the specific contract logic error, and instead just return
            # the base PypechainCallException
            return PypechainCallException(
                decoded_error=decoded_error,
                decoded_error_name=decoded_error_name,
                decoded_error_args=decoded_error_args,
                orig_exception=err,
                contract_call_type=contract_call_type,
                function_name=contract_function._function_name,  # pylint: disable=protected-access
                fn_args=contract_function.args,
                fn_kwargs=contract_function.kwargs,
                raw_txn=raw_txn,
                block_number=block_number,
            )
        case _:
            raise TypeError(f"Unexpected error type: {type(err)}")
