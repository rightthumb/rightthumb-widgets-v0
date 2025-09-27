@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

set funcListFile=%mytables%\base_functions.txt
type "%widgets%\widgets\python\_rightThumb\_base3\__init__.py" | p. line + "def " - # --c > %tmpf0%
rem type "%widgets%\widgets\python\_rightThumb\_base3\__init__.py" | p. line + "def " - " def " # --c > %tmpf0%
type %tmpf0% | p. line - __init__ --c -p ( 0 --c > %tmpf1%
type %tmpf1% | p. line -p "def " 1 > %tmpf2%
type %tmpf2% > %funcListFile%
call n %funcListFile%


set funcListFile=%mytables%\base_functions2.txt
type "%widgets%\widgets\python\_rightThumb\_base3\__init__.py" | p. line - " def " > %tmpf9%
type %tmpf9% | p. line + "def " - " def " # --c > %tmpf0%
type %tmpf0% | p. line - __init__ --c -p ( 0 --c > %tmpf1%
type %tmpf1% | p. line -p "def " 1 > %tmpf2%
type %tmpf2% > %funcListFile%
call n %funcListFile%

echo includes function in classes