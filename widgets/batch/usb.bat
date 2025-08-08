@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##


CALL findUSB

if not [%1] == [] (
	SET theusb=%1
	SET theusb=%theusb:~0,1%
)

cls
echo.
echo.
SET USB_APPS=
SET USB_PY_MOD=
SET USB_TA=
SET /p USB_APPS= Update Created programs on USB? 
echo.
SET /p USB_TA= Update tech apps on USB? 
echo.
SET /p USB_PY_MOD= Update USB Python 3 modules? 

IF NOT [%USB_APPS%] == [n] CALL :APPS
IF [%USB_TA%] == [y] CALL :TECH_APPS
IF [%USB_PY_MOD%] == [y] CALL :PY3_MOD

GOTO:EOF

:TECH_APPS
CALL p. copyTool -m -dst %theusb% -answer a -src ta 7-Zip
CALL p. copyTool -m -dst %theusb% -answer a -src ta MP3
CALL p. copyTool -m -dst %theusb% -answer a -src ta VLCPortable
CALL p. copyTool -m -dst %theusb% -answer a -src ta XMPlayPortable
CALL p. copyTool -m -dst %theusb% -answer a -src ta chrome-win
CALL p. copyTool -m -dst %theusb% -answer a -src ta KeePass-1.28
CALL p. copyTool -m -dst %theusb% -answer a -src ta Notepad++
CALL p. copyTool -m -dst %theusb% -answer a -src ta ProcessMonitor
CALL p. copyTool -m -dst %theusb% -answer a -src ta Shortcuts
CALL p. copyTool -m -dst %theusb% -answer a -src ta Sublime Text Build 3211
CALL p. copyTool -m -dst %theusb% -answer a -src ta tools
CALL p. copyTool -m -dst %theusb% -answer a -src ta WinRAR 3.9
CALL p. copyTool -m -dst %theusb% -answer a -src ta _installers
CALL p. copyTool -m -dst %theusb% -answer a -src ta _stand_alone
GOTO:EOF

:APPS

p f -in %myBookmarks%\BM* + {6FAB5628-94A1-410A-82D1-1D42A2A11750} -jn | p. line --c -make " copy {} %techdrive%:\%hostDefault%\bookmarks\ " | p. execute
p f -in %myBookmarks%\BM* + {A8693D4B-8A80-898F-83F0-E806D2F36800} -jn | p. line --c -make " copy {} %techdrive%:\%hostDefault%\bookmarks\ " | p. execute

CALL p. copyTool -m -src hd -dst %theusb% -answer a


CALL p. copyTool -answer a -src ma -dst mad
CALL p. copyTool -answer a -src ma -dst %theusb% mad

CALL p. copyTool -m -dst %theusb% -answer a -src ta Python_Installers
CALL p. copyTool -m -src p -dst %theusb% -answer a
GOTO:EOF


:PY3_MOD
CALL p. copyTool -m -src tapy3 -dst %theusb% -answer a
CALL p. USB_python_modules_synchronized -drive %theusb%
GOTO:EOF