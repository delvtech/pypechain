# Pypechain

Static python bindings for ethereum smart contracts.

- Parses JSON ABIs to create typesafe web3.py contract instances
- Functions have typesafe function parameters and return values
- Smart Contract internal types are exposed as dataclasses

This project is a work-in-progress. All code is provided as is and without guarantee.

## Install

```bash
pip install --upgrade pypechain
```

For development install instructions, see toplevel [INSTALL.md](https://github.com/delvtech/pypechain/blob/main/INSTALL.md)

## Usage

```bash
#  pypechain <ABI_FILE>          <OUT_FILE>
❯❯ pypechain './abis/ERC20.json' './build/ERC20Contract.py'
```

