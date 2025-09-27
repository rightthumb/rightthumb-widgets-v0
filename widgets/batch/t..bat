@echo off
call m back > nul
call b tickets > nul
if [%1] == [] (
	set ago=2w
) else (
	set "ago=%*"
)
p file -ago %ago% + open close -or | p. cat --c| p. line - session "<" --c | p. line - closed- open- | p. last-line
call b back > nul