@echo off
if [%1]==[] (
    set clipSlot=0
) else (
    set clipSlot=%1
)
call pa > %tmpf%-clipSlot-%clipSlot%


if [%clipSlot%]==[0] (
    set backupSlot=%clipSlot%
    set "clipSlot="
)

set /p pa%clipSlot%=<%tmpf%-clipSlot-%backupSlot%
set fpa%clipSlot%=%tmpf%-clipSlot-%backupSlot%

set "per=%%"

set printSlot=%per%clipSlot
set printSlot=%per%%printSlot%%per%%per%

set printVar=%per%pa%clipSlot%
set printVar=%per%%printVar%%per%%per%

set printFile=%per%fpa%clipSlot%
set printFile=%per%%printFile%%per%%per%

@REM echo %printSlot%
echo.

: "<" "'%printVar%'" ">" 


call p. colorize -txt pa%clipSlot% ")--" "Clipboard Slot saved to " "(" pa%clipSlot% ")" "[" "'%printVar%'" "]"  "<" "'%printFile%'" ">"  -hex aqua orange_red lawn_green cyan yellow cyan magenta_purple aqua magenta_purple   light_steel_blue pale_goldenrod light_steel_blue                                                        

echo.