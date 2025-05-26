@echo off
if [] == [%1] (
    call p. wt -a
) else (
    call p. wt -a + %*
)