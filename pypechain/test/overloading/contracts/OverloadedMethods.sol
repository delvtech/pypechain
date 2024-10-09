// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OverloadedMethods {

    struct SimpleStruct{
        string strVal;
        uint intVal;
    }
    

    // First version of the function accepts an integer, returns a uint
    function doSomething(uint x) public pure returns (uint) {
        return x * 2;
    }

    // Overloaded version accepts a string, returns a string
    function doSomething(string memory s) public pure returns (string memory) {
        return s;
    }

    // Another overloaded version accepts two integers, returns a named uint
    function doSomething(uint x, uint y) public pure returns (uint added) {
        return x + y;
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
        SimpleStruct calldata simpleStruct
    ) public pure returns (SimpleStruct memory) {
        return SimpleStruct({strVal: simpleStruct.strVal, intVal: simpleStruct.intVal});
    }
}
