## Generate ABIs

Install [`solc`](https://docs.soliditylang.org/en/latest/installing-solidity.html).

If pytest fails to run while editing tests, you'll need to recompile the contracts manually. From
this directory run:

```bash
rm abis/ReturnTypes.json
solc contracts/ReturnTypes.sol --combined-json abi,bin,metadata >> abis/ReturnTypes.json
```
