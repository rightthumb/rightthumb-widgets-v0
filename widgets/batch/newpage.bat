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



if [%1] == [] (
	call p. newpage
	goto:eof
)

call runSet isSwitch %*

if [%runSet%] == [true] (
	call p. newpage %*
) else (
	call p. newpage -t %*
)
goto:eof



rem set wwwPage_0=D:\techApps\Library\WEB\newpage\blank0.htm
rem set wwwPage_1=D:\techApps\Library\WEB\newpage\blank1.htm
set wwwPage_F=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html
rem set wwwPage_h=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\headers.htm
set wwwPage_php=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\php.php
set wwwPage_h=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\headers.php
set wwwPage_01=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\0.1.htm
set wwwPage_0=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\0.htm
set wwwPage_1=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\1.htm
set wwwPage_2=D:\techApps\Library\WEB\newpage\blank2.htm
set wwwPage_3=D:\techApps\Library\WEB\newpage\blank3.htm
set wwwPage_4=D:\techApps\Library\WEB\newpage\blank4.htm
set wwwPage_js1=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\js.js
set wwwPage_template=D:\websites\domains\apps.eyeformeta.com\public_html\templates\html\template.htm
set "newpage="
if ["%1"] == ["?"] (
	call :HELP
	GOTO:EOF
	)

rem o html0 %wwwPage_01%
rem o html.0 %wwwPage_01%
rem o html1 %wwwPage_1%
rem o html.1 %wwwPage_1%
rem o html2 %wwwPage_2%
rem o html.2 %wwwPage_2%
rem o html3 %wwwPage_3%
rem o html.3 %wwwPage_3%
rem o html4 %wwwPage_4%
rem o html.4 %wwwPage_4%
rem o html.js %wwwPage_js1%


if [%1] == [] (
	set wwwPage=%wwwPage_0%
) else if [%1] == [php] (
	set wwwPage=%wwwPage_php%
) else if [%1] == [t] (
	set wwwPage=%wwwPage_template%
) else if [%1] == [headers] (
	set wwwPage=%wwwPage_h%
) else if [%1] == [header] (
	set wwwPage=%wwwPage_h%
) else if [%1] == [head] (
	set wwwPage=%wwwPage_h%
) else if [%1] == [h] (
	set wwwPage=%wwwPage_h%
) else if [%1] == [0] (
	set wwwPage=%wwwPage_01%
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
) else (
	set wwwPage=%wwwPage_F%\%1
)

set "newpage=%wwwPage%"

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