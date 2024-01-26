#!/bin/bash

# Run the command in the example/ directory
echo "Running command in example/ directory:"
pypechain example/abis --output-dir example/types

# Run the command in every directory in pypechain/test/
echo "Running command in pypechain/test/ directories:"
for dir in pypechain/test/*; do
    if [ -d "$dir" ]; then
        echo "Processing $dir..."
        pypechain "$dir/abis" --output-dir "$dir/types"
    fi
done