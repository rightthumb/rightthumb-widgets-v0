@echo off
call m back --c
if [%1] == [] (
	call b w > nul
) else (
	call b %1 > nul
)
call uuid -e > %tmpf%
SET /p uuid=<%tmpf%
git commit -m "%uuid%
git push --force









@echo off
SETLOCAL ENABLEEXTENSIONS

REM ====== CONFIGURATION ======
SET REPO_PATH=C:\path\to\rightthumb-widgets-v0
SET GIT_REMOTE=https://github.com/rightthumb/rightthumb-widgets-v0.git
SET BRANCH_NAME=main
REM ===========================

ECHO.
ECHO Resetting Git history in %REPO_PATH%
CD /D %REPO_PATH%

REM Make sure the path exists and is a Git repo
IF NOT EXIST .git (
	ECHO ERROR: Not a Git repository at %REPO_PATH%
	EXIT /B 1
)

REM Checkout orphan branch
git checkout --orphan latest_branch

REM You must have already staged files manually!
git commit -m "Reset to current state (manual add)"

REM Delete old branch
git branch -D %BRANCH_NAME%

REM Rename orphan to main
git branch -m %BRANCH_NAME%

REM Force push to GitHub
git remote set-url origin %GIT_REMOTE%
git push -f origin %BRANCH_NAME%

ECHO.
ECHO ✅ Git history reset complete.
ENDLOCAL










call b back > nul