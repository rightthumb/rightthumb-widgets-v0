@echo off
if [%1] == [+] (
	call p. vps-KnoledgeBase -list + %*
) else (
	call p. vps-KnoledgeBase -nocolor -search %*
)
