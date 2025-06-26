@echo off
if [%2] == [-y] (
	call p. MoveDelete -src %1 -ghost -y
	goto:eof
)
if [%2] == [y] (
	call p. MoveDelete -src %1 -ghost -y
	goto:eof
)
call p. MoveDelete -src %1 -ghost
