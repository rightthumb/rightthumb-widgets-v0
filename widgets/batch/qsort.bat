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

set thisday=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%
set timestamp=%thisday%-%time:~0,2%.%time:~3,2%
setLocal EnableDelayedExpansion

set parent=qsort
set log=%parent%\qsort-%timestamp%-.txt
IF NOT EXIST %parent% (mkdir %parent%)

echo =================== >> %log%
date /t >> %log%
time /t >> %log%

for /f "tokens=* delims= " %%a in ('dir /b/a-d') do (

set name=%%~na
set ext=%%~xa
set last4=!name:~-4!

IF NOT EXIST %parent%\%%~xa (mkdir %parent%\%%~xa)

     move "%%a" %parent%\%%~xa


cls
)
IF NOT EXIST %parent%\misc (mkdir %parent%\misc)
move *.* %parent%\misc
dir /s/b %parent% >> %log%
::type %log%
cls



::::::::::::::::::::::::::::::::::
set "catFolder=Docs" && IF NOT EXIST %parent%\%catFolder% (md %parent%\%catFolder%)
md %parent%\.null && echo.>%parent%\.null\file.null && set folderObject=.null
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.txt
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.xls
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.xlsx
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.doc
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.docx
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.pdf
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.csv
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)

::::::::::::::::::::::::::::::::::
set "catFolder=Graphics" && IF NOT EXIST %parent%\%catFolder% (md %parent%\%catFolder%)
md %parent%\.null && echo.>%parent%\.null\file.null && set folderObject=.null
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.psd
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.jpg
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.jpeg
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.gif
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.bmp
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.png
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)

::::::::::::::::::::::::::::::::::
set "catFolder=Audio" && IF NOT EXIST %parent%\%catFolder% (md %parent%\%catFolder%)
md %parent%\.null && echo.>%parent%\.null\file.null && set folderObject=.null
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.wav
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.mp3
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.m4a
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)

::::::::::::::::::::::::::::::::::
set "catFolder=Tech" && IF NOT EXIST %parent%\%catFolder% (md %parent%\%catFolder%)
md %parent%\.null && echo.>%parent%\.null\file.null && set folderObject=.null
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.vbs
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.bat
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.fp7
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.fp5
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.fmp12
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.ini
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.inf
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.log
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)

::::::::::::::::::::::::::::::::::
set "catFolder=www" && IF NOT EXIST %parent%\%catFolder% (md %parent%\%catFolder%)
md %parent%\.null && echo.>%parent%\.null\file.null && set folderObject=.null
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.ico
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.css
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.htm
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.html
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.php
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)

::::::::::::::::::::::::::::::::::
set "catFolder=bin" && IF NOT EXIST %parent%\%catFolder% (md %parent%\%catFolder%)
md %parent%\.null && echo.>%parent%\.null\file.null && set folderObject=.null
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.zip
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.zip
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.7z
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.sit
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.gz
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.bin
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.img
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)

::::::::::::::::::::::::::::::::::
set "catFolder=misc" && IF NOT EXIST %parent%\%catFolder% (md %parent%\%catFolder%)
md %parent%\.null && echo.>%parent%\.null\file.null && set folderObject=.null
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.lnk
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
set folderObject=.url
IF EXIST "%parent%\%folderObject%" (move "%parent%\%folderObject%" %parent%\%catFolder%)
pause
del /q /s  %parent%\*.null

for /f "delims=" %%d in ('dir /s /b /ad ^| sort /r') do rd "%%d"
for /f "delims=" %%d in ('dir /s /b /ad %parent%\ ^| sort /r') do rd "%%d" 

cls

 
