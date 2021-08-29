#!/usr/bin/python3
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