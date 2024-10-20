#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Ensure the environment variable ROUTER_PASSWORD is set
if [[ -z "${ROUTER_PASSWORD}" ]]; then
    echo "Error: ROUTER_PASSWORD is not set."
    exit 1
fi

# Run the Python script to download router logs
python3 ./downloadrouterlogs.py

# Run the Bash script to transfer the logs
sudo bash ./routerlogtransfer.sh
