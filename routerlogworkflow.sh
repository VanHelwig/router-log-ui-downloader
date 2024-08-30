#!/bin/bash 

# runs python script to download router logs
# then runs bash script to transfer the files to desired location locally

/home/user/Scripts/Python/downloadrouterlogs.py
sudo /home/user/Scripts/Bash/routerlogtransfer.sh
