: from dnd script
@echo off

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
set browser_app=D:\Users\Scott\AppData\Local\Google\Chrome\Application\chrome.exe
set www0=https://mail.google.com/mail/?shva=1#search/
set www1=

	start "%browser_app%" "%www0%+%1%www1%"
Charecters not allowed in var set so....

*** replace encapsulating url from above vars to change search ***
	start "%browser_app%" "https://mail.google.com/mail/?shva=1#search/"
:END NOTES








:ONE
echo Search level: ONE variable
start "%browser_app%" "https://mail.google.com/mail/?shva=1#search/+%1"
GOTO END


:TWO
echo Search level: TWO variables
start "%browser_app%" "https://mail.google.com/mail/?shva=1#search/+%1+%2"
GOTO END


:THREE
echo Search level: THREE variables
start "%browser_app%" "https://mail.google.com/mail/?shva=1#search/+%1+%2+%3"
GOTO END


:FOUR
echo Search level: FOUR variables
start "%browser_app%" "https://mail.google.com/mail/?shva=1#search/+%1+%2+%3+%4"
GOTO END


:FIVE
echo Search level: FIVE variables
start "%browser_app%" "https://mail.google.com/mail/?shva=1#search/+%1+%2+%3+%4+%5"
GOTO END

:NULL
echo NULL
GOTO END

:END

