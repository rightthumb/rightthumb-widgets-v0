@echo off
if [%py%] == [%PY_1%] (
	set py=%PY_2%
	set pip3=%pip3_2%
	set pip=%pip3_2%
) else (
	set py=%PY_1%
	set pip3=%pip3_1%
	set pip=%pip3_1%
)