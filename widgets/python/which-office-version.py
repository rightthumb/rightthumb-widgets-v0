#!/usr/bin/python3
import os
table = [
	{
		"path": "C:\\Program Files(x86)\\Microsoft Office\\root\\Office16",
		"version": "Outlook 2016 Click-to-Run installation on a 32-bit"
	},
	{
		"path": "C:\\Program Files\\Microsoft Office\\root\\Office16",
		"version": "Outlook 2016 Click-to-Run installation on a 64-bit"
	},
	{
		"path": "C:\\Program Files(x86)\\Microsoft Office\\Office16",
		"version": "Outlook 2016 MSI-based installation on a 32-bit"
	},
	{
		"path": "C:\\Program Files\\Microsoft Office\\Office16",
		"version": "Outlook 2016 MSI-based installation on a 64-bit"
	},
	{
		"path": "C:\\Program Files\\Microsoft Office 15\\root\\office15",
		"version": "Outlook 2013 Click-to-Run installation on a 64-bit"
	},
	{
		"path": "C:\\Program Files(x86)\\Microsoft Office 15\\root\\office15",
		"version": "Outlook 2013 Click-to-Run installation on a 32-bit"
	},
	{
		"path": "C:\\Program Files\\Microsoft Office\\Office15",
		"version": "Outlook 2013 MSI-based installation on a 64-bit"
	},
	{
		"path": "C:\\Program Files(x86)\\Microsoft Office\\Office15",
		"version": "Outlook 2013 MSI-based installation on a 32-bit"
	},
	{
		"path": "C:\\Program Files\\Microsoft Office\\Office14",
		"version": "Outlook 2010 on a 64-bit"
	},
	{
		"path": "C:\\Program Files\\Microsoft Office(x86)\\Office14",
		"version": "Outlook 2010 on a 32-bit"
	},
	{
		"path": "C:\\Program Files\\Microsoft Office\\Office12",
		"version": "Outlook 2007 on a 64-bit"
	},
	{
		"path": "C:\\Program Files(x86)\\Microsoft Office\\Office12",
		"version": "Outlook 2007 on a 32-bit"
	},
	{
		"path": "C:\\Program Files\\Common Files\\System\\MSMAPI\\1033",
		"version": "Other, this less 2007 and this greater 2000"
	},
	{
		"path": "C:\\Program Files\\Common Files\\System\\Mapi\\1033\\NT",
		"version": "Other, Windows NT and Windows 2000"
	},
	{
		"path": "C:\\Program Files\\Common Files\\System\\Mapi\\1033\\95",
		"version": "Other, Windows 95 and Windows 98"
	}
]


if __name__ == '__main__':

	#i) instructionst change below variable

	which = 'scan'

	if which == 'bat':
		lines=[]
		lines.append('@echo off')
		for rec in table:
			lines.append('if exist "'+rec['path']+'\\'+'scanpst.exe'+'" echo '+rec['version'])
			# lines.append('if exist "'+rec['path']+'\\'+'scanpst.exe" (')
			# lines.append('    set "tmpversion='+rec['version']+'"')
			# lines.append('    echo %tmpversion%')
			# lines.append(')')
			# lines.append('')
			# '" echo "'+rec['version']+'"'
		lines.append('')
		for line in lines:
			print(line)

	if which == 'scan':
		for rec in table:
			if os.path.isfile(rec['path']+'\\'+'scanpst.exe'):
				print(rec['version'])

