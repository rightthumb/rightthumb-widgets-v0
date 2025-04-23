@echo off
if [%1] == [s] (
    call p. clipCache -save
    goto:eof
)
call p. cat -f %userprofile%/.rt/clip.cache  %* 