@echo off
REG Query HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\  /S > %stmp%\app_list.txt
REG Query HKLM\Software\WOW6432Node\RegisteredApplications\  /S > %stmp%\app_list2.txt

call p appList