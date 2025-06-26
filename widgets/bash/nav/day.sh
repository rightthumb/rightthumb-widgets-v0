#!/bin/bash

if [ "$1" == "" ]; then
	$p day
else
	theDay="$1"
	theD="d"
	$p day -ago "${theDay}${theD}"
fi