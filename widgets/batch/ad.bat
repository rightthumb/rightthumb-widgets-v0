@echo off

setlocal
set fi=%USERPROFILE%\.rt\profile\life\ads\apps\%1.ad
if not exist %fi% copy %USERPROFILE%\.rt\profile\life\ads\templates\apps.ad %fi%
call n %fi%