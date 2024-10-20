#!/bin/bash 

# Exit immediately if a command exits with a non-zero status
set -e

# Log function to print messages with timestamp
log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1"
}

# Ensure the environment variable ROUTER_PASSWORD is set
if [[ -z "${ROUTER_PASSWORD}" ]]; then
    log "Error: ROUTER_PASSWORD environment variable is not set."
    exit 1
fi

# Run the Python script to download router logs
log "Running Python script to download router logs..."
/home/user/Scripts/Python/downloadrouterlogs2.py
log "Python script completed."

# Run the Bash script to transfer the logs without prompting for sudo password
log "Running Bash script to transfer logs..."
sudo /home/user/Scripts/Bash/routerlogtransfer.sh
log "routerlogtransfer.sh Bash script completed."

# Final log to indicate successful execution
log "Workflow completed successfully."
