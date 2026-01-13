@echo off
set tPython=D:\.rightthumb-widgets\widgets\2python\categorized


if exist "%tPython%\ai\%1.py" set xPython=%tPython%\ai
if exist "%tPython%\archives\%1.py" set xPython=%tPython%\archives
if exist "%tPython%\backup\%1.py" set xPython=%tPython%\backup
if exist "%tPython%\code\%1.py" set xPython=%tPython%\code
if exist "%tPython%\data-files\%1.py" set xPython=%tPython%\data-files
if exist "%tPython%\db\%1.py" set xPython=%tPython%\db
if exist "%tPython%\files\%1.py" set xPython=%tPython%\files
if exist "%tPython%\geo\%1.py" set xPython=%tPython%\geo
if exist "%tPython%\images\%1.py" set xPython=%tPython%\images
if exist "%tPython%\media\%1.py" set xPython=%tPython%\media
if exist "%tPython%\messaging\%1.py" set xPython=%tPython%\messaging
if exist "%tPython%\misc\%1.py" set xPython=%tPython%\misc
if exist "%tPython%\network\%1.py" set xPython=%tPython%\network
if exist "%tPython%\security\%1.py" set xPython=%tPython%\security
if exist "%tPython%\servers\%1.py" set xPython=%tPython%\servers
if exist "%tPython%\social\%1.py" set xPython=%tPython%\social
if exist "%tPython%\special\%1.py" set xPython=%tPython%\special
if exist "%tPython%\text\%1.py" set xPython=%tPython%\text
if exist "%tPython%\time\%1.py" set xPython=%tPython%\time
if exist "%tPython%\vps\%1.py" set xPython=%tPython%\vps
if exist "%tPython%\web-scrape\%1.py" set xPython=%tPython%\web-scrape
if exist "%tPython%\windows\%1.py" set xPython=%tPython%\windows
if exist "%tPython%\os\%1.py" set xPython=%tPython%\os

if not exist "%xPython%\%1.py" (
	echo.
	echo script not found
	echo.
	goto:EOF
)

%py% "%xPython%\%1.py" %*