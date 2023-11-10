[![](https://codecov.io/gh/delvtech/pypechain/branch/main/graph/badge.svg?token=1S60MD42ZP)](https://app.codecov.io/gh/delvtech/pypechain?displayType=list)
[![](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![](https://img.shields.io/badge/testing-pytest-blue.svg)](https://docs.pytest.org/en/latest/contents.html)
<br><a href="https://app.codecov.io/gh/delvtech/pypechain?displayType=list"><img height="50px" src="https://codecov.io/gh/delvtech/pypechain/graphs/tree.svg?token=A3BTPZ02E6"><a>

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
