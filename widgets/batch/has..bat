@echo off
set aliasFo=%1
set subject=%2
set args=%3 %4 %5 %6 %7 %8 %9
p files -folder %aliasFo% -has %subject%  | p. cat + %subject% %args%
