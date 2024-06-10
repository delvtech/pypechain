// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReturnTypes {
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

    function noNameSingleValue(uint x) public pure returns (uint) {
        return x;
    }

    function noNameTwoValues(
        string memory s
    ) public pure returns (string memory, uint) {
        return (s, 2);
    }

    function namedSingleValue(uint x, uint y) public pure returns (uint added) {
        return x + y;
    }

    function namedTwoValues(
        uint x,
        uint y
    ) public pure returns (uint flip, uint flop) {
        return (y, x);
    }

    function singleSimpleStruct() public pure returns (SimpleStruct memory) {
        return SimpleStruct({ intVal: 1, strVal: "You are number 1" });
    }

    function singleNestedStruct() public pure returns (NestedStruct memory) {
        return
            NestedStruct({
                intVal: 1,
                strVal: "You are number 1",
                innerStruct: InnerStruct({ boolVal: true })
            });
    }

    function twoSimpleStructs()
        public
        pure
        returns (SimpleStruct memory, SimpleStruct memory)
    {
        SimpleStruct memory simpleStruct1 = SimpleStruct({
            intVal: 1,
            strVal: "You are number 1"
        });

        SimpleStruct memory simpleStruct2 = SimpleStruct({
            intVal: 2,
            strVal: "You are number 2"
        });

        return (simpleStruct1, simpleStruct2);
    }

    function twoMixedStructs()
        public
        pure
        returns (SimpleStruct memory, NestedStruct memory)
    {
        SimpleStruct memory simpleStruct = SimpleStruct({
            intVal: 1,
            strVal: "You are number 1"
        });
        NestedStruct memory nestedtStruct = NestedStruct({
            intVal: 2,
            strVal: "You are number 2",
            innerStruct: InnerStruct({ boolVal: true })
        });

        return (simpleStruct, nestedtStruct);
    }

    function namedSingleStruct()
        public
        pure
        returns (SimpleStruct memory struct1)
    {
        return SimpleStruct({ intVal: 1, strVal: "You are number 1" });
    }

    function namedTwoMixedStructs()
        public
        pure
        returns (
            SimpleStruct memory simpleStruct,
            NestedStruct memory nestedStruct
        )
    {
        simpleStruct = SimpleStruct({ intVal: 1, strVal: "You are number 1" });
        nestedStruct = NestedStruct({
            intVal: 2,
            strVal: "You are number 2",
            innerStruct: InnerStruct({ boolVal: true })
        });
    }

    function mixStructsAndPrimitives()
        public
        pure
        returns (
            SimpleStruct memory simpleStruct,
            NestedStruct memory,
            uint,
            string memory name,
            bool YesOrNo
        )
    {
        simpleStruct = SimpleStruct({ intVal: 1, strVal: "You are number 1" });
        NestedStruct memory nestedStruct = NestedStruct({
            intVal: 2,
            strVal: "You are number 2",
            innerStruct: InnerStruct({ boolVal: true })
        });

        return (simpleStruct, nestedStruct, 1, "ReturnTypesContract", false);
    }

    function singleNestedStructArray()
        public
        pure
        returns (NestedStruct[] memory)
    {
        NestedStruct[] memory out = new NestedStruct[](2);
        out[0] = NestedStruct({
            intVal: 1,
            strVal: "You are number 1",
            innerStruct: InnerStruct({ boolVal: true })
        });
        out[1] = NestedStruct({
            intVal: 2,
            strVal: "You are number 2",
            innerStruct: InnerStruct({ boolVal: true })
        });
        return out;
    }
}
