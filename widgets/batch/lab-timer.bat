@echo off
echo timer: %timer%
echo   lab: %lab%
if not [%timer%] == [] if not [%lab%] == [] (

	echo %lab%>%myTickets%\timer-%Session_ID%.lab
)