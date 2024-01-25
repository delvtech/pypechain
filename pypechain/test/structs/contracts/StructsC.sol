// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IStructs } from "./IStructs.sol";

contract StructsC {

    struct CStruct {
        IStructs.InnerStruct inner;
    }

    // testing against naming collisions from IStructs
    struct InnerStruct {
        uint256 innerVal;
    }

    // testing against naming collisions from IStructs
    struct NestedStruct {
        InnerStruct inner;
    }

    struct OuterStruct {
        NestedStruct nested;
    }

    function allStructsInternal() public pure returns (OuterStruct memory) {
        return OuterStruct({
            nested: NestedStruct({
                inner: InnerStruct({
                    innerVal: 1
                })
            })
        });
    }

    function innerStructIsExternal() public pure returns (CStruct memory) {
        return CStruct({
            inner: IStructs.InnerStruct({
                boolVal: false
            })
        });
    }
}