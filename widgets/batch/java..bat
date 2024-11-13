@echo off
SETLOCAL

REM Compile Java file
echo Compiling Java files...
javac %1.java
if NOT %ERRORLEVEL% == 0 (
    echo Compilation failed.
    exit /b %ERRORLEVEL%
)

REM Create JAR file
echo Creating JAR file...
jar cvfm %1.jar Manifest.txt %1.class
if NOT %ERRORLEVEL% == 0 (
    echo Failed to create JAR file.
    exit /b %ERRORLEVEL%
)

echo Build Complete. %1.jar is ready.

REM Create application image
echo Creating application image...
mkdir app
move %1.jar app\
jpackage --type app-image --input app --name %1 --main-jar %1.jar --main-class %1 --temp temp-dir
if NOT %ERRORLEVEL% == 0 (
    echo Failed to create application image.
    exit /b %ERRORLEVEL%
)

echo Application image created successfully.

ENDLOCAL
