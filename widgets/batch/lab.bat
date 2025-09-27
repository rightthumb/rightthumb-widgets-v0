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

SET lab=%*
if [%1] == [autocls] set lab=cls

IF NOT ["%lab%"] == [""] (
	set "terminalTitle=loc-%Session_ID_Suffix% :: %lab%"
) else (
	set "terminalTitle=loc-%Session_ID_Suffix%"
)
TITLE %vpDot%%terminalTitle%

if [%1] == [autocls] set autocls=1