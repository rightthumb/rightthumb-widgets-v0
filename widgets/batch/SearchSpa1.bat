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

set thisFile=spa_live.php

set search=
if ["%1"]==[""] GOTO END
if ["%2"]==[""] GOTO ONE
if ["%3"]==[""] GOTO TWO
if ["%4"]==[""] GOTO THREE
if ["%5"]==[""] GOTO FOUR
if ["%6"]==[""] GOTO FIVE
if ["%7"]==[""] GOTO SIX
if ["%8"]==[""] GOTO SEVEN
if ["%9"]==[""] GOTO EIGHT

:NINE
set search=%1 %2 %3 %4 %5 %6 %7 %8 %9
GOTO START
:EIGHT
set search=%1 %2 %3 %4 %5 %6 %7 %8
GOTO START
:SEVEN
set search=%1 %2 %3 %4 %5 %6 %7
GOTO START
:SIX
set search=%1 %2 %3 %4 %5 %6
GOTO START
:FIVE
set search=%1 %2 %3 %4 %5
GOTO START
:FOUR
set search=%1 %2 %3 %4
GOTO START
:THREE
set search=%1 %2 %3
GOTO START
:TWO
set search=%1 %2
GOTO START
:ONE
set search=%1
GOTO START

:START
cls
%php% %phpFiles%\%thisFile%
echo.
:END