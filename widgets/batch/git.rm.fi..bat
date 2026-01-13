@echo off
REM =====================================================
REM Delete a file from Git repo (working tree + history)
REM =====================================================

REM >>>> SET YOUR FILE PATH HERE (relative to repo root) <<<<

if  [%1] == [?] (
	echo git.rm.fi. --
	goto :eof
)

if  [%1] == [--] (

REM Step 3: Commit the change
git commit -m "Remove %TARGET_FILE% from repo"

REM Step 4: Force-push to remote
git push origin --force --all
git push origin --force --tags

REM Step 5: Clean up old objects
git reflog expire --expire=now --all
git gc --prune=now --aggressive

)

set TARGET_FILE=%1

echo.
echo === Removing file: %TARGET_FILE% ===
echo.

REM Make sure git-filter-repo is available
where git-filter-repo >nul 2>nul
if errorlevel 1 (
	echo ERROR: git-filter-repo not found. Install with:
	echo   pip install git-filter-repo
	exit /b 1
)

REM Step 1: Rewrite repo history (removes from all commits)
git filter-repo --path "%TARGET_FILE%" --invert-paths

REM Step 2: Remove from current working tree
git rm -f --cached "%TARGET_FILE%"
if exist "%TARGET_FILE%" del /f /q "%TARGET_FILE%"





echo.
echo === Done. File '%TARGET_FILE%' fully removed ===
echo.