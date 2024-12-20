"""Tests for overloading methods."""

from __future__ import annotations

import os

import pytest
from web3.exceptions import MismatchedABI

from .types.OverloadedMethods import OverloadedMethodsContract, OverloadedMethodsTypes

# using pytest fixtures necessitates this.
# pylint: disable=redefined-outer-name

current_path = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(os.path.dirname(current_path))


@pytest.mark.usefixtures("process_contracts")
class TestOverloading:
    """Tests pipeline from bots making trades to viewing the trades in the db"""

    def test_overloading(self, w3):
        """Runs the entire pipeline and checks the database at the end.
        All arguments are fixtures.
        """

        deployed_contract = OverloadedMethodsContract.deploy(w3=w3, account=w3.eth.accounts[0])

        s = "test string"
        x = 2
        y = 1

        result = deployed_contract.functions.doSomething().call()
        assert result == deployed_contract.address

        result = deployed_contract.functions.doSomething(s).call()
        assert result == "test string"

        result = deployed_contract.functions.doSomething(x).call()
        assert result == 2 * 2

        result = deployed_contract.functions.doSomething(x, y).call()
        # Expected result is integer division
        assert result == 2 // 1

        # Test kwargs, we pass arguments reversed, but with kwargs
        # so we still expect the same result as above
        result = deployed_contract.functions.doSomething(_y=y, _x=x).call()
        # Expected result is integer division
        assert result == 2 // 1

        result = deployed_contract.functions.doSomething(x, s).call()
        assert isinstance(result, deployed_contract.functions.doSomething(x, s).ReturnValues)
        assert result == deployed_contract.functions.doSomething(x, s).ReturnValues(x, s)

        # Test kwargs, we pass arguments reversed, but with kwargs
        # so we still expect the same result as above
        result = deployed_contract.functions.doSomething(_s=s, _x=x).call()
        assert isinstance(result, deployed_contract.functions.doSomething(x, s).ReturnValues)
        assert result == deployed_contract.functions.doSomething(x, s).ReturnValues(x, s)

        # Test remapped names but different types
        result = deployed_contract.functions.doSomething(s, x).call()
        assert isinstance(result, deployed_contract.functions.doSomething(s, x).ReturnValues)
        assert result == deployed_contract.functions.doSomething(s, x).ReturnValues(s, x)

        # Test kwargs, we pass arguments reversed, but with kwargs
        # so we still expect the same result as above
        result = deployed_contract.functions.doSomething(_s=x, _x=s).call()
        assert isinstance(result, deployed_contract.functions.doSomething(s, x).ReturnValues)
        assert result == deployed_contract.functions.doSomething(s, x).ReturnValues(s, x)

        result = deployed_contract.functions.doSomething(OverloadedMethodsTypes.SimpleStruct(s, x)).call()
        assert isinstance(result, OverloadedMethodsTypes.SimpleStruct)
        assert result == OverloadedMethodsTypes.SimpleStruct(s, x)

        # Test kwargs with structs
        result = deployed_contract.functions.doSomething(_simpleStruct=OverloadedMethodsTypes.SimpleStruct(s, x)).call()
        assert isinstance(result, OverloadedMethodsTypes.SimpleStruct)
        assert result == OverloadedMethodsTypes.SimpleStruct(s, x)

        result = deployed_contract.functions.doSomething(
            [
                OverloadedMethodsTypes.SimpleStruct(s, x),
                OverloadedMethodsTypes.SimpleStruct(s, y),
            ]
        ).call()
        # TODO although the typing of this function says it returns a list,
        # it actually returns a tuple. Fix the output type of this function.
        # assert isinstance(result, list)
        for r in result:
            assert isinstance(r, OverloadedMethodsTypes.SimpleStruct)
        assert result[0] == OverloadedMethodsTypes.SimpleStruct(s, x)
        assert result[1] == OverloadedMethodsTypes.SimpleStruct(s, y)

        result = deployed_contract.functions.doSomething(
            nestedStructVec=[
                OverloadedMethodsTypes.NestedStruct(x, s, OverloadedMethodsTypes.SimpleStruct(s, x)),
                OverloadedMethodsTypes.NestedStruct(y, s, OverloadedMethodsTypes.SimpleStruct(s, y)),
            ],
        ).call()
        # TODO although the typing of this function says it returns a list,
        # it actually returns a tuple. Fix the output type of this function.
        # assert isinstance(result, list)
        for r in result:
            assert isinstance(r, OverloadedMethodsTypes.NestedStruct)
        assert result[0] == OverloadedMethodsTypes.NestedStruct(x, s, OverloadedMethodsTypes.SimpleStruct(s, x))
        assert result[1] == OverloadedMethodsTypes.NestedStruct(y, s, OverloadedMethodsTypes.SimpleStruct(s, y))

        with pytest.raises(MismatchedABI) as err:
            result = deployed_contract.functions.doSomething(x, y, s).call()  # type: ignore
        assert "ABI Not Found!" in str(err.value)

    def test_factory(self, w3):
        """Tests creating multiple contracts with the same object"""
        # Deploy two contracts
        deployed_contract_1 = OverloadedMethodsContract.deploy(w3=w3, account=w3.eth.accounts[0])
        deployed_contract_2 = OverloadedMethodsContract.deploy(w3=w3, account=w3.eth.accounts[0])

        # Function overload with no arguments returns the address
        # Ensure the referenced contract is actually the contract being called
        result = deployed_contract_1.functions.doSomething().call()
        assert result == deployed_contract_1.address
        result = deployed_contract_2.functions.doSomething().call()
        assert result == deployed_contract_2.address
