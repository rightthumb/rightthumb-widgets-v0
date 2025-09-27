@echo off
setlocal

REM Define the application name and main class
set APP_NAME=%1
set MAIN_CLASS=%1

REM Compile the Java file
echo Compiling Java file...
javac %APP_NAME%.java
if NOT %ERRORLEVEL% == 0 (
	echo Compilation failed.
	exit /b %ERRORLEVEL%
)

REM Create the JAR file
echo Creating JAR file...
jar cvfm %APP_NAME%.jar Manifest.txt %APP_NAME%.class
if NOT %ERRORLEVEL% == 0 (
	echo Failed to create JAR file.
	exit /b %ERRORLEVEL%
)

echo JAR build complete. %APP_NAME%.jar is ready.

REM Convert Windows path to WSL path for the current directory
set WSL_PATH=%CD%
set WSL_PATH=%WSL_PATH:\=/%
set WSL_PATH=${WSL_PATH:/:/mnt/}

REM Create the application image and package as .deb using WSL
echo Creating application image and packaging into .deb...
wsl bash -c "cd '%WSL_PATH%' && jpackage --type deb --input . --name '%APP_NAME%' --main-jar '%APP_NAME%.jar' --main-class '%MAIN_CLASS%' --dest dist --verbose"

if NOT %ERRORLEVEL% == 0 (
	echo Failed to create .deb package.
	exit /b %ERRORLEVEL%
)

echo .deb package created successfully. Check the 'dist' directory.

endlocal