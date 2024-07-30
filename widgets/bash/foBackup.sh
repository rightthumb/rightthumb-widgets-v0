#!/bin/bash

#!/bin/bash

# Check for required input parameters and display usage instructions if not provided
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Incorrect usage. Please specify a source and a destination directory."
  echo "Syntax: $0 <source_directory> <target_directory>"
  exit 1
fi

source_dir="$1"
target_dir="$2"
# Normalize the source directory path by removing any trailing slash
source_dir="${source_dir%/}"

# Validate the existence of the source directory
if [ ! -d "$source_dir" ]; then
  echo "Error: The source directory '$source_dir' is not found."
  exit 1
fi

# Check and create the target directory if it doesn't exist
if [ ! -d "$target_dir" ]; then
  echo "The target directory '$target_dir' is not found. It will be created."
  mkdir -p "$target_dir"
fi

# Generate a unique archive name based on the source directory, its parent, a hash, and the current timestamp
src_basename=$(basename "$source_dir")
src_parentname=$(basename "$(dirname "$source_dir")")
current_timestamp=$(date +%s)
short_hash=$(echo -n "$source_dir" | md5sum | cut -c1-5)
archive_name="${src_parentname}-${src_basename}-${short_hash}-${current_timestamp}.tar.xz"

# Create a compressed archive of the source directory in the target directory
tar -cJf "$target_dir/$archive_name" -C "$(dirname "$source_dir")" "$src_basename"

echo "The archive has been successfully created at '$target_dir/$archive_name'"


# if [ -z "$1" ] || [ -z "$2" ]; then
#   echo "Usage: $0 <folder> <destination_folder>"
#   exit 1
# fi

# folder="$1"
# destination_folder="$2"
# folder="${folder%/}"  # Remove trailing slash if present

# if [ ! -d "$folder" ]; then
#   echo "Error: Folder '$folder' does not exist."
#   exit 1
# fi

# if [ ! -d "$destination_folder" ]; then
#   echo "Destination folder '$destination_folder' does not exist. Creating..."
#   mkdir -p "$destination_folder"
# fi

# folder_name=$(basename "$folder")
# parent_name=$(basename "$(dirname "$folder")")
# zip_name="${parent_name}-${folder_name}--$(echo -n "$folder" | md5sum | awk '{print substr($1, 1, 5)}')--$(date +%s).zip"

# # zip -9 -r "$destination_folder/$zip_name" "$folder"
# tar cJf "$destination_folder/$zip_name" "$folder"


# # tatooine
# # Weekly backup (runs every Sunday at 00:00)
# 0 0 * * 0 $ww/widgets/bash/foBackup.sh /home/admin/domains/eyeformeta.com/public_html/apps/md /opt/backups/folders/md/
# 0 0 * * 0 $ww/widgets/bash/foBackup.sh /home/admin/domains/eyeformeta.com/private_html/apps/clients/7i0ZA/gps /opt/backups/folders/gps/
# # Monthly backup (runs on the 1st day of every month at 01:00)
# 0 1 1 * * $ww/widgets/bash/foBackup.sh /home/admin/domains/eyeformeta.com/public_html/ /opt/backups/folders/websites/eyeformeta.com/
# # Quarterly backup (runs on the 1st day of January, April, July, and October at 02:00)
# 0 2 1 1,4,7,10 * $ww/widgets/bash/foBackup.sh /home/admin/domains/ /opt/backups/folders/websites/all/

# # yavin
# # Weekly backup (runs every Sunday at 00:00)

# # Monthly backup (runs on the 1st day of every month at 01:00)
# 0 1 1 * * $ww/widgets/bash/foBackup.sh /home/rightthumb/public_html /opt/backups/folders/websites/rightthumb.com/