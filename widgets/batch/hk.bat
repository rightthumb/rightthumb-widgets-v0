@echo off

rem same as kw
rem same as kw

rem if not [%1] == [] call p KeyWise -k + %*
if not [%1] == [] call p KeyWise -k | p line + %*
if [%1] == [] call p KeyWise -k 
