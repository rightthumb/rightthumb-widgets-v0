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









@REM @echo off
@REM SETLOCAL ENABLEEXTENSIONS

@REM REM ====== CONFIGURATION ======
@REM SET REPO_PATH=C:\path\to\rightthumb-widgets-v0
@REM SET GIT_REMOTE=https://github.com/rightthumb/rightthumb-widgets-v0.git
@REM SET BRANCH_NAME=main
@REM REM ===========================

@REM ECHO.
@REM ECHO Resetting Git history in %REPO_PATH%
@REM CD /D %REPO_PATH%

@REM REM Make sure the path exists and is a Git repo
@REM IF NOT EXIST .git (
@REM     ECHO ERROR: Not a Git repository at %REPO_PATH%
@REM     EXIT /B 1
@REM )

@REM REM Checkout orphan branch
@REM git checkout --orphan latest_branch

@REM REM You must have already staged files manually!
@REM git commit -m "Reset to current state (manual add)"

@REM REM Delete old branch
@REM git branch -D %BRANCH_NAME%

@REM REM Rename orphan to main
@REM git branch -m %BRANCH_NAME%

@REM REM Force push to GitHub
@REM git remote set-url origin %GIT_REMOTE%
@REM git push -f origin %BRANCH_NAME%

@REM ECHO.
@REM ECHO ✅ Git history reset complete.
@REM ENDLOCAL










call b back > nul
