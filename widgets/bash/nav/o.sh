#!/bin/bash

if [ -z "$1" ]; then
	$p file-open -backup secure -alias last
else
	$p file-open -backup secure -alias "$@"
	# Uncomment the line below if you need the equivalent of `call cdf`
	# $p cdf
fi