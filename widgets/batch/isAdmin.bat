@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

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