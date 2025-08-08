@echo off
if exist "C:\Program Files(x86)\Microsoft Office\root\Office16\scanpst.exe" echo Outlook 2016 Click-to-Run installation on a 32-bit
if exist "C:\Program Files\Microsoft Office\root\Office16\scanpst.exe" echo Outlook 2016 Click-to-Run installation on a 64-bit
if exist "C:\Program Files(x86)\Microsoft Office\Office16\scanpst.exe" echo Outlook 2016 MSI-based installation on a 32-bit
if exist "C:\Program Files\Microsoft Office\Office16\scanpst.exe" echo Outlook 2016 MSI-based installation on a 64-bit
if exist "C:\Program Files\Microsoft Office 15\root\office15\scanpst.exe" echo Outlook 2013 Click-to-Run installation on a 64-bit
if exist "C:\Program Files(x86)\Microsoft Office 15\root\office15\scanpst.exe" echo Outlook 2013 Click-to-Run installation on a 32-bit
if exist "C:\Program Files\Microsoft Office\Office15\scanpst.exe" echo Outlook 2013 MSI-based installation on a 64-bit
if exist "C:\Program Files(x86)\Microsoft Office\Office15\scanpst.exe" echo Outlook 2013 MSI-based installation on a 32-bit
if exist "C:\Program Files\Microsoft Office\Office14\scanpst.exe" echo Outlook 2010 on a 64-bit
if exist "C:\Program Files\Microsoft Office(x86)\Office14\scanpst.exe" echo Outlook 2010 on a 32-bit
if exist "C:\Program Files\Microsoft Office\Office12\scanpst.exe" echo Outlook 2007 on a 64-bit
if exist "C:\Program Files(x86)\Microsoft Office\Office12\scanpst.exe" echo Outlook 2007 on a 32-bit
if exist "C:\Program Files\Common Files\System\MSMAPI\1033\scanpst.exe" echo Other, this less 2007 and this greater 2000
if exist "C:\Program Files\Common Files\System\Mapi\1033\NT\scanpst.exe" echo Other, Windows NT and Windows 2000
if exist "C:\Program Files\Common Files\System\Mapi\1033\95\scanpst.exe" echo Other, Windows 95 and Windows 98