@echo off

if [%1] == [?] (
    echo 1 = Haystack
    echo 2 = Needle
) else (
    call p. findContains -slots %*
)