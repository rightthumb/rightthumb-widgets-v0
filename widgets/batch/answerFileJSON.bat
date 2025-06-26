@if (@CodeSection == @Batch) @then

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

rem @echo off & setlocal
@echo off 

CALL p. singleLineJSON -file %1

set /p JSON=<%1
echo %JSON%
rem // re-eval self with JScript interpreter and capture results
for /f "delims=" %%I in ('cscript /nologo /e:JScript "%~f0"') do set "%%~I"

rem // output captured results
set JSON[

rem // end main runtime
goto :EOF

@end // end Batch / begin JScript hybrid code

var htmlfile = WSH.CreateObject('htmlfile'),
    txt = WSH.CreateObject('Wscript.Shell').Environment('process').Item('JSON');

htmlfile.write('<meta http-equiv="x-ua-compatible" content="IE=9" />');
var obj = htmlfile.parentWindow.JSON.parse(txt);
htmlfile.close();

for (var i in obj) WSH.Echo('JSON[' + i + ']=' + obj[i]);

rem echo %JSON%


 
