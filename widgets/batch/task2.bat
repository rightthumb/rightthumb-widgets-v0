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

if [%1] == [-report] (
	p cmd2table -print | p. printTable -int mem_usage -s image_name d.mem_usage -g image_name -gt mem_usage
) else ( 
	p cmd2table -print | p. printTable -sort image_name - svchost -s image_name + .exe %*  -aggregate " eot?mem-total=add( int(MEM_USAGE) )); format(eot?mem-total,?size,??kb);"
)