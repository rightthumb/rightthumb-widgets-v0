@echo off
call p fileBackup -i "%phpFiles%\%1.php"
start "EDIT" %code_editor% "%phpFiles%\%1.php"
