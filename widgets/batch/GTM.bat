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

title Go To Meeting Link Manager
GOTO VAR
CLS
:LOOP
ECHO A. Paste Meeting
ECHO B. Delete Meeting
ECHO C. Test Link
echo ================
ECHO E. Edit Script
ECHO D. Download Script Changes
ECHO R. Reload Script
ECHO U. Upload Script Changes
ECHO F. Run FTP Command
ECHO G. Get SYS Update Scripts
ECHO Q. Quit
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
IF /I '%Choice%'=='S' GOTO SAVE

ECHO "%Choice%" is not valid. Please try again.
ECHO.
GOTO Loop


:VAR
set srv=reph.com
set user=gtm
set pass=meeting123
set htmlfile=meeting.htm
set ftpfile=ftpcmd.txt
set batch=GTM.bat
rename %0 %batch%
CLS
GOTO Loop



:ItemA
@echo off
cls
echo ========================
echo ========================
SET /P url1=Enter Meeting URL (2of7):
SET /P url=:
SET /P url1=:
SET /P mt=:
SET /P url1=:
SET /P url1=:
SET /P url1=:



Echo "<a href="%url%">Click here to load meeting</a>"> %htmlfile%
Echo %user%> %ftpfile%
echo %pass%>> %ftpfile%
echo binary>> %ftpfile%
echo prompt n>>%ftpfile%
echo put %htmlfile%>> %ftpfile%
echo bye >> %ftpfile%
ftp -s:%ftpfile% %srv%
del %ftpfile%
del %htmlfile%
cls
echo Meeting Loaded
echo ========================
GOTO Loop
-------------------



:ItemB
@echo off
cls
echo ========================
echo ========================
Echo "<span class="style6">No Meetings are in Session at this time</span>"> %htmlfile%
Echo %user%> %ftpfile%
echo %pass%>> %ftpfile%
echo binary>> %ftpfile%
echo prompt n>>%ftpfile%
echo put %htmlfile%>> %ftpfile%
echo bye >> %ftpfile%
ftp -s:%ftpfile% %srv%
del %ftpfile%
del %htmlfile%
cls
echo Meeting UnLoaded
echo ========================
GOTO Loop
-------------------




-------------------



:ItemC
"D:\Program Files\Internet Explorer\IEXPLORE.EXE" "http://www.tech%srv%/%user%/"
cls
echo Link Tested
echo ========================
GOTO Loop
:End
cls
echo thank you for using the techREPH Meeting Manager

exit



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

 
