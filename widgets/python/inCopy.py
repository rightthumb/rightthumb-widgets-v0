import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register('Contains', '-contains','')
	_.switches.register('Invert', '-i,-invert','')
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
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=False )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

_paste = _.regImp( __.appReg, '-paste' )

def clean(data):
	Type = type(data)
	if Type == str:
		data = data.split('\n')
	lines = []
	for i, line in enumerate(data):
		line = line.strip()
		if line:
			lines.append(line)
	if Type == str:
		lines = '\n'.join(lines)
	return lines

original = {}
def clean2(data):
	global original
	Type = type(data)
	if Type == str:
		data = data.split('\n')
	lines = []
	for i, line in enumerate(data):
		og = line
		line = line.strip()
		original[line] = og
		if line:
			lines.append(line)
	if Type == str:
		lines = '\n'.join(lines)
	return lines


def action():
	global original

	# Retrieve input data
	if _.switches.isActive('Files'):
		data = _.getText(_.switches.value('Files'))
	else:
		data = _.isData(p=1)
	dataOG = data

	# Clean and process data
	data = set(clean2(data))  # Use a set for quick lookups
	copy = clean2(_paste.imp.paste()).split('\n')
	copyOG = _paste.imp.paste().split('\n')
	# print(_paste.imp.paste())
	copy_set = set(copy)  # Convert to a set for fast lookups

	spent = set()
	spentI = set()

	contains = _.switches.isActive('Contains')
	invert = _.switches.isActive('Invert')

	# If 'Contains' mode is active
	if contains:
		for line in copy:
			match_found = any(c in line for c in data)

			if match_found and not invert:
				if line not in spent:
					spent.add(line)
					print(line)
			elif not match_found and invert:
				if line not in spentI:
					spentI.add(line)
					print(line)
	
	# Default mode (Iterate both lists to ensure invert works properly)
	else:
		copy = copy_set
		index = {}
		for line in data:
			index[line] =  0
		for line in copy:
			index[line] =  0
			if line in data:
				index[line] += 1
		
		if not invert:
			for line in dataOG:
				st = line.strip()
				if st in index and index[st] > 0:
					print(line)
		else:
			for line in dataOG:
				st = line.strip()
				if st in index and index[st] == 0:
					print(line)
			_.pr(line=1,c='yellow')
			for line in copyOG:
				st = line.strip()
				if st in index and index[st] == 0:
					print(line)



		# if not invert:
		# 	for line in index:
		# 		if not index[line] == 0:
		# 			print(original[line])
		# else:
		# 	for line in index:
		# 		if index[line] == 0:
		# 			print(original[line])
		# _.pr('data:',data)
		# _.pr('copy:',copy)

		# # Find lines present in both
		# for line in copy:
		#     if line in data and not invert:
		#         original_line = original.get(line, line)
		#         if original_line not in spent:
		#             spent.add(original_line)
		#             print(original_line)
		#     elif line not in data and invert:
		#         # print(line)
		#         original_line = original.get(line, line)
		#         if original_line not in spentI:
		#             spentI.add(original_line)
		#             print(original_line)

		# # Find lines from data that are NOT in copy (to ensure full inverted functionality)
		# if invert:
		#     for line in data:
		#         print(line)
		#         if line not in copy_set:
		#             original_line = original.get(line, line)
		#             if original_line not in spentI:
		#                 spentI.add(original_line)
		#                 print(original_line)







# def action():
# 	global original
# 	if _.switches.isActive('Files'):
# 		data = _.getText( _.switches.value('Files') )
# 	else:
# 		data = _.isData(r=0)

# 	data = clean(data)
# 	copy = clean2(_paste.imp.paste()).split('\n')
# 	spent=[]
# 	spentI=[]
# 	invert = []
# 	for line in copy:
# 		if _.switches.isActive('Contains'):
# 			for c in data:
# 				if c in line and not _.switches.isActive('Invert'):
# 					if not line in spent:
# 						spent.append(line)
# 						print(line)
# 				elif _.switches.isActive('Invert'):
# 					if not line in spentI:
# 						spentI.append(line)
# 						print(line)

# 		else:
# 			if line in data and not _.switches.isActive('Invert'):
# 				if not original[line] in spent:
# 					spent.append(original[line])
# 					print(original[line])
# 			elif _.switches.isActive('Invert'):
# 				if not original[line] in spentI:
# 					spentI.append(original[line])
# 					print(original[line])
		


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)