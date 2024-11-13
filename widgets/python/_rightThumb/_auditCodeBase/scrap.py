

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

characters
			id
			char
			print
			[database]
			[languages]
						code 'global', 'python'
						groupID False 12
						[is] ['inline comment','comment','end','quote']
						[set] [6,12]
						nest 0 1
						isOpen 0 1
						hasClose 0 1

action
		id
		description
		code
		[test] 1,['quote'],''
		specific
		caseStrict
		start
		[type] id
		[rules] id

type
	id
	name

rules
	id
	code
	description
	[pattern]
				required
				specific
				ifLast
				[test] 1,['quote'],''




processCharID( p, charRules )
charRules['languages']
characters

{
	'id': 6,
	'char': '/',
	'print': '/',
	'database': [],
	'languages': [{
		'code': 'javascript',
		'groupID': 3,
		'is': ['comment'],
		'set': [7],
		'nest': 0,
		'isOpen': 1,
		'hasClose': 1,
		}],
}

action
actionPlan( p )
ins['action']
{
	'id': 7,
	'description': 'orphans',
	'code': 'global',
	'test': [0,2,4,['quote'],'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'],
	'specific': False,
	'caseStrict': False,
	'start': True,
	'type': [3],
	'rules': [6],
}


rules
testRule( p, r )
rules['pattern']
{
	'id': 6,
	'code': 'python',
	'description': 'variable',
	'pattern': [{
					'required': True,
					'specific': False,
					'ifLast': False,
					'test': [0,2,4,12,11],

	}],

}
{
	'id': 3,
	'code': 'python',
	'description': 'variable',
	'pattern': [{
					'required': False,
					'specific': True,
					'ifLast': False,
					'test': ['var'],

	},{
					'required': True,
					'specific': False,
					'ifLast': False,
					'test': ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'],

	},{
					'required': True,
					'specific': True,
					'ifLast': False,
					'test': [13],

	},{
					'required': True,
					'specific': False,
					'ifLast': False,
					'test': [0,2,4,12,11,'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.'],

	},{
					'required': True,
					'specific': True,
					'ifLast': False,
					'test': [14],

	}],

}

