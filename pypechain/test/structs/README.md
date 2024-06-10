# Generate ABIs

Install [`solc`](https://docs.soliditylang.org/en/latest/installing-solidity.html).

If pytest fails to run while editing tests, you'll need to recompile the contracts manually. From
this directory run:

```bash
solc contracts/IStructs.sol --combined-json abi,bin,metadata > abis/IStructs.json
solc contracts/StructsA.sol --combined-json abi,bin,metadata > abis/StructsA.json
solc contracts/StructsB.sol --combined-json abi,bin,metadata > abis/StructsB.json
solc contracts/StructsC.sol --combined-json abi,bin,metadata > abis/StructsC.json
```
