#!/bin/bash

if [ $# -eq 0 ]
  then
	echo "No arguments supplied"
fi

if [ -z "$1" ]
  then
	echo "No argument supplied"
fi

if [ ! -z "$1" ]
  then
	echo "1st argument supplied"
fi