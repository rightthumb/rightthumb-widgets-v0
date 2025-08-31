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

IF EXIST "D:\Program Files (x86)\Nmap\nmap.exe" (
	CALL :RUN
) else (
	CALL :INSTALLER_CHECK
)

GOTO:EOF



:RUN
IF [%1] == [] GOTO:NO_IP_ERROR
"D:\Program Files (x86)\Nmap\nmap.exe" -T4 -A -v %1
GOTO:EOF
:INSTALLER_CHECK
echo.
CALL p. printMessage -message "Error: " " nmap is not installed"  -color red yellow
echo.
IF EXIST "%widgets%\techApps\_installers\nmap\nmap-7.80-setup.exe" (
	CALL p. printMessage -message "      installer found: %widgets%\techApps\_installers\nmap\nmap-7.80-setup.exe"  -color green
) else (
	CALL p. printMessage -message "      installer missing: \techApps\_installers\nmap\nmap-7.80-setup.exe"  -color red
)
IF EXIST "%widgets%\techApps\_installers\nmap\npcap-0.9991.exe" (
	CALL p. printMessage -message "      installer found: %widgets%\techApps\_installers\nmap\npcap-0.9991.exe"  -color green
) else (
	CALL p. printMessage -message "      installer missing: \techApps\_installers\nmap\npcap-0.9991.exe"  -color red
	echo.
	CALL p. printMessage -message "          *** " "NOTE: npcap installation is automatic if onine" " *** "  -color red green red
)

GOTO:EOF
:NO_IP_ERROR
CALL p. printMessage -message "Error: " " missing IP"  -color red yellow
echo.
CALL p. printMessage -message "      Example:    nmap 192.168.1.54"  -color green
GOTO:EOF