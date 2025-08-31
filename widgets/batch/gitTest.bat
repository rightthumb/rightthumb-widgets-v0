@echo off

:: ===============================
:: Set variables
:: ===============================
set path_backup=%PATH%
set "REPO_TEMP_PATH=%userprofile%\.rt\profile\temp\REPO_PATH.txt"

:: ===============================
:: Alter PATH for Git-safe operations
:: ===============================
%py% %python%\script-helper.py -color yellow     Alter PATH for Git-safe operations
call p. osPath -repo pre > "%REPO_TEMP_PATH%"
set /p CLEAN_PATH=<"%REPO_TEMP_PATH%"
set "PATH=%CLEAN_PATH%"
del "%REPO_TEMP_PATH%"

:: ===============================
:: Test PATH alteration
:: ===============================
%py% %python%\script-helper.py -color yellow     Test PATH alteration
@echo on
where p
@echo off

:: ===============================
:: Restore original PATH
:: ===============================
%py% %python%\script-helper.py -color yellow     Restore original PATH
set PATH=%path_backup%

:: ===============================
:: Test PATH alteration
:: ===============================
%py% %python%\script-helper.py -color yellow     Test PATH alteration
@echo on
where p

@echo off

call p. script-helper -color green    Everything is OK