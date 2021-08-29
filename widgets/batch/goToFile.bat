@echo on
	set selectedFile=%1
	set selectedFile=%selectedFile:"=%
	CD /D %selectedFile:~0,2%
	cd "%~dp1"
set "selectedFile="