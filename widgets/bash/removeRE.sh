#!/bin/bash

# Function to recursively find linked folders named ".re" and remove them
find_and_remove_linked_re_folders() {
    local dir="$1"
    
    # Check if the directory exists
    if [ -d "$dir" ]; then
        # Iterate through the entries in the directory
        for entry in "$dir"/*; do
            # Check if the entry is a symbolic link, a directory, and named ".re"
            if [ -L "$entry" ] && [ -d "$entry" ] && [ "$(basename "$entry")" = ".re" ]; then
                # Remove the linked directory
                echo "Removing linked folder: $entry"
                rm -rf "$entry"
            fi
            # Recursively call the function if the entry is a directory
            if [ -d "$entry" ]; then
                find_and_remove_linked_re_folders "$entry"
            fi
        done
    fi
}

# Start the search from the current directory
find_and_remove_linked_re_folders "$(pwd)"
