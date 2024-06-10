// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IStructs } from "./IStructs.sol";

contract StructsA {
    struct AStruct {
        uint intVal;
        string strVal;
    }

    function structA() public pure returns (AStruct memory) {
        return AStruct({ intVal: 1, strVal: "You are number 1" });
    }

    function singleSimpleStruct()
        public
        pure
        returns (IStructs.SimpleStruct memory)
    {
        return IStructs.SimpleStruct({ intVal: 1, strVal: "You are number 1" });
    }

    function singleNestedStruct()
        public
        pure
        returns (IStructs.NestedStruct memory)
    {
        return
            IStructs.NestedStruct({
                intVal: 1,
                strVal: "You are number 1",
                innerStruct: IStructs.InnerStruct({ boolVal: true })
            });
    }
}
