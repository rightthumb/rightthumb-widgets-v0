@echo off
call m tmp
C:
cd %userprofile%
call m p
cd Desktop
call m d

%widgets%
cd \tech\scripts
call m live
call m l
call m scripts
call m s

cd %log_folder%
call m logFolder

IF NOT ["%t3set%"] == ["y"] (GOTO END)
%t3Drive%:
cd\
call m t3
call m 3t
call m x
cd \backup
call m bk
call m backup
call m br
call m backuproot
:END
call b tmp
echo Auto Generated BMs