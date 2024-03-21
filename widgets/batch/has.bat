@echo off
set subject=%1
shift
set args=%*
p files -has %subject% %args% | p. cat + %subject%
