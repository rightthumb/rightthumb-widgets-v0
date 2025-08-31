@echo off 

call m back --c
call b py > nul




if [%1] == [] (
	call p. files -rr + *.py - _rightThumb --c | p. sortByLength  | p. line %*
) else (
	call p. files -rr + *.py - _rightThumb | p. sortByLength | p. line %*
)



call b back > nul