## Generate ABIs

from this directory run:

```bash
rm abis/OverloadedMethods.json
solc contracts/OverloadedMethods.sol --combined-json abi,bin,metadata >> abis/OverloadedMethods.json
```
