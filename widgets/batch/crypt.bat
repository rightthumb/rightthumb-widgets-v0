@echo off

SET fi=%1
SET entire=n

if [%2] == [-d] (
	call p. fileBackup -open -f %fi%
	call p. decrypt-docs -delete -f  %fi%
	call p. secureFiles -delete  -en -f  %fi%
	echo done
	GOTO:EOF
)

if [%2] == [-delete] (
	call p. fileBackup -open -f %fi%
	call p. secureFiles -delete  -en -f  %fi%
	call p. decrypt-docs -delete -f  %fi%
	echo done
	GOTO:EOF
)

if [%2] == [y] (
	CALL:ENTIRE
	GOTO:EOF
)

if [%2] == [-y] (
	CALL:ENTIRE
	GOTO:EOF
)
SET /p entire= encrypt entire file? 
if [%entire%] == [y] (
	CALL:ENTIRE
) else (
	CALL:PARTIAL
)
GOTO:EOF


:PARTIAL

echo PARTIAL selected
call p. secureFiles -delete  -en -f  %fi%
call p. decrypt-docs -f  %fi%
@REM call p. fileBackup -silent -flag lock -runonce -noschedule -f %fi%
call p. fileBackup  -flag lock -runonce -noschedule -f %fi%
echo partial encryption configured

rem if [%entire%] == [Y] (
rem 	CALL:ENTIRE %1
rem ) else (
rem 	echo PARTIAL selected
rem 	p decrypt-docs -f %1
rem 	echo partial encryption configured
rem )
GOTO:EOF

:ENTIRE
echo ENTIRE selected
call p. decrypt-docs -delete -f  %fi%
call p. secureFiles -en -f  %fi%
@REM call p. fileBackup -silent -flag lock -runonce -noschedule -f %fi%
call p. fileBackup  -flag lock -runonce -noschedule -f %fi%
echo entire-file encryption configured
GOTO:EOF
:ENTIRE2
echo works
GOTO:EOF