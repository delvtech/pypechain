// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OverloadedMethods {

    struct SimpleStruct{
        string strVal;
        uint intVal;
    }

    struct NestedStruct{
        uint intVal;
        string strVal;
        SimpleStruct simpleStruct;
    }
    
    // Function doesn't accept any parameters, returns a uint
    function doSomething() public pure returns (uint) {
        return 2;
    }

    // Function accepts an integer, returns a uint
    function doSomething(uint x) public pure returns (uint) {
        return x * 2;
    }

    // Overloaded version accepts a string, returns a string
    function doSomething(string memory s) public pure returns (string memory) {
        return s;
    }

    // Another overloaded version accepts two integers, returns a named uint
    function doSomething(uint x, uint y) public pure returns (uint added) {
        return x / y;
    }

    // Another overloaded version accepts an integer and a string, returns both unchanged
    function doSomething(
        uint x,
        string memory s
    ) public pure returns (uint int_input, string memory) {
        return (x, s);
    }

    // Another overloaded version accepts a struct, returns unchanged
    function doSomething(
        SimpleStruct memory simpleStruct
    ) public pure returns (SimpleStruct memory) {
        return SimpleStruct({strVal: simpleStruct.strVal, intVal: simpleStruct.intVal});
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
