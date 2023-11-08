# Pypechain

Static python bindings for ethereum smart contracts.

- Parses JSON ABI's to create typesafe web3.py contract instances
- Functions have typesafe function parameters and return values
- Smart Contract internal types are exposed as dataclasses

### Install

```bash
pip install --upgrade pypechain
```

For development install instructions, see toplevel [INSTALL.md](https://github.com/delvtech/pypechain/blob/main/INSTALL.md)

### Usage

```bash
#  pypechain <ABI_FILE>          <OUT_FILE>
❯❯ pypechain './abis/ERC20.json' './build/ERC20Contract.py'
```

Much of this is subject to change as more features are fleshed out.
