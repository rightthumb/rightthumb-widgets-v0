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


IF [%1] == [l] (start "" notepad %scriptroot%\Docs\HijackThis_Whitelist.txt)
IF [%1] == [list] (type %scriptroot%\Docs\HijackThis_Whitelist.txt)
IF [%1] == [g] (call HijackThisLog)
IF [%1] == [gen] (call HijackThisLog)
IF [%1] == [generate] (call HijackThisLog)
IF [%1] == [n] (GOTO NEW)
IF [%1] == [h] (GOTO HELP)
IF [%1] == [/?] (GOTO HELP)
GOTO END

:NEW
IF [%2] == [] GOTO NEWITEM
echo %2>> %scriptroot%\Docs\HijackThis_Whitelist.txt
GOTO END
:NEWITEM
set /p n=Whitelist Item: 
IF [%code_editor%] == [](GOTO END)
echo %code_editor%>> %scriptroot%\Docs\HijackThis_Whitelist.txt
GOTO END
:HELP
echo l list
echo g generate cmd
echo n new
GOTO END
:END