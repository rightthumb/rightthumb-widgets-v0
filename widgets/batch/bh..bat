@echo off

if exist "%myTables%\BookmarksBySession" (
    p cat -f  "%myTables%\BookmarksBySession\%Session_ID%.log" - "ECHO is off" --c
)
