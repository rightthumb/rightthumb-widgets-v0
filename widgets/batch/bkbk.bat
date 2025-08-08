@echo off
call D:\.rightthumb-widgets\widgets\batch\c.bat
call p. fileBackupBackupBackup

:: Related to:
:: bkbk-recover.bat



:: not scheduled
:: schtasks /create /tn "bkbk_Morning" /tr "\"D:\.rightthumb-widgets\widgets\batch\bkbk.bat\"" /sc DAILY /st 09:00
:: schtasks /create /tn "bkbk_Evening" /tr "\"D:\.rightthumb-widgets\widgets\batch\bkbk.bat\"" /sc DAILY /st 20:00

:: schtasks /delete /tn "bkbk_Morning" /f
:: schtasks /delete /tn "bkbk_Evening" /f


:: Scheduled!!
:: schtasks /create /tn "bkbk_Every3Hours" /tr "\"D:\.rightthumb-widgets\widgets\batch\bkbk.bat\"" /sc HOURLY /mo 3 /st 00:00
:: schtasks /create /tn "bkbk_Every3Hours" /tr "\"D:\.rightthumb-widgets\widgets\batch\bkbk.bat\"" /sc HOURLY /mo 3 /st 00:00 /ru SYSTEM

:: schtasks /delete /tn "bkbk_Every3Hours" /f