#!/bin/bash

# Check if there's at least one argument
if [ "$#" -lt 1 ]; then
	echo "Usage: mnt <drive_letter> [mount_point|-dis]"
	exit 1
fi

DRIVE_LETTER=$(echo "$1" | tr 'a-z' 'A-Z') # Convert to uppercase

# If second argument is not provided, default mount point is /mnt/<lowercase_of_first_argument>
if [ -z "$2" ]; then
	MOUNT_POINT="/mnt/$(echo "$1" | tr 'A-Z' 'a-z')"
else
	# If the second argument is provided and it's not "-dis", it becomes the mount point
	if [ "$2" != "-dis" ]; then
		MOUNT_POINT="/mnt/$2"
	fi
fi

# If second argument is "-dis", unmount the drive
if [ "$2" == "-dis" ]; then
	sudo umount "$MOUNT_POINT"
	if [ $? -eq 0 ]; then
		echo "Successfully dismounted $MOUNT_POINT"
	else
		echo "Failed to dismount $MOUNT_POINT"
	fi
	exit 0
fi

# Mount the drive to the specified mount point
sudo mount -t drvfs "$DRIVE_LETTER:/" "$MOUNT_POINT"
if [ $? -eq 0 ]; then
	echo "Successfully mounted $DRIVE_LETTER: to $MOUNT_POINT"
else
	echo "Failed to mount $DRIVE_LETTER: to $MOUNT_POINT"
fi