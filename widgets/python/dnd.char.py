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
# import platform
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


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'dnd.char.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Manage dungeons and dragons characters and campaigns',
	'categories': [
						'dnd',
						'dungeons',
						'dragons',
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
						'p dnd.char ',
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
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	
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
# START



def action():
	load()



def load():
	# _.v       = _.dot()
	_.v.user  = _.dot()
	_.v.spell = _.dot()
	_.v.spell.spells =            _.getTableProject( 'DnD.dndspellslist', 'spells.json' )
	_.v.spell.levels = indexInt(  _.getTableProject( 'DnD.sheet', 'level-spells.index'    )  )
	_.v.xp           = indexInt(  _.getTableProject( 'DnD.sheet', 'xp.index'             )  )
	_.v.mods         = indexInt(  _.getTableProject( 'DnD.sheet', 'modifiers.index'      )  )


	do = 2

	if do == 1:
		keys = list(  _.v.spell.spells[0].keys()  )
		_.pr( '\n'.join(keys) )

	if do == 2:
		classes = []
		spells = {}
		damage = {}
		for spell in _.v.spell.spells:
			for c in spell['availableClasses']:
				if not c in classes:
					classes.append(c)
				if not c in damage:
					damage[c] = 0
				if spell['isDamaging']:
					damage[c] += 1
				if not c in spells:
					spells[c] = 0
				spells[c] += 1
		classes.sort()
		# _.pr( 'sp\t', 'dmg\t', 'class'  )
		classInfo = []
		for c in classes:
			classInfo.append({ 'class': c, 'spells': spells[c], 'damage': damage[c] })
		_.tables.register( 'classes', classInfo  )
		_.switches.fieldSet( 'Sort', 'active', True )
		_.switches.fieldSet( 'Sort', 'value', 'class,spells,damage' )
		_.tables.print( 'classes', 'class,spells,damage'  )
		_.switches.fieldSet( 'Sort', 'value', 'spells,class,damage' )
		_.tables.print( 'classes', 'spells,class,damage'  )
		_.switches.fieldSet( 'Sort', 'value', 'damage,spells,class' )
		_.tables.print( 'classes', 'damage,spells,class'  )

		# _.pr( '\n'.join(classes) )
	if do == 3:

		_.cp( len(_.v.spell.spells), 'yellow' )
		for spell in _.v.spell.spells:
			_.pr( spell['name'] )
		_.cp( len(_.v.spell.spells), 'yellow' )

	if do == 4:
		table = {}
		old = _.getTable2( 'D:\\tech\\programs\\databank\\projects\\DnD\\configurations\\groups\\Church\\campaigns\\Curse_of_Strahd\\sorcerer\\players\\Scott_Reph\\characters\\Kilroth\\spells.json' )
		new = {}
		for n, nSpell in enumerate( _.v.spell.spells ):
			new[ nSpell['name'] ] = n
		bad = 0
		for o,oSpell in enumerate(old):
			# oSpell['name'] = oSpell['name'].replace( ' (UA)', '' )
			if oSpell['name'] in new:
				_.pr( o, new[oSpell['name']], oSpell['name'] )
				table[o] = new[oSpell['name']]
			else:
				_.cp(oSpell['name'])
				bad+=1
		_.pr('bad', bad)
		_.pr()
		_.pr()
		_.pr()
		_.printVarSimple(table)
	if do == 5:
		old = _.getTable2( 'D:\\tech\\programs\\databank\\projects\\DnD\\configurations\\groups\\Church\\campaigns\\Curse_of_Strahd\\sorcerer\\players\\Scott_Reph\\characters\\Kilroth\\spells.json' )
		# for 




	if do == 6:
		pass
	if do == 7:
		pass

def indexInt( table ):
	return table
	index = {}
	for k in table:
		index[int(k)] = table[k]
	return index

########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()







