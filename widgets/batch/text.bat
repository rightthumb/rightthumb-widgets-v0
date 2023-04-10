@echo off



call p isPhoneNumber -i %1 > %tmpf%
set /p isPhoneNumber=<%tmpf%
if [%isPhoneNumber%] == [yes] (
    set phone=%1
) else (
    set phone=8136901260
)


call p vps-srv-7facG-twilio-send -from 813-375-0606 -to %phone% -body %*
rem p vps-srv-7facG-twilio-send -from 813-375-0606 -to 8136901260 -body default EyeForMeta.com
rem p vps-srv-7facG-twilio-send -from 813-906-0992 -to 8136901260 -body Chat EyeForMeta.com
rem p vps-srv-7facG-twilio-send -from 813-797-7379 -to 8136901260 -body Gatekeeper EyeForMeta.com
rem p vps-srv-7facG-twilio-send -from 813-696-3592 -to 8136901260 -body Rick Astley
rem p vps-srv-7facG-twilio-send -from 813-696-3088 -to 8136901260 -body AI RightThumb.com



GOTO:EOF

rem 813-375-0606 default EyeForMeta.com
rem 813-906-0992 Chat EyeForMeta.com
rem 813-797-7379 Gatekeeper EyeForMeta.com
rem 813-696-3592 Rick Astley
