## Generate ABIs
Install [`solc`](https://docs.soliditylang.org/en/latest/installing-solidity.html).

from this directory run:

```bash
rm abis/OverloadedMethods.json
solc contracts/OverloadedMethods.sol --combined-json abi,bin,metadata >> abis/OverloadedMethods.json
```
