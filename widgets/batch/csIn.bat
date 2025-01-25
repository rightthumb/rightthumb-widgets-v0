@echo off
if [%1]==[] (
    set clipSlot=Default
) else (
    set clipSlot=%1
)
call pa > %tmpf%-clipSlot-%clipSlot%
set cs=%tmpf%-%1
echo.
call p. colorize -txt "Clipboard Slot saved to %clipSlot%" -hex light_slate_gray
if [%clipSlot%]==[Default] (
    call p. colorize -txt "Set back to clipboard with cs" -hex lawn_green
) else (
    call p. colorize -txt "Set back to clipboard with cs %clipSlot%" -hex lawn_green
    set cs%%clipSlot%%=%tmpf%-%1
)

echo.