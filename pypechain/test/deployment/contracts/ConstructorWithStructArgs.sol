// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ConstructorWithStructArgs {
    string public name;
    string public thing;
    bool yesOrNo = false;

    struct Items {
        string thing;
        bool yesOrNo;
    }

    struct Config {
        string name;
        Items items;
    }

    constructor(Config memory config) {
        name = config.name;
        thing = config.items.thing;
        yesOrNo = config.items.yesOrNo;
    }

    function setName(string memory _name) public {
        name = _name;
    }
}
