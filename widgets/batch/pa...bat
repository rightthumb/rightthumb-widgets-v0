@echo off
if [%1]==[] (
	set clipSlot=0
) else (
	set clipSlot=%1
)
call cat %tmpf%-clipSlot-%clipSlot% | call cp