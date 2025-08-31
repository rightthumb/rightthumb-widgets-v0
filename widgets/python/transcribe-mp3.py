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
# import sys, time
##################################################
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');
##################################################


def sw():
	pass
	#b)--> examples
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Segments', '-seg,-clips,-cl,-clip', '120 250 300 400', isRequired=False )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )

_._default_settings_()
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
# __.setting('receipt-log',True)
# __.setting('receipt-file',True)
# __.setting('myFileLocations-skip-validation',False)
# __.setting('require-pipe',False)
# __.setting('require-pipe||file',False)
# __.setting('pre-error',False)
# __.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [],
	'notes': [],
}
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	# _.switches.trigger( 'Ago', _.timeAgo )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );

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


# import os
# from pydub import AudioSegment
# from pocketsphinx import AudioFile, Pocketsphinx
# import subprocess
# def mp3_to_wav_ffmpeg(mp3_file_path):
#     wav_file_path = mp3_file_path.replace('.mp3', '.wav')
#     # Use ffmpeg to convert the file
#     command = f"ffmpeg -i \"{mp3_file_path}\" -ac 1 -ar 16000 \"{wav_file_path}\""
#     subprocess.call(command, shell=True)
#     return wav_file_path

# def mp3_to_wav(mp3_file_path):
# 	audio = AudioSegment.from_mp3(mp3_file_path)
# 	wav_file_path = mp3_file_path.replace('.mp3', '.wav')
# 	audio.export(wav_file_path, format="wav")
# 	return wav_file_path

# def transcribe_segment(wav_file_path, start_time=None, end_time=None):
# 	audio = AudioSegment.from_wav(wav_file_path)
	
# 	# If start_time and end_time are None, transcribe the whole file
# 	if start_time is None or end_time is None:
# 		segment = audio
# 		segment_file_path = wav_file_path
# 	else:
# 		segment = audio[start_time * 1000:end_time * 1000]  # pydub works in milliseconds
# 		segment_file_path = wav_file_path.replace('.wav', f'_segment_{start_time}_{end_time}.wav')
# 		segment.export(segment_file_path, format='wav')

# 	config = {
# 		'verbose': False,
# 		'audio_file': segment_file_path,
# 	}
# 	audio_file = AudioFile(**config)
# 	for phrase in audio_file:
# 		print(phrase.segments(detailed=True))  # You can also use phrase.hypothesis() for simple output

# def parse_timestamps(text):
# 	numbers = [int(num) for num in text.split()]
# 	return [(numbers[i], numbers[i+1]) for i in range(0, len(numbers) - 1, 2)]

# def action():
# 	if _.switches.isActive('Segments'):
# 		segments = parse_timestamps(_.switches.value('Segments'))
# 	else:
# 		segments = [None]  # Use a list with a single None element

# 	for path in _.myData():
# 		wav_file_path = mp3_to_wav_ffmpeg(path)

# 		for segment in segments:
# 			if segment is None:
# 				print(f"Transcribing the entire audio file {path}...")
# 				transcribe_segment(wav_file_path)
# 			else:
# 				start_time, end_time = segment
# 				print(f"Transcribing audio from {start_time} to {end_time} seconds...")
# 				transcribe_segment(wav_file_path, start_time, end_time)




import os
import subprocess
from pydub import AudioSegment
from pocketsphinx import AudioFile, Pocketsphinx

def mp3_to_wav_ffmpeg(mp3_file_path):
    wav_file_path = mp3_file_path.replace('.mp3', '.wav')
    # Use ffmpeg to convert the file, suppressing output
    command = f"ffmpeg -i \"{mp3_file_path}\" -ac 1 -ar 16000 \"{wav_file_path}\""
    subprocess.call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return wav_file_path

def transcribe_segment(wav_file_path, start_time=None, end_time=None):
	audio = AudioSegment.from_wav(wav_file_path)
	
	# If start_time and end_time are None, transcribe the whole file
	if start_time is None or end_time is None:
		segment = audio
		segment_file_path = wav_file_path
	else:
		segment = audio[start_time * 1000:end_time * 1000]  # pydub works in milliseconds
		segment_file_path = wav_file_path.replace('.wav', f'_segment_{start_time}_{end_time}.wav')
		segment.export(segment_file_path, format='wav')

	config = {
		'verbose': False,
		'audio_file': segment_file_path,
	}
	audio_file = AudioFile(**config)
	for phrase in audio_file:
		print(phrase.hypothesis())  # Output only the transcribed text

def parse_timestamps(text):
	numbers = [int(num) for num in text.split()]
	return [(numbers[i], numbers[i+1]) for i in range(0, len(numbers) - 1, 2)]

def action():
	if _.switches.isActive('Segments'):
		segments = parse_timestamps(_.switches.value('Segments'))
	else:
		segments = [None]  # Use a list with a single None element

	for path in _.myData():
		wav_file_path = mp3_to_wav_ffmpeg(path)

		for segment in segments:
			transcribe_segment(wav_file_path, *segment if segment else (None, None))






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
	action(); _.isExit(__file__);

