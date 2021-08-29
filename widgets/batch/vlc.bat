@echo off
start "VIDEO" "D:\Program Files (x86)\VideoLAN\VLC\vlc.exe" %*
rem "D:\Program Files (x86)\VideoLAN\VLC\vlc.exe" %1 --sout=#transcode{vcodec=mp4v,vb=1024,scale=1,height=240,width=320,acodec=mp4a,ab=128,channels=2}:duplicate{dst=std{access=file,mux=mp4,dst=%1
rem "D:\Program Files\VideoLAN\VLC\vlc.exe" %1 --sout=#transcode{vcodec=mp4v,vb=1024,scale=1,height=240,width=320,acodec=mp4a,ab=128,channels=2}:duplicate{dst=std{access=file,mux=mp4,dst=%1
