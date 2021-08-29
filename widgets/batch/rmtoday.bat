@echo off
IF EXIST %today% ( rmdir %today% /S )
IF EXIST ../%today% ( 
	cd..
	rmdir %today% /S 
	)
