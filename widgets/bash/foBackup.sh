#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <folder> <destination_folder>"
  exit 1
fi

folder="$1"
destination_folder="$2"
folder="${folder%/}"  # Remove trailing slash if present

if [ ! -d "$folder" ]; then
  echo "Error: Folder '$folder' does not exist."
  exit 1
fi

if [ ! -d "$destination_folder" ]; then
  echo "Destination folder '$destination_folder' does not exist. Creating..."
  mkdir -p "$destination_folder"
fi

folder_name=$(basename "$folder")
parent_name=$(basename "$(dirname "$folder")")
zip_name="${parent_name}-${folder_name}--$(echo -n "$folder" | md5sum | awk '{print substr($1, 1, 5)}')--$(date +%s).zip"

zip -9 -r "$destination_folder/$zip_name" "$folder"


# # tatooine
# # Weekly backup (runs every Sunday at 00:00)
# 0 0 * * 0 /opt/rightthumb-widgets-v0/widgets/bash/foBackup.sh /home/admin/domains/eyeformeta.com/public_html/apps/md /opt/backups/folders/md/
# 0 0 * * 0 /opt/rightthumb-widgets-v0/widgets/bash/foBackup.sh /home/admin/domains/eyeformeta.com/private_html/apps/clients/7i0ZA/gps /opt/backups/folders/gps/
# # Monthly backup (runs on the 1st day of every month at 01:00)
# 0 1 1 * * /opt/rightthumb-widgets-v0/widgets/bash/foBackup.sh /home/admin/domains/eyeformeta.com/public_html/ /opt/backups/folders/websites/eyeformeta.com/
# # Quarterly backup (runs on the 1st day of January, April, July, and October at 02:00)
# 0 2 1 1,4,7,10 * /opt/rightthumb-widgets-v0/widgets/bash/foBackup.sh /home/admin/domains/ /opt/backups/folders/websites/all/

# # yavin
# # Weekly backup (runs every Sunday at 00:00)

# # Monthly backup (runs on the 1st day of every month at 01:00)
# 0 1 1 * * /opt/rightthumb-widgets-v0/widgets/bash/foBackup.sh /home/rightthumb/public_html /opt/backups/folders/websites/rightthumb.com/
