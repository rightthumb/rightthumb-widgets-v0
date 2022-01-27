@echo off 

if [%1] == [] call p paths
if not [%1] == [] call p paths -f %*