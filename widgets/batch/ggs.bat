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

set ief=D:\Program Files\Internet Explorer
set ie=%ief%\IEXPLORE.EXE

"%ie%" "http://www.google.com/search?hl=en&btnG=Google+Search&q=%1"
if [%2] == [] GOTO END
"%ie%" "http://www.google.com/search?hl=en&btnG=Google+Search&q=%2"
if [%3] == [] GOTO END
"%ie%" "http://www.google.com/search?hl=en&btnG=Google+Search&q=%3"
if [%4] == [] GOTO END
"%ie%" "http://www.google.com/search?hl=en&btnG=Google+Search&q=%4"
if [%5] == [] GOTO END
"%ie%" "http://www.google.com/search?hl=en&btnG=Google+Search&q=%5"
if [%6] == [] GOTO END
"%ie%" "http://www.google.com/search?hl=en&btnG=Google+Search&q=%6"
if [%7] == [] GOTO END
"%ie%" "http://www.google.com/search?hl=en&btnG=Google+Search&q=%7"
if [%8] == [] GOTO END
"%ie%" "http://www.google.com/search?hl=en&btnG=Google+Search&q=%8"
if [%9] == [] GOTO END
"%ie%" "http://www.google.com/search?hl=en&btnG=Google+Search&q=%9"


:END