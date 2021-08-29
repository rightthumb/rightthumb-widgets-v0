@echo off
if [%1] == [] (
	call p ls -c ext --c -s ext | p countEach
) else (
	call p ls -c ext --c -s ext %* | p countEach
)

