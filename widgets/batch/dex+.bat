@echo off
call dex -has %* | call p. files -has %* | call p. cat + %*

:: dex = call p. search-indexDB-files %*