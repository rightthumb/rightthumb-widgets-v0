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


##################################################
import sys, time
##################################################
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################


def sw():
	pass
	#b)--> examples
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log',True)
__.setting('receipt-file',True)
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
# columns used for
# 	- abbreviation in switches
#		- ex: -column n s
#			- instead of: -column name size
#		- ex: -sort n
#		- ex: -group n
# 	- sort is used for things like size sort by bytes
# 	- responsiveness to terminal width
# 		- order is important
# 		- most important on top
		
		# this is used for personal usage to programmatically generate columns
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] },
		},
	}


def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )

def _local_(do): exec(do)

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# globals()['var']
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start


class BEEPS:
	def __init__( self ):
		###
		# Notes Config
		###

		# Set delay tempo
		self.tempo = 0.15
		# tempo = 1

		# Setup Notes
		self.notes = {}
		self.notes["pause"] = 0
		self.notes["c"] = 1
		self.notes["c#"] = 2
		self.notes["d"] = 3
		self.notes["d#"] = 4
		self.notes["e"] = 5
		self.notes["f"] = 6
		self.notes["f#"] = 7
		self.notes["g"] = 8
		self.notes["g#"] = 9
		self.notes["a"] = 10
		self.notes["a#"] = 11
		self.notes["b"] = 12

		# Note Types
		self.note_types = {}
		self.note_types["sixteenth"] = 50
		self.note_types["eigth"] = 100
		self.note_types["dotted_eigth"] = 150
		self.note_types["quarter"] = 200
		self.note_types["half"] = 400
		self.note_types["whole"] = 800
		self.note_types["triplet"] = 60
	def play_note( self, octave, note, note_type ):
		"""Play a note at a certain octave by calculating the frequency of the sound it would represent on the motherboard's speaker."""

		# Match the note and note type to the dictionaries
		note = self.notes[note]
		note_type = self.note_types[note_type]

		# Chill for a bit if it's a pause
		if not note:
			time.sleep(note_type/1000)
			return

		# Calculate C for the provided octave
		frequency = 32.7032 * (2**octave)

		# Calculate the frequency of the given note
		frequency *= 1.059463094**note

		# Beep it up
		try:
			winsound.Beep(int(frequency), note_type)
			# Delay after the beep so it doesn't all run together
			time.sleep(self.tempo)
		except Exception as e:
			# frameinfo = getframeinfo(currentframe()); _.pr( _.addComma(frameinfo.lineno),'\t', e,c='red');
			pass

	def simple_beep(self):
		_oct = 2
		self.play_note(_oct, 'g', 'quarter')

	def simple_beep2(self):
		_oct = 3
		self.play_note(_oct, 'e', 'quarter')
	def note(self,n='c',*args):
		_oct=3
		nt='half'
		for a in args:
			if type(a) == str: nt=a
			if type(a) == int: _oct=a
		self.play_note(_oct, n, nt)

def wait():

	print('w')
	while True:
		if keyboard.is_pressed('enter'):
			print('!')
			break
	time.sleep(.5)
	while True:
		if keyboard.is_pressed('enter'):
			print('!')
			break


import os
def action():
	load(); global logins;
	lines=[]
	wait()
	timing=1
	for login in logins:
		lg=login['login']
		parts=lg.split('@')
		user=parts[0]
		server=parts[1].split('.')[0]
		pw=_vault.imp.s.de(login['password'])
		_copy.imp.copy( f'.ssh {server} {user}'  )
		beepy.simple_beep2()
		time.sleep(timing)
		wait()
		_copy.imp.copy( 'yes'  )
		beepy.simple_beep2()
		time.sleep(timing)
		wait()
		_copy.imp.copy( pw ,p=0 )
		print('**********')
		beepy.simple_beep2()
		time.sleep(timing)
		wait()
		


def load():
	global logins
	logins = _.getTable2(_v.rt+os.sep+'logins.json')

_vault = _.regImp( __.appReg, '_rightThumb._vault' )
# _vault.imp.s.de(  )
_copy = _.regImp( __.appReg, '-copy' )

import winsound
import keyboard
beepy=BEEPS()
# beepy.simple_beep(); sys.exit();
##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action()
	_.isExit(__file__)

