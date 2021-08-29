@echo off

CALL b ttt

IF [%1] == [?] (
	CALL n "D:\_Scott\S_Documents\Projects\DND\Research\cmd.txt"
) else (
	CALL p file + 5e --c -folder %widgets%\widgets\databank\tables | p simpleList -r 5e-SRD- .json | p simpleList
)

