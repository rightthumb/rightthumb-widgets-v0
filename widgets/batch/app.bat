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


if [%1] == [] call:searchAppRegistrationInfo %*
if [%1] == [id] goto:appID
if [%1] == [a] goto:appID
if [%1] == [i] goto:appID
if [%1] == [p] goto:appID


goto:searchAppRegistrationInfo
goto:eof
:appID
call p. nID -app
rem call p. ago -f app
goto:eof
:searchAppRegistrationInfo
p searchAppRegistrationInfo %*
goto:eof
 
