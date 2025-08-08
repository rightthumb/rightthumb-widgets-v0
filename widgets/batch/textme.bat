@echo off



call p. isPhoneNumber -i %1 > %tmpf%
set /p isPhoneNumber=<%tmpf%
if [%isPhoneNumber%] == [yes] (
	set phone=%1
) else (
	set phone=8136901260
)


call p. vps-srv-7facG-twilio-send  -to %phone% -body %*