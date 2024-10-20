## README

# Router Log Downloader

**Project Purpose:** Automates the login process to a router's web interface, navigates to a submenu, and downloads log files using Selenium WebDriver in Python. It also includes a Bash script for transferring router logs and a shell script to run both tasks in sequence.

## Overview

This project allows you to:

- Automatically retrieve and download log files from a router's web interface.
- Transfer logs using a Bash script to a specified location.
- Automate both tasks together using a shell script.

---

## Installation and Setup

### Prerequisites

- Python 3.x
- Selenium WebDriver
- Mozilla Firefox browser
- GeckoDriver for Selenium
- PyYAML Python package
- Bash shell (for log transfer and shell script)

### Step 1: Install Dependencies

Install the required Python packages:

```bash
pip install selenium pyyaml
```

Download and install GeckoDriver from [here](https://github.com/mozilla/geckodriver/releases) and add it to your system's `PATH`.

### Step 2: Clone the Repository

```bash
git clone https://github.com/VanHelwig/routerwebinterfacelogdownloader
cd routerwebinterfacelogdownloader
```

### Step 3: Configure the YAML File

Update the YAML configuration file (`routerlogconfig.yml`) with your router's details (Note: the password should no longer be stored here):

```yaml
router:
  ip: "192.168.1.1"

urls:
  router_url: "http://192.168.1.1/login"
  submenu: "http://192.168.1.1/submenu"

xpaths:
  password_field: '//*[@id="password"]'
  download_button: '//*[@id="download"]'

settings:
  driver_path: "/path/to/geckodriver"
  timeout: 5  # Timeout in seconds
```

### Step 4: Set the `ROUTER_PASSWORD` Environment Variable

For security purposes, the router password is stored as an environment variable instead of in the YAML file. Set this environment variable before running the scripts:

1. **Temporary (Current Session Only)**:
   
   Run the following command to set the password for the current terminal session:

   ```bash
   export ROUTER_PASSWORD="your_secure_password"
   ```

2. **Permanent (For All Sessions)**:

   Add the following line to your `~/.bashrc` or `~/.bash_profile` to set the environment variable permanently:

   ```bash
   export ROUTER_PASSWORD="your_secure_password"
   ```

   After adding, run:

   ```bash
   source ~/.bashrc
   ```

This ensures the password is retrieved securely from the environment when the Python script is executed.

### Step 5: Configure Passwordless Sudo for Log Transfer

To avoid entering your password every time the log transfer script runs with `sudo`, you can configure your `sudoers` file to allow this specific command to be run without a password:

1. Open the `sudoers` file using `visudo`:

   ```bash
   sudo visudo
   ```

2. Add the following line, replacing `user` with your username, changing the filepath to routerlogtransfer file:

   ```bash
   user ALL=(ALL) NOPASSWD: /home/user/Scripts/Bash/routerlogtransfer.sh
   ```

This allows the script to run with `sudo` without prompting for a password.

### Step 6: Run the Workflow Script

After configuring everything, you can automate the entire process by running the provided shell script. This script will first run the Python script to download the logs, and then transfer the downloaded logs using the Bash script:

```bash
./routerlogworkflow.sh
```

---

## Scripts Overview

### Python Script (downloadrouterlogs.py)

This script automates the login to the router's web interface, navigates to the submenu, and downloads log files. The router password is securely retrieved from the `ROUTER_PASSWORD` environment variable, and configuration details like IP address, URLs, and element XPaths are stored in the YAML file.

### Bash Script (routerlogtransfer.sh)

This script transfers the downloaded log files from the default `~/Downloads` folder to the specified destination (`/var/log/routerlogs`):

```bash
#!/bin/bash

# Set source and destination directories
SOURCE_DIR=/home/user/Downloads
DEST_DIR=/var/log/routerlogs

# Move syslog files from source to destination
for file in $(ls $SOURCE_DIR/syslog-*); do
    if [ -e $file ]; then
        mv -v $file $DEST_DIR
    fi
done
```

### Shell Script (routerlogworkflow.sh)

This script runs both the Python download script and the Bash transfer script sequentially:

```bash
#!/bin/bash

# Ensure the environment variable is set
if [[ -z "${ROUTER_PASSWORD}" ]]; then
    echo "Error: ROUTER_PASSWORD is not set."
    exit 1
fi

# Run the Python script to download router logs
/home/user/Scripts/Python/downloadrouterlogs.py

# Run the Bash script to transfer the logs
sudo /home/user/Scripts/Bash/routerlogtransfer.sh
```

---

## License

This project is licensed under the MIT License 

## Contributing

Feel free to submit merge requests, issues, or feature requests. Your contributions are welcome!

---

### Summary of Updates:
1. **Environment Variable**: Instructions added to securely set the `ROUTER_PASSWORD` as an environment variable.
2. **Passwordless Sudo**: Steps added to configure passwordless sudo for running the log transfer script.
3. **Updated Script Descriptions**: Modified descriptions to reflect changes in the workflow and how password management is handled.

Let me know if this looks good or if you'd like any further modifications!
