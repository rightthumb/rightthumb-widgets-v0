@echo off
setlocal
set save_clip_auto="%stmp%\hotkeys-save_clip-auto"
if exist %save_clip_auto% (
    del %save_clip_auto%>nul 2>&1
    echo save clip auto disabled
) else (
    echo save_clip_auto > %save_clip_auto%
    echo save clip auto enabled
)

endlocal