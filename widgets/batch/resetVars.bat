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

SET /p Drive=<%userprofile%\.tk421
SET widgets=%Drive:~0,1%

reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path | %PY% "%widgets%\widgets\python\regKeyClean.py" > %widgets%\widgets\batch\originalPath.bat
CALL %widgets%\widgets\batch\originalPath.bat

SET widgets=
SET Drive=
SET api=
SET batch=
SET cID=
SET computername2=
SET contextTemp=
SET DD=
SET dID=
SET dircache=
SET dircachep=
SET DriverData=
SET widgets=
SET exe=
SET FF=
SET hack=
SET hacks=
SET HH=
SET hostDefault=
SET i=
SET idea=
SET ideas=
SET installID=
SET isAdmin=
SET LastID=
SET mcData=
SET mData=
SET mdt=
SET MI=
SET mID=
SET MM=
SET myBatch=
SET myBookmarks=
SET myDatabases=
SET myHome=
SET myImports=
SET myIndexes=
SET myInfo=
SET myNotes=
SET myPhp=
SET myPowershell=
SET myPrograms=
SET myProjects=
SET myPython=
SET myTables=
SET myTickets=
SET myTxt=
SET myVars=
SET myWebApp=
SET n=
SET n2=
SET n=
SET now=
SET OneDrive=
SET OneDriveConsumer=
SET open=
SET open_timestamp=
SET originalPath=
SET OS=
SET PATHEXT=
SET percent=
SET percentage=
SET php=
SET php2=
SET widgets=
SET phpFiles=
SET pip=
SET powershell=
SET privID=
SET programs=
SET PROMPT=
SET ps=
SET pubID=
SET PUBLIC=
SET py=
SET py2=
SET python=
SET qi=
SET quote=
SET widgets=
SET scriptroot=
SET SESSIONNAME=
SET Session_ID=
SET SS=
SET stmp=
SET widgets=
SET widgets=
SET theEcho=
SET thisHost=
SET timestamp=
SET timestamp_start=
SET tmpf=
SET tmpf0=
SET tmpf1=
SET tmpf2=
SET tmpf3=
SET tmpf4=
SET tmpf5=
SET tmpf6=
SET tmpf7=
SET tmpf8=
SET tmpf9=
SET tmpfl=
SET today=
SET todo=
SET todoo=
SET ts=
SET webapp=
SET YYYY=
SET back=
SET bname=
%USERPROFILE:~0,1%:
cd %USERPROFILE%