#!/bin/bash

domainsRemln() {
	domainslnR .re  > /dev/null 2>&1
	domainslnS .re > /dev/null 2>&1
	domainslnP .re  > /dev/null 2>&1
	echo ".re remove"
}


domainslnRemS() {
	dst="$2"

	folders=(
		"/home/softwaredev/public_html"
	)

	for folder in "${folders[@]}"; do
		# Remove the symbolic link in the root folder
		[ -L "$folder/$dst" ] && rm "$folder/$dst"
		for domain_folder in "$folder"/*; do
			if [ -d "$domain_folder" ] && [[ "$domain_folder" != .* ]] && [[ "$domain_folder" == *.* ]]; then
				domain=$(basename "$domain_folder")
				# Check and remove the symbolic link in the domain folder or its public_html subfolder
				if [ ! -d "$domain_folder/public_html" ]; then
					[ -L "$domain_folder/$dst" ] && rm "$domain_folder/$dst"
				else
					[ -L "$domain_folder/public_html/$dst" ] && rm "$domain_folder/public_html/$dst"
				fi
			fi
		done
	done
}


domainslnRemP() {
	dst="$2"

	folders=(
		"/home/programmer/public_html"
	)

	for folder in "${folders[@]}"; do
		# Remove the symbolic link in the root folder
		[ -L "$folder/$dst" ] && rm "$folder/$dst"
		for domain_folder in "$folder"/*; do
			if [ -d "$domain_folder" ] && [[ "$domain_folder" != .* ]] && [[ "$domain_folder" == *.* ]]; then
				domain=$(basename "$domain_folder")
				# Check and remove the symbolic link in the domain folder or its public_html subfolder
				if [ ! -d "$domain_folder/public_html" ]; then
					[ -L "$domain_folder/$dst" ] && rm "$domain_folder/$dst"
				else
					[ -L "$domain_folder/public_html/$dst" ] && rm "$domain_folder/public_html/$dst"
				fi
			fi
		done
	done
}

domainslnRemR() {
	dst="$2"

	folders=(
		"/home/rightthumb/public_html"
		"/home/rightthumb/public_html/domains"
	)

	for folder in "${folders[@]}"; do
		# Remove the symbolic link in the root folder
		[ -L "$folder/$dst" ] && rm "$folder/$dst"
		for domain_folder in "$folder"/*; do
			if [ -d "$domain_folder" ] && [[ "$domain_folder" != .* ]] && [[ "$domain_folder" == *.* ]]; then
				domain=$(basename "$domain_folder")
				# Check and remove the symbolic link in the domain folder or its public_html subfolder
				if [ ! -d "$domain_folder/public_html" ]; then
					[ -L "$domain_folder/$dst" ] && rm "$domain_folder/$dst"
				else
					[ -L "$domain_folder/public_html/$dst" ] && rm "$domain_folder/public_html/$dst"
				fi
			fi
		done
	done
}
alias .rem="domainsRemln"