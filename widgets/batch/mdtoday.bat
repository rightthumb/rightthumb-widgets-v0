@echo off
set today=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%
md %today%
cd %today%
title %today%
cd
:also mdt
