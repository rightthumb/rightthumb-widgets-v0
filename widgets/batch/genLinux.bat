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


CALL:process_folder python py
CALL:process_folder bash *
CALL:process_folder documentation *
CALL:process_folder library *
CALL:process_folder javascript *
CALL:process_folder batch *
CALL:process_folder remote *
CALL:process_folder vbs *
CALL:process_folder php *
CALL:process_folder powershell *


rem call m back
rem call b tech
SET run=y
rem SET /p run= Zip Linux: 
if [%run%] == [n] goto:eof
rem p zip -folder D:\tech\linux  -save D:\websites\tools.RightThumb\tools\linux.zip
start cmd /c %userprofile%\cx.bat call p. zip -folder D:\tech\linux -save D:\websites\tools.RightThumb\tools\linux.zip
call p. wait -w 2
rem move /y D:\tech\linux.zip D:\websites\tools.RightThumb\tools\
echo moved 
SET /p run= Zip Linux, upload: 
if [%run%] == [n] goto:DB
rem call p. genLinux + linux.zip
echo wget https://reph.us/tools/linux.zip

:DB
SET /p run= Zip databank:
if [%run%] == [n] goto:eof
rem p zip -folder %widgets%\widgets\databank -save D:\websites\tools.RightThumb\tools\databank.zip
start cmd /c %userprofile%\cx.bat call p. zip -folder %widgets%\widgets\databank -save D:\websites\tools.RightThumb\tools\databank.zip
rem SET /p run= Zip databank, done: 
call p. wait -w 2
rem move /y %widgets%\widgets\databank.zip D:\websites\tools.RightThumb\tools\
echo moved 
SET /p run= uploading databank.zip: 
if [%run%] == [n] goto:eof
rem call p. genLinux + databank.zip
echo wget https://reph.us/tools/databank.zip



rem rmdir /s/q D:\tech\linux\

rem start cmd /c %userprofile%\cx.bat LinuxZip
rem echo Waiting for zip
rem ping google.com -n 10 >nul




rem call:upload



goto:eof

:upload
rem CALL p. genLinux
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
set xt=%2
echo.
echo.
echo Processing %fld% .......................
set subject_folder=D:\tech\linux\%fld%
rmdir /s/q %subject_folder%
mkdir %subject_folder%
xcopy /s/d/y/c %widgets%\widgets\%fld%\*.%xt%  %subject_folder%\
echo.
echo.
goto:eof