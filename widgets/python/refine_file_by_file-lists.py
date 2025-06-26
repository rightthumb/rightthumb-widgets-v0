import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
	_.switches.register( 'Emails', '-e,-email,-emails' )
	_.switches.register( 'File_To_Refine', '-r' )
	_.switches.register( 'File_Refine_By', '-b' )
	_.switches.register( 'Bad', '-bad' )
	
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


def compare_lists(list1, list2):
	# Convert lists to sets
	set1 = set(list1)
	set2 = set(list2)

	# Find items unique to each list
	unique_to_list1 = list(set1 - set2)
	unique_to_list2 = list(set2 - set1)

	# Find items common to both lists
	common_items = list(set1 & set2)

	return {
		'unique_to_list1': unique_to_list1,
		'unique_to_list2': unique_to_list2,
		'common_items': common_items
	}

def has_common_item(list1, list2):
	# Convert the first list to a set
	set1 = set(list1)

	# Check if any item from the second list is in the set of the first list
	for item in list2:
		if item in set1:
			return True
	return False

import re

def extract_emails(text):
	email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	emails = re.findall(email_pattern, text)
	return list(set(emails))


def has_all_common_items(listA, listB):
	"""
	Returns True if *every* item in listA is present in listB.
	"""
	setB = set(listB)  # Convert listB to a set for O(1) lookups
	for item in listA:
		if item not in setB:
			return False
	return True


def has_common_item2(item, text):
	"""
	Returns True if *any* item in listA is present in listB.
	"""
	item=item.lower().strip()
	if type(text) == list:
		text = '\n'.join(text)
	if item.lower() in text.lower():
		return True
	return False


def main_logic(fileRefineBy, FileToRefine):
	# 1) If *all* items in fileRefineBy are in FileToRefine, note it and stop.
	
	if has_all_common_items(fileRefineBy, FileToRefine):
		_.pr()
		_.pr('    Has Common Item', c='yellow')
		return
	# 2) Otherwise, for each item in fileRefineBy, decide if it's "good" or "bad".
	_.pr('Good:', c='yellow')
	Bad = []
	for by in fileRefineBy:
		if has_common_item2(by, FileToRefine):
			# "Good" item, print unless we are in 'Bad' mode
			pass
			_.pr('\t'+by,c='green')
		else:
			Bad.append(by)	
			# _.pr(by,c='red')
	_.pr('Bad:', c='yellow')
	for bad in Bad:
		_.pr('\t'+bad,c='red')
	_.pr()
	_.pr()
	_.pr()
	_.pr('    Not All Items Are Common', c='Background.red')


def action():
	# File_To_Refine File_Refine_By
	if not _.switches.isActive('File_To_Refine') or not _.switches.isActive('File_Refine_By'): _.e('File_To_Refine File_Refine_By')
	fileRefineBy = _.getText(_.switches.value('File_Refine_By'),raw=True).lower()
	FileToRefine = _.getText(_.switches.value('File_To_Refine'),raw=True).split('\n')
	Refined = []
	Bad = []
	if not _.switches.isActive('Emails'):
		fileRefineBy = fileRefineBy.split('\n')
		# not, emails > here
		main_logic(fileRefineBy, FileToRefine)

		return None
		# fileRefineBy = fileRefineBy.split('\n')
		# for i,by in enumerate(fileRefineBy):
		# 	fileRefineBy[i] = by.strip()
		
		# if has_all_common_items(fileRefineBy,FileToRefine):
		# 	_.pr()
		# 	_.pr('    Has Common Item',c='yellow')
		# 	return None
		
		# for by in fileRefineBy:
		# 	if has_common_item([by],FileToRefine):
		# 		if not _.switches.isActive('Bad'):
		# 			_.pr(by)
		# 	else:
		# 		if _.switches.isActive('Bad'):
		# 			_.pr(by)
		# # spent = []
		# # for by in fileRefineBy:
		# 	# print(by)
		# 	# for i,ref in enumerate(FileToRefine):
		# 	# 	ref = ref.strip()
		# 	# 	if by.lower() in ref.lower():
		# 	# 		if not by in spent:
		# 	# 			spent.append(by)
		# 	# 			Refined.append(ref)
		# 	# 			if not _.switches.isActive('Bad'):
		# 	# 				_.pr(by.replace(', ','","'))
		# 	# 	else:
		# 	# 		if not by in spent:
		# 	# 			spent.append(by)
		# 	# 			if _.switches.isActive('Bad'):
		# 	# 				_.pr(by.replace(', ','","'))
		# 	# 			Bad.append(by)
		
		# # not, emails > end
		# _.pr()
		# _.pr('    Not Emails',c='yellow')
		return None
	
	# yes, emails > here

	bEmails = extract_emails(fileRefineBy)
	for line in FileToRefine:
		rEmails = extract_emails(line.lower())
		if has_common_item(rEmails,bEmails):
			Refined.append(line)
			if not _.switches.isActive('Bad'):
				_.pr(line.replace(', ','","'))
		else:
			if _.switches.isActive('Bad'):
				_.pr(line.replace(', ','","'))
			Bad.append(line)
		
		
		return None
	
	bEmails = extract_emails(fileRefineBy)
	# for i,e in enumerate(bEmails):
	# 	emails[i] = e.strip()
	# 	# _.pr(e)

	Bad = []
	Refined = []


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)