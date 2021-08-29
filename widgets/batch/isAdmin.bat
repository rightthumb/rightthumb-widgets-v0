@echo off
CALL getResult "attrib -H D:\drive.id.sys"
set testTMP=%result:~,13%
IF ["%testTMP%"] == ["Access denied"] (
		set isAdmin=N
		echo N
	) else (
		attrib +H D:\drive.id.sys
		set isAdmin=Y
		echo Y
	)
set result=