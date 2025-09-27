@echo off
REM =====================================================
REM Delete a folder from Git repo (working tree + history)
REM =====================================================

REM >>>> SET YOUR FOLDER PATH HERE (relative to repo root) <<<<
set TARGET=%1

echo Confirm, delete "%TARGET%" RECURSIVELY ??
set "shouldRun="
set /p shouldRun=Run? (YES/):
if not [%shouldRun%] == [YES] goto :eof

echo.
echo === Removing folder: %TARGET% ===
echo.

REM Make sure git-filter-repo is available
where git-filter-repo >nul 2>nul
if errorlevel 1 (
	echo ERROR: git-filter-repo not found. Install with:
	echo   pip install git-filter-repo
	exit /b 1
)

REM Step 1: Rewrite repo history (removes from all commits)
git filter-repo --path "%TARGET%/" --invert-paths

REM Step 2: Remove from current working tree
git rm -r -f --cached "%TARGET%"
if exist "%TARGET%" rd /s /q "%TARGET%"

REM Step 3: Commit the change
git commit -m "Remove %TARGET% from repo"

REM Step 4: Force-push to remote
git push origin --force --all
git push origin --force --tags

REM Step 5: Clean up old objects
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo.
echo === Done. Folder '%TARGET%' fully removed ===
echo.
pause