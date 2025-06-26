#!/bin/bash

# Check if required tools are installed, and install them if not
if ! command -v isoinfo &> /dev/null
then
	echo "isoinfo could not be found. Installing..."
	sudo apt-get update
	sudo apt-get install -y genisoimage
fi

if ! command -v parted &> /dev/null
then
	echo "parted could not be found. Installing..."
	sudo apt-get update
	sudo apt-get install -y parted
fi

# Function to analyze ISO
analyze_iso() {
	local file_path=$1
	local iso_info=$(isoinfo -d -i "$file_path")

	# Extract information
	volume_identifier=$(echo "$iso_info" | grep 'Volume id:' | awk -F'Volume id: ' '{print $2}')
	logical_block_size=$(echo "$iso_info" | grep 'Logical block size is:' | awk -F'Logical block size is: ' '{print $2}')
	bootable=$(echo "$iso_info" | grep -q 'Bootable' && echo "true" || echo "false")

	# Create JSON object
	iso_json=$(cat <<EOF
{
	"file_path": "$file_path",
	"file_extension": "iso",
	"volume_identifier": "$volume_identifier",
	"logical_block_size": $logical_block_size,
	"bootable": $bootable
}
EOF
)
	echo "$iso_json"
}

# Function to analyze partition scheme (if applicable)
analyze_partition_scheme() {
	local file_path=$1
	local part_info=$(sudo parted "$file_path" print 2>/dev/null)

	# Extract information
	partition_scheme=$(echo "$part_info" | grep 'Partition Table:' | awk -F'Partition Table: ' '{print $2}')
	target_system_type=$(echo "$part_info" | grep 'Target system type:' | awk -F'Target system type: ' '{print $2}')

	# Create JSON object
	part_json=$(cat <<EOF
{
	"file_path": "$file_path",
	"partition_scheme": "$partition_scheme",
	"target_system_type": "$target_system_type"
}
EOF
)
	echo "$part_json"
}

# Main script
results=()

for file_path in "$@"
do
	file_extension="${file_path##*.}"
	if [[ "$file_extension" == "iso" ]]; then
		iso_result=$(analyze_iso "$file_path")
		results+=("$iso_result")
	else
		echo "{\"error\": \"Unsupported file type\"}"
	fi
done

# Print results in JSON format
echo "["
printf "%s\n" "${results[@]}" | sed 's/,$//'
echo "]"