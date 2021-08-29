@echo off

set find=IPv4
ipconfig | find /i "%find%"

