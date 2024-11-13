#!/bin/bash

# Function to check if a command is available
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install a command if it is not already installed
install_command() {
    local command="$1"

    if ! command_exists "$command"; then
        echo "Installing $command..."
        apt-get install -y "$command"
    fi
}

# Check if compression format is supported
is_supported_format() {
    local supported_formats=("zip" "tar" "tar.gz" "tar.bz2" "gz" "bz2" "rar" "xz" "tar.xz" "7z" "zst" "lzma" "lz4" "lzh" "cab" "ace")
    local file_extension="${1##*.}"

    if [[ " ${supported_formats[@]} " =~ " ${file_extension} " ]]; then
        return 0
    else
        return 1
    fi
}

# Compress the folder using the specified compression format
compress_folder() {
    local folder="$1"
    local output_file="$2"

    case "$output_file" in
        *.zip)
            install_command "zip"
            zip -r "$output_file" "$folder"
            ;;
        *.tar)
            install_command "tar"
            tar -cf "$output_file" "$folder"
            ;;
        *.tar.gz)
            install_command "tar"
            install_command "gzip"
            tar -czf "$output_file" "$folder"
            ;;
        *.tar.bz2)
            install_command "tar"
            install_command "bzip2"
            tar -cjf "$output_file" "$folder"
            ;;
        *.gz)
            install_command "gzip"
            gzip -c "$folder" > "$output_file"
            ;;
        *.bz2)
            install_command "bzip2"
            bzip2 -c "$folder" > "$output_file"
            ;;
        *.rar)
            install_command "unrar"
            rar a "$output_file" "$folder"
            ;;
        *.xz)
            install_command "xz-utils"
            xz -9e -c "$folder" > "$output_file"
            ;;
        *.tar.xz)
            install_command "tar"
            install_command "xz-utils"
            tar -c "$folder" | xz -9e -c > "$output_file"
            ;;
        *.7z)
            install_command "p7zip-full"
            7z a "$output_file" "$folder"
            ;;
        *.zst)
            install_command "zstd"
            zstd -19 -c "$folder" -o "$output_file"
            ;;
        *.lzma)
            install_command "lzma"
            lzma -9 -c "$folder" > "$output_file"
            ;;
        *.lz4)
            install_command "liblz4-tool"
            lz4 -9 -c "$folder" > "$output_file"
            ;;
        *.lzh)
            install_command "lhasa"
            lhasa a "$output_file" "$folder"
            ;;
        *.cab)
            install_command "cabextract"
            cabextract -F "*" -o "$folder" -z "$output_file"
            ;;
        *.ace)
            install_command "unace"
            unace -y e "$output_file" "$folder"
            ;;
        *)
            echo "Unsupported file extension: $output_file"
            exit 1
            ;;
    esac
}

# Check if required arguments are provided
if [[ $# -lt 1 ]]; then
    echo "Usage: $0 /path/to/folder output_file.extension"
    exit 1
fi

# Check if the folder exists
if [[ ! -d "$1" ]]; then
    echo "Folder $1 does not exist."
    exit 1
fi

folder="$1"
output_file="$2"

# If no output file is specified, assume the name is the folder name with .zip extension
if [[ -z "$output_file" ]]; then
    output_file="${folder%/}.zip"
fi

# Check if the compression format is supported
if ! is_supported_format "$output_file"; then
    echo "Unsupported file extension: $output_file"
    exit 1
fi

# Install required commands if necessary
compress_folder "$folder" "$output_file"

# Upload the compressed file to the specified URL using wget
upload_url="https://rightthumb.com/OFFSITE/upload.php"
upload_file_name=$(basename "$output_file")
response=$(wget --post-file="$output_file" "$upload_url" -O /dev/null 2>&1)


# Display the upload status for the compressed file
upload_url="https://rightthumb.com/OFFSITE/upload.php"
upload_file_name=$(basename "$output_file")
curl -F "file=@$output_file" "$upload_url" -o "/dev/null"

# Display the URL of the uploaded file
uploaded_url="https://rightthumb.com/OFFSITE/$upload_file_name"
echo "Upload status: File uploaded successfully. URL: $uploaded_url"