@echo off

SET index=%scriptroot%\manage_drives\%computername%\index\01*
IF [%1] == [/p] (
		SET index=%scriptroot%\manage_drives\%computername%\index\%2*
		SHIFT
		SHIFT
	)




SET search=%1
::SET index=d:\index.txt




IF NOT [%5] == [] GOTO FIVE
IF NOT [%4] == [] GOTO FOUR
IF NOT [%3] == [] GOTO THREE
IF NOT [%2] == [] GOTO TWO




GOTO ONE

IF [%1] == [] GOTO END

:ONE
:echo Search level: ONE variable
findstr /i /r %search% "%index%" > ~out.txt & parse ~out.txt ":" "3,4"  & del ~out.txt
GOTO END


:TWO
:echo Search level: TWO variables
findstr /i /r %search% "%index%" | find /i "%2" > ~out.txt & parse ~out.txt ":" "3,4"  & del ~out.txt
GOTO END


:THREE
:echo Search level: THREE variables
findstr /i /r %search% "%index%" | find /i "%2" | find /i "%3" > ~out.txt & parse ~out.txt ":" "3,4"  & del ~out.txt
GOTO END


:FOUR
:echo Search level: FOUR variables
findstr /i /r %search% "%index%" | find /i "%2" | find /i "%3" | find /i "%4" > ~out.txt & parse ~out.txt ":" "3,4"  & del ~out.txt
GOTO END


:FIVE
:echo Search level: FIVE variables
findstr /i /r %search% "%index%" | find /i "%2" | find /i "%3" | find /i "%4" | find /i "%5" > ~out.txt & parse ~out.txt ":" "3,4"  & del ~out.txt
GOTO END



:END 
