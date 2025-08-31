@echo off
if [%2] == [-y] (
	call p. MoveDelete -src %1 -ghost all -y
	goto:eof
)
if [%2] == [y] (
	call p. MoveDelete -src %1 -ghost all -y
	goto:eof
)
call p. MoveDelete -src %1 -ghost all