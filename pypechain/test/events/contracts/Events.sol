// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Events {
    event EventA(address indexed who, uint256 value);
    event EventB();

    function emitOneEvent(uint256 value, address who) public {
        emit EventA(who, value);
    }

    function emitTwoEvents(uint256 value, address who) public {
        emit EventA(who, value);
        emit EventB();
    }

    function emitNoEvents(uint x, uint y) public pure returns (uint added) {
        return x + y;
    }
}
