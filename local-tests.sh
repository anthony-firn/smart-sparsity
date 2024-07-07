#!/bin/bash

# Source the .env file to set LOCAL_RUN
source .env

# Run the tests using act
echo "Running tests using act..."
if [ "$LOCAL_RUN" == "true" ]; then
    if lspci | grep -i nvidia; then
        echo "Running all tests including intensive tests..."
        act -j test
        act -j intensive-test
    else
        echo "Running only standard tests (no GPU detected)..."
        act -j test
    fi
else
    echo "Running standard tests..."
    act -j test
fi