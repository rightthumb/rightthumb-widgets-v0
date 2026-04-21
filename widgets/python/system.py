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

import socket
import os 
import sys
import platform
import psutil
import uuid

print( "Name: " +socket.gethostname() )
print( "FQDN: " +socket.getfqdn() )
print( "System Platform: "+sys.platform )
print( "Machine: " +platform.machine() )
print( "Node " +platform.node() )
print( "Platform: "+platform.platform() )
print( "Pocessor: " +platform.processor() )
print( "System OS: "+platform.system() )
print( "Release: " +platform.release() )
print( "Version: " +platform.version() )
print( "Number of CPUs: " +str(psutil.cpu_count()) )
print( "Number of Physical CPUs: " +str(psutil.cpu_count(logical=False)) )
#Need  Model of Computer i.e.  HP Compaq 8100 Elite SFF, HP X600 workstation
#need Ram
#need Disk space
#Need Manufacturer i.e. HP, Dell, Lenova

