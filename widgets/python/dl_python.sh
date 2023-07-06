#!/bin/bash

if [ $# -lt 1 ]; then
  echo "Usage: $0 <arg1> [arg2] [arg3] ..."
  exit 1
fi


for arg in "$@"
do
  new_filename="${arg}.py"
  file_path="/opt/rightthumb-widgets-v0/widgets/python/$new_filename"

  if [ -e "$file_path" ]; then
	echo "File exists."
	
	# Get the modification date in the format YYYY-MM-DD
	mod_date=$(date -r "$file_path" +%Y-%m-%d)
	
	# Extract the file's basename and extension
	file_basename=$(basename "$file_path" ".${file_path##*.}")
	file_extension="${file_path##*.}"
	
	# Create the backup file name
	backup_file_path="${file_basename}_${mod_date}.${file_extension}"
	
	# Copy the original file to the backup file
	cp "$file_path" "$backup_file_path"
	
	echo "Backup created: $backup_file_path"
  else
	echo "File does not exist."
  fi

  rm -f "$file_path"
  wget -q "https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/main/widgets/python/$new_filename"
  chmod +x "$file_path"
done

