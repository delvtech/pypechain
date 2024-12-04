#!/bin/bash

# Run the command in every directory in pypechain/test/
echo "Running command in pypechain/test/ directories:"
for dir in pypechain/test/*; do
    if [ -d "$dir" ]; then
        echo "Processing $dir..."
        forge build "$dir/contracts" -o "$dir/abis"
    fi
done