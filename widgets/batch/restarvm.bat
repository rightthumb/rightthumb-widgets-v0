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

set /p confirm= Are you sure you want to shutdown vm* and restart?: 
taskkill /im vm* /f
start "D:\Program Files (x86)\VMware\VMware Workstation\" "D:\Program Files (x86)\VMware\VMware Workstation\vmnat.exe"
start "D:\Windows\SysWOW64\" "D:\Windows\SysWOW64\vmnat.exe"
start "D:\Program Files (x86)\VMware\VMware Workstation\" "D:\Program Files (x86)\VMware\VMware Workstation\vmware-authd.exe"
start "D:\Program Files (x86)\VMware\VMware Workstation\" "D:\Program Files (x86)\VMware\VMware Workstation\VMnetDHCP.exe"
start "D:\Windows\SysWOW64\" "D:\Windows\SysWOW64\vmnetdhcp.exe"
start "D:\Program Files (x86)\Common Files\VMware\USB\" "D:\Program Files (x86)\Common Files\VMware\USB\vmware-usbarbitrator64.exe"
start "D:\Program Files (x86)\VMware\VMware Workstation\" "D:\Program Files (x86)\VMware\VMware Workstation\vmware-hostd.exe"
start "D:\Program Files (x86)\VMware\VMware Workstation\" "D:\Program Files (x86)\VMware\VMware Workstation\vmware-tray.exe"
start "D:\Program Files (x86)\VMware\VMware Workstation\" "D:\Program Files (x86)\VMware\VMware Workstation\vmware-unity-helper.exe"
start "D:\Program Files (x86)\VMware\VMware Workstation\" "D:\Program Files (x86)\VMware\VMware Workstation\vmware-vmx.exe"
start "D:\Program Files (x86)\VMware\VMware Workstation\x64\" "D:\Program Files (x86)\VMware\VMware Workstation\x64\vmware-vmx.exe"


 
