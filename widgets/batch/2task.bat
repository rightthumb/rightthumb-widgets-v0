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
 rem p cmd2table -print | p. printTable -sort image_name - svchost  + .exe %*  -aggregate " eot?mem-total=add( int(MEM_USAGE) )); format(eot?mem-total,?size,??kb);"
 p cmd2table -print | p. printTable -int mem_usage -sort mem_usage - svchost  + .exe %*  -aggregate " eot?mem-total=add( int(MEM_USAGE) )); format(eot?mem-total,?size,??kb);"