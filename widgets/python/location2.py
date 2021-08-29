#!/usr/bin/python3
#835B0032-Legacy
import IP2Location
IP2LocObj = IP2Location.IP2Location()
IP2LocObj.open('IP2LOCATION-LITE-DB11.BIN')
rec = IP2LocObj.get_all(_v.ip)
print rec

