#!/bin/bash

if [[ ( "$PWD" == "/home/scott" && "$HOME" != "/home/scott" ) ]]; then
	cd $HOME
fi