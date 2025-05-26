@echo off

if not "%1" == "run" echo must be in folder you want to remove. run: git.rm.fo run
if not "%1" == "run" goto :eof

:: Define the temporary storage path if not already defined
if not defined stmp set "stmp=%TEMP%"

:: Store the current directory path in a temporary file
cd > "%stmp%\full-path.tmp"

:: Read the full path from the temporary file into the variable
set /p full_path=<"%stmp%\full-path.tmp"
@REM echo %full_path%

:: Optional calls to 'm back' and 'b w' commands, output suppressed
call m back > nul 2>&1
call b w > nul 2>&1

:: Check if the script is in the git root folder
if not exist .git (
    echo You need to be in the git root folder.
    goto :eof
)

:: Use git filter-branch to remove the specified path from all commits
git filter-branch --force --index-filter "git rm -r -f --cached --ignore-unmatch \"%full_path%\"" --prune-empty --tag-name-filter cat -- --all

:: Remove the folder from the current directory using git rm
git rm -r -f "%full_path%"

:: Final call to 'b back' command, output suppressed
call b back > nul 2>&1

:: Cleanup the temporary file
del "%stmp%\full-path.tmp"

:: End of the script
goto :eof
