@echo off
cd > %tmpf%
SET /p wsl_path=<%tmpf%
wsl --cd "%wsl_path%"