@echo off
title= fixing IP Address
ipconfig /flushdns
ipconfig /release
ipconfig /renew

call myip