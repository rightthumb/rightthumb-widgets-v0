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


GOTO VAR
CLS
:LOOP
title %title1% v1b
echo ================================
ECHO A. %ItemA%
ECHO B. %ItemB%
ECHO C. %ItemC%
ECHO Q. Quit
echo ================================
GOTO SELECT



:LOOP2
cls
title %title1% v1b
echo ================================
ECHO A. %ItemA%
ECHO B. %ItemB%
ECHO C. %ItemC%
echo ================
ECHO E. Edit Script
ECHO D. Download Script Changes
ECHO R. Reload Script
ECHO U. Upload Script Changes
ECHO F. Run FTP Command
ECHO G. Get SYS Update Scripts
ECHO Q. Quit
echo ================================
GOTO SELECT







:SELECT

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
IF /I '%Choice%'=='L' GOTO LOOP2

ECHO "%Choice%" is not valid. Please try again.
ECHO.
GOTO Loop


:VAR
set title1=techREPH.com Remote Help
set srv=file.techreph.com
set user=script
set pass=script
set htmlfile=meeting.htm
set ftpfile=ftpcmd.txt
set batch=RHelp.bat
set note1=note.txt
set ItemA=Get Script
set ItemB=Get File
set ItemC=Run Item
set Itemx=Upload Item

rename %0 %batch%



CLS
GOTO Loop



:ItemA
@echo off
cls
title %title1% - %ItemA%
echo ========================
Echo %ItemA%
SET File1=
SET /P File1=Enter File Name:
echo ========================
Echo %user%> %ftpfile%
echo %pass%>> %ftpfile%
echo ascii>> %ftpfile%
echo prompt n>>%ftpfile%
echo get %File1%>> %ftpfile%
echo bye >> %ftpfile%
ftp -s:%ftpfile% %srv%
del %ftpfile%
cls
echo %ItemA% Completed
echo ========================
GOTO Loop







:ItemB
cls
title %title1% - %ItemB%
echo ========================
Echo %ItemB%
SET File1=
SET /P File1=Enter File Name:
echo ========================
Echo %user%> %ftpfile%
echo %pass%>> %ftpfile%
echo binary>> %ftpfile%
echo prompt n>>%ftpfile%
echo get %File1%>> %ftpfile%
echo bye >> %ftpfile%
ftp -s:%ftpfile% %srv%
del %ftpfile%
cls
echo %ItemB% Completed
echo ========================
GOTO Loop




:ItemC
cls
title %title1% - %ItemC%
echo ========================
Echo %ItemC%
::IF NOT '%File1%'=='' SET /P File1=Enter File Name:


%File1%
cls
echo %ItemC% Completed
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