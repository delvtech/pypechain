"""Setup for pypechain command line tool."""

from setuptools import find_packages, setup

setup(
    name="pypechain",
    version="0.0.0",
    packages=find_packages(),
    install_requires=["web3", "jinja2", "black"],
    entry_points={
        "console_scripts": [
            "pypechain = mypackage.core:main_function",
        ],
    },
)
