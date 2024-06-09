// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IStructs } from "./IStructs.sol";

contract StructsC {
    struct CStruct {
        IStructs.InnerStruct inner;
    }

    // TODO: this will cause naming colision with IStructs if it has the same name and both are used
    // in CStructsContract.py.  Fix ASAP

    // testing against naming collisions from IStructs
    struct InnyStruct {
        uint256 innerVal;
    }

    // testing against naming collisions from IStructs
    struct NestedStruct {
        InnyStruct inner;
    }

    struct OuterStruct {
        NestedStruct nested;
    }

    function allStructsInternal() public pure returns (OuterStruct memory) {
        return
            OuterStruct({
                nested: NestedStruct({ inner: InnyStruct({ innerVal: 1 }) })
            });
    }

    function innerStructIsExternal() public pure returns (CStruct memory) {
        return CStruct({ inner: IStructs.InnerStruct({ boolVal: false }) });
    }
}
