@echo off
set log=i.i
date /t > %log%
time /t >> %log%
dir /s/b  >> %log%


:TEST
echo index file %log% has been created
echo ============== >> \index\logs\i.log.txt
date /t >> \index\logs\i.log.txt
time /t >> \index\logs\i.log.txt
dir /b %log% >> \index\logs\i.log.txt