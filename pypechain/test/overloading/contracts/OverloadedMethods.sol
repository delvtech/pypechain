// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OverloadedMethods {

    struct SimpleStruct{
        string _strVal;
        uint _intVal;
    }

    struct NestedStruct{
        uint intVal;
        string strVal;
        SimpleStruct simpleStruct;
    }
    
    // Function doesn't accept any parameters, returns the address of the contract
    function doSomething() public view returns (address) {
        return address(this);
    }

    // Function accepts an integer, returns a uint
    function doSomething(uint _x) public pure returns (uint) {
        return _x * 2;
    }

    // Overloaded version accepts a string, returns a string
    function doSomething(string memory _s) public pure returns (string memory) {
        return _s;
    }

    // Another overloaded version accepts two integers, returns a named uint
    function doSomething(uint _x, uint _y) public pure returns (uint added) {
        return _x / _y;
    }

    // Another overloaded version accepts an integer and a string, returns both unchanged
    function doSomething(
        uint _x,
        string memory _s
    ) public pure returns (uint int_input, string memory) {
        return (_x, _s);
    }

    // Another overloaded version uses same varible names but types are different
    function doSomething(
        string memory _x,
        uint _s
    ) public pure returns (string memory, uint int_input) {
        return (_x, _s);
    }

    // Another overloaded version accepts a struct, returns unchanged
    function doSomething(
        SimpleStruct memory _simpleStruct
    ) public pure returns (SimpleStruct memory) {
        return SimpleStruct({_strVal: _simpleStruct._strVal, _intVal: _simpleStruct._intVal});
    }

    // Overloaded vec of structs as input
    function doSomething(
        SimpleStruct[] memory simpleStructVec
    ) public pure returns (SimpleStruct[] memory) {
        return simpleStructVec;
    }

    // Overloaded vec of nested struct as input
    function doSomething(
        NestedStruct[] memory nestedStructVec
    ) public pure returns (NestedStruct[] memory outNestedStructVec) {
        return nestedStructVec;
    }
}
