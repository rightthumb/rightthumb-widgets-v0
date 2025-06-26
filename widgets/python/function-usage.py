import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

# def sections(line):
# 	line = line.replace('(','( ').replace(')',' )').replace('[',' ')
# 	parts = line.split(' ')
# 	allParts = []
# 	has = [
# 		'.split',
# 		'.intersection',
# 		'.append',
# 		'.lower',
# 		'.float',
# 		'.search',
# 		're.',
# 		]
# 	itIs = [
# 		'len',
# 		'set',
# 		'min',
# 		'max',
# 		'str',
# 		'bool',
# 	]
# 	for part in parts:
# 		if '(' in part:
# 			part = part.split('(')[0]
# 			part = part.strip() 
# 			add = True
# 			for o in has:
# 				if o in part:
# 					add = False
# 			for o in itIs:
# 				if o == part:
# 					add = False
# 			if add:
# 				if part:
# 					allParts.append(part)

# 	return allParts



# def findFunctions(line):
# 	if '(' in line and not 'def' in line:
# 		line = line.split('#')[0]

# 		parts = sections(line)
# 		if len(parts) > 1:
# 			return parts
# 	return []

# def clean(line):
# 	line = line.replace()

# def action():
# 	index = {}
# 	for line in _.isData():
# 		parts = findFunctions(line)
# 		for part in parts:
# 			if _.showLine(part):
# 				_.pr(part)
# 				if not part in index:
# 					index[part] = 0
# 				index[part] += 1
# 	table = []
# 	_.pv(table)
# 	return table
# 	for i in index:
# 		table.append({'count':index[i], 'name':i})
# 	_.pt( part )

########################################################################################

# def sections(line):
#     line = line.replace('(', '( ').replace(')', ' )').replace('[', ' ').replace('+', ' ').replace(',', ' ').replace("'", ' ').replace('\\t', ' ')
#     parts = line.split(' ')
#     allParts = []
#     has = [
#         '.split',
#         '.intersection',
#         '.append',
#         '.lower',
#         '.float',
#         '.search',
#         '.strftime',
#         '.join',
#         '.replace',
#         '.endswith',
#         '.strip',
#         're.',
#         'os.',
#     ]
#     itIs = [
#         'len',
#         'set',
#         'min',
#         'max',
#         'str',
#         'bool',
#         'int',
#     ]
#     for part in parts:
#         if '(' in part:
#             part = part.split('(')[0]
#             part = part.strip()
#             add = True
#             for o in has:
#                 if o in part:
#                     add = False
#             for o in itIs:
#                 if o == part:
#                     add = False
#             if add:
#                 if part:
#                     allParts.append(part)
#     return allParts


# def findFunctions(line):
#     if '(' in line and 'def' not in line:
#         line = line.split('#')[0]
#         parts = sections(line)
#         if len(parts) > 1:
#             return parts
#     return []


# def clean(line):
#     return line.replace('(', '').replace(')', '').replace('[', '').replace(']', '')


# def action():
#     index = {}
#     for line in _.isData():
#         parts = findFunctions(line)
#         for part in parts:
#             if _.showLine(part):
#                 # _.pr(part)
#                 if part not in index:
#                     index[part] = 0
#                 index[part] += 1
#     table = []
#     for i in index:
#         table.append({'count': index[i], 'name': i})
#     table = _.sort(table,'count')
#     _.pt(table)
#     return table



itIs = [
	'if',
	'in',
	'0:',
	'-i',
	'-f',
	'Error:',
	'bool:',
	'elif',
	'!V!',
	'!v!',
	'.md',
	'for',
	'not',
	'len',
	'bk:',
	'.py',
	'C:',
	'NOT',
	'and',
	'True',
	'list:',
	'None:',
	'len',
	'set',
	'min',
	'max',
	'str',
	'bool',
	'int',
	')',
	'(',
	'sys.exit',
]
startsWith = [
	'-',
]



import re

def extract_function_calls(lines):
    # Join lines into a single string
    code = "\n".join(lines)

    # Regular expression to find function calls, including nested ones
    function_call_pattern = re.compile(r'[\w.]+\s*\([^()]*\s*(?:\([^()]*\s*)*\)')
    
    # Find all matches
    matches = function_call_pattern.findall(code)
    items = []

    # Collect all function calls
    for match in matches:
        items.append(match.strip())
    return items
has = [
	':',
	'-',
]
def action():
    global has, itIs, startsWith
    functions = extract_function_calls(_.isData())
    index = {}
    
    for func in functions:
        func = func.split('(')[0].strip()
        
        # Check if the function name matches or contains any items in `itIs`
        if any(func.lower().strip() == o.lower().strip() for o in itIs) or \
           any(o.lower().strip() in func.lower().strip() for o in itIs):
            continue
        if '.append' in func: continue
        if '.split' in func: continue
        if '.intersection' in func: continue
        if '.lower' in func: continue
        if '.float' in func: continue
        if '.search' in func: continue
        if '.strftime' in func: continue
        if '.join' in func: continue
        if '.replace' in func: continue
        if '.pop' in func: continue
        if '.reverse' in func: continue
        if '.endswith' in func: continue
        if '.strip' in func: continue
        if '.startswith' in func: continue
        
        if 're.' in func: continue
        if 'os.' in func: continue
        
        if 'type' == func: continue
        if 'float' == func: continue
        if not _.showLine(func): continue
        # Count occurrences of each function
        if func not in index:
            index[func] = 0
        index[func] += 1

    # Sort the results by count
    table = [{'count': index[i], 'name': i, 'length': len(i)} for i in index]
    table = _.sort(table, 'count,length,name')
    
    # Print the results using your framework's print function
    _.pt(table, 'count,name')




########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);