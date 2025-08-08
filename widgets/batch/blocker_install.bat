@echo off
setlocal enabledelayedexpansion

rem Define an array of batch file names (without extension) and their corresponding URLs
set "batchFiles[0]=block"
set "batchFiles[1]=block2"
set "batchFiles[2]=blocker"
set "batchFiles[3]=change"
set "batchFiles[4]=unblock"
set "batchFiles[5]=update"

set "baseURL=https://sds.sh/block/youtube/"
set "downloadFolder=%userprofile%"

rem Loop through the array and update each batch file
for /L %%i in (0,1,5) do (
	set "batchFile=!batchFiles[%%i]!"
	set "fileURL=!baseURL!!batchFile!"
	set "filePath=!downloadFolder!\!batchFile!.bat"

	echo Getting content of !batchFile!...
	
	rem Print the URL for debugging
	echo !fileURL!

	rem Use curl to download the file from the URL
	curl -o "!filePath!" "!fileURL!"

	echo !batchFile!.bat updated.
)

echo All batch files updated.
rem pause

rem https://sds.sh/block/youtube/curl.zip
rem curl.