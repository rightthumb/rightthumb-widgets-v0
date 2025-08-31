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
	set /p cdf_path=<%tt%\file-open.last
) else (
	set cdf_path=%1
)

CALL p. popFile -f %cdf_path% > %tmpf%

rem echo 1 "%1"
SET /p folder=<%tmpf%
rem echo f "%folder%"
cd /d "%folder%"
rem %folder:~0,1%:
rem cd "%folder%"
echo %folder%
echo.