#!/bin/bash

# Install necessary tools
install_tools() {
    echo "Installing necessary tools..."
    sudo apt-get update
    sudo apt-get install -y libpst-dev pff-tools jq
}

# Function to get header by message ID
get_header_by_id() {
    local pst_file=$1
    local message_id=$2
    local folder_option=$3
    local recursive_option=$4

    if [ "$recursive_option" == "true" ]; then
        readpst -r -R -o - "$pst_file" 2>/dev/null | grep -B 10 -A 10 "$message_id"
    else
        readpst -r $folder_option -o - "$pst_file" 2>/dev/null | grep -B 10 -A 10 "$message_id"
    fi
}

# Function to search emails by sender and return JSON
search_emails_by_sender() {
    local pst_file=$1
    local sender=$2
    local folder_option=$3
    local recursive_option=$4

    if [ "$recursive_option" == "true" ]; then
        readpst -r -R -o - "$pst_file" 2>/dev/null | grep -B 5 -A 15 "From: $sender" | while read -r line; do
            id=$(echo "$line" | grep -oP 'Message-ID: <\K[^>]+')
            subject=$(echo "$line" | grep -oP 'Subject: \K.*')
            attachments=$(echo "$line" | grep -oP 'Attachment: \K.*')
            body=$(echo "$line" | grep -oP 'Body: \K.*')
            json=$(jq -n --arg id "$id" --arg subject "$subject" --arg attachments "$attachments" --arg body "$body" '{id: $id, subject: $subject, attachments: $attachments, body: $body}')
            echo "$json"
        done
    else
        readpst -r $folder_option -o - "$pst_file" 2>/dev/null | grep -B 5 -A 15 "From: $sender" | while read -r line; do
            id=$(echo "$line" | grep -oP 'Message-ID: <\K[^>]+')
            subject=$(echo "$line" | grep -oP 'Subject: \K.*')
            attachments=$(echo "$line" | grep -oP 'Attachment: \K.*')
            body=$(echo "$line" | grep -oP 'Body: \K.*')
            json=$(jq -n --arg id "$id" --arg subject "$subject" --arg attachments "$attachments" --arg body "$body" '{id: $id, subject: $subject, attachments: $attachments, body: $body}')
            echo "$json"
        done
    fi
}

# Function to search emails by subject and return JSON
search_emails_by_subject() {
    local pst_file=$1
    local subject_search=$2
    local folder_option=$3
    local recursive_option=$4

    if [ "$recursive_option" == "true" ]; then
        readpst -r -R -o - "$pst_file" 2>/dev/null | grep -B 5 -A 15 "Subject: $subject_search" | while read -r line; do
            id=$(echo "$line" | grep -oP 'Message-ID: <\K[^>]+')
            subject=$(echo "$line" | grep -oP 'Subject: \K.*')
            attachments=$(echo "$line" | grep -oP 'Attachment: \K.*')
            body=$(echo "$line" | grep -oP 'Body: \K.*')
            json=$(jq -n --arg id "$id" --arg subject "$subject" --arg attachments "$attachments" --arg body "$body" '{id: $id, subject: $subject, attachments: $attachments, body: $body}')
            echo "$json"
        done
    else
        readpst -r $folder_option -o - "$pst_file" 2>/dev/null | grep -B 5 -A 15 "Subject: $subject_search" | while read -r line; do
            id=$(echo "$line" | grep -oP 'Message-ID: <\K[^>]+')
            subject=$(echo "$line" | grep -oP 'Subject: \K.*')
            attachments=$(echo "$line" | grep -oP 'Attachment: \K.*')
            body=$(echo "$line" | grep -oP 'Body: \K.*')
            json=$(jq -n --arg id "$id" --arg subject "$subject" --arg attachments "$attachments" --arg body "$body" '{id: $id, subject: $subject, attachments: $attachments, body: $body}')
            echo "$json"
        done
    fi
}

# Function to search emails by subject and body and return JSON
search_emails_by_subject_and_body() {
    local pst_file=$1
    local subject_search=$2
    local body_search=$3
    local folder_option=$4
    local recursive_option=$5

    if [ "$recursive_option" == "true" ]; then
        readpst -r -R -o - "$pst_file" 2>/dev/null | grep -B 5 -A 15 -e "Subject: $subject_search" -e "$body_search" | while read -r line; do
            id=$(echo "$line" | grep -oP 'Message-ID: <\K[^>]+')
            subject=$(echo "$line" | grep -oP 'Subject: \K.*')
            attachments=$(echo "$line" | grep -oP 'Attachment: \K.*')
            body=$(echo "$line" | grep -oP 'Body: \K.*')
            json=$(jq -n --arg id "$id" --arg subject "$subject" --arg attachments "$attachments" --arg body "$body" '{id: $id, subject: $subject, attachments: $attachments, body: $body}')
            echo "$json"
        done
    else
        readpst -r $folder_option -o - "$pst_file" 2>/dev/null | grep -B 5 -A 15 -e "Subject: $subject_search" -e "$body_search" | while read -r line; do
            id=$(echo "$line" | grep -oP 'Message-ID: <\K[^>]+')
            subject=$(echo "$line" | grep -oP 'Subject: \K.*')
            attachments=$(echo "$line" | grep -oP 'Attachment: \K.*')
            body=$(echo "$line" | grep -oP 'Body: \K.*')
            json=$(jq -n --arg id "$id" --arg subject "$subject" --arg attachments "$attachments" --arg body "$body" '{id: $id, subject: $subject, attachments: $attachments, body: $body}')
            echo "$json"
        done
    fi
}

# Function to save attachments by message ID
save_attachments_by_id() {
    local pst_file=$1
    local message_id=$2
    local folder_option=$3
    local recursive_option=$4

    if [ "$recursive_option" == "true" ]; then
        readpst -r -R -o - "$pst_file" 2>/dev/null | grep -B 10 -A 10 "$message_id" | grep -oP 'Attachment: \K.*' | while read -r attachment; do
            echo "$attachment" > "$(basename "$attachment")"
        done
    else
        readpst -r $folder_option -o - "$pst_file" 2>/dev/null | grep -B 10 -A 10 "$message_id" | grep -oP 'Attachment: \K.*' | while read -r attachment; do
            echo "$attachment" > "$(basename "$attachment")"
        done
    fi
}

# Function to download email by message ID
download_email_by_id() {
    local pst_file=$1
    local message_id=$2
    local folder_option=$3
    local recursive_option=$4

    if [ "$recursive_option" == "true" ]; then
        readpst -r -R -o - "$pst_file" 2>/dev/null | grep -B 10 -A 10 "$message_id"
    else
        readpst -r $folder_option -o - "$pst_file" 2>/dev/null | grep -B 10 -A 10 "$message_id"
    fi
}

# Function to export contacts
export_contacts() {
    local pst_file=$1
    pffexport -t contacts "$pst_file"
}

# Function to export calendar
export_calendar() {
    local pst_file=$1
    pffexport -t calendar "$pst_file"
}

# Function to list folders
list_folders() {
    local pst_file=$1
    readpst -l "$pst_file"
}

# Main script execution
main() {
    local folder_option=""
    local recursive_option="false"

    while [[ "$1" != "" ]]; do
        case "$1" in
            --install-tools|-i)
                install_tools
                ;;
            --get-header-by-id|-h)
                shift
                get_header_by_id "$1" "$2" "$folder_option" "$recursive_option"
                ;;
            --search-emails-by-sender|-s)
                shift
                search_emails_by_sender "$1" "$2" "$folder_option" "$recursive_option"
                ;;
            --search-emails-by-subject|-j)
                shift
                search_emails_by_subject "$1" "$2" "$folder_option" "$recursive_option"
                ;;
            --search-emails-by-subject-and-body|-b)
                shift
                search_emails_by_subject_and_body "$1" "$2" "$3" "$folder_option" "$recursive_option"
                ;;
            --save-attachments-by-id|-a)
                shift
                save_attachments_by_id "$1" "$2" "$folder_option" "$recursive_option"
                ;;
            --download-email-by-id|-d)
                shift
                download_email_by_id "$1" "$2" "$folder_option" "$recursive_option"
                ;;
            --export-contacts|-c)
                shift
                export_contacts "$1"
                ;;
            --export-calendar|-e)
                shift
                export_calendar "$1"
                ;;
            --list-folders|-f)
                shift
                list_folders "$1"
                ;;
            --folder|-F)
                shift
                folder_option="-V \"$1\""
                ;;
            --recursive|-r)
                recursive_option="true"
                ;;
            *)
                echo "Invalid option. Available options are:"
                echo "--install-tools | -i"
                echo "--get-header-by-id | -h <pst_file> <message_id>"
                echo "--search-emails-by-sender | -s <pst_file> <sender>"
                echo "--search-emails-by-subject | -j <pst_file> <subject_search>"
                echo "--search-emails-by-subject-and-body | -b <pst_file> <subject_search> <body_search>"
                echo "--save-attachments-by-id | -a <pst_file> <message_id>"
                echo "--download-email-by-id | -d <pst_file> <message_id>"
                echo "--export-contacts | -c <pst_file>"
                echo "--export-calendar | -e <pst_file>"
                echo "--list-folders | -f <pst_file>"
                echo "--folder | -F <folder_name>"
                echo "--recursive | -r"
                exit 1
                ;;
        esac
        shift
    done
}

main "$@"
