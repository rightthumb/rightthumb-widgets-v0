@echo off
cls
title encode
echo                  ...               encode               ....
set /p in=Enter filename in.txt ::
base64 -e %in% out_file.txt
notepad out_file.txt