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
	_.switches.register( 'Label', '-i,-l,-label' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

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


import random

def get_random_title():
    titles = [
        "Unveiling the Mystery",
        "The Secret Path",
        "Breaking the Silence",
        "Journey to the Unknown",
        "Beyond the Horizon",
        "The Hidden Treasure",
        "A Twist of Fate",
        "Shadows of the Past",
        "Echoes of the Future",
        "Lost in Time",
        "The Forbidden Quest",
        "Chasing Dreams",
        "A Leap of Faith",
        "Crossroads of Destiny",
        "Dancing with Shadows",
        "Whispers in the Dark",
        "Escape from Reality",
        "Into the Abyss",
        "Rising from the Ashes",
        "The Road Less Traveled",
        "Under the Moonlight",
        "Reign of the Unknown",
        "Tales of the Unexpected",
        "Beyond Imagination",
        "The Invisible Thread",
        "Symphony of the Night",
        "Between the Lines",
        "A Glimpse of Eternity",
        "The Enigma Unfolds",
        "Through the Looking Glass",
        "The Final Countdown",
        "A Moment in Time",
        "Uncharted Waters",
        "Edge of the World",
        "Voyage to the Extraordinary",
        "The Hidden Dimension",
        "Realm of Wonders",
        "In Pursuit of Magic",
        "Twilight of the Gods",
        "The Eternal Flame",
        "The Silent Watcher",
        "Guardians of the Lost",
        "In the Shadow of Giants",
        "A Dance with Dragons",
        "The Last Frontier",
        "Echoes of Atlantis",
        "Beyond the Stars",
        "The Phoenix Rises",
        "A Whisper in the Wind",
        "The Path Less Trodden"
    ]

    return random.choice(titles)



def to_markdown_table(label, data):
    # Start with the header
    markdown_table = f"| {label} |\n|-----|\n"

    # If data is a list, iterate and add each item
    if isinstance(data, list):
        for item in data:
            markdown_table += f"| {item} |\n"
    # If data is a string, split into lines and add each line
    elif isinstance(data, str):
        for line in data.split('\n'):
            markdown_table += f"| {line} |\n"
    
    return markdown_table



def action():

	if _.switches.isActive('Label'):
		label = ' '.join(_.switches.values('Label'))
	else:
		label = get_random_title()

	data = _.myData()
	results = to_markdown_table(label, data)
	print(results)


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

