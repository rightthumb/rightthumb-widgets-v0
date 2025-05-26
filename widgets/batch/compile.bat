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

CALL m back

SET appServer="%widgets%\widgets\databank\tables\appServer.txt"
SET appServerFiles="%widgets%\widgets\databank\tables\appServerFiles.txt"
SET appServerCompiledUnix=%widgets%\widgets\python\compiled\unix
SET appServerCompiledWin=%widgets%\widgets\python\compiled\windows
SET appServerCC=%userprofile%\cc.bat
SET appServerSrcWin=%widgets%\widgets\python\_rightThumb
SET appServerPython=%widgets%\widgets\python
SET appServerKeySub=%widgets%\widgets\keys\sublime.txt
SET appServerPro=%widgets%\widgets

SET appServerTechApps=%widgets%\techApps

ECHO %appServerTechApps%\KeePass-2.45\Database.kdbx> %appServerFiles%

IF NOT [%1] == [] (



    ECHO %appServerTechApps%\7-Zip>> %appServerFiles%
    ECHO %appServerTechApps%\KeePass-2.45>> %appServerFiles%
    ECHO %appServerTechApps%\chrome-win>> %appServerFiles%
    ECHO %appServerTechApps%\sublime>> %appServerFiles%
    ECHO %appServerTechApps%\ProcessMonitor>> %appServerFiles%
    ECHO %appServerTechApps%\tools\HijackThisPortable_2.0.5_English.paf.exe>> %appServerFiles%
    ECHO %appServerTechApps%\tools\CCleaner_Portable.zip>> %appServerFiles%
    ECHO %appServerTechApps%\tools\revo.exe>> %appServerFiles%
    ECHO %appServerTechApps%\tools\putty.exe>> %appServerFiles%
    ECHO %appServerTechApps%\tools\Tcpview.exe>> %appServerFiles%
    ECHO %appServerTechApps%\tools\NetInfo>> %appServerFiles%
    ECHO %appServerTechApps%\tools\PC-Audit>> %appServerFiles%
    ECHO %appServerTechApps%\_stand_alone\WirelessKeyView>> %appServerFiles%
    ECHO %appServerTechApps%\_stand_alone\NetBrute.exe>> %appServerFiles%
    ECHO %appServerTechApps%\_stand_alone\WinRAR.zip>> %appServerFiles%
    ECHO %appServerTechApps%\_stand_alone\Debuggers.zip>> %appServerFiles%
    ECHO %appServerPro%\databank>> %appServerFiles%
    rem ECHO %appServerPro%\exe>> %appServerFiles%
    ECHO %appServerPro%\webApp>> %appServerFiles%


)

IF [%1] == [] (
    ECHO %appServerPro%\exe\exe>> %appServerFiles%
    ECHO %appServerPro%\databank\tables>> %appServerFiles%


    ECHO %appServerCC%>> %appServerFiles%
    ECHO %appServerCompiledUnix%>> %appServerFiles%
    ECHO %appServerCompiledWin%>> %appServerFiles%
    ECHO %appServerSrcWin%>> %appServerFiles%
    ECHO %appServerKeySub%>> %appServerFiles%
    ECHO %appServerPython%\src>> %appServerFiles%
    ECHO %appServerPython%\imploded\unix>> %appServerFiles%
    ECHO %appServerPython%\imploded\windows>> %appServerFiles%


    ECHO %appServerPro%\bash>> %appServerFiles%
    ECHO %appServerPro%\batch>> %appServerFiles%

    ECHO %appServerPro%\powershell>> %appServerFiles%
    ECHO %appServerPro%\html>> %appServerFiles%
    ECHO %appServerPro%\php>> %appServerFiles%
    ECHO %appServerPro%\javascript>> %appServerFiles%
    ECHO %appServerPro%\keys>> %appServerFiles%
)







CALL p. unix

CALL b pysw
rem type %appServer% | p. path -valid >> %appServerFiles%
type %appServer% | p. inline -make " p implode -f {}" | p. execute
rem CALL p. file --c + *.py | p. inline -make " p implode -f {}" | p. execute

CALL b pysu
rem type %appServer% | p. path -valid >> %appServerFiles%
type %appServer% | p. inline -make " p implode -f {}" | p. execute
rem CALL p. file --c + *.py | p. inline -make " p implode -f {}" | p. execute
rem CALL b pyc
rem CALL p. appServer -crypt en 

SET shouldRun=NO
SET /p shouldRun=Upload? 
IF [%shouldRun%] == [y] GOTO:RUN

GOTO:END
:RUN
echo.
echo.
type %appServerFiles% | p. appServer -crypt en 
GOTO:END
:END
rem SET "appServer="
SET "appServerFiles="
SET "appServerCompiledUnix="
SET "appServerCompiledWin="
SET "appServerCC="
SET "appServerSrcWin="
SET "appServerKeySub="
SET "appServerPro="
SET "appServerTechApps="
SET "appServerPython="



SET appServerHelper=%widgets%\widgets\python\appServerHelper.py
SET appServerBlank=%widgets%\widgets\python\blank.txt
SET appServerUnix=%widgets%\widgets\python\imploded\unix\appServer.py
SET appServerWin=%widgets%\widgets\python\imploded\windows\appServer.py
SET serverNumber=D:\_Scott\S_Documents\Sites\RephRecruiting\projects\lynx\number
SET serverWin=D:\_Scott\S_Documents\Sites\RephRecruiting\projects\lynx\number\appServer.win
SET serverUnix=D:\_Scott\S_Documents\Sites\RephRecruiting\projects\lynx\number\appServer.unix

IF EXIST %serverNumber% GOTO:RUN2

GOTO:END2
:RUN2
GOTO:END2

CALL b lynx
IF EXIST appServer.win  rmdir /s /q appServer.win
IF EXIST appServer.unix rmdir /s /q appServer.unix
mkdir appServer.unix
mkdir appServer.win

xcopy /y %appServerHelper% %serverWin%\
xcopy /y %appServerHelper% %serverUnix%\

xcopy /y %appServerBlank% %serverUnix%\
xcopy /y %appServerBlank% %serverWin%\

xcopy /y %appServerUnix% %serverUnix%\
xcopy /y %appServerWin% %serverWin%\

CALL b appServer.unix
%py% appServerHelper.py en appServer.py appServer.unix
del appServer.py
CALL b appServer.win
%py% appServerHelper.py en appServer.py appServer.win
del appServer.py
cd ..
IF EXIST appServer.win.zip  del appServer.win.zip
IF EXIST appServer.unix.zip del appServer.unix.zip
CALL ## %widgets%\widgets\batch\zipTerminal.bat win
CALL ## %widgets%\widgets\batch\zipTerminal.bat unix
SET /p pause=pause: 
rem zip appServer.win appServer.win
rem zip appServer.unix appServer.unix
IF EXIST appServer.win  rmdir /s /q appServer.win
IF EXIST appServer.unix rmdir /s /q appServer.unix

GOTO:END2

:END2
SET "appServerHelper="
SET "appServerBlank="
SET "appServerUnix="
SET "appServerWin="
SET "serverWin="
SET "serverUnix="
SET "serverNumber="

CALL b back


 
