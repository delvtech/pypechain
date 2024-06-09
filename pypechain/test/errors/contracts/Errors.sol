// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Errors {
    struct Ages {
        uint256 bart;
        uint256 lisa;
        uint256 homer;
        uint256 marge;
    }

    enum Simpsons {
        BART,
        LISA,
        HOMER,
        MARGE
    }

    error One();
    error Two(string message, address who, uint8 value);
    error Three(bool trueOrFalse, Ages theSimpsons, Simpsons who);

    function revertWithErrorOne() public pure {
        revert One();
    }

    function revertWithErrorTwo() public pure {
        revert Two(
            "I will not pledge allegiance to Bart. I will not pledge allegiance to Bart. I will not pledge allegiance to Bart.",
            address(0),
            255
        );
    }

    function revertWithErrorThree() public pure {
        Ages memory ages = Ages(1, 2, 3, 4);
        revert Three(false, ages, Simpsons.BART);
    }
}
