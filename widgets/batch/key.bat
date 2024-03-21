@echo off
setlocal enabledelayedexpansion

set key=%1
if [%key%] == [r] set "key=rightthumb@yavin.m-eta.app"
if [%key%] == [rt] set "key=rightthumb@yavin.m-eta.app"
if [%key%] == [s] set "key=softwaredev@yavin.m-eta.app"
if [%key%] == [sw] set "key=softwaredev@yavin.m-eta.app"
if [%key%] == [p] set "key=programmer@yavin.m-eta.app"
if [%key%] == [pg] set "key=programmer@yavin.m-eta.app"
if [%key%] == [a] set "key=admin@tatooine.m-eta.app"
if [%key%] == [aa] set "key=admin@tatooine.m-eta.app"
if [%key%] == [py] set key=python

if "%~2"=="" (
    call p. keychain -temp -get -label "!key!"
) else if "%~2"=="-crypt" (
    call p. keychain -get -label "!key!"
    call p. cryptString -en -clip
)

endlocal
