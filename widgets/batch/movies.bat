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

rem CALL p dir -cache %mData% -movietitle -movies  - 24    %*
type  %tmpf0%-franchise  | p. cmd2table -print | p. printTable -g first second -s first second label
rem type  %tmpf0%-franchise-marvel  | p. cmd2table -print | p. printTable -g first second -s first second label
 
rem p dir -cache %mData% -movietitle -movies -franchise marvel