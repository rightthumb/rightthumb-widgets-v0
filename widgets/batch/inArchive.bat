@echo off
title Auto Archive Research
if [%1] == [?] (	
	echo inArchive skype ^> %%tmpf9%%
	echo type %%tmpf9%% ^| p dir --c -c p ^> %%tmpf8%%
	echo type %%tmpf8%% ^| p f + skype -n - "C;.;;'" "D;.;;'" ^> %%tmpf7%%
	echo n %%tmpf7%%
	echo done
	goto:eof
)
rem echo %myIndexes%\01{F8E01519-3977-04B8-3416-1F0048BD97C3}
call p f -in %myIndexes%\01* + *.txt | p f -jn + %*
rem inArchive skype > %tmpf9%


