@echo off

call p. folders + __pycache__ -folder D:\.rightthumb-widgets\widgets\python\_rightThumb\_base3\library --c > %stmp%-lib.cache.folders
call p. script-helper -f %stmp%-lib.cache.folders --file-contains FolderPath > %stmp%-lib.cache.valid

set /p _valid=<%stmp%-lib.cache.valid
echo Valid: %_valid%

if "%_valid%"=="yes" (
    call p. folders + __pycache__ -folder D:\.rightthumb-widgets\widgets\python\_rightThumb\_base3\library --c | .mx rmdir /s/q
)