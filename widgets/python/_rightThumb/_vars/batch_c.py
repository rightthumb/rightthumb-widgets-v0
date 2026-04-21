import _rightThumb._vars as _v

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import os.path
def GENERATE_FILE(programs):
	fileName = programs + _v.slash+'batch\\c.bat'


	fileData = """



@echo off

SET PYTHON_BASE=3


DOSKEY /LISTSIZE=999
CLS
echo Loading...
IF [%1] == [r] SET api=

IF NOT ["%api%"] == ["loaded"] (
	CALL :LOAD
) else (
	CLS
)
CALL :TIMESTAMP

GOTO:EOF

:TIMESTAMP


CALL timestamp d noEcho
SET open_timestamp=%now%
CALL timestamp dt noEcho
SET open_timestamp2=%now%


CALL timestamp sdel noEcho
SET ts=%now%

SET timestamp=%now%
CALL timestamp d2 noEcho
SET today=%now%
if not [%lab%] == [] (
		title %today%  -  %lab%
	) else (
		title %today%
	)
CALL timestamp t2 noEcho
GOTO:EOF




:GENERATE_API_ID
SET /p LastID=<%myVars%\\ID.sys
SET /a Session_ID=%LastID% + 1
SET Session_ID_BK=%Session_ID%
echo %Session_ID% > %myVars%\\ID.sys
CALL timestamp ats2 noEcho
SET timestamp_start=%now%
echo %timestamp_start%
:::::::::::::::::::::::: DOESNT WORK - :: CALL getSID
GOTO:EOF

:LOAD

				rem echo TODO:
				rem echo    change id to host vars
				rem echo    auto add archive folder to indexes
				rem echo    default bookmarks
				rem echo    change dirCache to tables
				rem echo    auto id resolution
				rem echo    compareFiles to tables ( rename to negotiation_statistics and file_negotiation_table)
				rem echo    fix dir folder issue
				rem echo    line -x get best match json to var set at end with highest path match count
				rem echo.
SET /p Drive=<%userprofile%\\.tk421
SET phpDrive=%Drive:~0,1%
SET techDrive=%Drive:~0,1%
SET scriptDrive=%Drive:~0,1%
SET driveRoot=%Drive:~0,1%
SET phpDrive=%Drive:~0,1%
SET techFolder=%techDrive%:\\tech
SET /p installID=<%techDrive%:\\tech\\scripts\\instanceID.sys
SET Drive=

::::::: PHP Drive
if EXIST C:\\xampp\\php\\php.exe (
	SET php=C:\\xampp\\php\\php.exe
) else (
	SET php=%techDrive%:\\techApps\\xampp\\php\\php.exe
)




::::::: App shortcuts
rem CALL findExcel
rem CALL findChrome
rem SET lib=%techDrive%:\\tech\\programs\\library
rem SET acro="c:\\Program Files (x86)\\Adobe\\Acrobat 11.0\\Acrobat\\Acrobat.exe"
rem SET bzip2="C:\\Program Files\\GnuWin32\\bin\\bzip2.exe"

if EXIST c:\\drive.id.sys (SET /p cID=<c:\\drive.id.sys) else (set cID={})
rem if EXIST %techDrive%:\\drive.id.sys (SET /p dID=<%techDrive%:\\drive.id.sys) else (set dID={})
rem echo %cID%
if EXIST "C:\\Program Files\\Sublime Text 3\\sublime_text.exe" (
	SET notepadAPP="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
	set n2="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"

) else (
	SET notepadAPP="%techDrive%:\\techApps\\Sublime Text Build 3211\\sublime_text.exe"
	SET n2="%techDrive%:\\techApps\\Notepad++\\notepad++.exe"
)

rem if ["%cID%"] == ["{F8E01519-3977-04B8-3416-1F0048BD97C3}"] (
rem ) else (
rem )

SET n=%notepadAPP%

rem SET w="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"

rem SET py="C:\\Users\\Scott\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe"
rem SET py2="C:\\Python27\\python.exe"
SET py="%techDrive%:\\techApps\\Python\\Python36-32\\python.exe"
SET pyFolder="%techDrive%:\\techApps\\Python\\Python36-32"
SET py2="%techDrive%:\\techApps\\Python\\Python27\\python.exe"
::SET pys="C:\\Users\\Scott\\AppData\\Local\\Programs\\Python\\Python35\\Scripts"
rem SET pys=C:\\Users\\Scott\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts
rem SET pytools=C:\\Users\\Scott\\AppData\\Local\\Programs\\Python\\Python36-32\\Tools\\scripts

::::::: API Variable Extras

rem SET stemp=%scriptroot%\\temp

rem SET stempfile=%stmp%\\{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}
rem SET sql=%techDrive%:\\_Scott\\S_Documents\\Projects\\sql

set pip=%techDrive%:\\techApps\\Python\\Python36-32\\Scripts\\pip.exe
set pip2=%techDrive%:\\techApps\\Python\\Python27\\Scripts\\pip.exe

set "computername2=%computername: =_%"

SET hostDefault=tech\\hosts\\{D599DDFE-28B1-4CBD-B300-78DB4BCA7DF5}

SET thisHost=hosts\\%computername2%
SET myHome=%techFolder%\\%thisHost%
SET myVars=%myHome%\\vars
SET myBookmarks=%myHome%\\bookmarks
SET myTickets=%myHome%\\tickets
SET myIndexes=%myHome%\\indexes
SET i=%myHome%\\indexes
SET myTables=%myHome%\\tables
SET myDatabases=%myHome%\\databases
SET myInfo=%myHome%\\info
SET myProjects=%myHome%\\projects
SET myPrograms=%myHome%\\programs
SET myNotes=%myHome%\\notes
SET myWebApp=%myHome%\\WebApp
SET webapp=%myWebApp%
SET myBatch=%myHome%\\programs\\batch
SET myPython=%myHome%\\programs\\python
SET myPowershell=%myHome%\\programs\\powershell
SET myPhp=%myHome%\\programs\\php
SET stmp=%myHome%\\temp
SET myTxt=%myHome%\\txt
SET mdt=%myVars%\\mdt.txt


SET m3Data=%i%\\Movie_Drive_t3.dirCache
SET mcData=%i%\\Movies_Cloud.dirCache


rem SET cID={F8E01519-3977-04B8-3416-1F0048BD97C3}
SET dID={65E57A88-6471-E426-D878-AD55F117A804}
SET mID={D86E7BD3-2C52-0C57-9DA2-447309490DB4}
SET m3ID={D644A899-89BB-9748-8339-3FC5F75B8A16}
SET pubID={C7DA4040-A42C-0372-B54A-8E40F835D3E1}
SET privID={5B55D9AE-6C90-B44B-2071-5376CBB2AAAE}

IF NOT EXIST %techFolder%\\hosts (md %techFolder%\\hosts) 
IF NOT EXIST %myHome% (
		md %myHome%
		echo Building profile on USB
		xcopy /s/d/y/c %techDrive%:\\%hostDefault%\\*.* %myHome%\\>nul
	)
IF NOT EXIST %myVars% (md %myVars%) 
IF NOT EXIST %myBookmarks% (md %myBookmarks%) 
IF NOT EXIST %myTickets% (md %myTickets%) 
IF NOT EXIST %myIndexes% (md %myIndexes%) 
IF NOT EXIST %myIndexes%\\archive (md %myIndexes%\\archive) 
IF NOT EXIST %myTables% (md %myTables%) 
IF NOT EXIST %myDatabases% (md %myDatabases%) 
IF NOT EXIST %myInfo% (md %myInfo%) 
IF NOT EXIST %myProjects% (md %myProjects%) 
IF NOT EXIST %myPrograms% (md %myPrograms%) 
IF NOT EXIST %myNotes% (md %myNotes%) 
IF NOT EXIST %myWebApp% (md %myWebApp%)

IF NOT EXIST %myBatch% (md %myBatch%) 
IF NOT EXIST %myPython% (md %myPython%) 
IF NOT EXIST %myPowershell% (md %myPowershell%) 
IF NOT EXIST %myPhp% (md %myPhp%) 
IF NOT EXIST %stmp% (md %stmp%) 
IF NOT EXIST %myTxt% (md %myTxt%) 

SET programs=%techFolder%\\programs

SET batch=%programs%\\batch
SET python=%programs%\\python\\src\\windows
SET powershell=%programs%\\powershell
SET php2=%programs%\\php
SET exe=%programs%\\exe
SET research=%programs%\\data
SET data=%programs%\\data

SET compiled=%programs%\\compiled


SET myImports=%python%\\_rightThumb

IF NOT EXIST %programs% (md %programs%) 

IF NOT EXIST %batch% (md %batch%)
IF NOT EXIST %python% (md %python%) 
IF NOT EXIST %powershell% (md %powershell%) 
IF NOT EXIST %php2% (md %php2%) 
IF NOT EXIST %exe% (md %exe%) 
IF NOT EXIST %research% (
	md %research%
	md %research%\\indexes
	md %research%\\databank
)


::::::: Command Paths
rem SET oldPath=%path%
rem SET pathAPI=%scriptroot%\\;%scriptrootAlias%\\
rem SET pathApps=C:\\Program Files (x86)\\ImageMagick-6.9.2-Q16;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\Windows Live\\Shared;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\Common Files\\Acronis\\SnapAPI\\;C:\\Program Files (x86)\\Skype\\Phone\\;C:\\Program Files (x86)\\Windows Kits\\10\\Windows Performance Toolkit\\;C:\\Users\\Scott\\AppData\\Local\\Microsoft\\WindowsApps
SET appPaths=%batch%;%python%;%myBatch%;%myPython%;%exe%
SET pathPython=C:\\Users\\Scott\\AppData\\Local\\Programs\\Python\\Python36-32;C:\\Users\\Scott\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib;C:\\Users\\Scott\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages;C:\\Users\\Scott\\AppData\\Local\\Programs\\Python\\Python36-32;C:\\Users\\Scott\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts
rem SET pathBuilder=%pathPython%;%path%;%pathAPI%;%pathApps%;
rem pause
rem echo %originalPath%
rem IF [%originalPath%] == [] SET originalPath=%path%
rem reg query "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment" /v Path | "%techDrive%:\\techApps\\Python\\Python36-32\\python.exe" "%techDrive%:\\tech\\programs\\python\\src\\windows\\regKeyClean.py" > %techDrive%:\\tech\\programs\\batch\\originalPath.bat>nul
CALL %batch%\\originalPath.bat
SET originalPath=%Path%
SET pathBuilder=%compiled%;%appPaths%;%pathPython%;%originalPath%
SET path=%pathBuilder%
SET appPaths=
SET pathAPI=
SET pathBuilder=
SET pathPython=

SET phpFiles=%php2%


SET /p quote=<%myVars%\\quote.txt
SET /p percentage=<%myVars%\\percentage.txt
SET /p percent=<%myVars%\\percentage.txt

SET tmpf=%stmp%\\{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}
SET tmpf0=%stmp%\\{B820137A-79B8-45E3-BCBD-A6CAC50892D0}
SET tmpf1=%stmp%\\{C0FA8E56-8426-46BB-9CE8-4A14C51EA261}
SET tmpf2=%stmp%\\{5FBF34C0-9A95-4C7E-BA53-44F84ECECCB5}
SET tmpf3=%stmp%\\{F139D191-FA1A-44D5-855C-7E5141B30E0D}
SET tmpf4=%stmp%\\{AA8EC8E1-EA9D-460D-A593-7B0FAEB9243E}
SET tmpf5=%stmp%\\{201D82D6-2DC0-4552-A598-54F5481399A1}

SET tmpf6=%stmp%\\{26B3B9C6-0A59-432A-9386-D432B53001CB}
SET tmpf7=%stmp%\\{C03C0132-CFFC-4E3A-8F0F-614BB95164C7}
SET tmpf8=%stmp%\\{4CCA3EBD-4535-42B7-9C75-05EFAACB00E0}
SET tmpf9=%stmp%\\{DF1D4EBC-838E-419C-9C58-943C1767391A}

SET tmpfl=%stmp%\\{79E8C4B0-2AAA-2083-B812-AD1B9283B30A}


SET ideas=%stmp%\\{6EF01C5C-E6A8-585D-F946-1C9BC46C1D7A}
SET pips=%stmp%\\pips.txt
SET disc=%stmp%\\disc.txt

SET todoo=%stmp%\\todo.txt
SET todo=%myHome%\\projects\\todo.txt
set open=%myHome%\\projects\\open_projects.txt
SET lastP=%myHome%\\projects\\last_projects.txt
SET scrap=%myHome%\\projects\\last_projects.txt

SET documentation=%programs%\\documentation
SET instructions=%documentation%\\instructions.txt
SET imports=%documentation%\\python_imports.py
SET algorithms=%documentation%\\algorithms.txt
SET basic_scripts=%documentation%\\algorithms.txt

SET behavior=%myHome%\\projects\\behavior.txt

SET DB=%techDrive%:\\tech\\hosts\\MSI\\tables\\clients_databases.txt
set appAliasLog=%myTables%\\app_alias_record.csv

SET behave=%behavior%
SET hack=%techDrive%:\\tech\\programs\\library\\WEB\\javascript\\website_hacks.js
SET hacks=%techDrive%:\\tech\\programs\\library\\WEB\\javascript\\website_hacks.js
SET sites=%programs%\\javascript\\my_website_projects.js
SET minecraft=%programs%\\javascript\\minecraft.txt

SET idea=%stmp%\\{6EF01C5C-E6A8-585D-F946-1C9BC46C1D7A}
SET contextTemp=%stmp%\\{21E8D046-A855-EE9B-B772-9EECBD922D87}
SET pyi=%techDrive%:\\techApps\\Python\\Python36-32\\index.txt
SET ps="C:\\Program Files\\Adobe\\Adobe Photoshop CC 2014\\Photoshop.exe"
SET battery="%programs%\\vbs\\battery.vbs"
SET fileBackup=%myTables%\\fileBackup_log.json
SET bkLog=%myTables%\\fileBackup_log.json
SET 7z="%techDrive%:\\techApps\\7-Zip\\7zFM.exe"
SET rootpython=C:\\Users\\Scott\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu18.04onWindows_79rhkp1fndgsc\\LocalState\\rootfs\\root\\programs\\python
SET HOSTS=C:\\Windows\\System32\\drivers\\etc\\hosts

SET databank=%techFolder%\\programs\\databank
SET dbTables=%databank%\\tables
SET mData=%dbTables%\\movie.cache

SET archive7z=%techDrive%:\\tech\\archive_7z_files
IF NOT EXIST %archive7z% (md %archive7z%) 


	net session >nul 2>&1
	if %errorLevel% == 0 (
		SET isAdmin=True
	) else (
		SET isAdmin=False
	)

SET dircache=%myTables%\\dirCache.json
SET dircachep=%myTables%\\dirCacheP.json
CALL theUSB
set qi=%myIndexes%\\0A{465C1A34-D22F-184E-F713-F8E5149E212D}
echo %n%>"%myVars%\\notepad.txt"
::::::: API Paths (Asside from PHP)

rem SET scriptroot=%techDrive%:\\tech\\scripts
SET scriptroot=%batch%

IF ["%Session_ID%"] == [""] CALL :GENERATE_API_ID
SET api=loaded
rem pause
CLS
echo.
rem CALL p drive -scan

rem type %behavior%
rem echo.

prompt - 
GOTO:EOF









	"""


	if not os.path.isfile( fileName ):
		open(fileName,'w', encoding='utf-8').write(fileData)


