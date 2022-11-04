@echo off

if [%1] == [] (
	call p day
) else if [%1] == [1] (
	call p day -ago 1d
) else if [%1] == [2] (
	call p day -ago 2d
) else if [%1] == [3] (
	call p day -ago 3d
) else (
	call p day -ago %*
) 
 
