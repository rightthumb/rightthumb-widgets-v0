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




echo wget http://reph.us/tools/file.php?file=tool.sh -O ~/.rt/tool.sh
set subject_folder=D:\tech\linux\python
rmdir /s/q %subject_folder%
mkdir %subject_folder%
mkdir %subject_folder%\src
mkdir %subject_folder%\
xcopy /s/d/y/c %widgets%\widgets\python\*.py  %subject_folder%\


CALL:process_folder bash
CALL:process_folder documentation
CALL:process_folder library
CALL:process_folder javascript
CALL:process_folder batch
CALL:process_folder remote
CALL:process_folder vbs
CALL:process_folder php
CALL:process_folder powershell


rem call m back
rem call b tech
SET run=y
rem SET /p run= Zip Linux: 
if [%run%] == [n] goto:eof
start cmd /c D:\Users\Scott\cx.bat call p zip -folder D:\tech\linux
move /y D:\tech\linux.zip D:\websites\tools.RightThumb\tools\
echo moved 
SET /p run= Zip Linux, upload: 
if [%run%] == [n] goto:DB
call p genLinux + linux.zip
echo wget https://reph.us/tools/linux.zip

:DB
SET /p run= Zip databank:
if [%run%] == [n] goto:eof
start cmd /c D:\Users\Scott\cx.bat call p zip -folder %widgets%\widgets\databank
rem SET /p run= Zip databank, done: 
move /y %widgets%\widgets\databank.zip D:\websites\tools.RightThumb\tools\
echo moved 
SET /p run= uploading databank.zip: 
if [%run%] == [n] goto:eof
call p genLinux + databank.zip
echo wget https://reph.us/tools/databank.zip



rem rmdir /s/q D:\tech\linux\

rem start cmd /c D:\Users\Scott\cx.bat LinuxZip
rem echo Waiting for zip
rem ping google.com -n 10 >nul




rem call:upload



goto:eof

:upload
CALL p genLinux
echo.
echo.
echo sudo wget -O - -q "http://reph.us/tools/file.php?file=tool.sh" ^| bash
rem echo wget https://reph.us/tools/Linux.zip
rem echo wget https://reph.us/tools/databank.zip
echo.
echo unzip Linux.zip -d linux
echo.
echo.
rem call b back
goto:eof

:process_folder
set fld=%1
echo.
echo.
echo Processing %fld% .......................
set subject_folder=D:\tech\linux\%fld%
rmdir /s/q %subject_folder%
mkdir %subject_folder%
xcopy /s/d/y/c %widgets%\widgets\%fld%\*.*  %subject_folder%\
echo.
echo.
goto:eof


