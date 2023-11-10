# Pypechain build to pypi

To create the distribution, first update the version by updating the version field in the pyproject.toml:

```python
# pyproject.toml

# change this line according to semver
version = "0.0.5"
```

Next, build the distribution:

```bash
python -m build
```

This will generate distribution files in the dist/ directory.
To upload to PyPI run (You'll be prompted for your PyPI credentials):

```bash
# twine upload dist/pypechain-[VERSION]*
twine upload dist/pypechain-0.0.1*
```

Optionally, you can setup a .env (see .env.sample) file with your pypi username
and passowrd and run:

```bash
./scripts/upload_latest.sh
```
