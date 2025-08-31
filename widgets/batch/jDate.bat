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

:JDate
:: Convert date to Julian
:: Arguments : YYYY MM DD
:: Returns   : Julian date
::
:: First strip leading zeroes
SET shouldEcho=false
if ["%4"] == ["print"] SET shouldEcho=true
if ["%1"] == ["print"] SET shouldEcho=true



if [%3] == [] (
	SET YYYY=%date:~-4,4%
	SET MM=%date:~-10,2%
	SET DD=%date:~-7,2%
) else (
	SET YYYY=%1
	SET MM=%2
	SET DD=%3
)


IF %MM:~0,1% EQU 0 SET MM=%MM:~1%
IF %DD:~0,1% EQU 0 SET DD=%DD:~1%
::
:: Algorithm based on Fliegel-Van Flandern
:: algorithm from the Astronomical Almanac,
:: provided by Doctor Fenton on the Math Forum
:: (http://mathforum.org/library/drmath/view/51907.html),
:: and converted to batch code by Ron Bakowski.
SET /A Month1 = ( %MM% - 14 ) / 12
SET /A Year1  = %YYYY% + 4800
SET /A JDate  = 1461 * ( %Year1% + %Month1% ) / 4 + 367 * ( %MM% - 2 -12 * %Month1% ) / 12 - ( 3 * ( ( %Year1% + %Month1% + 100 ) / 100 ) ) / 4 + %DD% - 32075
SET Month1=
SET Year1=
SET YYYY=
SET MM=
SET DD=

if [%shouldEcho%] == [true] ECHO %JDate%
SET shouldEcho=
GOTO:EOF