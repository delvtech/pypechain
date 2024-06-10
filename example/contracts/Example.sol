// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Example {
    event Flip(uint flip);
    event Flop(uint flop);

    string contractName;

    enum Letters {
        A,
        B,
        C
    }
    error WrongChoice(Letters answer, string errorMessage);

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

    constructor(string memory name) {
        contractName = name;
    }

    function guessALetter(Letters guess) public pure {
        Letters answer = Letters((uint8(guess) + uint8(1)) % 3);

        revert WrongChoice(
            answer,
            "Thank you for playing, but you chose the wrong letter"
        );
    }

    function flipFlop(
        uint flip,
        uint flop
    ) public returns (uint _flop, uint _flip) {
        emit Flip(flip);
        emit Flop(flop);
        return (flop, flip);
    }

    function singleSimpleStruct(
        SimpleStruct calldata simpleStruct
    ) public pure returns (SimpleStruct memory) {
        return simpleStruct;
    }

    function singleNestedStruct(
        NestedStruct calldata nestedStruct
    ) public pure returns (NestedStruct memory) {
        return nestedStruct;
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
            string memory _name,
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

    function vecOfStruct(
        SimpleStruct[] memory inVecSimpleStruct
    ) public pure returns (SimpleStruct[] memory vecSimpleStruct) {
        return inVecSimpleStruct;
    }
}
