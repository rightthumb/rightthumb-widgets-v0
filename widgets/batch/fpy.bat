@echo off

rem CALL p f -in %widgets%\widgets\python\*.py -jn  - #  + %*

CALL p files -folder %widgets%\widgets\python\ + *.py | p f -jn  - #  + %*

