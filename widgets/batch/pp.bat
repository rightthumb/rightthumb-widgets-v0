@echo off 

if [%1] == [] call p. paths -m
if not [%1] == [] call p. paths -f %* 
