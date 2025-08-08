@echo off


rem if not [%1] == [] call p. hotkeys -k + %*
if not [%1] == [] call p. hotkeys -k | p. line + %*
if [%1] == [] call p. hotkeys -k