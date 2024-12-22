#!/usr/bin/env bash
# aes256.sh - AES encryption and decryption using OpenSSL

c='\033[0m'
b='\033[1m'

help="$(cat << EOF
${b}NAME${c}
	aes256 - aes 256 algorithm (part of cross-language-encryption library)

${b}SYNOPSIS${c}
	${b}aes256${c} [encrypt|decrypt] [${b}-p${c} passphrase|${b}--passphrase${c}=passphrase]
	[${b}-i${c} input_file|${b}--in${c}=input_file] [${b}-o${c} output_file|${b}--out${c}=output_file]

${b}DESCRIPTION${c}
	Encrypt or decrypt strings or files using AES-256-CBC with OpenSSL.

	Options:
	${b}-p${c}, ${b}--passphrase${c} passphrase
		Specifies passphrase

	${b}-i${c}, ${b}--in${c} input_file
		Input file to encrypt or decrypt

	${b}-o${c}, ${b}--out${c} output_file
		Output file for the result

	${b}--help${c}
		Show this help

${b}AUTHORS${c}
	Andrey Izman, part of AES-everywhere project.
EOF
)"

usage="usage: aes256 encrypt|decrypt [-p passphrase|--passphrase=passphrase] [-i input_file|--in=input_file] [-o output_file|--out=output_file]"

operation="encrypt"
in=""
out=""
passphrase=""

# Check for no arguments
if [[ $# -eq 0 ]]; then
	(1>&2 echo "Error: No options provided")
	echo -e "$usage"
	exit 1
fi

# Determine operation
if [[ $1 == "decrypt" ]]; then
	operation="decrypt"
	shift
elif [[ $1 == "encrypt" ]]; then
	shift
fi

# Parse arguments
while [[ $# -gt 0 ]]; do
	case "$1" in
		-p|--passphrase)
			shift
			passphrase="${1:-}"
			if [[ -z "$passphrase" ]]; then
				(1>&2 echo "Error: Missing passphrase")
				exit 2
			fi
			;;
		--passphrase=*)
			passphrase="${1#--passphrase=}"
			;;
		-i|--in)
			shift
			in="${1:-}"
			if [[ -z "$in" || ! -f "$in" ]]; then
				(1>&2 echo "Error: Input file '$in' does not exist")
				exit 3
			fi
			;;
		--in=*)
			in="${1#--in=}"
			if [[ ! -f "$in" ]]; then
				(1>&2 echo "Error: Input file '$in' does not exist")
				exit 3
			fi
			;;
		-o|--out)
			shift
			out="${1:-}"
			;;
		--out=*)
			out="${1#--out=}"
			;;
		--help)
			echo -e "$help"
			exit 0
			;;
		*)
			(1>&2 echo "Error: Unknown option '$1'")
			echo -e "$usage"
			exit 1
			;;
	esac
	shift
done

# Validate passphrase
if [[ -z "$passphrase" ]]; then
	(1>&2 echo "Error: Passphrase is required")
	exit 4
fi

# Read input file or stdin
input_data=""
if [[ -n "$in" ]]; then
	input_data="$(cat "$in")"
else
	if [[ -p /dev/stdin ]]; then
		input_data="$(cat)"
	else
		(1>&2 echo "Error: No input provided")
		exit 5
	fi
fi

# Perform encryption or decryption
result=""
if [[ "$operation" == "decrypt" ]]; then
	result=$(echo -n "$input_data" | openssl enc -aes-256-cbc -md md5 -a -A -pass pass:"$passphrase" -d 2>/dev/null)
	if [[ $? -ne 0 ]]; then
		(1>&2 echo "Error: Decryption failed")
		exit 6
	fi
else
	result=$(echo -n "$input_data" | openssl enc -aes-256-cbc -md md5 -a -A -pass pass:"$passphrase" 2>/dev/null)
	if [[ $? -ne 0 ]]; then
		(1>&2 echo "Error: Encryption failed")
		exit 7
	fi
fi

# Write result to output file or stdout
if [[ -n "$out" ]]; then
	echo -n "$result" > "$out"
	if [[ $? -ne 0 ]]; then
		(1>&2 echo "Error: Failed to write to output file '$out'")
		exit 8
	fi
else
	echo -n "$result"
fi