@echo off
REM Check if the script is run from the root of a Git repository
if not exist .git (
		echo need to be in git root folder
		goto:eof
)

REM The input should be the relative path to the folder you want to remove
SET FOLDER_TO_REMOVE=%1

REM Check if a folder name was provided
if "%FOLDER_TO_REMOVE%"=="" (
	echo Please specify a folder to remove.
	goto:eof
)

REM Removing the folder from the repository history using git filter-branch
REM This step is optional and can be skipped if you do not need to modify the history
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch %FOLDER_TO_REMOVE%" --prune-empty --tag-name-filter cat -- --all

REM Removing the folder from the current working tree
git rm -rf %FOLDER_TO_REMOVE%

REM Note: The 'git filter-branch' command is used to rewrite the repository history, removing the specified folder from all commits.
REM This operation can significantly alter your repository's history. Use with caution, especially on shared repositories.
REM If you only need to remove the folder from the current state and not alter the history, you can skip the 'git filter-branch' command.