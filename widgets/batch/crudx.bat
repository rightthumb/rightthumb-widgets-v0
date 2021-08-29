@echo off
CALL crud.bat
type _auto_functions.js > tmpjson.js
type tmpjson.js | find /i /v "staff_availability_json"  > _auto_functions.js