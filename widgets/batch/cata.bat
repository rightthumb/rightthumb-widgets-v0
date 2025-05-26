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

set cate_subject="%myBatch%\%1.bat"

rem #g) NEW   shift /1 + :getRemainingArgs
shift /1
set "remainingArgs="
:getRemainingArgs
if "%~1" neq "" (
  set ^"remainingArgs=%remainingArgs% %1"
  shift /1
  goto :getRemainingArgs
)
rem echo remainingArgs=%remainingArgs%


call cat %cate_subject% %remainingArgs%
rem echo %1
rem shift
rem echo %1
rem call cat %cate% 
