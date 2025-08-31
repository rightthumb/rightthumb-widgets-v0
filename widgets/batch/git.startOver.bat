@echo off

set "addAll="

set /p addAll=Do you want to add everything? (y/n):

if not [%addAll%] == [y] (
    echo No changes were made to the repository.
    goto :eof
)

if [%addAll%] == [y] (
    rmdir /s/q .git
)

if exist .git (
    echo Git repository was not successfully removed.
    goto :eof
)

if [%addAll%] == [y] (
    git init
    @REM git add .
    call git.files 10y x
    git branch -M main
    git push -f origin main
    git commit -m "Initial commit"
    git remote remove origin

    git remote add origin https://github.com/rightthumb/rightthumb-widgets-v0.git
    git push -f origin main
) else (
    echo No changes were made to the repository.
)

goto :eof

Files:
         README.md
         require.txt

 2

Folders:
         install
         widgets

 2