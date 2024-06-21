## Generate ABIs

Install [`solc`](https://docs.soliditylang.org/en/latest/installing-solidity.html).

If pytest fails to run while editing tests, you'll need to recompile the contracts manually. From
this directory run:

```bash
solc contracts/NoConstructor.sol --combined-json abi,bin,metadata > abis/NoConstructor.json
solc contracts/ConstructorNoArgs.sol --combined-json abi,bin,metadata > abis/ConstructorNoArgs.json
solc contracts/ConstructorWithArgs.sol --combined-json abi,bin,metadata > abis/ConstructorWithArgs.json
solc contracts/ConstructorWithStructArgs.sol --combined-json abi,bin,metadata > abis/ConstructorWithStructArgs.json
```
