#!/bin/bash

# Check if the required arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <domain_name> <email_address>"
    exit 1
fi

# Assign the provided arguments to variables
domain=$1
email=$2

# Retrieve the authoritative nameserver for the domain
nameserver=$(dig +short NS "$domain" | head -n1)

# Extract the domain's serial number from the SOA record
serial=$(dig +short SOA "$domain" | awk '{print $3}')

# Extract the other values from the SOA record
refresh=$(dig +short SOA "$domain" | awk '{print $4}')
retry=$(dig +short SOA "$domain" | awk '{print $5}')
expire=$(dig +short SOA "$domain" | awk '{print $6}')
minimum=$(dig +short SOA "$domain" | awk '{print $7}')

# Replace "@" with a dot in the email address
email=${email/@/.}

# Generate the DNS line
dns_line="${domain}.    86400    IN    SOA    ${nameserver} ${email}. ${serial} ${refresh} ${retry} ${expire} ${minimum}"

# Print the generated DNS line
echo "$dns_line"
