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

from rightthumb import app
from rightthumb import func as _
reg = app.space(__name__, __file__)

reg.documentation = {
	'file': app.this_app( __file__ ),
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
						app.hp('p thisApp -file file.txt'),
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
reg.data = {
		'start': app.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] }, 
		},
	}


reg.rent = app.register(reg)
app.rent = app.focus(reg.rent)
app.switches()
# app.tables()




def app_switches():
	app.switch.reg( 'Name', '-n', 'description', req=1 )




def sw( argvProcessForce=False ):
	if not app.rent == reg.rent and reg.rent in app.rent:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		app.load()
	app.construct_registration( reg.documentation['file'],app.rent )
	app_switches()
	# app.switch.trigger( 'Ago', _.timeAgo )


	
	_.default_script_triggers()
	app.switch.process()


if not __name__ == '__main__':
	app.argv_process = False
else:
	_.argvProcess = True

registerSwitches()


def field_set( switchName, switchField, switchValue, rent=False ):
	if not type( rent ) == bool:
		rent = rent
	app.switch.field_set( switchName, switchField, switchValue, rent )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		app.set_pipe_data( sys.stdin.readlines(), app.rent, clean=True )


app.post_load( __file__ )







def action:
	# should be   Single-Task   OR   Imply-Architecture-Functions   OR   CLASSES!!
	# app.arch( o(r()), fn=' description '  )
	if app.switch('Files').status:
		pass
	if a.s('Files').s:
	__.softExit()

if a.f() and ( True ) and a.a( o(r()), fi=' description '  ):
	pass


if __name__ == '__main__':
	action()
	__.isExit(diagram=False)



