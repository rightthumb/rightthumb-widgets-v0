@echo off
setlocal

REM --- Optional: pass a remote URL to set origin each run ---
set REMOTE_URL=%~1

REM --- Make sure we're a git repo (idempotent) ---
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 git init

REM --- Ensure branch 'main' (idempotent) ---
git checkout -B main >nul 2>&1

REM --- If a URL was given, (re)set origin to it ---
if "%REMOTE_URL%"=="" goto check_origin
git remote remove origin >nul 2>&1
git remote add origin "%REMOTE_URL%" >nul 2>&1

:check_origin
REM --- Verify origin exists (bail if missing and no URL provided) ---
git remote get-url origin >nul 2>&1
if not errorlevel 1 goto have_origin
echo [ERROR] No 'origin' remote found, and no URL was provided.
echo Usage: push_force.bat https://github.com/you/yourrepo.git
exit /b 1

:have_origin
REM --- Stage everything (new/modified/deleted) ---
@REM git add -A

REM --- Always commit (even if empty) ---
set MSG=force-push-%RANDOM%
git commit --allow-empty -m "%MSG%" >nul 2>&1

REM --- FORCE push to origin/main (and set upstream) ---
git push -u -f origin main
if errorlevel 1 (
  echo [FAIL] Force push failed.
  exit /b 1
)

echo [OK] Force-pushed to origin/main with commit: %MSG%
exit /b 0
