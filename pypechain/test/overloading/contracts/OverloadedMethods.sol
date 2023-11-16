// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OverloadedMethods {

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
}