@echo off

setlocal


SET FILE_PATH="%stmp%\pin_ask"

IF EXIST %FILE_PATH% (
    del %FILE_PATH%
    echo pin off
) ELSE (
    echo ask > %FILE_PATH%
    echo pin on
)


endlocal