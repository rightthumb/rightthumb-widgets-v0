@echo off
if [%1]==[] (
	set clipSlot=Default
) else (
	set clipSlot=%1
)
call cat %tmpf%-clipSlot-%clipSlot%