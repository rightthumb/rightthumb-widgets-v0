@echo off

call p. full-path -script -f %1    > nul 2>&1
set /p full_path=<%stmp%\full-path.tmp
@REM echo %full_path%
call m back   > nul 2>&1
call b w   > nul 2>&1
@REM goto:eof
if not exist .git (
	echo need to be in git root folder
	goto:eof
)
@REM git filter-branch --force --index-filter "git rm -f --cached --ignore-unmatch %1" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -f --cached --ignore-unmatch %full_path%" --prune-empty --tag-name-filter cat -- --all
@REM git rm -f %1
git rm -f %full_path%

call b back   > nul 2>&1