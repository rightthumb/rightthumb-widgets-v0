@echo off
set subject=%1
shift
set args=%2 %3 %4 %5 %6 %7 %8 %9
p files -has %subject%  | p. cat + %subject% %args%