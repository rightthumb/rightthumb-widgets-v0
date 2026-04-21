#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

# importing the required modules

import platform

# printing the Architecture of the OS
print("[+] Architecture :", platform.architecture()[0])

# Displaying the machine
print("[+] Machine :", platform.machine())

# printing the Operating System release information
print("[+] Operating System Release :", platform.release())

# prints the currently using system name
print("[+] System Name :",platform.system())

# This line will print the version of your Operating System
print("[+] Operating System Version :", platform.version())

# This will print the Node or hostname of your Operating System
print("[+] Node: " + platform.node())

# This will print your system platform
print("[+] Platform :", platform.platform())

# This will print the processor information
print("[+] Processor :",platform.processor())