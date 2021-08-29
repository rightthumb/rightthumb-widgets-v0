@echo off

ffmpeg -i %1 -codec:a libmp3lame -qscale:a 2 output.mp3