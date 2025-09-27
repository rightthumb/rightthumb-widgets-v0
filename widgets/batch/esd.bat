@echo off

set /p esDays=Days: 
set /p esExt=EXT (py): 
set "esOmit=msys64 RightThumb_Git py3.12 projects\git\ sds.sh\public_html\widgets\widgets\python\  Scott\.codeium\ QMK_MSYS Dreamweaver bk old "
es.exe dm:last%esDays%days type:file *.%EXT% | p line - AppData .vscode temp backup --c | sort | p line --c - "Program Files" %esOmit% %*