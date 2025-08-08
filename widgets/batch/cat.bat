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

if [%1] == [] (
	call p. cat
) else if [%1] == [-f] (
	shift
	call p. cat --c noline -f %*
) else (
	call p. cat --c noline -f %*
)

rem related to cat

rem if cat does not work
rem if cat does not work
rem if cat does not work
rem set file=%1
rem shift /1
rem set "remainingArgs="
rem :getRemainingArgs
rem if "%~1" neq "" (
rem   set ^"remainingArgs=%remainingArgs% %1"
rem   shift /1
rem   goto :getRemainingArgs
rem )
rem echo remainingArgs=%remainingArgs%
rem type %file% | p. line %remainingArgs%