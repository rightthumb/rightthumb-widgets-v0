#!/bin/bash

# /usr/share/cowsay/cows

# Define the folder variable (you can change its value as needed)
the_folder="$HOME/cowsay"  # Replace "$HOME" with the appropriate path, e.g., "/tmp"

# Check if the folder exists
if [ -d "$the_folder" ]; then
  # If the folder exists, remove it recursively
  rm -r "$the_folder"
fi

# Create the folder
mkdir "$the_folder"

# Print a message indicating that the folder has been created
echo "The folder '$the_folder' has been created."

# Subject for cowsay
subject="$1"

if [ -z "$subject" ]; then
    subject="Love you guys"
fi

# Directory containing cow files
cowsay_dir="/usr/share/cowsay/cows"

# Iterate over all files in the specified directory
for file in "$cowsay_dir"/*.cow; do
  # Extract the filename without the path
  filename=$(basename "$file")
  
  # Remove the file extension using the basename command
  file_without_ext=$(basename "$filename" .cow)
  
  # Execute the cowsay command and redirect the output to a new file in the same directory
  echo $file_without_ext
  cowsay -f "$file_without_ext" "$subject" > "$the_folder/$file_without_ext.cow"
done

# Delete empty files
find "$the_folder" -type f -name "*.cow" -empty -exec rm -v {} \;

echo "Empty files deleted."

# Clear the terminal
clear

source $HOME/.bashrc

$p cowsay_helper -fo $the_folder -save cows.txt

nano cows.txt

# # Create a file to concatenate all the cowsay outputs
# echo $subject > cows.txt

# # Use a for loop to iterate over all files in the folder
# for file in "$the_folder"/*; do
#   # Check if the item is a regular file (not a directory or other type of file)
#   if [ -f "$file" ]; then
#     # Print the contents of the file
#     cat "$file" >> cows.txt
#   fi
# done

# # Open the concatenated file in nano
# nano cows.txt

# /usr/share/cowsay/cows