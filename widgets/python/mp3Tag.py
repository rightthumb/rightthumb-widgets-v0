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

# https://pypi.python.org/pypi/mp3-tagger/1.0
import sys
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

# Create MP3File instance.
mp3 = MP3File(sys.argv[2])

# Get/set/del tags value.
alb = mp3.album
mp3.album = 'some title..'
del mp3.album

"""
Allowed tags:

	- artist;
	- album;
	- song;
	- track;
	- comment;
	- year;
	- genre;
	- band (version 2.x);
	- composer (version 2.x);
	- copyright (version 2.x);
	- url (version 2.x);
	- publisher (version 2.x).
"""

# Get all tags.
tags = mp3.get_tags()
print(tags)

"""
Output:
{'ID3TagV1': {'song': 'Prowler', 'artist': 'Iron Maiden', 'album': 'Iron Maiden',
'year': '1980', 'comment': None, 'track': 1, 'genre': 'Other'},
'ID3TagV2': {'artist': 'Iron Maiden', 'band': 'Iron Maiden', 'album': 'Iron Maiden',
'song': 'Prowler', 'track': '1/9', 'genre': 'Heavy Metal', 'year': '1980'}}
"""

# By default selected tags in both versions.
mp3.set_version(VERSION_BOTH)

# Change to 2.x version.
mp3.set_version(VERSION_2)

# For 1.x version
mp3.set_version(VERSION_1)

# After the tags are edited, you must call the save method.
mp3.save()

