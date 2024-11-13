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
	_.switches.register( 'AddBreaks', '-br' )
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
books = {
	"Genesis": ["Gen", "Ge", "Gn"],
	"Exodus": ["Ex", "Exod", "Exo"],
	"Leviticus": ["Lev", "Le", "Lv"],
	"Numbers": ["Num", "Nu", "Nm", "Nb"],
	"Deuteronomy": ["Deut", "De", "Dt"],
	"Joshua": ["Josh", "Jos", "Jsh"],
	"Judges": ["Judg", "Jdg", "Jg", "Jdgs"],
	"Ruth": ["Rth", "Ru"],
	"1 Samuel": ["1 Sam", "1 Sm", "1 Sa", "1 S", "I Sam", "I Sa", "1Sam", "1Sa", "1S", "1 S", "1st Samuel", "1st Sam", "First Samuel", "First Sam"],
	"2 Samuel": ["2 Sam", "2 Sm", "2 Sa", "2 S", "II Sam", "II Sa", "2Sam", "2Sa", "2S", "2 S", "2nd Samuel", "2nd Sam", "Second Samuel", "Second Sam"],
	"1 Kings": ["1 Kgs", "1 Ki", "1Kgs", "1Kin", "1Ki", "1K", "1 K", "I Kgs", "I Ki", "1st Kings", "1st Kgs", "First Kings", "First Kgs"],
	"2 Kings": ["2 Kgs", "2 Ki", "2Kgs", "2Kin", "2Ki", "2K", "2 K", "II Kgs", "II Ki", "2nd Kings", "2nd Kgs", "Second Kings", "Second Kgs"],
	"1 Chronicles": ["1 Chron", "1 Chr", "1 Ch", "1Chron", "1Chr", "1Ch", "I Chron", "I Chr", "I Ch", "1st Chronicles", "1st Chron", "First Chronicles", "First Chron"],
	"2 Chronicles": ["2 Chron", "2 Chr", "2 Ch", "2Chron", "2Chr", "2Ch", "II Chron", "II Chr", "II Ch", "2nd Chronicles", "2nd Chron", "Second Chronicles", "Second Chron"],
	"Ezra": ["Ezr", "Ez"],
	"Nehemiah": ["Neh", "Ne"],
	"Esther": ["Est", "Esth", "Es"],
	"Job": ["Jb"],
	"Psalms": ["Ps", "Psalm", "Pslm", "Psa", "Psm", "Pss", "P"],
	"Proverbs": ["Prov", "Pro", "Prv", "Pr"],
	"Ecclesiastes": ["Eccles", "Eccle", "Ecc", "Ec", "Qoh"],
	"Song of Solomon": ["Song", "Song of Songs", "SOS", "So", "Canticle of Canticles", "Canticles", "Cant"],
	"Isaiah": ["Isa", "Is"],
	"Jeremiah": ["Jer", "Je", "Jr"],
	"Lamentations": ["Lam", "La"],
	"Ezekiel": ["Ezek", "Eze", "Ezk"],
	"Daniel": ["Dan", "Da", "Dn"],
	"Hosea": ["Hos", "Ho"],
	"Joel": ["Jl"],
	"Amos": ["Am"],
	"Obadiah": ["Obad", "Ob"],
	"Jonah": ["Jon", "Jnh"],
	"Micah": ["Mic", "Mc"],
	"Nahum": ["Nah", "Na"],
	"Habakkuk": ["Hab", "Hb"],
	"Zephaniah": ["Zeph", "Zep", "Zp"],
	"Haggai": ["Hag", "Hg"],
	"Zechariah": ["Zech", "Zec", "Zc"],
	"Malachi": ["Mal", "Ml"],
	"Matthew": ["Matt", "Mt"],
	"Mark": ["Mrk", "Mar", "Mk", "Mr"],
	"Luke": ["Luk", "Lk"],
	"John": ["Joh", "Jhn", "Jn", "J"],
	"Acts": ["Act", "Ac"],
	"Romans": ["Rom", "Ro", "Rm", "R"],
	"1 Corinthians": ["1 Cor", "1 Co", "I Cor", "I Co", "1Cor", "1Co", "I Corinthians", "1Corinthians", "1st Corinthians", "First Corinthians"],
	"2 Corinthians": ["2 Cor", "2 Co", "II Cor", "II Co", "2Cor", "2Co", "II Corinthians", "2Corinthians", "2nd Corinthians", "Second Corinthians"],
	"Galatians": ["Gal", "Ga"],
	"Ephesians": ["Eph", "Ephes"],
	"Philippians": ["Phil", "Php", "Pp", "ph", "pl"],
	"Colossians": ["Col", "Co"],
	"1 Thessalonians": ["1 Thess", "1 Thes", "1 Th", "I Thessalonians", "I Thess", "I Thes", "I Th", "1Thessalonians", "1Thess", "1Thes", "1Th", "1st Thessalonians", "1st Thess", "First Thessalonians", "First Thess"],
	"2 Thessalonians": ["2 Thess", "2 Thes", "2 Th", "II Thessalonians", "II Thess", "II Thes", "II Th", "2Thessalonians", "2Thess", "2Thes", "2Th", "2nd Thessalonians", "2nd Thess", "Second Thessalonians", "Second Thess"],
	"1 Timothy": ["1 Tim", "1 Ti", "I Timothy", "I Tim", "I Ti", "1Timothy", "1Tim", "1Ti", "1st Timothy", "1st Tim", "First Timothy", "First Tim"],
	"2 Timothy": ["2 Tim", "2 Ti", "II Timothy", "II Tim", "II Ti", "2Timothy", "2Tim", "2Ti", "2nd Timothy", "2nd Tim", "Second Timothy", "Second Tim"],
	"Titus": ["Tit", "Ti"],
	"Philemon": ["Philem", "Phm", "Pm"],
	"Hebrews": ["Heb", "He"],
	"James": ["Jas", "Jm"],
	"1 Peter": ["1 Pet", "1 Pe", "1 Pt", "1 P", "I Pet", "I Pt", "I Pe", "1Peter", "1Pet", "1Pe", "1Pt", "1P", "I Peter", "1st Peter", "First Peter"],
	"2 Peter": ["2 Pet", "2 Pe", "2 Pt", "2 P", "II Peter", "II Pet", "II Pt", "II Pe", "2Peter", "2Pet", "2Pe", "2Pt", "2P", "2nd Peter", "Second Peter"],
	"1 John": ["1 John", "1 Jhn", "1 Jn", "1 J", "1John", "1Jhn", "1Joh", "1Jn", "1Jo", "1J", "I John", "I Jhn", "I Joh", "I Jn", "I Jo", "1st John", "First John"],
	"2 John": ["2 John", "2 Jhn", "2 Jn", "2 J", "2John", "2Jhn", "2Joh", "2Jn", "2Jo", "2J", "II John", "II Jhn", "II Joh", "II Jn", "II Jo", "2nd John", "Second John"],
	"3 John": ["3 John", "3 Jhn", "3 Jn", "3 J", "3John", "3Jhn", "3Joh", "3Jn", "3Jo", "3J", "III John", "III Jhn", "III Joh", "III Jn", "III Jo", "3rd John", "Third John"],
	"Jude": ["Jud", "Jude", "Jd"],
	"Revelation": ["Rev", "Re", "Rv"]
}

import re

def add_space_before_first_number(s):
    return re.sub(r'(?<!\d)(\d)', r' \1', s, count=1)

def add_plus_before_first_number(s):
    return re.sub(r'(?<!\d)(\d)', r'+\1', s, count=1)

def linkify_books_and_verses(text, books):
    # Pattern to capture book name and verses with a colon
    pattern = r'\b(' + '|'.join(re.escape(book) for book in books.keys()) + r')(\s*\d+:\d+(?:[-,\s\d]+)?)\b'

    def make_link(matchobj):
        match_book = matchobj.group(1)
        match_verse = matchobj.group(2)
        for full_name, abbreviations in books.items():
            if match_book in abbreviations or match_book == full_name:
                pre = match_verse
                match_verse = match_verse.strip()
                try:
                    if match_verse[-1] == ',':
                        match_verse = match_verse[:-1].strip()
                except IndexError:
                    pass
                add = pre.replace(match_verse, '').replace('+', ' ').lstrip()
                vsT = add_space_before_first_number(match_verse)
                vsR = add_plus_before_first_number(match_verse)
                return f'<a href="https://bible.biblicalheart.com/?translation=niv&v={full_name.replace(" ", "+")}{vsR}">{match_book}{vsT}</a>{add}'

    # Using the re.IGNORECASE flag with re.sub
    return re.sub(pattern, make_link, text, flags=re.IGNORECASE)



# import re
# def strip_existing_links(text):
#     # Regular expression pattern to remove all links 
#     link_pattern = re.compile(r'<a [^>]*>([^<]+)</a>')
#     return link_pattern.sub(r'\1', text)

# def linkify_bible_verses(text):
#     # Strip all links
#     text = strip_existing_links(text)
	
#     # Regular expression pattern to find Bible verses, including ranges and comma-separated verses
#     bible_verse_pattern = re.compile(r'(\b(?:\d\s)?[A-Za-z]+\s\d+(?::\d+(?:[,-]\d+)*)([a-z])?)\b')

#     def make_link(matchobj):
#         verse = matchobj.group(1).replace(" ", "+").rstrip('abcdefghijklmnopqrstuvwxyz')  # Remove trailing alpha
#         return f'<a target="_blank" href="https://bible.biblicalheart.com/?translation=niv&v={verse}">{matchobj.group(1)}</a>'
	
#     return bible_verse_pattern.sub(make_link, text)

def action():
	global books
	# print(_.pp()); exit();
	text='\n'.join(_.pp()).strip()
	# print(text);exit();
	html=linkify_books_and_verses(text,books)
	if _.switches.isActive('AddBreaks'):
		html=html.replace('\n','\n<br/>\n')
	html=html.replace('<>','<p>')
	html=html.replace('</>','</p>')
	_copy.imp.copy( html )

_copy = _.regImp( __.appReg, '-copy' )

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

