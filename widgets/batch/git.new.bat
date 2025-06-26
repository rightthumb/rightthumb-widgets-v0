@echo off
REM Set global configurations for Git
git config --global user.name "rightthumb"
git config --global user.email "scott.reph@gmail.com"

REM Initialize a new Git repository and make an initial commit
git init
git add .
call uuid -e  > %tmpf%
SET /p uuid=<%tmpf%
git commit -m "%uuid%"
git push --force
echo Repository initialized and first commit made!
pause
