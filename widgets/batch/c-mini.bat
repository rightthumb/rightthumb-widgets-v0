@echo off
call C:\Users\Scott\.rt\profile\vars\config.bat
call C:\Users\Scott\.rt\profile\vars\personal.bat

SET batch=%widgets%\widgets\batch
SET python=%widgets%\widgets\python
SET myBatch=%myHome%\widgets\batch
SET myPython=%myHome%\widgets\python
SET appPaths=%batch%;%python%;%myBatch%;%myPython%

SET path=%path%;%appPaths%
SET appPaths=