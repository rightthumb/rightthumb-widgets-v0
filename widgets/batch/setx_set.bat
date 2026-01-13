@echo off
set setx_name=%1
call shifty %*
setx RT_%setx_name% "%shifty%"  > nul 2>&1