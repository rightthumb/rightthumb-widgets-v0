@echo off
taskkill /im explorer.exe /f
ping google.com > null
start explorer.exe
del null

