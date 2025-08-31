#!/bin/bash

dns_server="8.8.8.8"
if [ -z "$2" ]; then
    port_number="80"
else
    port_number="$2"
fi

echo "~~~"
echo "__________________________________________________________________"
echo "Performing nslookup queries for domain: $1"
echo

echo "______"
echo "Perform an MX record lookup"
nslookup -type=mx "$1" "$dns_server"
echo

echo "______"
echo "Perform a TXT record lookup"
nslookup -type=txt "$1" "$dns_server"
echo

echo "______"
echo "Perform a PTR (reverse DNS) lookup for a hostname"
nslookup "$1" "$dns_server"
echo

echo "______"
echo "Perform a SOA record lookup"
nslookup -type=soa "$1" "$dns_server"
echo

echo "______"
echo "Perform a NS record lookup"
nslookup -type=ns "$1" "$dns_server"
echo

echo "______"
echo "Perform a CNAME record lookup"
nslookup -type=cname "$1" "$dns_server"
echo

echo "______"
echo "Perform an AAAA (IPv6) record lookup"
nslookup -type=aaaa "$1" "$dns_server"
echo

# Add more nslookup commands here with comments

echo
echo "______"
echo "Example of custom query: Query for a specific DNS server"
nslookup "$1" "$dns_server"
echo

echo "______"
echo "Example of custom query: Query for a specific port $port_number or 80"
nslookup -port="$port_number" "$1" "$dns_server"
echo

# Additional nslookup commands can be added here as needed

echo "Nslookup queries completed for domain: $1"
echo "~~~"
