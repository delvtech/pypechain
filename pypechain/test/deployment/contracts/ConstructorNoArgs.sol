// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ConstructorNoArgs {
    string public name;

    constructor() {
        name = "default";
    }

    function setName(string memory _name) public {
        name = _name;
    }
}
