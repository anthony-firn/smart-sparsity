#!/bin/bash

# Source the .env file to set LOCAL_RUN
source .env

# Run the tests using act
echo "Running tests using act..."
if [ "$LOCAL_RUN" == "true" ]; then
    if lspci | grep -i nvidia; then
        echo "Running all tests including intensive tests..."
        act -e event.json -j test
        act -e event.json -j intensive-test
    else
        echo "Running only standard tests (no GPU detected)..."
        act -e event.json -j test
    fi
else
    echo "Running standard tests..."
    act -e event.json -j test
fi