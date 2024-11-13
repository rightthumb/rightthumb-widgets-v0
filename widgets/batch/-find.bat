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


:custom
set title=finding:   "%1"
set file=-find


:VAR___________________

set self=%systemroot%\system32\%file%.bat
set tmp=tmp.file.txt
cd > %tmp%
set /p folder=< %tmp%
:___________________


title Saly is %title% for %username%
cls
IF "%1" == "" GOTO END
:___________________
echo ===================
echo Sally is finding:  %1

echo ===================
IF "%1" == "w" GOTO WILD
dir /s/b %1
echo Sally Found this in %folder%
echo ___________________

pause
GOTO END
:WILD
dir /s/b *%1*
echo Sally Found this in %folder%
echo --
echo ___________________

pause
GOTO END


___________________
:edit
notepad "%self%"
GOTO END
___________________
:view
type "%self%"
GOTO END
___________________

:END


title Sally says: How can I help you %username%
cls
echo dir /s/b *

 
