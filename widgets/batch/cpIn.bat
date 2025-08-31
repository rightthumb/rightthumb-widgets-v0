@echo off
if [%1]==[] (
	set clipSlot=Default
) else (
	set clipSlot=%1
)
call pa > %tmpf%-clipSlot-%clipSlot%
set cs%clipSlot%=%tmpf%-clipSlot-%clipSlot%
call pa > %tmpf%-clipSlot-%clipSlot%
set /p pa%clipSlot%=<%tmpf%-clipSlot-%clipSlot%
if [%clipSlot%]==[Default] (
	set "clipSlot="
)
set "per=%%"
@REM echo %quote%
set printSlot=%per%clipSlot
set printSlot=%per%%printSlot%%per%%per%
set printVar=%per%pa%clipSlot%
set printVar=%per%%printVar%%per%%per%
@REM echo %printSlot%
echo.

: "<" "'%printVar%'" ">" 


call p. colorize -txt cs%clipSlot% ")--" "Clipboard Slot saved to " "(" cs%clipSlot% ")" "[" "'%printVar%'" "]" -hex aqua orange_red lawn_green cyan yellow cyan magenta_purple aqua magenta_purple   light_steel_blue pale_goldenrod light_steel_blue                                                        
@REM if [%clipSlot%]==[Default] ( 
@REM     call p. colorize -txt cs ")--" "Set back to clipboard with " "(" cs ")" -hex light_cyan orange_red lawn_green cyan yellow cyan
@REM ) else (
@REM     call p. colorize -txt cs%clipSlot% ")--" "Set back to clipboard with " "(" cs%clipSlot% ")" -hex light_cyan orange_red lawn_green cyan yellow cyan
@REM     set cs%%clipSlot%%=%tmpf%-%1
@REM )

echo.