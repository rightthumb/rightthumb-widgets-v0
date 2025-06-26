@echo off


if [%1]==[] (
    echo.
    echo obb index.php
    echo obb wt
    echo obb https://sds.sh/
    echo.


    goto :eof
)

call p. script-helper -t r:_.al -i %* 
echo.