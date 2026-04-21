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
import os, sys, time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	### EXAMPLE: END

### EXAMPLE: START
# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
#     finds the file in probable locations
#     and 
#         if  _.autoBackupData = True
#         and __.releaseAcquiredData = True
#             GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#         you can run apps on usb at a clients office
#             when you get home run: p app -loadepoch epoch 
#                 backed up
#                     pipe
#                     files
#                     tables
### EXAMPLE: END
_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
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
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	### EXAMPLE: START
	# _.default_switch_trigger('Plus', trigger_plus)
	# _.switches.trigger( 'Files',_.inRelevantFolder )    
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START

table = [
			{
				"Extension": ".aac",
				"Kind of document": "AAC audio",
				"MIME Type": "audio/aac"
			},
			{
				"Extension": ".abw",
				"Kind of document": "AbiWord document",
				"MIME Type": "application/x-abiword"
			},
			{
				"Extension": ".arc",
				"Kind of document": "Archive document (multiple files embedded)",
				"MIME Type": "application/x-freearc"
			},
			{
				"Extension": ".avif",
				"Kind of document": "AVIF image",
				"MIME Type": "image/avif"
			},
			{
				"Extension": ".avi",
				"Kind of document": "AVI: Audio Video Interleave",
				"MIME Type": "video/x-msvideo"
			},
			{
				"Extension": ".azw",
				"Kind of document": "Amazon Kindle eBook format",
				"MIME Type": "application/vnd.amazon.ebook"
			},
			{
				"Extension": ".bin",
				"Kind of document": "Any kind of binary data",
				"MIME Type": "application/octet-stream"
			},
			{
				"Extension": ".bmp",
				"Kind of document": "Windows OS/2 Bitmap Graphics",
				"MIME Type": "image/bmp"
			},
			{
				"Extension": ".bz",
				"Kind of document": "BZip archive",
				"MIME Type": "application/x-bzip"
			},
			{
				"Extension": ".bz2",
				"Kind of document": "BZip2 archive",
				"MIME Type": "application/x-bzip2"
			},
			{
				"Extension": ".cda",
				"Kind of document": "CD audio",
				"MIME Type": "application/x-cdf"
			},
			{
				"Extension": ".csh",
				"Kind of document": "C-Shell script",
				"MIME Type": "application/x-csh"
			},
			{
				"Extension": ".css",
				"Kind of document": "Cascading Style Sheets (CSS)",
				"MIME Type": "text/css"
			},
			{
				"Extension": ".csv",
				"Kind of document": "Comma-separated values (CSV)",
				"MIME Type": "text/csv"
			},
			{
				"Extension": ".doc",
				"Kind of document": "Microsoft Word",
				"MIME Type": "application/msword"
			},
			{
				"Extension": ".docx",
				"Kind of document": "Microsoft Word (OpenXML)",
				"MIME Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
			},
			{
				"Extension": ".eot",
				"Kind of document": "MS Embedded OpenType fonts",
				"MIME Type": "application/vnd.ms-fontobject"
			},
			{
				"Extension": ".epub",
				"Kind of document": "Electronic publication (EPUB)",
				"MIME Type": "application/epub+zip"
			},
			{
				"Extension": ".gz",
				"Kind of document": "GZip Compressed Archive",
				"MIME Type": "application/gzip"
			},
			{
				"Extension": ".gif",
				"Kind of document": "Graphics Interchange Format (GIF)",
				"MIME Type": "image/gif"
			},
			{
				"Extension": ".htm .html",
				"Kind of document": "HyperText Markup Language (HTML)",
				"MIME Type": "text/html"
			},
			{
				"Extension": ".ico",
				"Kind of document": "Icon format",
				"MIME Type": "image/vnd.microsoft.icon"
			},
			{
				"Extension": ".ics",
				"Kind of document": "iCalendar format",
				"MIME Type": "text/calendar"
			},
			{
				"Extension": ".jar",
				"Kind of document": "Java Archive (JAR)",
				"MIME Type": "application/java-archive"
			},
			{
				"Extension": ".jpeg .jpg",
				"Kind of document": "JPEG images",
				"MIME Type": "image/jpeg"
			},
			{
				"Extension": ".js",
				"Kind of document": "JavaScript",
				"MIME Type": "text/javascript (Specifications: HTML and its reasoning, and IETF)"
			},
			{
				"Extension": ".json",
				"Kind of document": "JSON format",
				"MIME Type": "application/json"
			},
			{
				"Extension": ".jsonld",
				"Kind of document": "JSON-LD format",
				"MIME Type": "application/ld+json"
			},
			{
				"Extension": ".mid .midi",
				"Kind of document": "Musical Instrument Digital Interface (MIDI)",
				"MIME Type": "audio/midi audio/x-midi"
			},
			{
				"Extension": ".mjs",
				"Kind of document": "JavaScript module",
				"MIME Type": "text/javascript"
			},
			{
				"Extension": ".mp3",
				"Kind of document": "MP3 audio",
				"MIME Type": "audio/mpeg"
			},
			{
				"Extension": ".mp4",
				"Kind of document": "MP4 video",
				"MIME Type": "video/mp4"
			},
			{
				"Extension": ".mpeg",
				"Kind of document": "MPEG Video",
				"MIME Type": "video/mpeg"
			},
			{
				"Extension": ".mpkg",
				"Kind of document": "Apple Installer Package",
				"MIME Type": "application/vnd.apple.installer+xml"
			},
			{
				"Extension": ".odp",
				"Kind of document": "OpenDocument presentation document",
				"MIME Type": "application/vnd.oasis.opendocument.presentation"
			},
			{
				"Extension": ".ods",
				"Kind of document": "OpenDocument spreadsheet document",
				"MIME Type": "application/vnd.oasis.opendocument.spreadsheet"
			},
			{
				"Extension": ".odt",
				"Kind of document": "OpenDocument text document",
				"MIME Type": "application/vnd.oasis.opendocument.text"
			},
			{
				"Extension": ".oga",
				"Kind of document": "OGG audio",
				"MIME Type": "audio/ogg"
			},
			{
				"Extension": ".ogv",
				"Kind of document": "OGG video",
				"MIME Type": "video/ogg"
			},
			{
				"Extension": ".ogx",
				"Kind of document": "OGG",
				"MIME Type": "application/ogg"
			},
			{
				"Extension": ".opus",
				"Kind of document": "Opus audio",
				"MIME Type": "audio/opus"
			},
			{
				"Extension": ".otf",
				"Kind of document": "OpenType font",
				"MIME Type": "font/otf"
			},
			{
				"Extension": ".png",
				"Kind of document": "Portable Network Graphics",
				"MIME Type": "image/png"
			},
			{
				"Extension": ".pdf",
				"Kind of document": "Adobe Portable Document Format (PDF)",
				"MIME Type": "application/pdf"
			},
			{
				"Extension": ".php",
				"Kind of document": "Hypertext Preprocessor (Personal Home Page)",
				"MIME Type": "application/x-httpd-php"
			},
			{
				"Extension": ".ppt",
				"Kind of document": "Microsoft PowerPoint",
				"MIME Type": "application/vnd.ms-powerpoint"
			},
			{
				"Extension": ".pptx",
				"Kind of document": "Microsoft PowerPoint (OpenXML)",
				"MIME Type": "application/vnd.openxmlformats-officedocument.presentationml.presentation"
			},
			{
				"Extension": ".rar",
				"Kind of document": "RAR archive",
				"MIME Type": "application/vnd.rar"
			},
			{
				"Extension": ".rtf",
				"Kind of document": "Rich Text Format (RTF)",
				"MIME Type": "application/rtf"
			},
			{
				"Extension": ".sh",
				"Kind of document": "Bourne shell script",
				"MIME Type": "application/x-sh"
			},
			{
				"Extension": ".svg",
				"Kind of document": "Scalable Vector Graphics (SVG)",
				"MIME Type": "image/svg+xml"
			},
			{
				"Extension": ".swf",
				"Kind of document": "Small web format (SWF) or Adobe Flash document",
				"MIME Type": "application/x-shockwave-flash"
			},
			{
				"Extension": ".tar",
				"Kind of document": "Tape Archive (TAR)",
				"MIME Type": "application/x-tar"
			},
			{
				"Extension": ".tif .tiff",
				"Kind of document": "Tagged Image File Format (TIFF)",
				"MIME Type": "image/tiff"
			},
			{
				"Extension": ".ts",
				"Kind of document": "MPEG transport stream",
				"MIME Type": "video/mp2t"
			},
			{
				"Extension": ".ttf",
				"Kind of document": "TrueType Font",
				"MIME Type": "font/ttf"
			},
			{
				"Extension": ".txt",
				"Kind of document": "Text, (generally ASCII or ISO 8859-n)",
				"MIME Type": "text/plain"
			},
			{
				"Extension": ".vsd",
				"Kind of document": "Microsoft Visio",
				"MIME Type": "application/vnd.visio"
			},
			{
				"Extension": ".wav",
				"Kind of document": "Waveform Audio Format",
				"MIME Type": "audio/wav"
			},
			{
				"Extension": ".weba",
				"Kind of document": "WEBM audio",
				"MIME Type": "audio/webm"
			},
			{
				"Extension": ".webm",
				"Kind of document": "WEBM video",
				"MIME Type": "video/webm"
			},
			{
				"Extension": ".webp",
				"Kind of document": "WEBP image",
				"MIME Type": "image/webp"
			},
			{
				"Extension": ".woff",
				"Kind of document": "Web Open Font Format (WOFF)",
				"MIME Type": "font/woff"
			},
			{
				"Extension": ".woff2",
				"Kind of document": "Web Open Font Format (WOFF)",
				"MIME Type": "font/woff2"
			},
			{
				"Extension": ".xhtml",
				"Kind of document": "XHTML",
				"MIME Type": "application/xhtml+xml"
			},
			{
				"Extension": ".xls",
				"Kind of document": "Microsoft Excel",
				"MIME Type": "application/vnd.ms-excel"
			},
			{
				"Extension": ".xlsx",
				"Kind of document": "Microsoft Excel (OpenXML)",
				"MIME Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
			},
			{
				"Extension": ".xml",
				"Kind of document": "XML",
				"MIME Type": "application/xml is recommended as of RFC 7303 (section 4.1), but text/xml is still used sometimes. You can assign a specific MIME type to a file with .xml extension depending on how its contents are meant to be interpreted. For instance, an Atom feed is application/atom+xml, but application/xml serves as a valid default."
			},
			{
				"Extension": ".xul",
				"Kind of document": "XUL",
				"MIME Type": "application/vnd.mozilla.xul+xml"
			},
			{
				"Extension": ".zip",
				"Kind of document": "ZIP archive",
				"MIME Type": "application/zip"
			},
			{
				"Extension": ".3gp",
				"Kind of document": "3GPP audio/video container",
				"MIME Type": "video/3gpp; audio/3gpp if it doesn't contain video"
			},
			{
				"Extension": ".3g2",
				"Kind of document": "3GPP2 audio/video container",
				"MIME Type": "video/3gpp2; audio/3gpp2 if it doesn't contain video"
			},
			{
				"Extension": ".7z",
				"Kind of document": "7-zip archive",
				"MIME Type": "application/x-7z-compressed"
			}
		]

def action():
	global table
	index = {}
	for i,rec in enumerate( table ):
		ext = rec['Extension']
		if ' ' in ext:
			_.pv(rec)
			for ii,x in enumerate(ext.split(' ')):
				_.pr( ii, x )
			ask=input('?: ')
			ext = ext.split(' ')[int(ask)]
		index[ rec['MIME Type'] ] = ext


	_.saveTableDB( index, 'mime-ext.index' )


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()