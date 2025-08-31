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

#835B0032-Legacy
import IP2Location
IP2LocObj = IP2Location.IP2Location()
IP2LocObj.open('IP2LOCATION-LITE-DB11.BIN')
rec = IP2LocObj.get_all(_v.ip)
print rec



