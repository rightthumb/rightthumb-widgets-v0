@echo off
call uuid -e > %tmpf%
SET /p uuid=<%tmpf%
git commit -m "%uuid%
git push --force