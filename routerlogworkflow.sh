#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Log function to print messages with timestamp
log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1"
}

# Ensure the environment variable ROUTER_PASSWORD is set
if [[ -z '${ROUTER_PASSWORD}' ]]; then
    echo 'Error: ROUTER_PASSWORD is not set.'
    exit 1
fi

# Run the Python script to download router logs
log 'Running Python script to download router logs...'
python3 ./downloadrouterlogs.py
log 'Python script completed.'

# Run the Bash script to transfer the logs
log 'Running Bash script to transfer logs...'
sudo ./routerlogtransfer.sh
log 'Workflow completed successfully.'
