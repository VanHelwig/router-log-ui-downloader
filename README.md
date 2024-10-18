

## Updated README 

```markdown
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

Update the YAML configuration file (`routerlogconfig.yml`) with your router's details:

```yaml
router:
  ip: "192.168.1.1"
  password: "your_router_password"

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

### Step 4: Run the Shell Script

After configuring the YAML file, you can automate the entire process by running the provided shell script. This script will first run the Python script to download the logs, and then transfer the downloaded logs using the Bash script.

```bash
./routerlogworkdlow.sh
```

This shell script includes:

```bash
#!/bin/bash 

# Run the Python script to download router logs
/home/user/Scripts/Python/downloadrouterlogs.py

# Transfer logs using the router log transfer script
sudo /home/user/Scripts/Bash/routerlogtransfer.sh
```

---

## Scripts Overview

### Python Script (downloadrouterlogs.py)

This script automates the login to the router's web interface, navigates to the submenu, and downloads log files. Configuration details such as IP address, credentials, and element XPaths are stored in the YAML file.

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

# Run the Python script to download router logs
/home/user/Scripts/Python/downloadrouterlogs.py

# Transfer logs using the router log transfer script
sudo /home/user/Scripts/Bash/routerlogtransfer.sh
```

---

## License

This project is licensed under the MIT License 

## Contributing

Feel free to submit merge requests, issues, or feature requests. Your contributions are welcome!
```

### Summary of Updates:
1. **Router Log Transfer Script**: Described what the transfer script does and how it moves the logs to a specified location.
2. **Shell Script**: Added instructions on how to run the Python and Bash scripts together using a workflow shell script.
3. **Script Explanations**: Provided detailed descriptions of each script and how they work together.

Let me know if you need any further adjustments!
