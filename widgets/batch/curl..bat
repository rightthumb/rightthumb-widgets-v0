@echo off

call p. site -f %1 | call cp

GOTO :EOF

call p. download -url https://sds.sh/block/youtube/curl.zip