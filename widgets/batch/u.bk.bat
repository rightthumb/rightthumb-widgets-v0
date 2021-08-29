@echo off
IF NOT EXIST %myPython%\_rightThumb\ (md %myPython%\_rightThumb\)
xcopy /s/d/y/c %python%\_rightThumb\*.* %myPython%\_rightThumb\