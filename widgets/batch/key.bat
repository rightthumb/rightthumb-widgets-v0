@echo off
setlocal enabledelayedexpansion

set key=%1
if [%key%] == [r] set "key=rightthumb@sullust.sds.sh"
if [%key%] == [rt] set "key=rightthumb@sullust.sds.sh"
if [%key%] == [s] set "key=softwaredev@sullust.sds.sh"
if [%key%] == [sw] set "key=softwaredev@sullust.sds.sh"
if [%key%] == [p] set "key=programmer@sullust.sds.sh"
if [%key%] == [pg] set "key=programmer@sullust.sds.sh"
if [%key%] == [e] set "key=ecoterm@sullust.sds.sh"
if [%key%] == [et] set "key=ecoterm@sullust.sds.sh"
if [%key%] == [py] set key=python

if "%~2"=="" (
	call p. keychain -temp 10 -get -label "!key!"
) else if "%~2"=="-crypt" (
	call p. keychain -get -label "!key!"
	call p. cryptString -en -clip
)

endlocal