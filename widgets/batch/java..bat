@echo off

SETLOCAL

echo Compiling Java files...
javac %1.java
if %errorlevel% neq 0 (
    echo Compilation failed.
    exit /b %errorlevel%
)

echo Creating JAR file...
jar cvfm %1.jar Manifest.txt %1.class
if %errorlevel% neq 0 (
    echo Failed to create JAR file.
    exit /b %errorlevel%
)
echo Build Complete. %1.jar is ready.

jpackage --type app-image --input . --name %1 --main-jar %1.jar --main-class %1
if %errorlevel% neq 0 (
    echo Failed to create JAR file.
    exit /b %errorlevel%
)
ENDLOCAL
pause
