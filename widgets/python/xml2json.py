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
os=__.os
##################################################


def sw():
	pass
	#b)--> examples
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'RecordKey', '-k,-key,-r,-rec,-record', 'Field Script Object' )
	_.switches.register( 'Save', '-save', '..\\json   OR   ..\\json\\fields.json' )

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






########################################################################################

# from bs4 import BeautifulSoup, Comment
# import json


# def extract_attributes_and_text(tag):
#     data = {}
#     for attr, value in tag.attrs.items():
#         data[f"{tag.name}_{attr}'] = value
#     text_content = tag.get_text(strip=True)
#     if text_content:
#         data['CONTENT'] = text_content
#     return data

# def extract_script_content(tag):
#     script_content = {}
#     cdata = tag.find(text=lambda text: isinstance(text, Comment))
#     if cdata:
#         script_content['SCRIPT_CDATA'] = str(cdata)
#     else:
#         script_content['SCRIPT_TEXT'] = tag.get_text()
#     return script_content

# def traverse_xml_for_tag(file_name, tag_name="Field"):
#     with open(file_name, 'r', encoding="utf-8") as file:
#         contents = file.read()
	
#     soup = BeautifulSoup(contents, 'lxml-xml')
#     records = []

#     for tag in soup.find_all(tag_name):
#         record = extract_attributes_and_text(tag)
#         script_tag = tag.find('Script')
#         if script_tag:
#             record.update(extract_script_content(script_tag))
#         records.append(record)

#     return records

# def xml_to_json(tag):
# 	"""Convert a BeautifulSoup tag and its children into a JSON-compatible dictionary."""
# 	result = {}

# 	# Process tag attributes
# 	if tag.attrs:
# 		result.update(tag.attrs)

# 	# Recursively process child tags
# 	child_json = {}
# 	for child in tag.children:
# 		if child.name:
# 			# Recurse into child
# 			child_data = xml_to_json(child)
# 			# Handle multiple children with the same name by storing them in a list
# 			if child.name in child_json:
# 				# Ensure we have a list to add to
# 				if not isinstance(child_json[child.name], list):
# 					child_json[child.name] = [child_json[child.name]]
# 				child_json[child.name].append(child_data)
# 			else:
# 				child_json[child.name] = child_data

# 	# Combine text (stripped of whitespace) with child tags
# 	text_content = tag.get_text(strip=True)
# 	if child_json:
# 		if text_content:
# 			result['_text'] = text_content
# 		result.update(child_json)
# 	elif text_content:
# 		return text_content
# 	else:
# 		return result

# 	return result

# def search_and_convert_to_json(filename, tag_name="Field"):
# 	with open(filename, 'r', encoding='utf-8') as file:
# 		soup = BeautifulSoup(file, 'lxml-xml')

# 	records = []

# 	# Find all tags that match the given tag_name
# 	for tag in soup.find_all(tag_name):
# 		record = xml_to_json(tag)
# 		records.append(record)

# 	return records


# def action():
# 	flatten=False
# 	tag_name = "Field"
# 	if _.switches.isActive('RecordKey') and len(_.switches.value('RecordKey')):
# 		tag_name = _.switches.values('RecordKey')[0]

# 	if flatten:
# 		records = traverse_xml_for_tag(_.pp()[0], tag_name)
# 		for record in records:
# 			print(record)
# 	else:
# 		records = search_and_convert_to_json(_.pp()[0], tag_name)
# 		print(json.dumps(records, indent=2))
# 	_.saveTable2(records,_.pp()[0].replace('.xml','')+'.json')
########################################################################################



from bs4 import BeautifulSoup, Comment
import json

# Convert BeautifulSoup tag to JSON
def xml_to_json(tag):
	result = {}
	if tag.attrs:
		result.update(tag.attrs)
	child_json = {}
	for child in tag.children:
		if child.name:
			child_data = xml_to_json(child)
			if child.name in child_json:
				if not isinstance(child_json[child.name], list):
					child_json[child.name] = [child_json[child.name]]
				child_json[child.name].append(child_data)
			else:
				child_json[child.name] = child_data

	text_content = tag.get_text(strip=True)
	if child_json:
		if text_content:
			result['_text'] = text_content
		result.update(child_json)
	elif text_content:
		return text_content
	else:
		return result
	return result

# Convert XML to JSON based on a tag name
def search_and_convert_to_json(xml_str, tag_name="Script"):
	soup = BeautifulSoup(xml_str, 'lxml-xml')
	records = []
	for tag in soup.find_all(tag_name):
		record = xml_to_json(tag)
		records.append(record)
	return records

# Your existing action function
def action():
	return None
	flatten = False
	tag_name = "Field"
	if _.switches.isActive('RecordKey') and len(_.switches.value('RecordKey')):
		tag_name = _.switches.values('RecordKey')[0]

	if flatten:
		records = traverse_xml_for_tag(_.pp()[0], tag_name)  # Assuming traverse_xml_for_tag is defined
		for record in records:
			print(record)
	else:
		records = search_and_convert_to_json(_.pp()[0], tag_name)
		print(json.dumps(records, indent=2))
	_.saveTable2(records, _.pp()[0].replace('.xml', '') + '.json')

# # Example XML string
# xml_str = '''<fmxmlsnippet type="FMObjectList"> ... </fmxmlsnippet>'''  # Replace '...' with your actual XML content

# Test the function
if __name__ == "__main__":
	xml_str=_.getText(_.switches.values('Files')[0],raw=True)
	# print(xml_str)
	search='Script'
	if _.switches.isActive('RecordKey'):
		search=_.switches.value('RecordKey')
	else:
		if 'field' in _.switches.value('Files').lower(): search='Field'
		elif 'script' in _.switches.value('Files').lower(): search='Script'
		elif 'layout' in _.switches.value('Files').lower(): search='Object'
		else: search='Object'
	result = search_and_convert_to_json(xml_str, search)
	print(json.dumps(result, indent=4))
	if _.switches.isActive('Save'):
		save=_.switches.value('Save')
		if os.path.isdir(save):
			if not save.endswith(os.sep): save+=os.sep
			fi=_.switches.values('Files')[0]
			if os.sep in fi:
				fi=fi.split(os.sep)[-1]
			if fi.lower().endswith('.xml'):
				fi=fi[0:len(fi)-4]
			save+=fi+'.json'
		save2=__.path(save)
		_.saveTable2(result,save)
		_.pr('Saved:',save,c='green')




########################################################################################


# from bs4 import BeautifulSoup, Comment
# import json

# def extract_attributes_and_text(tag):
#     data = {}
#     for attr, value in tag.attrs.items():
#         data[f"{tag.name}_{attr}'] = value
#     text_content = tag.get_text(strip=True)
#     if text_content:
#         data['CONTENT'] = text_content
#     return data

# def extract_script_content(tag):
#     script_content = {}
#     cdata = tag.find(text=lambda text: isinstance(text, Comment))
#     if cdata:
#         script_content['SCRIPT_CDATA'] = str(cdata)
#     else:
#         script_content['SCRIPT_TEXT'] = tag.get_text()
#     return script_content

# def traverse_xml_for_tag(file_name, tag_name="Field"):
#     with open(file_name, 'r', encoding="utf-8") as file:
#         contents = file.read()
	
#     soup = BeautifulSoup(contents, 'lxml-xml')
#     records = []

#     for tag in soup.find_all(tag_name):
#         record = extract_attributes_and_text(tag)
#         for script_tag in tag.find_all('Script'):
#             record.update(extract_script_content(script_tag))
#         records.append(record)

#     return records

# def xml_to_json(tag):
#     result = {}
#     if tag.attrs:
#         result.update(tag.attrs)
#     child_json = {}
#     for child in tag.children:
#         if child.name:
#             child_data = xml_to_json(child)
#             if child.name in child_json:
#                 if not isinstance(child_json[child.name], list):
#                     child_json[child.name] = [child_json[child.name]]
#                 child_json[child.name].append(child_data)
#             else:
#                 child_json[child.name] = child_data
#     text_content = tag.get_text(strip=True)
#     if child_json:
#         if text_content:
#             result['_text'] = text_content
#         result.update(child_json)
#     elif text_content:
#         return text_content
#     else:
#         return result
#     return result

# def search_and_convert_to_json(filename, tag_name="Field"):
#     with open(filename, 'r', encoding='utf-8') as file:
#         soup = BeautifulSoup(file, 'lxml-xml')

#     records = []
#     for tag in soup.find_all(tag_name):
#         record = xml_to_json(tag)
#         records.append(record)
#     return records

# def action():
#     flatten = False
#     tag_name = "Field"
#     if _.switches.isActive('RecordKey') and len(_.switches.value('RecordKey')):
#         tag_name = _.switches.values('RecordKey')[0]

#     if flatten:
#         records = traverse_xml_for_tag(_.pp()[0], tag_name)
#         for record in records:
#             print(record)
#     else:
#         records = search_and_convert_to_json(_.pp()[0], tag_name)
#         print(json.dumps(records, indent=2))
#     _.saveTable2(records, _.pp()[0].replace('.xml', '') + '.json')

# if __name__ == '__main__':
	# action()


# https://chat.openai.com/c/a2eb5199-63d2-454c-9ea0-329b77a8e502


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

