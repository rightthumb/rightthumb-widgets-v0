@echo off

if [%1] == [] (
	call p. transcribe-mp3
) else (
	call p. transcribe-mp3 -f %*
)