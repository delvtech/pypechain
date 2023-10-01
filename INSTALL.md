# Install -- overview

Pypechain is currently supported only for Python 3.10.

## 1. Install Pyenv

Follow [Pyenv install instructions](https://github.com/pyenv/pyenv#installation).

## 2. Clone Elf-simulations repo

Clone the repo into a <repo_location> of your choice.

```bash
git clone https://github.com/delvtech/elf-simulations.git <repo_location>
```

## 3. Set up virtual environment

You can use any environment, but we recommend [venv](https://docs.python.org/3/library/venv.html), which is part of the standard Python library.

```bash
cd <repo_location>
pyenv install 3.10
pyenv local 3.10
python -m venv .venv
source .venv/bin/activate
```

## 4. Install dependencies

The flit build system is used to install dependencies. Make sure you have flit installed:

```bash
pip install flit
```

To install the base dependencies to run the code:

````bash
pip install ".[base]"```
````

To install the build dependencies to upload to pypi:

````bash
pip install ".[build]"```
````

To install all the dependencies, run:

````bash
pip install "pypechain[all]"```
````
