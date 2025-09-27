@echo off
set ecoPy=D:\ecology_terminal_framework\eco\python\

if exist "%ecoPy%%1.py" (
	set ecoApp="%ecoPy%%1.py"
	shift
	%py% %ecoApp% %1 %2 %3 %4 %5 %6 %7 %8 %9
) else (
	echo %ecoPy%%1.py not found.
)