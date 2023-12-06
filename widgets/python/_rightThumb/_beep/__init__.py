#!/usr/bin/env python

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import _rightThumb._construct as __
__.v.beep=__.Meta_Namespace()
__.v.beep.timer=None
__.v.beep.print=False
#
# Internal Speaker Beeping Module for Windows
import threading
import time
try:
	import winsound
except Exception as e:
	pass

###
# Notes Config
###


# Set delay tempo
tempo = 0.15

# Setup Notes
notes = {
	"pause": 0,
	"c": 1,
	"c#": 2,
	"d": 3,
	"d#": 4,
	"e": 5,
	"f": 6,
	"f#": 7,
	"g": 8,
	"g#": 9,
	"a": 10,
	"a#": 11,
	"b": 12
}

# Note Types
note_types0 = {
	"sixteenth": 50,
	"eigth": 100,
	"dotted_eigth": 150,
	"quarter": 200,
	"half": 400,
	"whole": 800,
	"triplet": 60
}




############################# START: note
# The original shortest duration is for the sixteenth note (50 ms)
shortest_duration = 50
min_duration_allowed = 400

# The multiplier to scale all durations proportionally
multiplier = min_duration_allowed / shortest_duration

note_types1 = {
	"sixteenth": int(50 * multiplier),
	"eigth": int(100 * multiplier),
	"dotted_eigth": int(150 * multiplier),
	"quarter": int(200 * multiplier),
	"half": int(400 * multiplier),
	"whole": int(800 * multiplier),
	"triplet": int(60 * multiplier)
}
############################# END: note

note_types2 = {
	"sixteenth": 400,     # Adjusted from 50 to 400 ms
	"eigth": 400,         # Adjusted from 100 to 400 ms, can go higher if needed
	"dotted_eigth": 600,  # Adjusted from 150 to 600 ms
	"quarter": 800,       # Adjusted from 200 to 800 ms
	"half": 1200,         # Adjusted from 400 to 1200 ms
	"whole": 2400,        # Adjusted from 800 to 2400 ms
	"triplet": 400        # Adjusted from 60 to 400 ms
}

__.v.beep.note={
	'0': note_types0,
	'1': note_types1,
	'2': note_types2,
}
__.v.beep.type='2'
note_types=__.v.beep.note[__.v.beep.type]
def play_note(octave, note, note_type, timeout_duration=None):

	def play_note_internal(octave, note, note_type, timeout=False):
		minLength = 500
		if not __.v.beep.timer is None: timeout=__.v.beep.timer
		"""Play a note at a certain octave by calculating the frequency of the sound it would represent on the motherboard's speaker."""
		note_types=__.v.beep.note[__.v.beep.type]
		# Match the note and note type to the dictionaries
		note = notes[note]
		note_type = note_types[note_type]

		# Chill for a bit if it's a pause
		if note == 0:
			time.sleep(note_type / 1000)
			return

		# Calculate C for the provided octave
		frequency = 32.7032 * (2 ** octave)

		# Calculate the frequency of the given note
		frequency *= (1.059463094 ** note)
		if note_type < minLength: note_type=minLength
		if __.v.beep.print:
			print('frequency:',frequency)
			print('note_type:',note_type)
		# Beep it up
		try:
			winsound.Beep(int(frequency), note_type)
		except Exception as e:
			if __.v.beep.print:
				print('Err:',e)

		# Delay after the beep so it doesn't all run together
		if timeout:
			time.sleep(tempo)
  # Create a thread to run the play_note_internal function with the necessary arguments
	note_thread = threading.Thread(target=play_note_internal, args=(octave, note, note_type))

	# Start the thread
	note_thread.start()

	# If a timeout is specified, wait for the duration of the timeout
	if timeout_duration is not None:
		note_thread.join(timeout_duration)

		# # If the thread is still alive after the timeout, it means the function is taking too long
		# if note_thread.is_alive():
		# 	# Handle the timeout case, e.g., print a message, stop the note, etc.
		# 	print("Note playing exceeded the time limit.")
		# 	# Optionally, you can forcefully stop the thread here, but it's generally not recommended

# Example usage:
# play_note(4, "c", "quarter")


def beep():
	oct = 3
	play_note(oct, "g", "half")

def mission_impossible():
	try:
		mission_impossible_play()
	except Exception as e:
		pass

def mission_impossible_play():
	oct = 3
	play_note(oct, "g", "half")
	play_note(oct, "g", "half")
	play_note(oct+1, "a#", "quarter")
	play_note(oct+1, "c", "quarter")
	play_note(oct, "g", "half")
	play_note(oct, "g", "half")
	play_note(oct, "f", "quarter")
	play_note(oct,  "f#", "quarter")
	play_note(oct, "g", "half")
	play_note(oct, "g", "half")
	play_note(oct+1, "a#", "quarter")
	play_note(oct+1, "c", "quarter")
	play_note(oct, "g", "half")
	play_note(oct, "g", "half")
	play_note(oct, "f", "quarter")
	play_note(oct,  "f#", "quarter")

def final_fantasy_victory():
	oct = 4
	play_note(oct+1, "c", "triplet")
	play_note(oct+1, "c", "triplet")
	play_note(oct+1, "c", "triplet")
	play_note(oct+1, "c", "quarter")
	play_note(oct, "g#", "quarter")
	play_note(oct, "a#", "quarter")
	play_note(oct+1, "c", "dotted_eigth")
	play_note(oct, "a#", "sixteenth")
	play_note(oct+1, "c", "whole")

def praise_to_the_man():
	oct = 4
	play_note(oct, "c", "quarter")
	play_note(oct, "c", "dotted_eigth")
	play_note(oct, "c", "sixteenth")
	play_note(oct, "e", "eigth")
	play_note(oct, "c", "eigth")
	play_note(oct, "e", "eigth")
	play_note(oct, "g", "eigth")
	play_note(oct+1, "c", "quarter")
	play_note(oct+1, "e", "dotted_eigth")
	play_note(oct+1, "d", "sixteenth")
	play_note(oct+1, "c", "quarter")
	play_note(oct, "g", "quarter")
	play_note(oct, "f", "quarter")
	play_note(oct, "a", "dotted_eigth")
	play_note(oct, "f", "sixteenth")
	play_note(oct, "e", "quarter")
	play_note(oct, "g", "dotted_eigth")
	play_note(oct, "e", "sixteenth")
	play_note(oct, "d", "eigth")
	play_note(oct, "c", "eigth")
	play_note(oct, "d", "eigth")
	play_note(oct, "e", "eigth")
	play_note(oct, "d", "half")
	play_note(oct, "c", "quarter")
	play_note(oct, "c", "dotted_eigth")
	play_note(oct, "c", "sixteenth")
	play_note(oct, "e", "eigth")
	play_note(oct, "c", "eigth")
	play_note(oct, "e", "eigth")
	play_note(oct, "g", "eigth")
	play_note(oct+1, "c", "eigth")
	play_note(oct+1, "e", "dotted_eigth")
	play_note(oct+1, "d", "sixteenth")
	play_note(oct+1, "c", "eigth")
	play_note(oct, "g", "eigth")
	play_note(oct, "f", "eigth")
	play_note(oct, "a", "dotted_eigth")
	play_note(oct, "f", "sixteenth")
	play_note(oct, "e", "eigth")
	play_note(oct, "g", "dotted_eigth")
	play_note(oct, "e", "sixteenth")
	play_note(oct, "d", "eigth")
	play_note(oct, "c", "eigth")
	play_note(oct, "d", "eigth")
	play_note(oct, "e", "eigth")
	play_note(oct, "c", "half")
	play_note(oct+1, "c", "eigth")
	play_note(oct+1, "c", "dotted_eigth")
	play_note(oct+1, "c", "sixteenth")
	play_note(oct, "b", "eigth")
	play_note(oct, "a", "eigth")
	play_note(oct, "g", "eigth")
	play_note(oct, "g", "eigth")
	play_note(oct+1, "c", "quarter")
	play_note(oct+1, "c", "dotted_eigth")
	play_note(oct+1, "c", "sixteenth")
	play_note(oct, "b", "eigth")
	play_note(oct, "a", "eigth")
	play_note(oct, "g", "eigth")
	play_note(oct, "f", "eigth")
	play_note(oct+1, "c", "quarter")
	play_note(oct+1, "c", "dotted_eigth")
	play_note(oct+1, "c", "sixteenth")
	play_note(oct, "b", "eigth")
	play_note(oct, "g", "eigth")
	play_note(oct+1, "d", "whole")
	play_note(oct+1, "c", "eigth")
	play_note(oct, "b", "eigth")
	play_note(oct, "g", "eigth")
	play_note(oct+1, "c", "eigth")
	play_note(oct, "a", "eigth")
	play_note(oct, "g", "eigth")
	play_note(oct, "f", "eigth")
	play_note(oct, "e", "eigth")
	play_note(oct, "d", "eigth")
	play_note(oct, "c", "quarter")
	play_note(oct, "c", "dotted_eigth")
	play_note(oct, "c", "sixteenth")
	play_note(oct, "e", "eigth")
	play_note(oct, "c", "eigth")
	play_note(oct, "e", "eigth")
	play_note(oct, "g", "eigth")
	play_note(oct+1, "c", "quarter")
	play_note(oct+1, "e", "dotted_eigth")
	play_note(oct+1, "d", "sixteenth")
	play_note(oct+1, "c", "quarter")
	play_note(oct, "g", "quarter")
	play_note(oct, "f", "quarter")
	play_note(oct, "a", "dotted_eigth")
	play_note(oct, "f", "sixteenth")
	play_note(oct, "e", "quarter")
	play_note(oct, "g", "dotted_eigth")
	play_note(oct, "e", "sixteenth")
	play_note(oct, "d", "eigth")
	play_note(oct, "c", "eigth")
	play_note(oct, "d", "eigth")
	play_note(oct, "e", "eigth")
	play_note(oct, "c", "whole")

def party_time():
	mission_impossible()
	time.sleep(.4)
	final_fantasy_victory()
	time.sleep(.4)
	praise_to_the_man()

if __name__ == '__main__':
	party_time()

