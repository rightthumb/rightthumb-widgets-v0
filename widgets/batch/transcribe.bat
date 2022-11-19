@echo off 
if not exist wavs (
	mkdir wavs
	call p file --c + *.mp3  | p line --c -make "ffmpeg -i {} -acodec pcm_u8 -ar 22050 wavs\{}.wav" | p execute
)
if not exist *.wav (
	cd wavs
)
if not exist *.wav (
	cd wavs
)
call p file --c + *.wav | p line --c -make "p speech -f {}" | p execute > transcribe.txt
call p transcript -f transcribe.txt > ..\transcript.txt
rem del transcribe.txt
cd ..
rmdir /s/q wavs
call cat transcript.txt - "Error:"
