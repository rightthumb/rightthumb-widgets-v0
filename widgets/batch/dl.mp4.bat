@echo off

echo wsl OR L
echo dl.mp4 https://www.youtube.com/watch?v=34x_GL5Zxpk

rem if [%1] == [] (
rem 	echo dl.mp4 "https://www.youtube.com/watch?v=34x_GL5Zxpk"
rem 	goto:eof
rem )

rem SET VIDEO=%1
rem CALL :dequote VIDEO

rem echo %VIDEO%
rem echo youtube-dl -f bestvideo+bestaudio %VIDEO%
rem youtube-dl -f bestvideo+bestaudio %VIDEO%
rem rem youtube-dl --extract-audio --audio-format mp3 %VIDEO%
rem goto :eof

rem :DeQuote
rem for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
rem goto :eof

rem https://github.com/blackjack4494/yt-dlc

rem sudo wget https://github.com/blackjack4494/yt-dlc/releases/latest/download/youtube-dlc -O /usr/local/bin/youtube-dlc
rem sudo chmod a+rx /usr/local/bin/youtube-dlc
rem sudo chmod 777 /usr/local/bin/youtube-dlc