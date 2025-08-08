@echo off 

rem shift /1

set "remainingArgs="
:getRemainingArgs
if "%~1" neq "" (
  set ^"remainingArgs=%remainingArgs% %1"
  shift /1
  goto :getRemainingArgs
)
rem echo remainingArgs=%remainingArgs%

call p. bot -r "%remainingArgs%"