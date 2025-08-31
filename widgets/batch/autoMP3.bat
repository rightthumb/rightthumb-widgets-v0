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




CALL p. file --c - *.mp3 + *.opus *.webm *.m4a  -or > %tmpf%
rem dir /b *.opus  > %tmpf%
SET /p audioFile=<%tmpf%

CALL p. rename_file_safe -file "%audioFile%"

CALL ppause 3
rem dir /b *.opus  > %tmpf%
CALL p. file --c - *.mp3 + *.opus *.webm *.m4a  -or > %tmpf%
SET /p audioFile=<%tmpf%

echo file: %audioFile%
ffmpeg -i "%audioFile%" -codec:a libmp3lame -qscale:a 2 "output.mp3"

CALL p. pop_last   -string "%audioFile%" -f -p ;- .  > %tmpf%
SET /p audioFileLabel=<%tmpf%
if [%1] == [] (
	rename "output.mp3" "%audioFileLabel%.mp3"
) else (
	rename "output.mp3" "%1 %audioFileLabel%.mp3"
)
rem rename "output.mp3" "%*.mp3"
del "%audioFile%"

rem yAudio "https://www.youtube.com/watch?v=NGFToiLtXrod" & autoMP3 Can't Take My Eyes off You

rem type %tmpf2% | a.playlist 1