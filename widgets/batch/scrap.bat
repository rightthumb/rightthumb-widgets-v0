@echo off
SET /p Drive=<%userprofile%\.tk421
rem echo fileLine & CALL p fileLine -f %Drive%:\tech\hosts\%computername%\config\.unix_id -line 7 --c
rem echo.


CALL p fileLine -f %Drive%:\tech\hosts\%computername%\config\.unix_id -line 7 --c > %tmpf%
SET /p unixID7=<%tmpf%
SET scrap2="%Drive%:\widgets\bash\notes\RT-scrap-%unixID7%.txt"
if not exist "%Drive%:\widgets\bash" mkdir "%Drive%:\widgets\bash"
if not exist "%Drive%:\widgets\bash\notes" mkdir "%Drive%:\widgets\bash\notes"
if not exist %scrap2% (
	echo %computername% - %distro% >> %scrap2%
	echo ______________________________________________________________________ >> %scrap2%
	echo.  >> %scrap2%
	echo ______________________________________________________________________ >> %scrap2%
)



rem echo tmpf: %tmpf%
rem echo unixID7: %unixID7%
rem echo scrap2: %scrap2%
rem goto:eof

call p fileBackup -i %scrap2%
start "EDIT" %code_editor% %scrap2%

