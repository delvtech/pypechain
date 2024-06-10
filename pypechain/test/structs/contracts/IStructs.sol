// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IStructs {
    struct SimpleStruct {
        uint intVal;
        string strVal;
    }

    struct InnerStruct {
        bool boolVal;
    }

    struct NestedStruct {
        uint intVal;
        string strVal;
        InnerStruct innerStruct;
    }
}
