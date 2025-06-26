#!/bin/bash

if [ -z "$1" ]; then
	$p on -session "$Session_ID" -folder "$(pwd)"
	$p tag -trigger expires 1w -fo .
else
	$p on -session "$Session_ID" -delete
	$p tag -trigger expires 1w -fo . -delete
fi