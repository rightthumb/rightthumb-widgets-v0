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
call b back > nul
