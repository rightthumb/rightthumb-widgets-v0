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

cls
title :: Ultimate nslookup ::
set who=paring.com
set out=test.txt
set input=input.txt
:
:
echo Ultimate nslookup
echo example msn, google  -not google.com
set /p name=Enter the name without the .com, .net, etc.:
cls
echo example MX, Any, cname
echo Do not leave this blank if unsure type Any.
set /p q=Set query Paramiters:
echo set q=%q% > %input%
echo %name%.com >> %input%
echo %name%.net >> %input%
echo %name%.org >> %input%
echo %name%.us >> %input%
echo %name%.biz >> %input%
echo %name%.info >> %input%
echo %name%.us >> %input%
echo %name%.ws >> %input%
echo %name%.cc >> %input%
echo %name%.bz >> %input%
echo %name%.tv >> %input%
cls
title :: Finding information ::
nslookup<%input% > %out%
start notepad %out%
cls
echo To sort the data...
pause
title :: Sorting Data ::
nslookup<%input% |sort /R > %out%
start notepad %out%
echo To delete temp files...
pause
del %input%
del %out%

 
