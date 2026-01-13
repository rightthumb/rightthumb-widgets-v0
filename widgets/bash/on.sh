#!/bin/bash

if [ -z "$1" ]; then
	$p on -session "$Session_ID" -folder "$(pwd)"
else
	$p on -session "$Session_ID" -delete
fi