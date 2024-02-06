#!/usr/bin/python3

import os
import subprocess
import tempfile
from datetime import datetime

# Variables
OUTPUT_DIR = "/home/rightthumb/phone/YoutTube_mp3"
URLS_FILE = "/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/Scrolls/_docs_/_YouTube/mp3/queue.md"
ERROR_FILE = "/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/Scrolls/_docs_/_YouTube/mp3/.App/err.md"
SUCCESS_FILE = "/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/Scrolls/_docs_/_YouTube/mp3/.App/success.md"
INITIATION_FILE = "/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/Scrolls/_docs_/_YouTube/mp3/.App/initiation.md"
LOG_FILE = "/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/Scrolls/_docs_/_YouTube/mp3/.App/run.md"
CONFIGS_FOLDER = os.path.dirname(URLS_FILE)

# Create a named temporary file to keep a backup of URLs for safety
with tempfile.NamedTemporaryFile(delete=False) as temp_copy_file:
    TEMP_COPY = temp_copy_file.name

# Change permissions
os.chmod(OUTPUT_DIR, 0o777)
os.chmod(CONFIGS_FOLDER, 0o777)

if not os.path.exists(URLS_FILE):
    with open(ERROR_FILE, "a") as error_file:
        error_file.write(f"{datetime.now()}: No queue file\n")
    exit(0)

file_size = os.path.getsize(URLS_FILE)

if file_size < 10:
    exit(0)

# Ensure youtube-dlc is installed
if not subprocess.run(["which", "youtube-dlc"], stdout=subprocess.PIPE).returncode == 0:
    print("youtube-dlc is not installed. Please install it first.")
    exit(0)

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Backup content of URLs file to the named temporary file and then clear the URLs file
with open(URLS_FILE, "r") as urls_file, open(TEMP_COPY, "w") as temp_copy_file:
    temp_copy_file.write(urls_file.read())
    temp_copy_file.write("\n")
    temp_copy_file.write(f"{datetime.now()}\n")
    urls_file.seek(0)
    temp_copy_file.write(urls_file.read())

# Append URLs and timestamp to the INITIATION_FILE
with open(INITIATION_FILE, "a") as initiation_file:
    initiation_file.write("\n")
    initiation_file.write("_________________________________")
    initiation_file.write(f"{datetime.now()}\n")
    with open(TEMP_COPY, "r") as temp_copy_file:
        initiation_file.write(temp_copy_file.read())
import shutil
shutil.copyfile(URLS_FILE, TEMP_COPY)

with open(URLS_FILE, "w"):
    pass

# Process each URL from the temporary backup file
with open(TEMP_COPY, "r") as temp_copy_file:
    for line in temp_copy_file:
        # Trim whitespace
        dirty = line.strip()
        
        # Skip blank lines
        if not dirty:
            continue
        for part in dirty.split(' '):
            u='https://'
            if u in part:
                url=u+part.split(u)[1]

                print(f"Processing {url}")

                # Use youtube-dlc to download the audio in mp3 format
                download_cmd = [
                    "youtube-dlc",
                    "-x",
                    "--audio-format",
                    "mp3",
                    "-o",
                    os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s"),
                    url,
                ]

                if subprocess.run(download_cmd).returncode == 0:
                    # If the above command was successful, log to the success file
                    with open(SUCCESS_FILE, "a") as success_file:
                        success_file.write(f"{url} - Successfully downloaded\n")
                else:
                    # If there was an error, save the URL to the error file
                    with open(ERROR_FILE, "a") as error_file:
                        error_file.write(f"{url}\n")

# Cleanup
os.remove(TEMP_COPY)
os.chmod(OUTPUT_DIR, 0o777)
os.chmod(CONFIGS_FOLDER, 0o777)
with open(LOG_FILE, "w"):
    pass

print("Processing complete.")
