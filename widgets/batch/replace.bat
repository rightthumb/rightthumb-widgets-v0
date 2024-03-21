@echo off
if [%3] == [] (
	p files -has "%1" --c | p. replaceText -replace "%1" -insert "%2"
) else (
	p files + %1 -has "%2" --c | p. replaceText -replace "%2" -insert "%3"
)
