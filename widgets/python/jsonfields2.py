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

# import os
import sys
import simplejson as json
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str


_.switches.register('Input', ',-i','file.json')
_.switches.register('Output', ',-o','folder\file.json')
_.switches.register('Move', '-move','folder_2_move_completed_input_files')
# {'name': 'Action','switch': '-action', 'pos': None, 'active': False,'expected_input_example': 'len'}
_.switches.register('Fields', '-fields','"newField=Dallas;fie ld0,field1*newField02=FL;field04,field05"')
_.switches.register('Default', '-default','Dallas')


import shutil


_.appInfo=    {
	'file': 'jsonfields2.py',
	'description': 'add a field and set data for an entire json file',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

# _.appInfo['examples'].append('p jsonfields2 -i file.json -o appended\\file.json -move done -fields "Business City" "Other City" -newfield City')
_.appInfo['examples'].append('p jsonfields2 -i file.json -o _file.json -fields "newField=Dallas;fie ld0,field1*newField02=FL;field04,field05"')
_.appInfo['examples'].append('')
_.switches.process()



########################################################################################
def action():
	if _.switches.isActive('Input') == False or _.switches.isActive('Output') == False or _.switches.isActive('Fields') == False:
		print('Error: Missing input')
		sys.exit()
	# print(_.ci(_.switches.value('Input')))
	# sys.exit()
	jsonFile = _.getTable2(_.ci(_.switches.value('Input')))
	# jsonFile = _.getTable2('Alababama_b.CSV.json')
	# sys.exit()
	fields = _.switches.value('Fields')

	i = 0
	for item in jsonFile:
		for thisFieldSet in fields.split('*'):
			thisSet = thisFieldSet.split(';')
			newSet = thisSet[0].split('=')
			newfieldData = newSet[1]
			cnt = 0
			for thisField in thisSet[1].split(','):
				# print(thisField)
				# print(jsonFile[i][thisField])
				try:
					if len(jsonFile[i][thisField]) > cnt:
						# print(jsonFile[i][thisField])
						cnt = len(jsonFile[i][thisField])
						newfieldData = jsonFile[i][thisField]
				except Exception as e:
					pass
			jsonFile[i][newSet[0]] = newfieldData
			# jsonFile[i][newSet[0]] = newfieldData.encode('UTF-8')
			
		i += 1

	_.saveTable2(jsonFile,_.switches.value('Output'))

	if _.switches.isActive('Move') == True:
		shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))




'''
newField=Dallas;field0 field1*newField02=FL;field04 field05

Address=;Home Address PO Box,Other Address PO Box,Business Address PO Box*
City=;Business City,Home City,Other City*
State=;Business State,Home State,Other State*
Zip=;Business Postal Code,Home Postal Code,Other Postal Code*
Email=;E-mail Address,E-mail 2 Address,E-mail 3 Address*
Phone=;Business Phone,Business Phone 2,Car Phone,Company Main Phone,Home Phone,Home Phone 2,Mobile Phone,Other Phone,Primary Phone*
Fax=;Business Fax,Home Fax,Other Fax*

543

p file --c + .json | p line --c -make "p jsonfields2 -i {} -o repaired\{} -fields ;'Address=;Home Address PO Box,Other Address PO Box,Business Address PO Box*City=;Business City,Home City,Other City*State=;Business State,Home State,Other State*Zip=;Business Postal Code,Home Postal Code,Other Postal Code*Email=;E-mail Address,E-mail 2 Address,E-mail 3 Address*Phone=;Business Phone,Business Phone 2,Car Phone,Company Main Phone,Home Phone,Home Phone 2,Mobile Phone,Other Phone,Primary Phone*Fax=;Business Fax,Home Fax,Other Fax;'" | p execute

p jsonfields2 -i Ohio_b.CSV.json -o repaired\Ohio_b.CSV.json -fields "Address=;Home Address PO Box,Other Address PO Box,Business Address PO Box*City=;Business City,Home City,Other City*State=;Business State,Home State,Other State*Zip=;Business Postal Code,Home Postal Code,Other Postal Code*Email=;E-mail Address,E-mail 2 Address,E-mail 3 Address*Phone=;Business Phone,Business Phone 2,Car Phone,Company Main Phone,Home Phone,Home Phone 2,Mobile Phone,Other Phone,Primary Phone*Fax=;Business Fax,Home Fax,Other Fax"

Address City State Zip Email Phone Fax

'''

	


########################################################################################
if __name__ == '__main__':
	action()





