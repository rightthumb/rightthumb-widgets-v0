@echo off
title :: easy note ::
cls
echo ==========================================
echo =                                        =
echo =     You are responsible for misuse!    =
echo =                                        =
echo =           (activity may be monitored)  =
echo =                                        =
echo ==========================================

set /p to=Enter the computer name:)
set /p m=Enter the single line Message:)
net send %to% %m%
echo success