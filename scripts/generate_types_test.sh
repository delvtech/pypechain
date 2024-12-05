#!/bin/bash

# Run the command in every directory in pypechain/test/
echo "Running command in pypechain/test/ directories:"
for dir in pypechain/test/*; do
    if [ -d "$dir" ]; then
        echo "Processing $dir..."
        pypechain "$dir/abis" --output-dir "$dir/types"
    fi
done