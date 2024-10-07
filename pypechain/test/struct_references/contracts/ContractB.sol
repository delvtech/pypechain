// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { ContractA } from "./ContractA.sol";

contract ContractB {

    struct InnerStruct{
        uint intVal;
        string strVal;
    }

    // StructsB uses StructsA to define 
    struct StructsB{
        // Defined in other file
        ContractA.StructsA structA;
        // Defined in this file
        InnerStruct structB;
    }
}
