#!/bin/bash

if [ -z "$2" ]; then
	$p tag -trigger expires 1w -f "$@"
	$p on -session "$Session_id" -folder .
else
	$p tag -trigger expires 1w -delete -f "$@"
	$p on -session "$Session_id" -folder . -delete
fi