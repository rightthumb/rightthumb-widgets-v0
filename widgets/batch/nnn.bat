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

if exist %* (

call p. fileBackup -open -i %*
start "EDIT" %code_editor% %*
echo %*

) else if exist %python%\%*.py (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %python%\%*.py
echo %python%\%*.py

) else if exist %phpFiles%\%*.php (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %phpFiles%\%*.php
echo %phpFiles%\%*.php

) else if exist %scriptroot%\%*.bat (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %scriptroot%\%*.bat
echo %scriptroot%\%*.bat

) else if exist %powershell%\%*.ps1 (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %powershell%\%*.ps1
echo %powershell%\%*.ps1

) else if exist D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1 (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1
echo D:\_Scott\S_Documents\Projects\self\Powershell\%*.ps1

) else if exist %myPhp%\%*.php (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %myPhp%\%*.php
echo %myPhp%\%*.php

) else if exist %myPowershell%\%*.ps1 (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %myPowershell%\%*.ps1
echo %myPowershell%\%*.ps1

) else if exist %myPython%\%*.py (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %myPython%\%*.py
echo %myPython%\%*.py

) else if exist %myTables%\%* (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %myTables%\%*
echo %myTables%\%*

) else if exist %myTables%\%*.json (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %myTables%\%*.json
echo %myTables%\%*.json

) else if exist %myDatabases%\%* (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %myDatabases%\%*
echo %myDatabases%\%*

) else if exist %myWebApp%\%* (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %myWebApp%\%*
echo %myWebApp%\%*

) else if exist %USERPROFILE%\Desktop\%* (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %USERPROFILE%\Desktop\%*
echo %USERPROFILE%\Desktop\%*

) else (

call p. fileBackup -open -i %* 
start "EDIT" %code_editor% %*
echo %*

)



 
