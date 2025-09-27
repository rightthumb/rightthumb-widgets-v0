@echo off 

call p. file -folder %python%  -noext + *.py %*


@REM call p. cat -f *.php + exec( | call p. pipe-split -dirty + .py --c