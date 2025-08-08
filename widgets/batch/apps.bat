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

REG Query HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\  /S > %stmp%\app_list.txt
REG Query HKLM\Software\WOW6432Node\RegisteredApplications\  /S > %stmp%\app_list2.txt

call p. appList