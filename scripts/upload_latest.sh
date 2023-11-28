#!/bin/bash

# Check if there is a .env file with TWINE_USERNAME and TWINE_PASSWORD
# or if the environment variables are already set.
if [ -f ".env" ]; then
    echo "Overwriting TWINE_USERNAME and TWINE_PASSWORD environment variables from .env"
    export $(cat .env | xargs)
else
    echo "Checking for TWINE_USERNAME and TWINE_PASSWORD environment variables..."

    if  [ -z "$TWINE_USERNAME" ]; then
        echo "TWINE_USERNAME environment variable was not set"
        exit 1
    fi

    if  [ -z "$TWINE_PASSWORD" ]; then
        echo "TWINE_PASSWORD environment variable was not set"
        exit 1
    fi
fi

# Navigate to the dist directory
cd dist || exit 1

# Find the latest version of the package, assuming the naming convention is 'pypechain-VERSION'
# This will extract the version numbers, sort them, and get the highest version
latest_version=$(ls pypechain-*.tar.gz | sort -V | tail -n 1 | sed -E 's/pypechain-(.*)\.tar\.gz/\1/')

# Check if latest_version is not empty
if [[ -z "$latest_version" ]]; then
    echo "No distribution files found for upload."
    exit 1
fi

# Use twine to upload all packages for the latest version
# The * after the version number is important to match all files for the version
twine upload "pypechain-${latest_version}"*

# Navigate back to the original directory
cd -
