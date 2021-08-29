@echo off
if [%1] == [] (
	%py%
) else (
	CALL p file -noext --c -folder %widgets%widgetspython + %*
)

rem @echo off
rem if [%1] == [] (
rem 	%py%
rem ) else if exist %widgets%widgetspython\%1.py (
rem 	set subject=%1
rem 	shift
rem 	%py% %widgets%widgetspython\%subject%.py %*
rem ) else (
rem 	CALL p file -noext --c -folder %widgets%widgetspython + %*
rem )

