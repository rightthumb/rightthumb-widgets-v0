@echo off
type %myTables%\wifi_passwords.txt | p line -p "," 0;5 -make ";n      id: {0};npassword: {1}" %*
