#!/bin/bash

# Change directory to the dist folder
cd dist

# Find the latest package version, assuming the naming convention is like 'pypechain-VERSION'
# Sorts by version number and gets the last one
latest_package=$(ls pypechain-* | sort -V | tail -n 1)

# Extract only the version part from the filename
latest_version=$(echo "$latest_package" | sed -E 's/pypechain-(.*)\.tar\.gz/\1/')

# Use twine to upload the latest version of the package
# The glob pattern will match all files for the given version
twine upload "pypechain-${latest_version}"*

# Change back to the original directory if needed
cd -