@echo off

if ["%1"] == [""] (
	echo Usage: pyinstaller [options] scriptname.py
	exit /b 1
)
if [%pyinstaller%] == [] (
	for /f "delims=" %%i in ('where pyinstaller ^| findstr /i "pyinstaller.exe"') do (
		set "pyinstaller=%%i"
	)
)

if [%debug%] == [yes]  (
	echo %pyinstaller% %*
	goto:eof
)



"%pyinstaller%" %*