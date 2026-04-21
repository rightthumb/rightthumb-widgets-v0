@echo off

set "addAll="

set /p addAll=Do you want to add everything? (y/n):

if not [%addAll%] == [y] (
	echo No changes were made to the repository.
	goto :eof
)

if [%addAll%] == [y] (
	rmdir /s/q .git
)

if exist .git (
	echo Git repository was not successfully removed.
	goto :eof
)

if [%addAll%] == [y] (
	git init
	@REM git add .
	call git.files 10y x
	git add D:\.rightthumb-widgets\widgets\batch\
	git add D:\.rightthumb-widgets\widgets\databank\indexes\queries\FILE-EXTENS
	git add D:\.rightthumb-widgets\widgets\databank\vault\TECHNOLOG\OS\FILE\EXTENS
	git add D:\.rightthumb-widgets\widgets\databank\tables\extensions.json
	git add D:\.rightthumb-widgets\widgets\databank\tables\auditCodeBase.index
	git add D:\.rightthumb-widgets\widgets\databank\tables\cal-days.json
	git add D:\.rightthumb-widgets\widgets\databank\tables\countries_abbreviations.json
	git add D:\.rightthumb-widgets\widgets\databank\tables\leap-years.list
	git add D:\.rightthumb-widgets\widgets\databank\tables\emotions.json
	git add D:\.rightthumb-widgets\widgets\databank\tables\mac-vendors.zip
	git add D:\.rightthumb-widgets\widgets\databank\tables\words.zip
	git add D:\.rightthumb-widgets\widgets\databank\tables\mime_type.db
	git add D:\.rightthumb-widgets\widgets\python\library\os\file\mime_type.db
	git add D:\.rightthumb-widgets\widgets\python\library\os\file\taboo.json
	git add D:\.rightthumb-widgets\widgets\python\library\os\file\lunar_calendar.json
	git add D:\.rightthumb-widgets\widgets\python\library\os\file\domains.json.zip
	git add D:\.rightthumb-widgets\widgets\python\library\os\file\tz.json
	git add D:\.rightthumb-widgets\widgets\python\library\os\file\default.zip

	git branch -M main
	git push -f origin main
	git commit -m "Initial commit"
	git remote remove origin

	git remote add origin https://github.com/rightthumb/rightthumb-widgets-v0.git
	git push -f origin main
) else (
	echo No changes were made to the repository.
)

goto :eof

Files:
		README.md
		require.txt

 2

Folders:
		install
		widgets

 2