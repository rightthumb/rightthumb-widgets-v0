#!/usr/bin/env python3
#
# References:
# https://github.com/PyUserInput/PyUserInput
#
# Author: Alexandre C Vieira <acamargo.vieira@gmail.com>
#
# http://alexandrecvieira.droppages.com
#
# I did this little program because I didn't find any indicators that worked the way I wanted, this is the first version with kdialog
#
# Installation:
# sudo apt install kdialog
# sudo mkdir /opt/ss-key-indicator
# sudo cp super-simple-keyboard-indicator /opt/ss-key-indicator/ss-key-indicator
# Set it to boot with the system: python3 /opt/ss-key-indicator/ss-key-indicator
#

__appname__ = "Super Simple Keyboard Indicator"
__version__ = "0.10"
__author__  = "Alexandre C Vieira"
__license__ = "GNU GPL 2.0 or later"

import os, subprocess
from pykeyboard import PyKeyboardEvent

TIMEOUT = 3

class MonitorSuper(PyKeyboardEvent):
	def tap(self, keycode, character, press):
		if press:
			None
		else:
			if character == 'Caps_Lock':
				capsStatus = subprocess.getoutput("xset q | grep Caps | tr -s ' ' | cut -d ' ' -f 5")
				if capsStatus == 'off':
					cmd = "kdialog --title \"%s\" --passivepopup \"<p style='text-align: center'>Caps Lock <b>OFF</b></p>\" %s" % (__appname__, TIMEOUT)
					os.system(cmd)
				if capsStatus == 'on':
					cmd = "kdialog --title \"%s\" --passivepopup \"<p style='text-align: center'>Caps Lock <b>ON</b></p>\" %s" % (__appname__, TIMEOUT)
					os.system(cmd) 
			if character == 'Num_Lock':
				numStatus = subprocess.getoutput("xset q | grep Caps | tr -s ' ' | cut -d ' ' -f 9")
				if numStatus == 'off':
					cmd = "kdialog --title \"%s\" --passivepopup \"<p style='text-align: center'>Num Lock <b>OFF</b></p>\" %s" % (__appname__, TIMEOUT)
					os.system(cmd)
				if numStatus == 'on':
					cmd = "kdialog --title \"%s\" --passivepopup \"<p style='text-align: center'>Num Lock <b>ON</b></p>\" %s" % (__appname__, TIMEOUT)
					os.system(cmd)
			if character == 'Scroll_Lock':
				scrollStatus = subprocess.getoutput("xset q | grep Caps | tr -s ' ' | cut -d ' ' -f 13")
				if scrollStatus == 'off':
					cmd = "kdialog --title \"%s\" --passivepopup \"<p style='text-align: center'>Scroll Lock <b>OFF</b></p>\" %s" % (__appname__, TIMEOUT)
					os.system(cmd)
				if scrollStatus == 'on':
					cmd = "kdialog --title \"%s\" --passivepopup \"<p style='text-align: center'>Scroll Lock <b>ON</b></p>\" %s" % (__appname__, TIMEOUT)
					os.system(cmd)
mon = MonitorSuper()
mon.run()