@echo off
setlocal enabledelayedexpansion

echo [INFO] Starting aggressive git force-push script...
echo [INFO] Refreshing working state...

REM ---------- Configuration ----------
set MAX_RETRIES=3
set RETRY_DELAY=5
set BRANCH=main
set REMOTE=origin
set UUID_FILE=%TEMP%\_git_push_uuid.txt
set SCAN_TOKENS=true

REM ---------- Parse Arguments ----------
:parse_args
if "%~1"=="" goto args_done

if /I "%~1"=="--branch" (
	shift
	set "BRANCH=%~1"
	shift
	goto parse_args
)

if /I "%~1"=="--remote" (
	shift
	set "REMOTE=%~1"
	shift
	goto parse_args
)

if /I "%~1"=="--no-scan" (
	set "SCAN_TOKENS=false"
	shift
	goto parse_args
)

if /I "%~1"=="--retries" (
	shift
	set "MAX_RETRIES=%~1"
	shift
	goto parse_args
)

echo [WARN] Unknown argument: %~1
shift
goto parse_args

:args_done

REM ---------- Helper Functions ----------
:refresh_shell
echo [INFO] Refreshing shell environment...
call m back --c >nul 2>&1
if [%1] == [] (
	call b w --c >nul 2>&1
) else (
	call b %1 --c >nul 2>&1
)
exit /b 0

:generate_uuid
setlocal
set "uuid="
for /f "delims=" %%i in ('powershell -Command "[guid]::NewGuid().ToString()" 2^>nul') do set "uuid=%%i"
if not defined uuid (
	set /a "rand1=!random! * 100000 + !random!"
	set /a "rand2=!random! * 100000 + !random!"
	set "uuid=force-!rand1!!rand2!"
)
endlocal & set "uuid=%uuid%"
exit /b 0

:check_secrets
setlocal
echo [INFO] Scanning for potential secrets in staged changes...
git diff --cached | findstr /R /C:"ghp_[A-Za-z0-9][A-Za-z0-9]*" /C:"gho_[A-Za-z0-9][A-Za-z0-9]*" /C:"ghu_[A-Za-z0-9][A-Za-z0-9]*" /C:"ghs_[A-Za-z0-9][A-Za-z0-9]*" /C:"ghr_[A-Za-z0-9][A-Za-z0-9]*" > nul
if !errorlevel! equ 0 (
	echo [ERROR] Potential GitHub token detected in staged changes! Aborting for security.
	exit /b 1
)
endlocal
exit /b 0

:force_push
setlocal
set /a attempt=0
set push_success=0

:push_retry
set /a attempt+=1
echo [INFO] Force push attempt !attempt! of %MAX_RETRIES%...

REM Try multiple push strategies with increasing aggression
git push --force-with-lease %REMOTE% %BRANCH% >nul 2>&1
if !errorlevel! equ 0 (
	set push_success=1
	goto push_result
)

git push --force %REMOTE% %BRANCH% >nul 2>&1
if !errorlevel! equ 0 (
	set push_success=1
	goto push_result
)

REM If still failing, try to delete and recreate the branch (nuclear option)
if !attempt! equ %MAX_RETRIES% (
	echo [WARN] Standard push methods failed, trying nuclear option...
	git push --delete %REMOTE% %BRANCH% >nul 2>&1
	timeout /t 2 >nul
	git push -u %REMOTE% %BRANCH% >nul 2>&1
	if !errorlevel! equ 0 set push_success=1
)

if !push_success! equ 0 (
	if !attempt! lss %MAX_RETRIES% (
		echo [WARN] Push failed, retrying in %RETRY_DELAY% seconds...
		timeout /t %RETRY_DELAY% >nul
		goto push_retry
	)
)

:push_result
endlocal & set push_success=%push_success%
exit /b %push_success%

REM ---------- Main Execution ----------
call :refresh_shell %1

REM Check if we're in a git repository
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
	echo [ERROR] Not a git repository
	goto cleanup
)

REM Ensure we're on the correct branch
git checkout %BRANCH% >nul 2>&1
if errorlevel 1 (
	echo [INFO] Creating branch %BRANCH%
	git checkout -b %BRANCH% >nul 2>&1
	if errorlevel 1 (
		echo [ERROR] Failed to create branch %BRANCH%
		goto cleanup
	)
)

REM Stage all changes
echo [INFO] Staging all changes...
git add --all >nul 2>&1

REM Check for changes
git diff --cached --quiet >nul 2>&1
if errorlevel 1 (
	echo [INFO] Changes detected, proceeding with commit
) else (
	echo [INFO] No changes to commit, creating empty commit to ensure push
	git commit --allow-empty -m "Empty commit to maintain branch" >nul 2>&1
	goto push
)

REM Security check for tokens
if "%SCAN_TOKENS%"=="true" (
	call :check_secrets
	if errorlevel 1 goto cleanup
)

REM Generate commit message
call :generate_uuid
set "commit_msg=Force push: %uuid%"

REM Commit changes
echo [INFO] Committing changes...
git commit -m "%commit_msg%" >nul 2>&1
if errorlevel 1 (
	echo [ERROR] Commit failed
	goto cleanup
)

:push
REM Force push with retry logic
call :force_push
if errorlevel 1 (
	echo [ERROR] All push attempts failed
	goto cleanup
)

echo [SUCCESS] Force push completed successfully!

:cleanup
REM Clean up temporary files
if exist "%UUID_FILE%" del "%UUID_FILE%" >nul 2>&1

REM Restore shell environment
call :refresh_shell %1

echo [DONE] Script execution complete.
exit /b 0