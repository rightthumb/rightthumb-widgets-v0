@echo off

if [%1]==[] (
    call p. files -rr -r -folder "C:\Users\Scott\OneDrive - rightthumb.com\Pictures\Screenshots" -ago 1d
) else (
    call p. files -rr -r -folder "C:\Users\Scott\OneDrive - rightthumb.com\Pictures\Screenshots" %*
)