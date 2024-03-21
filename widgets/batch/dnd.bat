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



 CALL p. dnd -ss


GOTO:EOF
if [%1] == [] GOTO NULL
set browser_app=

if NOT [%5] == [] GOTO FIVE
if NOT [%4] == [] GOTO FOUR
if NOT [%3] == [] GOTO THREE
if NOT [%2] == [] GOTO TWO

GOTO ONE

if [%1] == [] GOTO END







:NOTES
GOTO END
set browser_app=%USERPROFILE%\AppData\Local\Google\Chrome\Application\chrome.exe
set www0=http://www.google.com/#hl=en&newwindow=1&safe=off&q=+dnd
set www1=&aq=f&aqi=g1g-z1g8&aql=&oq=&gs_rfai=&fp=84c7fb41710deb10

    start "%browser_app%" "%www0%+%1%www1%"
Charecters not allowed in var set so....

*** replace encapsulating url from above vars to change search ***
    start "%browser_app%" "http://www.google.com/#hl=en&newwindow=1&safe=off&q=+dnd&aq=f&aqi=g1g-z1g8&aql=&oq=&gs_rfai=&fp=84c7fb41710deb10"
:END NOTES








:ONE
echo Search level: ONE variable
start "%browser_app%" "http://www.google.com/#hl=en&newwindow=1&safe=off&q=+dnd+%1&aq=f&aqi=g1g-z1g8&aql=&oq=&gs_rfai=&fp=84c7fb41710deb10"
GOTO END


:TWO
echo Search level: TWO variables
start "%browser_app%" "http://www.google.com/#hl=en&newwindow=1&safe=off&q=+dnd+%1+%2&aq=f&aqi=g1g-z1g8&aql=&oq=&gs_rfai=&fp=84c7fb41710deb10"
GOTO END


:THREE
echo Search level: THREE variables
start "%browser_app%" "http://www.google.com/#hl=en&newwindow=1&safe=off&q=+dnd+%1+%2+%3&aq=f&aqi=g1g-z1g8&aql=&oq=&gs_rfai=&fp=84c7fb41710deb10"
GOTO END


:FOUR
echo Search level: FOUR variables
start "%browser_app%" "http://www.google.com/#hl=en&newwindow=1&safe=off&q=+dnd+%1+%2+%3+%4&aq=f&aqi=g1g-z1g8&aql=&oq=&gs_rfai=&fp=84c7fb41710deb10"
GOTO END


:FIVE
echo Search level: FIVE variables
start "%browser_app%" "http://www.google.com/#hl=en&newwindow=1&safe=off&q=+dnd+%1+%2+%3+%4+%5&aq=f&aqi=g1g-z1g8&aql=&oq=&gs_rfai=&fp=84c7fb41710deb10"
GOTO END

:NULL
echo NULL
GOTO END

:END



 
