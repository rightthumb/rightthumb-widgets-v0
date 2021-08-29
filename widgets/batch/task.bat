@echo off
rem tasklist | f %1
tasklist | p cmd2table -print | p printTable -sort image_name - svchost -s image_name + .exe %*  
