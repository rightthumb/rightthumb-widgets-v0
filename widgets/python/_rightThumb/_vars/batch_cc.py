import os.path 
def GENERATE_FILE(home):
	
	fileName = home + _v.slash+'cc.bat'


	fileData = """




@echo off

set /p shouldRun=Run? 

IF [%shouldRun%] == [n] GOTO:END
IF [%shouldRun%] == [N] GOTO:END
IF [%shouldRun%] == [NO] GOTO:END
IF [%shouldRun%] == [no] GOTO:END
IF [%shouldRun%] == [c] GOTO:END


:RUN
SET /p Drive=<%userprofile%\\.tk421
SET techDrive=%Drive:~0,1%
SET scriptDrive=%Drive:~0,1%
SET Drive=
rem echo %techDrive%
echo Loading...


IF NOT EXIST %techDrive%:\\ (CALL:ERROR)
IF EXIST %techDrive%:\\ (CALL:START)
GOTO:END
:ERROR
prompt - 
cls
IF [] == [y] GOTO END
echo USB Drive Failure
SET errorDisplayOnce=y
GOTO END
:START
call %techDrive%:\\tech\\programs\\batch\\resetVars.bat
SET /p Drive=<%userprofile%\\.tk421
SET techDrive=%Drive:~0,1%
call %techDrive%:\\tech\\programs\\batch\\c.bat %1 
GOTO END
:END
cls
GOTO:EOF


	



	

	



	"""


	if not os.path.isfile( fileName ):
		open(fileName,'w', encoding='utf-8').write(fileData)
