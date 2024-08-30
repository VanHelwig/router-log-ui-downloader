#!/bin/bash

#sets source and destination directories
SOURCE_DIR=/home/user/Downloads
DEST_DIR=/var/log/routerlogs

# loops for router syslog files is source directory
for file in $(ls $SOURCE_DIR/syslog-*); do
        # checks if there files that match the name pattern
        if [ -e $file ]; then
                # copies syslog files to destination directory if matched
                mv -v $file $DEST_DIR
        fi
done
