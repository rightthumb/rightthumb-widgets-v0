#!/bin/bash

# /usr/share/figlet

source $HOME/.bashrc


#################################################################

#!/bin/bash

# Define the folder variable (you can change its value as needed)
the_folder="$HOME/figlet"  # Replace "$HOME" with the appropriate path, e.g., "/tmp"

# Check if the folder exists
if [ -d "$the_folder" ]; then
  # If the folder exists, remove it recursively
  rm -r "$the_folder"
fi

# Create the folder
mkdir "$the_folder"

# Print a message indicating that the folder has been created
echo "The folder '$the_folder' has been created."


#################################################################






subject="$1"

if [ -z "$subject" ]; then
	subject="KeyWise"
fi



figlet_dir="/usr/share/figlet"

# Iterate over all files in the specified directory
for file in "$figlet_dir"/*; do
  # Extract the filename without the path
  filename=$(basename "$file")
  
  # Remove the file extension using the basename command
  file_without_ext=$(basename "$filename" .flf)
  
  # Execute the figlet command and redirect the output to a new file in the same directory
  # figlet -f $file_without_ext "$subject" > "$the_folder/$file_without_ext.figlet"
  figlet -w 1000 -f "$file_without_ext" "$subject" > "$the_folder/$file_without_ext.figlet"

done




# figlet -f wideterm $subject > wideterm.figlet

#################################################################

#!/bin/bash

# Usage: ./delete_empty_files.sh /path/to/directory

#directory="$1"
directory="."
if [ -z "$directory" ]; then
	echo "Please provide a directory path."
	exit 1
fi

if [ ! -d "$directory" ]; then
	echo "Invalid directory path."
	exit 1
fi

# find "$directory" -type f -empty -exec rm -v {} \;
find "$directory" -type f -name "*.figlet" -empty -exec rm -v {} \;

echo "Empty files deleted."

#################################################################
clear

# $p cat -f $the_folder/*.figlet > _figs.txt
# nano _figs.txt
echo $subject > figs.txt
echo "" >> figs.txt
echo "" >> figs.txt

# the_folder="$HOME/figlet"
echo $subject > figs.txt
# Use a for loop to iterate over all files in the folder
for file in "$the_folder"/*; do
  # Check if the item is a regular file (not a directory or other type of file)
  if [ -f "$file" ]; then
	# Print the contents of the file
	# echo "$file" >> figs.txt
	cat "$file" >> figs.txt
  fi
done
# $p cat -f $the_folder/*.figlet >> figs2.txt
nano figs.txt

# /usr/share/figlet