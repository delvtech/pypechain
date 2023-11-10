# Install -- overview

Pypechain is currently supported only for Python 3.10.

## Quick setup

You can install pypechain via pypi:

```bash
pip install --upgrade pypechain
```

## Development install

### 1. Install Pyenv

Follow [Pyenv install instructions](https://github.com/pyenv/pyenv#installation).

### 2. Clone Pypechain repo

Clone the repo into a <repo_location> of your choice.

```bash
git clone git@github.com:delvtech/pypechain.git <repo_location>
```

### 3. Set up virtual environment

You can use any environment, but we recommend [venv](https://docs.python.org/3/library/venv.html), which is part of the standard Python library.

```bash
cd <repo_location>
pyenv install 3.10
pyenv local 3.10
python -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

To install the build dependencies to upload to pypi:

````bash
pip install ".[build]"```
````

To install the test dependencies to upload to pypi:

````bash
pip install ".[test]"```
````

To install all the dependencies, run:

````bash
pip install ".[all]"```
````
