// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { ContractA } from "./ContractA.sol";

contract ContractB {
    // StructsB uses StructsA to define 
    struct StructsB{
        ContractA.StructsA structA;
    }
}
