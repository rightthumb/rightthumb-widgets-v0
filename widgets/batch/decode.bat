@echo off
cls
title decode
echo                  ...               decode               ....
title                  ...               decode               ....
echo Past Code Here > in.txt
in.txt
echo input file in.txt
set /p ext=Enter output extention .txt ::
base64 -d -n in.txt out_file.%ext%
echo done

cls
echo                  ...               AVG SCAN               ....
title                  ...               AVG SCAN               ....


"D:\Program Files\Grisoft\AVG Free\avgscan.exe" /SCAN /TRASH /IGNLOCKED "out_file.%ext%"
echo Scan Complete

cls
echo                  ...               Run File               ....
title                  ...               Run File               ....


"out_file.%ext%"
cls

echo                  ...               Clear Input File               ....
title                  ...               Clear Input File               ....

del in.txt /q