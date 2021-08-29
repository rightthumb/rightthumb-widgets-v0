@echo off
fciv.exe d:\ -r -md5 > d:\md5.txt
fciv c:\ -r -md5 -type *.dll >> d:\md5.txt
fciv c:\ -r -md5 -type *.exe >> d:\md5.txt
