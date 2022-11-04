@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

start "VIDEO" "D:\Program Files (x86)\VideoLAN\VLC\vlc.exe" %*
rem "D:\Program Files (x86)\VideoLAN\VLC\vlc.exe" %1 --sout=#transcode{vcodec=mp4v,vb=1024,scale=1,height=240,width=320,acodec=mp4a,ab=128,channels=2}:duplicate{dst=std{access=file,mux=mp4,dst=%1
rem "D:\Program Files\VideoLAN\VLC\vlc.exe" %1 --sout=#transcode{vcodec=mp4v,vb=1024,scale=1,height=240,width=320,acodec=mp4a,ab=128,channels=2}:duplicate{dst=std{access=file,mux=mp4,dst=%1


 
