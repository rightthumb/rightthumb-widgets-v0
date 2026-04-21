#!/usr/bin/python3

########################################################################################
import sys, os
###########################################
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'switches')))
import SwitchManager0 as SwitchManager   # type: ignore
###########################################
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'security', 'otp')))
from OTP import OTP   # type: ignore
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################


ss = SwitchManager.y('Code: -code,-secret,-password,-c,-s,-p')

sw = SwitchManager.SwitchManager(ss)
def action():
    code = sw.value('Code')
    if code:
        print(code)
        out = otp = OTP.code({'secret': code})

########################################################################################
if __name__ == '__main__':
    action()