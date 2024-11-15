#!/bin/bash

# Sets source and destination directories (customize these paths)
SOURCE_DIR='$HOME/Downloads'  # Default to user's Downloads directory
DEST_DIR='/var/log/routerlogs'  # This can be modified to your preference 

# Loops through router syslog files in the source directory
for file in $(ls $SOURCE_DIR/syslog-* 2>/dev/null); do
	# Checks if there are files that match the name pattern
	if [ -e '$file' ]; then
		# Moves syslog files to the destination directory if matched
		mv -v '$file' '$DEST_DIR'
	fi
done
