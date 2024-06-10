// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IStructs } from "./IStructs.sol";

contract StructsB {
    function noNameSingleValue(uint x) public pure returns (uint) {
        return x;
    }

    function singleSimpleStruct()
        public
        pure
        returns (IStructs.SimpleStruct memory)
    {
        return IStructs.SimpleStruct({ intVal: 1, strVal: "You are number 1" });
    }
}
