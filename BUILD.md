To create the distribution, run:

```bash
python -m build
```

This will generate distribution files in the dist/ directory.
To upload to PyPI run (You'll be prompted for your PyPI credentials):

```bash
# twine upload dist/pypechain-[VERSION]*
twine upload dist/pypechain-0.0.1*
```
