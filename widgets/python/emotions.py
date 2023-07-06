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

import os
import sys
import time
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
	_.switches.register( 'Build', '-build' )



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'emotions.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Emotion identification and documentation app',
	'categories': [
						'emotion',
						'emotions',
						'health',
						'help',
						'social',
						'personal',
						'wellbeing',
						'safe',
						'safety',
						'documentation',
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
						'p emotions -build',
						''
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
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
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# START



def action():
	global data
	load()

	if _.switches.isActive('Build'):

		emotions = {}
		emotions['suprised'] = {}
		emotions['happy'] = {}
		emotions['sad'] = {}
		emotions['disgusted'] = {}
		emotions['angry'] = {}
		emotions['fearful'] = {}
		emotions['bad'] = {}



		emotions['suprised']['startled'] = {}
		emotions['suprised']['confused'] = {}
		emotions['suprised']['amazed'] = {}
		emotions['suprised']['excited'] = {}
		
		emotions['happy']['playful'] = {}
		emotions['happy']['content'] = {}
		emotions['happy']['interested'] = {}
		emotions['happy']['proud'] = {}
		emotions['happy']['accepted'] = {}
		emotions['happy']['powerful'] = {}
		emotions['happy']['peaceful'] = {}
		emotions['happy']['trusting'] = {}
		emotions['happy']['optimistic'] = {}
		
		emotions['sad']['lonely'] = {}
		emotions['sad']['vulnerable'] = {}
		emotions['sad']['despair'] = {}
		emotions['sad']['guilty'] = {}
		emotions['sad']['depressed'] = {}
		emotions['sad']['hurt'] = {}
		
		emotions['disgusted']['dissaproving'] = {}
		emotions['disgusted']['disappointed'] = {}
		emotions['disgusted']['awful'] = {}
		emotions['disgusted']['repelled'] = {}
		
		emotions['angry']['let down'] = {}
		emotions['angry']['humiliated'] = {}
		emotions['angry']['bitter'] = {}
		emotions['angry']['mad'] = {}
		emotions['angry']['aggressive'] = {}
		emotions['angry']['frustrated'] = {}
		emotions['angry']['distant'] = {}
		emotions['angry']['critical'] = {}
		
		emotions['fearful']['scared'] = {}
		emotions['fearful']['anxious'] = {}
		emotions['fearful']['insecure'] = {}
		emotions['fearful']['weak'] = {}
		emotions['fearful']['rejected'] = {}
		emotions['fearful']['threatened'] = {}
		
		emotions['bad']['bored'] = {}
		emotions['bad']['busy'] = {}
		emotions['bad']['stressed'] = {}
		emotions['bad']['tired'] = {}



		emotions['suprised']['startled']['shocked'] = []
		emotions['suprised']['startled']['dismayed'] = []
		emotions['suprised']['confused']['disilusioned'] = []
		emotions['suprised']['confused']['perplexed'] = []
		emotions['suprised']['amazed']['astonished'] = []
		emotions['suprised']['amazed']['awe'] = []
		emotions['suprised']['excited']['eager'] = []
		emotions['suprised']['excited']['energetic'] = []
		
		emotions['happy']['playful']['aroused'] = []
		emotions['happy']['playful']['cheeky'] = []
		emotions['happy']['content']['free'] = []
		emotions['happy']['content']['joyful'] = []
		emotions['happy']['interested']['curious'] = []
		emotions['happy']['interested']['inquisitive'] = []
		emotions['happy']['proud']['successful'] = []
		emotions['happy']['proud']['confident'] = []
		emotions['happy']['accepted']['respected'] = []
		emotions['happy']['accepted']['valued'] = []
		emotions['happy']['powerful']['couragous'] = []
		emotions['happy']['powerful']['creative'] = []
		emotions['happy']['peaceful']['loving'] = []
		emotions['happy']['peaceful']['thankful'] = []
		emotions['happy']['trusting']['sensitive'] = []
		emotions['happy']['trusting']['intimate'] = []
		emotions['happy']['optimistic']['hopeful'] = []
		emotions['happy']['optimistic']['inspired'] = []
		
		emotions['sad']['lonely']['isolated'] = []
		emotions['sad']['lonely']['abandoned'] = []
		emotions['sad']['vulnerable']['victimised'] = []
		emotions['sad']['vulnerable']['fragile'] = []
		emotions['sad']['despair']['grief'] = []
		emotions['sad']['despair']['powerless'] = []
		emotions['sad']['guilty']['ashamed'] = []
		emotions['sad']['guilty']['remorseful'] = []
		emotions['sad']['depressed']['empty'] = []
		emotions['sad']['depressed']['inferior'] = []
		emotions['sad']['hurt']['embarassed'] = []
		emotions['sad']['hurt']['dissapointed'] = []
		
		emotions['disgusted']['dissaproving']['judgemental'] = []
		emotions['disgusted']['dissaproving']['embarrassed'] = []
		emotions['disgusted']['disappointed']['appalled'] = []
		emotions['disgusted']['disappointed']['revolted'] = []
		emotions['disgusted']['awful']['nauseated'] = []
		emotions['disgusted']['awful']['detestable'] = []
		emotions['disgusted']['repelled']['horrified'] = []
		emotions['disgusted']['repelled']['hesitant '] = []
		
		emotions['angry']['let down']['betrayed'] = []
		emotions['angry']['let down']['resentful'] = []
		emotions['angry']['humiliated']['disrespected'] = []
		emotions['angry']['humiliated']['ridiculed'] = []
		emotions['angry']['bitter']['indignant'] = []
		emotions['angry']['bitter']['violated'] = []
		emotions['angry']['mad']['furious'] = []
		emotions['angry']['mad']['jealous'] = []
		emotions['angry']['aggressive']['provoked'] = []
		emotions['angry']['aggressive']['hostile'] = []
		emotions['angry']['frustrated']['infuriated'] = []
		emotions['angry']['frustrated']['annoyed'] = []
		emotions['angry']['distant']['withdrawn'] = []
		emotions['angry']['distant']['numb'] = []
		emotions['angry']['critical']['sceptical'] = []
		emotions['angry']['critical']['dismissive'] = []
		
		emotions['fearful']['scared']['helpless'] = []
		emotions['fearful']['scared']['frightened'] = []
		emotions['fearful']['anxious']['overwhelmed'] = []
		emotions['fearful']['anxious']['worried'] = []
		emotions['fearful']['insecure']['inadequate'] = []
		emotions['fearful']['insecure']['inferior'] = []
		emotions['fearful']['weak']['worthless'] = []
		emotions['fearful']['weak']['insignificant'] = []
		emotions['fearful']['rejected']['excluded'] = []
		emotions['fearful']['rejected']['persecuted'] = []
		emotions['fearful']['threatened']['nervous'] = []
		emotions['fearful']['threatened']['exposed'] = []
		
		emotions['bad']['bored']['indifferent'] = []
		emotions['bad']['bored']['apathetic'] = []
		emotions['bad']['busy']['pressured'] = []
		emotions['bad']['busy']['rushed'] = []
		emotions['bad']['stressed']['overwhelmed'] = []
		emotions['bad']['stressed']['out of control'] = []
		emotions['bad']['tired']['sleepy'] = []
		emotions['bad']['tired']['unfocussed'] = []
		

		_.saveTableDB( emotions, 'emotions.json' )



	if not _.switches.isActive('Build'):

		_.traverse_dic_research['fields'] = []
		_.traverse_dic( data )
		
		records = []
		for record in _.traverse_dic_research['fields']:
			records.append( record['parents'] + [record['field']] )

		selected = []
		for record in records:
			select = False
			for rec in record:
				if _.showLine( rec ):
					select = True
			if select:
				selected.append( record )


		if len(selected):
			newSelected = []
			for record in selected:
				if len(record) == 3:
					newSelected.append({
											'one': record[0],
											'two': record[1],
											'three': record[2],
						})
			
			_.fields.asset( 'data', newSelected )
			for record in selected:
				if len(record) == 3:

					part  = _.fields.value( 'data', 'one', record[0], right=1 )
					part += '   '
					part += _.fields.value( 'data', 'two', record[1] )
					part += '   '
					part += _.fields.value( 'data', 'three', record[2] )

					_.pr( part )

def load():
	global data
	if not _.switches.isActive('Build'):
		data = _.getTableDB( 'emotions.json' )


data = []



########################################################################################
if __name__ == '__main__':
	action()







