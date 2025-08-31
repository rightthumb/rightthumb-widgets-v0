@echo off
if [%2] == [] (
    call p. -File2Folder -fo %1 -move
) else (
    call p. -File2Folder -f %1 -fo %2 -move
)