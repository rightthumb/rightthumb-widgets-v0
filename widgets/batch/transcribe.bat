@echo off 

rem if not exist wavs (
rem 	mkdir wavs
rem 	call p. file --c + *.mp3  | p. line --c -make "ffmpeg -i {} -acodec pcm_u8 -ar 22050 wavs\{}.wav" | p. execute
rem )
rem if not exist *.wav (
rem 	cd wavs
rem )
rem if not exist *.wav (
rem 	cd wavs
rem )
echo. > transcribe.txt
call p. file --c + *.mp3 | p. line --c -make "%py% %transcribe% {} --local --api_key=eadcbd483dae422da3cf4c92e39b3d02" | p. execute >> transcribe.txt
call p. transcript -f transcribe.txt > transcript.txt
GOTO:NEXT
GOTO:EOF

rem :OLD
rem call p. transcript -f transcribe.txt > ..\transcript.txt
rem rem del transcribe.txt
rem call p. file --c + *.wav | p. line --c -make "p speech -f {}" | p. execute >> transcribe.txt
rem cd ..
rem rmdir /s/q wavs
rem call c
rem GOTO:NEXT
rem GOTO:EOF

:NEXT
call cat transcript.txt - "Error:"
GOTO:EOF

