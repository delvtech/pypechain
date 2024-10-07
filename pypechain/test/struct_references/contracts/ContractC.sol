// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { ContractA } from "./ContractA.sol";
import { ContractB } from "./ContractB.sol";

contract ContractC {
    // StructsC uses StructsB
    function buildStruct() public pure returns (ContractB.StructsB memory) {
        return
            ContractB.StructsB({
                structA: ContractA.StructsA({ intVal: 1, strVal: "a" }),
                structB: ContractB.InnerStruct({ intVal: 2, strVal: "b" })
            });
    }
}
