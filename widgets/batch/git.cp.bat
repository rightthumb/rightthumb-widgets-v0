@echo off
setlocal enabledelayedexpansion

echo [INFO] Starting script...
echo [INFO] Refreshing working state...

call m back --c
echo [INFO] Returned from: call m back --c

if [%1] == [] (
    echo [INFO] No argument passed. Running: call b w
    call b w > nul
) else (
    echo [INFO] Argument passed: %1. Running: call b %1
    call b %1 > nul
)

echo [INFO] Generating UUID...
call uuid -e > %tmpf%
echo [INFO] Reading UUID from file: %tmpf%
SET /p uuid=<%tmpf%
echo [INFO] UUID generated: %uuid%

set AMENDED=false
echo [INFO] AMENDED initially set to false

REM [NEW] Check if anything is staged
git diff --cached --quiet
if %ERRORLEVEL% NEQ 0 (
    echo [INFO] Detected staged changes.
) else (
    echo [!] No staged changes detected. Skipping commit.
    goto end
)

echo [INFO] Checking for staged secrets...
git diff --cached | findstr /R "ghp_[A-Za-z0-9][A-Za-z0-9]*" > nul
if %ERRORLEVEL% EQU 0 (
    echo [!] Token detected in STAGED changes. Edit the file before continuing.
    pause
)

echo [INFO] Checking for secrets in commit history...
set FOUND=false
for /f %%i in ('git rev-list --all') do (
    git grep -q -E "ghp_[A-Za-z0-9]{36}" %%i >nul 2>nul
    if !ERRORLEVEL! EQU 0 (
        echo [!] Token detected in COMMIT HISTORY at commit: %%i
        set FOUND=true
        goto amend_commit
    )
)

:amend_commit
if "!FOUND!" == "true" (
    echo [INFO] Running: git commit --amend --no-edit
    git commit --amend --no-edit
    set AMENDED=true
    echo [INFO] AMENDED set to true
)

echo [INFO] Checking whether commit is needed...
if "!AMENDED!" == "false" (
    echo [INFO] Running: git commit -m "%uuid%"
    git commit -m "%uuid%"
)

echo [INFO] Running: git push --force
git push --force

:end
echo [INFO] Restoring shell...
call b back > nul

echo [DONE] Script complete.
