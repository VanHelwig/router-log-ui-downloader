# routerwebinterfacelogdownloader
Downloads logs from router web UI

This repo is a collection of scripts and configuration files 
designed to collect logs from a routers web ui. it was made to circumvent an issue with certain brands of hardware 
not allowing ssh connection asside from their designated web management tool. 

The default configurations for the script assume a tp-link router, and a linux operating system. 
Most of the configuration will be done in the .yaml configuration file,

Be mindful that there are a few dependencies involved, 
you will have to install the selenium package for python
and download and install the Geckodriver for interacting with firefox.
Keep note of where you save the driver as the filepath will need to be referenced in the config file
