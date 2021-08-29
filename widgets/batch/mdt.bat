@echo off
set today=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%
md %today%
cd %today%
title %today%
cd
call mdtShift

rem cd>>%mdt%
:also mdtoday