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

rem set wwwPage_0=D:\techApps\Library\WEB\newpage\blank0.htm
rem set wwwPage_1=D:\techApps\Library\WEB\newpage\blank1.htm
set wwwPage_0=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\0.htm
set wwwPage_1=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\1.htm
set wwwPage_2=D:\techApps\Library\WEB\newpage\blank2.htm
set wwwPage_3=D:\techApps\Library\WEB\newpage\blank3.htm
set wwwPage_4=D:\techApps\Library\WEB\newpage\blank4.htm
set wwwPage_js1=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\js.js

if ["%1"] == ["?"] (
        call :HELP
        GOTO:EOF
    )



if [%1] == [] (
        set wwwPage=%wwwPage_0%
) else if [%1] == [1] (
        set wwwPage=%wwwPage_1%
) else if [%1] == [2] (
        set wwwPage=%wwwPage_2%
) else if [%1] == [3] (
        set wwwPage=%wwwPage_3%
) else if [%1] == [4] (
        set wwwPage=%wwwPage_4%
) else if [%1] == [js] (
        set wwwPage=%wwwPage_js1%
)



if not [%2] == [] (
        echo %wwwPage%
    ) else (
        type "%wwwPage%"
    )

echo.

GOTO:EOF

:HELP
echo newpage 0
echo newpage 1
echo newpage 0 path
GOTO:EOF


 
