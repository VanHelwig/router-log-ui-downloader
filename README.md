# routerwebinterfacelogdownloader
Downloads logs from router web UI

This repo is a collection of scripts and configuration files 
designed to collect logs from a router's web UI. It was made to circumvent an issue with certain brands of hardware 
not allowing SSH connection aside from their designated web management tool. 

The default configurations for the script assume a tp-link router, and a linux operating system. 
Most of the configuration will be done in the YAML configuration file.

Be mindful that there are a few dependencies involved; 
you will have to install the Selenium web framework package for Python
and download and install the Geckodriver for interfacing with Firefox.
Keep note of where you save the driver, as the filepath will need to be referenced in the config file.

Also of note is that the config YAML file stores the router admin password. 
For demo purposes I have left the password as 'password' in plaintext, but I highly recommend against using this methodology in your production environment.
I recommend at least taking the password as an environment variable on the server you run the script from if you do not have a dedicated secrets manager.
