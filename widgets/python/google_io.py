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

# https://docs.google.com/spreadsheets/d/1eA-baxXeY_6VrnzCTrLwxcTKA62xs116UKQozjElF_k/edit#gid=0
# http://gspread.readthedocs.io/en/latest/oauth2.html
# http://www.makeuseof.com/tag/read-write-google-sheets-python/
# http://www.makeuseof.com/tag/best-free-php-script-resources-online/



# next maybe
# https://www.google.com/search?q=python+google+sheets+to+json&rlz=1C1CHWA_enUS629US631&oq=python+google+sheets+to+json&aqs=chrome..69i57.9687j0j7&sourceid=chrome&ie=UTF-8
# https://gist.github.com/nickjevershed/332d1fa264d1d7d93e95


import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('MapDB-4fbf124ec325.json', scope)

gc = gspread.authorize(credentials)

sheet = gc.open("Test_File").sheet1

all_cells = sheet.range('A1:F3')
print(all_cells)

sheet.update_acell('G1', 'Updated from console')
sheet.update_acell('A6', 'Check this out')

