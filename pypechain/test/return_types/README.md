## Generate ABIs

from this directory run:

```bash
rm abis/ReturnTypes.json
solc contracts/ReturnTypes.sol --combined-json abi,bin,metadata >> abis/ReturnTypes.json
```
