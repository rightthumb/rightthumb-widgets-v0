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
# https://pypi.python.org/pypi/pinterest-client/1.0.2
from pinterest import Pinterest
import sys

import json

# C:\Python27\Lib\site-packages\pinterest\Pinterest.py

##### KILL SWITCH
# sys.exit()

# print sys.argv[3]

pinterest = Pinterest(username_or_email='scott.reph@gmail.com', password='9111436')

# Login to pinterest site, if 'ok' return True otherwise return False
logged_in = pinterest.login()

# Get all boards of logged in user
# boards = pinterest.boards()
# boards = pinterest.search_boards(query='--Rel')
# for board in boards:
	# print board['name']

# print boards
# print json.dumps(boards, sort_keys=True, indent=4, separators=(',', ': '))



# print json.dumps(boards)

# pins = pinterest.search_pins(query='461548661794872237')
# pinID = '461548661794872237'
# pinID = sys.argv[3]


# with open('exportedIDs.txt') as f:
# with open('IDs.txt') as f:
#     IDs = f.read().splitlines()

# for pinID in IDs:
#     try:
#         pins = pinterest.thisPin(pin=pinID)
#         link = ''
#         try:
#             link = pins['pins'][pinID]['tracked_link']
#         except Exception as e:
#             pass
#         print str(pinID) + ',' + str(link)
#         with open('pin_url.csv','a') as logFile:
#             logFile.write(str('\n' + pinID) + ',' + str(link))
#     except Exception as e:
#         pass
data = pinterest.thisPin(pin=sys.argv[0])
jsonData = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
print jsonData
print
print 'saved to: pinterestData_dump_pin.json'
# jsonFile = 'pinterestData_dump_boards.json'
jsonFile = 'pinterestData_dump_pin.json'
obj = open(jsonFile, 'wb')
obj.write(jsonData)
obj.close



