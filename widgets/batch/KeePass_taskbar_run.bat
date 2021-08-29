@echo off
call "D:\Users\Scott\cc.bat"
set /p id=Enter ID: 
if [%id%] == [] (
	set id=me
)
call p fileBackup -open -f D:\.rightthumb-widgetswidgetskeys\p\%id%.kdbx
start "D:\.rightthumb-widgetsApps\KeePass-2.48.1\KeePass.exe" "D:\.rightthumb-widgetswidgetskeys\p\%id%.kdbx"