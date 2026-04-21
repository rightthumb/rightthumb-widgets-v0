@echo off

start "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" %*


goto:eof


:: For testing, hanging issue

 "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  --disable-backgrounding-occluded-windows   --disable-background-timer-throttling   --disable-renderer-backgrounding   --disable-tab-discarding   --disable-occlusion-tracking   --disable-gpu-driver-bug-workarounds   --enable-direct-composition-layers   --enable-features=UseSkiaRenderer   --force-device-scale-factor=1
 
 "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --use-gl=desktop  --disable-backgrounding-occluded-windows  --disable-background-timer-throttling  --disable-renderer-backgrounding  --disable-tab-discarding  --disable-occlusion-tracking  --disable-gpu-driver-bug-workarounds  --enable-direct-composition-layers 
 
 "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
 
 "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
 
 
 
 start "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" ^
--disable-backgrounding-occluded-windows ^
--disable-background-timer-throttling ^
--disable-renderer-backgrounding ^
--disable-tab-discarding ^
--disable-occlusion-tracking ^
--disable-gpu-driver-bug-workarounds ^
--enable-direct-composition-layers ^
--enable-features=UseSkiaRenderer ^
--force-device-scale-factor=1