@echo off
set pulse="C:\Program Files (x86)\PulseAudio\bin\pulseaudio.exe"
@REM %pulse%  -n --load=module-native-protocol-tcp auth-anonymous=1

mkdir "C:\Program Files (x86)\PulseAudio\etc\pulse\daemon.conf.d"

@REM %pulse% -n --load="module-native-protocol-tcp"
%pulse% -n -F "%userprofile%\.rt\default.pa"