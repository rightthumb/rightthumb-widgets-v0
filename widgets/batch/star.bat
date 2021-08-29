@echo off &setlocal
if not exist ~ echo  " >~ & star string "
if not exist ~ goto END
set "search=%1"
set "em= -*#*- "
set "replace=%em%%search%%em%"
set "textfile=~"
set "newfile=_new.txt"

(for /f "delims=" %%i in ('findstr "^" "%textfile%"') do (
    set "line=%%i"
    setlocal enabledelayedexpansion
    set "line=!line:%search%=%replace%!"
    echo(!line!
    endlocal
))>"%newfile%"
type "%newfile%"
GOTO END

:end 

 
 
 
 
 
 
 
 
 
 
 
 
