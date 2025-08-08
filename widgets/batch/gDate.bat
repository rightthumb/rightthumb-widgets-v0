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


:GDate
:: Convert Julian date back to "normal" Gregorian date
:: Argument : Julian date
:: Returns  : YYYY MM DD
::
:: Algorithm based on Fliegel-Van Flandern
:: algorithm from the Astronomical Almanac,
:: provided by Doctor Fenton on the Math Forum
:: (http://mathforum.org/library/drmath/view/51907.html),
:: and converted to batch code by Ron Bakowski.
::
SET shouldPrint=false
CALL :SHOULDPRINT %*
CALL :JULIAN %*
CALL :CONVERTDATE


SET julian=

rem CALL jDate
rem SET julian=%jDate%




GOTO:EOF

:JULIAN
IF ["%1"] == ["print"] SHIFT
IF [%1] == [] (
	CALL jDate
	SET julian=%jDate%
) ELSE IF ["%1"] == ["print"] (
	CALL jDate
	SET julian=%jDate%
) ELSE (
	SET julian=%1
)

GOTO:EOF

:SHOULDPRINT
IF ["%1"] == ["print"] SET shouldPrint=true
IF ["%2"] == ["print"] SET shouldPrint=true
GOTO:EOF


GOTO:EOF
:CONVERTDATE
SET /A P      = %julian% + 68569
SET /A Q      = 4 * %P% / 146097
SET /A R      = %P% - ( 146097 * %Q% +3 ) / 4
SET /A S      = 4000 * ( %R% + 1 ) / 1461001
SET /A T      = %R% - 1461 * %S% / 4 + 31
SET /A U      = 80 * %T% / 2447
SET /A V      = %U% / 11
SET /A GYear  = 100 * ( %Q% - 49 ) + %S% + %V%
SET /A GMonth = %U% + 2 - 12 * %V%
SET /A GDay   = %T% - 2447 * %U% / 80
:: Clean up the mess
FOR %%A IN (P Q R S T U V) DO SET %%A=
:: Add leading zeroes
IF 1%GMonth% LSS 20 SET GMonth=0%GMonth%
IF 1%GDay%   LSS 20 SET GDay=0%GDay%
:: Return value
SET gDate2=%GYear% %GMonth% %GDay%
SET gDate=%GYear%/%GMonth%/%GDay%
IF [%shouldPrint%] == [true] ECHO %GDate%
SET shouldPrint=
SET julian=
GOTO:EOF