"""A typed version of combomethod from eth_utils."""

import functools
from typing import Any, Callable, Concatenate, Generic, Optional, ParamSpec, Type, TypeVar

# TODO remove this file once https://github.com/ethereum/eth-utils/pull/264 gets merged

# We use generics to define the structure of the wrapped method
# Here, `T` is the `self` or `cls` object, `P` is the parameter of the wrapped function, and
# `R` is the return type

T = TypeVar("T")
P = ParamSpec("P")
R = TypeVar("R")


# We define the generic that attaches to the function we're decorating
# so here, P and R are the types of the parameters and return of the decorated function
class combomethod_typed(Generic[P, R]):  # pylint: disable=invalid-name
    """A typed version of combomethod from eth_utils."""

    # The callable `Any` takes place of the obj or class
    method: Callable[Concatenate[Any, P], R]

    # The method passed in has a spot for obj or class in `Any`
    def __init__(self, method: Callable[Concatenate[Any, P], R]) -> None:
        self.method = method

    # The getter allows for logic to call either cls or obj method
    # with the original type decorators in the output wrapper function
    def __get__(self, obj: Optional[T] = None, objtype: Optional[Type[T]] = None) -> Callable[P, R]:
        # The _wrapper function is unchanged from eth-utils
        @functools.wraps(self.method)
        def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            if obj is not None:
                return self.method(obj, *args, **kwargs)
            return self.method(objtype, *args, **kwargs)

        return _wrapper
