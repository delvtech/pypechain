// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import {MyLibrary} from "./MyLibrary.sol";

contract Contract {
    constructor() {
    }

    function add(int256 a, int256 b) external pure returns (int256){
        return MyLibrary.add(a, b);
    }

}