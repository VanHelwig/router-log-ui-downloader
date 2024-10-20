#!/bin/bash 

# Exit immediately if a command exits with a non-zero status
set -e

# Log function to print messages with a timestamp
log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1"
}

# Ensure the environment variable ROUTER_PASSWORD is set
if [[ -z "${ROUTER_PASSWORD}" ]]; then
    log "Error: ROUTER_PASSWORD environment variable is not set."
    exit 1
fi

# Set default script paths (can be customized via environment variables)
DOWNLOAD_SCRIPT_PATH="${DOWNLOAD_SCRIPT_PATH:-./downloadrouterlogs.py}"
TRANSFER_SCRIPT_PATH="${TRANSFER_SCRIPT_PATH:-./routerlogtransfer.sh}"

# Run the Python script to download router logs
log "Running Python script to download router logs..."
python3 "$DOWNLOAD_SCRIPT_PATH"
log "Python script completed."

# Run the Bash script to transfer the logs without prompting for sudo password
log "Running Bash script to transfer logs..."
sudo bash "$TRANSFER_SCRIPT_PATH"
log "routerlogtransfer.sh Bash script completed."

# Final log to indicate successful execution
log "Workflow completed successfully."
