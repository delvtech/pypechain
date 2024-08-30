#!/bin/bash

# Run the command in the example/ directory
echo "Running command in example/ directory:"
forge build example/contracts -o example/abis

# Run the command in every directory in pypechain/test/
echo "Running command in pypechain/test/ directories:"
for dir in pypechain/test/*; do
    if [ -d "$dir" ]; then
        echo "Processing $dir..."
        forge build "$dir/contracts" -o "$dir/abis"
    fi
done