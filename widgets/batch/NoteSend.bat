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

title Remote Note Manager v1b
GOTO VAR
CLS
:LOOP
echo ================================
ECHO A. Get Note
ECHO B. PUT Note
echo ================
ECHO E. Edit Script
ECHO D. Download Script Changes
ECHO R. Reload Script
ECHO U. Upload Script Changes
ECHO F. Run FTP Command
ECHO G. Get SYS Update Scripts
ECHO Q. Quit
echo ================================
:: SET /P prompts for input and sets the variable
:: to whatever the user types
SET Choice=
SET /P Choice=Type the letter and press Enter: 
:: The syntax in the next line extracts the substring
:: starting at 0 (the beginning) and 1 character long
IF NOT '%Choice%'=='' SET Choice=%Choice:~0,1%
ECHO.
:: /I makes the IF comparison case-insensitive
IF /I '%Choice%'=='A' GOTO ItemA
IF /I '%Choice%'=='B' GOTO ItemB
IF /I '%Choice%'=='C' GOTO ItemC

IF /I '%Choice%'=='E' GOTO EDIT
IF /I '%Choice%'=='D' GOTO Download
IF /I '%Choice%'=='R' GOTO RELOAD
IF /I '%Choice%'=='U' GOTO Upload
IF /I '%Choice%'=='F' GOTO DIR
IF /I '%Choice%'=='G' GOTO TECHFILES
IF /I '%Choice%'=='Q' GOTO end
IF /I '%Choice%'=='S' GOTO Save

ECHO "%Choice%" is not valid. Please try again.
ECHO.
GOTO Loop


:VAR
set srv=file.techreph.com
set user=script
set pass=script
set htmlfile=meeting.htm
set ftpfile=ftpcmd.txt
set batch=NoteSend.bat
set note1=note.txt
rename %0 %batch%
CLS
GOTO Loop



:ItemA
@echo off
Echo Get Note
cls
echo ========================
Echo %user%> %ftpfile%
echo %pass%>> %ftpfile%
echo binary>> %ftpfile%
echo prompt n>>%ftpfile%
echo get %note1%>> %ftpfile%
echo bye >> %ftpfile%
ftp -s:%ftpfile% %srv%
del %ftpfile%
set note1=note.txt
notepad.exe %note1%
cls
echo Note Received
echo ========================
GOTO Loop







:ItemB

@echo off
cls
echo ========================

ECHO Paste Here > %note1%
notepad.exe %note1%



Echo %user%> %ftpfile%
echo %pass%>> %ftpfile%
echo binary>> %ftpfile%
echo prompt n>>%ftpfile%
echo put %note1%>> %ftpfile%
echo bye >> %ftpfile%
ftp -s:%ftpfile% %srv%
del %ftpfile%
cls
echo Note Sent
echo ========================
GOTO Loop






:Download
@echo off
Echo %user%> %ftpfile%
echo %pass%>> %ftpfile%
echo ascii>> %ftpfile%
echo prompt n>>%ftpfile%
echo get %batch%>> %ftpfile%
echo bye >> %ftpfile%
ftp -s:%ftpfile% %srv%
del %ftpfile%
cls
echo Download Complete
echo ========================
goto loop



:Upload
@echo off
cls
echo ========================
echo .
echo         Upload?
echo .
echo ========================
pause
Echo %user%> %ftpfile%
echo %pass%>> %ftpfile%
echo ascii>> %ftpfile%
echo prompt n>>%ftpfile%
echo put %batch%>> %ftpfile%
echo bye >> %ftpfile%
ftp -s:%ftpfile% %srv%
del %ftpfile%
cls
echo Upload Complete
echo ========================
goto loop



:DIR
@echo off
Echo %user%> %ftpfile%
echo %pass%>> %ftpfile%
echo binary>> %ftpfile%
echo dir>> %ftpfile%
ftp -s:%ftpfile% %srv%
pause
del %ftpfile%
cls
echo Secret FTP FREE Complete
echo ========================
goto loop

:RELOAD
@echo off
%0

:EDIT
start /MAX notepad.exe %0
cls
echo Edit Completed
echo ========================
%0

:TECHFILES
@echo off
Echo %user%> %ftpfile%
echo %pass%>> %ftpfile%
echo ASCII>> %ftpfile%
echo cd tech>> %ftpfile%
echo get GETEXE.bat>> %ftpfile%
echo get GETbatcuts.bat>> %ftpfile%
echo bye>> %ftpfile%
ftp -s:%ftpfile% %srv%
del %ftpfile%
cls
echo Get Tech Files Complete
echo ========================
goto loop

:SAVE
xcopy /d %0 c:\
xcopy /d %0 "%windir%\system32\"
cls
echo Saved to C: and System Root
echo ========================
goto loop