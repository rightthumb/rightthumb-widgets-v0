@echo off

setlocal
set fi=C:\Users\Scott\.rt\profile\life\ads\apps\%1.ad
if not exist %fi% copy C:\Users\Scott\.rt\profile\life\ads\templates\apps.ad %fi%
call n %fi%