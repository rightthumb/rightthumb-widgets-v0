@echo off
call m back
call b tech
echo.> %tmpf%
call p files + *.7z --c - archive_7z | p line - archive_7z --c -make "move ;'{};'"  > %tmpf%

call b archive_7z_files

type %tmpf% | p execute

rem type %tmpf0%

call b back