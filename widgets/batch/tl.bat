@echo off

call wl
goto :eof
SET fi=%1

SET do_paste=FALSE

if [%1] == [-p] SET do_paste=TRUE
if [%1] == [pa] SET do_paste=TRUE
if [%1] == [-pa] SET do_paste=TRUE
if [%1] == [paste] SET do_paste=TRUE
if [%1] == [-paste] SET do_paste=TRUE


if [%do_paste%] == [TRUE] (
	call pa > %tmpf%-tl
	SET fi=%tmpf%-tl
)


rem call p. cat -f %fi%
rem goto:eof


if [%2] == [] (
	call p. cat -f %fi%  | p. cmd2table -print -int Mem_Usage | p. printTable  - svchost + .exe   -aggregate " eot?mem-total=add( int(MEM_USAGE) )); format(eot?mem-total,?size,??kb);" -int Mem_Usage -s Mem_Usage 
) else if [%2] == [all] (
	call p. cat -f %fi%  | p. cmd2table -print -int Mem_Usage | p. printTable     -aggregate " eot?mem-total=add( int(MEM_USAGE) )); format(eot?mem-total,?size,??kb);" -int Mem_Usage -s Mem_Usage 
) else (
	shift
	call p. cat -f %fi%  | p. cmd2table -print -int Mem_Usage | p. printTable  - svchost + .exe   -aggregate " eot?mem-total=add( int(MEM_USAGE) )); format(eot?mem-total,?size,??kb);" -int Mem_Usage -s Mem_Usage %*
)

 
