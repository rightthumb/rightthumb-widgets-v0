@echo off
setlocal

set obf_php=%ww%\obfuscators\php.php
set obf_py=%ww%\obfuscators\python.php
set obf_js=%ww%\obfuscators\javascript.php

if "%2"=="" (
    goto :HELP
)

if /i "%1"=="php" (
    php "%obf_php%" %2 %3
    goto :EOF
) else if /i "%1"=="py" (
    php "%obf_py%" %2 %3
    goto :EOF
) else if /i "%1"=="js" (
    php "%obf_js%" %2 %3
    goto :EOF
) else (
    goto :HELP
)

:HELP
echo.
echo Usage:
echo   obfuscate.bat ^<lang^> ^<input^> ^<output^>
echo.
echo Languages:
echo   php   - Obfuscate PHP and output eval(gzinflate(base64_decode(...)))
echo   py    - Obfuscate and output Python code using zlib + base64
echo   js    - Obfuscate and output JavaScript (requires pako for inflation)
echo.
echo Example:
echo   obfuscate.bat php script.php obf.php
echo   obfuscate.bat py script.py obf.py
echo   obfuscate.bat js script.js obf.js
echo.
exit /b 1
