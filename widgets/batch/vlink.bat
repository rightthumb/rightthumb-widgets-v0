@echo off
set sroot=%userprofile%\Favorites\Office\scripts\log
set p=%sroot%\script-bookmarks\BM-%1.txt
set /p back=<"%p%"
start explorer %back%
:END

