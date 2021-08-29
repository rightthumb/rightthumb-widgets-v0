@echo off
::set thisTimeStamp=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%@%time:~0,2%:%time:~3,2%
set thisTimeStamp=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%.%time:~0,2%.%time:~3,2%
echo %thisTimeStamp% > %widgets%:\tech\scripts\verDate.txt
::echo :)
