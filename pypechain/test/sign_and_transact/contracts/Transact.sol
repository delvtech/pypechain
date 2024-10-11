// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Transact {
    event Success();
    function TransactFunction() public{
        emit Success();
    }
}
