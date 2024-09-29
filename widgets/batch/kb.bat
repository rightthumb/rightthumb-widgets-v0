@echo off
cls
if [%1] == [+] (
	call p. vps-KnoledgeBase -list + %* | p color -or + %* "(" ")" -upper
) else (
	call p. vps-KnoledgeBase -nocolor -search %* | p color -or + %* "(" ")" -upper
)
