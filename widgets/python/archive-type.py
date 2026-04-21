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
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
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

def check_compressed_file(path):
	file_header_map = {
		"50 4B 03 04": "ZIP",
		"50 4B 01 02": "ZIP (Central Directory)",
		"1F 8B 08": "GZIP",
		"75 73 74 61 72 20 20 00": "TAR (ustar format)",
		"75 73 74 61 72 00 30 30": "TAR (gnu tar format)",
		"52 61 72 21 1A 07 00": "RAR",
		"37 7A BC AF 27 1C": "7-Zip",
		"42 5A 68": "BZIP2",
		"04 22 4D 18": "LZ4",
		"5D 00 00 80 00": "LZMA",
		"78 9C": "ZLIB",
		"2D 6C 68 1B": "LZH (LHA)",
		"4D 53 43 46": "CAB (Microsoft Cabinet)",
		"1F 9D": "Z (Unix Compressed Archive File)",
		"60 EA": "ARJ",
		"FD 37 7A 58 5A 00": "XZ (LZMA2)",
		"52 61 72 21 1A 07 01 00": "RAR5",
		"4C 5A 49 50": "LZIP",
		"28 B5 2F FD": "Zstd (Zstandard)",
		"1F A0": "LZHUF",
		"89 4C 5A 4F": "LZO",
		"5A 4F 4F 20": "ZOO",
		"53 51 58 20": "SQX (SQueeZe)",
		"18 00": "LZ77",
		"1F A1": "LZRW1",
		"1F A2": "LZRW3",
		"1F A3": "LZRW4",
		"4C 5A 50": "LZP (Lempel-Ziv-Pliant)",
		"4C 5A 53": "LZS",
		"18 5A 4A 42": "LZJB",
		"5D 00 00 80 00": "LZMA2",
		"78 01": "LZ77 (DEFLATE)",
		"1A 4C 5A 48": "LZHAM",
		"04 22 4D 18": "LZ4 (Legacy Format)",
		"4C 5A 53": "LZS (MiniLZO)",
		"04 22 4D 44": "LZ4 (Frame Format)",
		"5A 50 41 51": "ZPAQ",
		"53 68 6E 21": "SHN (Shorten)",
		"4C 5A 58": "LZX",
		"42 53 43 31": "BSC (Bitwise Source Code)",
		"53 5A 44 44": "LZC (Lempel-Ziv-Welch)",
		"53 5A 44 44": "LZC (Lempel-Ziv-Welch)",
		"49 43 45 4F 57 53": "ICE (ICEOWS Archive)",
		"53 45 41": "SEA (Self-Extracting Archive)",
		"59 5A 31 0D 0A 1A 0A": "YZ1 (YAC Compressed Archive)",
		"53 44 4E 46": "SDN (DN Spy Archive)",
		"50 50 4D 44": "PPMd (Prediction by Partial Matching Dissipating)",
		"41 4C 5A 02": "AZO (ALZip Splitted Archive)",
		"4C 00 00 00 01 14 02 00": "LNK (Windows Shortcut)",
		"30 37": "CPIO (Unix CPIO Archive)",
		"4B 47 42 5F 61 72 63 68": "KGB (KGB Archiver)",
		"55 48 41 1A": "UHA (UHarc Archive)",
		"49 43 45 4F 57 53": "ICE (ICEOWS Archive)",
		"53 45 41": "SEA (Self-Extracting Archive)",
		"59 5A 31 0D 0A 1A 0A": "YZ1 (YAC Compressed Archive)",
		"53 44 4E 46": "SDN (DN Spy Archive)",
		"50 50 4D 44": "PPMd (Prediction by Partial Matching Dissipating)",
		"41 4C 5A 02": "AZO (ALZip Splitted Archive)",
		"4C 00 00 00 01 14 02 00": "LNK (Windows Shortcut)",
		"30 37": "CPIO (Unix CPIO Archive)",
		"4B 47 42 5F 61 72 63 68": "KGB (KGB Archiver)",
		"D7 CD C6 C7": "IMG (Amiga Disk Image)",
		"53 45 41 20": "SEA (StuffIt Expander Archive)",
		"30 37 30 37": "PAX (Portable Archive Exchange)",
		"43 49 53 4F": "CISO (Compact ISO)",
		"50 50 20 20 20": "PP (Packard Bell Archive)",
		"48 42 43 32 0D 0A": "HBC2 (HyperBac Compressed Archive)",
		"78 01 73 0D 62 62 60": "HAP (HAP Archive)",
		"50 4B 05 06": "ZIP 9",
	}

	header=_.IS(path)
	for sig in file_header_map:
		if header.startswith(sig):
			return file_header_map[sig]
	return "NOT_ARCHIVE"
	




def action():
	for path in _.pp():
		# _.pr(_.IS(path),c='cyan')
		result=check_compressed_file(path)
		if result == 'NOT_ARCHIVE':
			_.pr(result,c='red')
		else:
			_.pr(result,c='green')



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