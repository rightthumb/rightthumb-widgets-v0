@echo off
setlocal enabledelayedexpansion


:: ===============================
:: Validate arguments
:: ===============================
if "%2" == "" (
    echo [!] Missing arguments.
    echo Usage: create_repo.bat <github_user> <repo_name>
    exit /b 1
)

:: ===============================
:: Backup current PATH
:: ===============================
set path_backup=%PATH%


:: ===============================
:: ARGUMENTS
:: ===============================
set "GITHUB_USER=%1"
set "REPO_NAME=%2"

if "%GITHUB_USER%"=="" (
    echo [!] Missing GitHub username.
    echo Usage: create_repo.bat <github_user> <repo_name>
    exit /b 1
)

if "%REPO_NAME%"=="" (
    echo [!] Missing repository name.
    echo Usage: create_repo.bat <github_user> <repo_name>
    exit /b 1
)

:: ===============================
:: Git-safe PATH setup
:: ===============================
set "REPO_TEMP_PATH=%userprofile%\.rt\profile\temp\REPO_PATH.txt"

echo [*] Preparing Git-safe PATH
call p. osPath -repo pre > "%REPO_TEMP_PATH%"
set /p CLEAN_PATH=<"%REPO_TEMP_PATH%"
set "PATH=%CLEAN_PATH%"

:: ===============================
:: Create and initialize repo
:: ===============================
echo [*] Cloning GitHub repo: https://github.com/%GITHUB_USER%/%REPO_NAME%.git

mkdir "%REPO_NAME%"
cd "%REPO_NAME%"
git init
git remote add origin https://github.com/%GITHUB_USER%/%REPO_NAME%.git
echo "# %REPO_NAME%" > README.md
git add .
git commit -m "Initial commit"
git push -u origin main

:: ===============================
:: Restore PATH
:: ===============================
cd
cd ..
cd

echo [*] Restoring original PATH
set PATH=%path_backup%

echo [✔] Repo created and PATH restored.
endlocal
