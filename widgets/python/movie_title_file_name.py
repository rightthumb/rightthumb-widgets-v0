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
#   - abbreviation in switches
#       - ex: -column n s
#           - instead of: -column name size
#       - ex: -sort n
#       - ex: -group n
#   - sort is used for things like size sort by bytes
#   - responsiveness to terminal width
#       - order is important
#       - most important on top
		
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


import subprocess
import os
import shutil

ext = {
	"FFmpeg": {
		"Video": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm", ".mpeg", ".mpg", ".m4v", ".3gp", ".3g2", ".f4v"],
		"Audio": [".mp3", ".wav", ".flac", ".aac", ".m4a", ".ogg", ".opus", ".wma"],
		"Streaming": [".m3u8", ".ts"],
		"ImageSequences": [".jpg", ".png", ".tiff"]
	},
	"ExifTool": {
		"Images": [".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".dng", ".cr2", ".nef", ".orf", ".pef", ".raf", ".raw", ".rw2", ".srw", ".heif", ".heic"],
		"Audio": [".mp3", ".flac", ".aiff", ".ogg", ".opus", ".m4a", ".m4p", ".wav"],
		"Video": [".mov", ".mp4", ".m4v", ".avi", ".mpeg", ".mpg", ".mkv"],
		"Documents": [".pdf", ".eps", ".psd"]
	},
}
extensions=[]
for k in ext:
	for t in ext[k]:
		for e in ext[k][t]:
			if not e in extensions:
				extensions.append(e)
# _.pv(extensions)
# sys.exit()

def determine_tool(path):
	file_extension = os.path.splitext(path)[1]
	for tool, categories in ext.items():
		for category, extensions in categories.items():
			if file_extension in extensions:
				return tool
	return None

def format_for_command_line(text: str) -> str:
	def escape_char(char):
		chars_to_escape = set(r'&*()[]{};$|`<>?"\\')
		if char in chars_to_escape:
			return r"\{}".format(char)
		return char
	text=text.strip()
	# valid_chars = set(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-./")
	valid_chars = set(r" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-./\\:()[]{}!@#$%^&*~+`|;=,'")
	text = ''.join(escape_char(char) for char in text if char in valid_chars)
	# text = ''.join(char for char in text if char in valid_chars)
	text = text.replace(" ", r"\ ")
	return text

def edit_movie_metadata(path, field, new_value):
	tool = determine_tool(path)

	if not tool:
		print(f"Unsupported file format for {path}")
		return

	if tool == "ExifTool":
		path=format_for_command_line(path)
		new_value=format_for_command_line(new_value)
		command = ["exiftool", f"-{field}={new_value}", f'{path}']
	elif tool == "FFmpeg":
		_ext_=path.split('.')[-1]
		# command = ["ffmpeg", "-i", f'"{path}"', "-c", "copy", "-metadata", f'{field}="{new_value}"', f'"{path}_output.{_ext_}"']
		temp_output = f"{path}_temp.{_ext_}"
		command = ["ffmpeg", "-i", path, "-c", "copy", "-metadata", f"{field}={new_value}", temp_output]
	



	else:
		print(f"Unsupported tool: {tool}")
		return
	_.pr(command,c='yellow')
	try:
		subprocess.run(command, check=True)
		if tool == "FFmpeg":
			os.unlink(path)
			shutil.move(f'{path}_temp.{_ext_}',path)


		_.pr(f"Successfully set {field} to {new_value} for {path}",c='green')
	except subprocess.CalledProcessError:
		_.pr(f"Error setting {field} to {new_value} for {path}",c='red')

# Example Usage:
# edit_movie_metadata("/path/to/file.mp4", "title", "New Title")





namePatternsDic = {}
def namePatterns(path):
	if os.sep in path: path=path.split(os.sep)[-1]
	global namePatternsDic
	filename = os.path.basename(path)
	spaced = os.path.splitext(filename)[0].replace('_',' ')
	for part in spaced.split(' '):
		if not part in namePatternsDic:
			namePatternsDic[part] = 0
		namePatternsDic[part] +=1
def nameClean(spaced):
	if os.sep in spaced: spaced=spaced.split(os.sep)[-1]
	global namePatternsDic
	global number_of_files
	if number_of_files == 1: return spaced
	name_parts=[]
	for part in spaced.split(' '):
		if part in namePatternsDic:
			if namePatternsDic[part] >= number_of_files-3:
				pass
			elif not 'DW' == part:
				name_parts.append(part)
	return ' '.join(name_parts)

				

def change_title_to_filename(path,field='title'):


	# Extract the filename without the extension to set as the new title
	filename = os.path.basename(path)
	spaced = os.path.splitext(filename)[0].replace('_',' ')
	new_title = nameClean(spaced)

	try:
		if path.lower().endswith('.mkv'):
			subprocess.run(["mkvpropedit", path, f"--set", f"title={new_title}"], check=True)
			_.pr(f"Successfully changed the title of {path} to {new_title}",c='green')
		else:
			edit_movie_metadata(path, field, new_title)
		# subprocess.run(["mkvpropedit", path, f"--set", f"title={new_title}"], check=True)
	except subprocess.CalledProcessError:
		print(f"Failed to change the title of {path}")
	except FileNotFoundError:
		print("mkvpropedit not found. Please ensure MKVToolNix is installed.")



number_of_files=0
def action():
	global number_of_files
	global extensions
	files=[]
	try:
		for path in _.pp():
			if os.path.isfile(path):
				files.append(path)
	except Exception as e:
		pass
	if not files:
		files=_.fo(r=1)
	# print(files)
	relevant=[]
	for path in files:
		for e in extensions:
			if path.endswith(e):
				if not path in relevant:
					path=path.replace(os.getcwd()+os.sep, '')
					relevant.append(path)
	number_of_files=len(relevant)
	for path in relevant: namePatterns(path)
	for path in relevant:
		if os.path.isfile(path):
			change_title_to_filename(path)


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


