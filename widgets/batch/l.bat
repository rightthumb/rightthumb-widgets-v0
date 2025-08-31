@echo off
:: Hybrid script running original l. and new p. line

:::: if no options run as `l .`        - ** --> ADD A DOT AT THE END <-- **
:::: if no options run as `l .`        - ** --> ADD A DOT AT THE END <-- **
:::: if no options run as `l .`        - ** --> ADD A DOT AT THE END <-- **
:::: if no options run as `l .`        - ** --> ADD A DOT AT THE END <-- **
:::: if no options run as `l .`        - ** --> ADD A DOT AT THE END <-- **
:::: if no options run as `l .`        - ** --> ADD A DOT AT THE END <-- **
:::: if no options run as `l .`        - ** --> ADD A DOT AT THE END <-- **

if "%1" == "" (
	wsl
) else (
	call p. line %*
)