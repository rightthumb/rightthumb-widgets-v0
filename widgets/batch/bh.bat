@echo off

if [%1] == [] (
	echo Please specify a file
	goto:eof
)

set should_build=y

if exist %1 set /p should_build= Replace ?:  

if [%should_build%] == [y] (
	type %widgets%\widgets\python\_rightThumb\_base3\_build-here_.py > %1
	echo. >> %1
	echo. >> %1
	if not [%2] == [] echo ########################### >> %1
	if not [%2] == [] echo ################################################## >> %1
	echo ######################################################################################## >> %1
	if not [%2] == [] echo ################################################## >> %1
	if not [%2] == [] echo ################################################## >> %1
	echo. >> %1
	echo. >> %1
	type %widgets%\widgets\python\_rightThumb\_base3\_base3_init_example.py >> %1
)
call n %1