@echo off
rem https://superuser.com/questions/743197/how-to-shift-all-parameters-in-a-batch
shift /1

set "remainingArgs="
:getRemainingArgs
if "%~1" neq "" (
  set ^"remainingArgs=%remainingArgs% %1"
  shift /1
  goto :getRemainingArgs
)
echo remainingArgs=%remainingArgs%