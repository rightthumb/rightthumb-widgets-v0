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

if [%1] == [] GOTO END
if [%2] == [] GOTO END
set eventid=%1
set source=%2
if not [%3] == [] set source=%2 %3

start "%USERPROFILE%\AppData\Local\Google\Chrome\Application\chrome.exe" "http://www.eventid.net/display.asp?eventid=%eventid%&eventno=1274&source=%source%&phase=1"

:END