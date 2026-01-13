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

rem tasklist | f %1

tasklist | p tasklist2table     -s Name MemUsage -g Name -gt MemUsage -aggregate " eot?mem-total=add( int(MemUsage) )); format(eot?mem-total,?size,??kb);" %*
