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
import os
# import simplejson as json
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
import simplejson as json

from collections import OrderedDict

_.switches.register('Input', '-i,-in')
_.switches.register('Output', '-o')

_.switches.register('Fields', '-fields')

_.appInfo=    {
	'file': 'refinejson.py',
	'description': 'select json fields to use',
	'prerequisite': [],
	'examples': [],
	'postrequisite': [],
	'projectRelated': [],
	'exampleNotes': [],
	'columns': [],
	'switchRequired': True,
	
	}

_.appInfo['prerequisite'].append('p file --c | p line --c -make "type {} | p line --c -noclean > cleaned\{} " | p execute')
_.appInfo['prerequisite'].append('p  file --c + .csv | p line --c -make "p csv2json -i {} -o json\\{}.json" | p execute')
_.appInfo['examples'].append('p refinejson -i Alababama_b.CSV.json -o refined\outfile.json -fields "First Name" "Last Name" "E-mail Address"')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p file --c + .json | p line --c -make "p refinejson -i {} -o refined\\{} -fields ;\'First Name;\' ;\'Last Name;\' ;\'E-mail Address;\' " | p execute')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('Post:\n\t\tp json2csv -i outfile.json -o csv\\file.csv')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('\tp file --c + .json | p line --c -make "p json2csv -i {} -o csv\\{}.csv" | p execute')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('\tp file --c + .csv | p line --c -make "type {} | p line --c > cleaned\\{}" | p execute')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('\tp file --c + .csv | p line --c -make "type {} | p line --c + @ First -or > withEmail\\{}" | p execute')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('\tPostPost:\n\t\t\ttype file.csv | p line --c > cleaned\\file.csv')

_.appInfo['examples'].append('')
_.appInfo['examples'].append('\tp jsonfields -i New_York_b.CSV.json -o _New_York_b.CSV.json -fields "Business City" "Other City" -newfield City')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('type "Florida Georgia.CSV.json" | p line - null00 null ;\'Notes;\';. + company')
_.appInfo['examples'].append('p f -in *.json -n - null00 null ;\'Notes;\';. + company')

_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})

#     Address 1
#     Address 2
#     City
#     State
#     Zip Code
#     First & Last Name
#     Client Company
#     Direct Phone
#     Email 1 & Email 2
#     Fax
#     Department
#     General Comments
#     Mobile Phone
#     Country

# def formatColumns(columns):
#     result = ''
#     for c in columns.split(','):
#         for col in _.appInfo['columns']:
#             for a in col['abbreviation'].split(','):
#                 if a == c:
#                     c = col['name']
#         result += c + ','
#     result = result[:-1]
#     return result

# _.switches.trigger('Fields',formatColumns)
# _.switches.trigger('Input',formatColumns)
_.switches.process()


########################################################################################

def action():
	if _.switches.isActive('Input') == False:
		print('Error: No input')
		sys.exit()
	columnNames = _.switches.value('Fields')
	# print(columnNames)
	jsonFile = _.getTable2(_.switches.value('Input'))
	newJSON = []
	for item in jsonFile:
		row = []
		for c in columnNames.split(','):
			row.append(item[c])

		newJSON.append({})
		ii = 0
		for r in row:
			try:
				newJSON[len(newJSON)-1][columnNames.split(',')[ii]] = r
			except Exception as e:
				try:
					newJSON[len(newJSON)-1][columnNames.split(',')[ii]] = ''
				except Exception as e:
					print('error')
			ii += 1

	# print(newJSON)
	if _.switches.isActive('Output') == True:
		_.saveTable2(newJSON,_.switches.value('Output'))


########################################################################################
if __name__ == '__main__':
	action()





'''
p renamespace
md cleaned
p file --c + .csv | p line --c -make "type {} | p line --c -precsv2json > cleaned\{}" | p execute
cd cleaned
md json
p  file --c + .csv | p line --c -make "p csv2json -i {} -o json\{}.json" | p execute
cd json
::            md cleaned
::            p file --c + .csv | p line --c -make "type {} | p line --c -fixchar  > cleaned\{}" | p execute
::            cd cleaned
::            md cleaned
::            p file --c + .csv | p line --c -make "type {} | p line --c  -postcsv2json > cleaned\{}" | p execute
::            cd cleaned
md repaired
p file --c + .json | p line --c -make "p jsonfields2 -i {} -o repaired\{} -fields ;'Address=;Home Address PO Box,Other Address PO Box,Business Address PO Box*City=;Business City,Home City,Other City*State=;Business State,Home State,Other State*Zip=;Business Postal Code,Home Postal Code,Other Postal Code*Email=;E-mail Address,E-mail 2 Address,E-mail 3 Address*Phone=;Business Phone,Business Phone 2,Car Phone,Company Main Phone,Home Phone,Home Phone 2,Mobile Phone,Other Phone,Primary Phone*Fax=;Business Fax,Home Fax,Other Fax;'" | p execute
cd repaired

md appended

:::        p appendjson -i %file% -o appended\%file% -fields State 00;City ""

set file=Alababama_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State AL

set file=Arizona_Phoe_Scotts_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State AZ

set file=Atlanta_big_b_add_to_other_atlanta.CSV.json
p appendjson -i %file% -o appended\%file% -fields State GA;City Atlanta

set file=Atlanta_b_add_to_other_atlanta.CSV.json
p appendjson -i %file% -o appended\%file% -fields State GA;City Atlanta

set file=Boston_B.CSV.json
p appendjson -i %file% -o appended\%file% -fields State MA;City Boston

set file=California_B.CSV.json
p appendjson -i %file% -o appended\%file% -fields State CA

set file=Chicago_large_B_merger_with_chi.CSV.json
p appendjson -i %file% -o appended\%file% -fields State IL;City Chicago

set file=Chicago_small_B_merger_with_chi_large.CSV.json
p appendjson -i %file% -o appended\%file% -fields State IL;City Chicago

set file=Dallas_Houston_Wichita_a_Seperate_out_Wichita.CSV.json
p appendjson -i %file% -o appended\%file% -fields State TX

set file=Florida_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State FL

set file=IND_Indianapolis_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State IN;City Indianapolis

set file=Louisiana_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State LA

set file=Nashville_Tenn_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State TN;City Nashville

set file=NC_SC_b_Split_these_into_two_states.CSV.json
p jsonfields2 -i %file% -o appended\%file% -fields "State=NC-SC;Business State,Home State,Other State"


set file=New_York_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State NY

set file=Ohio_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State OH

set file=PA_Pitts_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State PA;City Pittsburgh

set file=St_Louis_MO_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State MO;City "St Louis"

set file=Texas_South_b_blend_with_dallas_etc.CSV.json
p appendjson -i %file% -o _%file% -fields State TX
p jsonfields2 -i _%file% -o appended\%file% -fields "City=Dallas;Business City,Home City,Other City"

set file=Texas_So_10a.CSV.json
p appendjson -i %file% -o appended\%file% -fields State TX

set file=TX_San_Antonio_a.CSV.json
p appendjson -i %file% -o _%file% -fields State TX
p jsonfields2 -i _%file% -o appended\%file% -fields "City=San Antonio;Business City,Home City,Other City"

set file=Wash_DC_VA_b.CSV.json
p appendjson -i %file% -o appended\%file% -fields State WA;City "Washington DC"


set file=

cd appended
md refined
p file --c + .json | p line --c -make "p refinejson -i {} -o refined\{} -fields ;'First Name;' ;'Last Name;' Company Email Phone Fax Address City State Zip Notes" | p execute
cd refined
md csv
p file --c + .json | p line --c -make "p json2csv -i {} -o csv\{}.csv" | p execute
cd csv
md cleaned
p file --c + .csv | p line --c -make "type {} | p line --c -strict -fixcsv > cleaned\{}" | p execute
cd cleaned
md ordered
p file --c + .csv | p line --c -make "p csvColumnOrder -i {} -o ordered\{} -fields ;'First Name;' ;'Last Name;' Company Email Phone Fax Address City State Zip Notes" | p execute
cd ordered
md cleaned
p file --c + .csv | p line --c -make "type {} | p line --c -strict > cleaned\{}" | p execute
rename cleaned Contacts_Final
zip Contacts_Final
cd Contacts_Final
d



md cleaned
p file --c + .csv | p line --c -make "type {} | p line --c -postcsv2json > cleaned\{}" | p execute
cd cleaned





md withEmail
p file --c + .csv | p line --c -make "type {} | p line --c + ;'@;' First -or > withEmail\{}" | p execute
md all
move *.csv all\

done




p json2csv -i Alababama_b.CSV.json -o _test.csv

p json2csv -i _Alababama_b.CSV.json -o csv\_Alababama_b.CSV.json.csv



refinejson
appendjson
combinejsonfiles
jsonfields2

csv2json
json2csv

csvColumnOrder

csv2json
json2csv
json2csv2




'''
'''
newField=Dallas;fie ld0,field1*newField02=FL;field04,field05

Address=;Home Address PO Box,Other Address PO Box,Business Address PO Box*
City=;Business City,Home City,Other City*
State=;Business State,Home State,Other State*
Zip=;Business Postal Code,Home Postal Code,Other Postal Code*
Email=;E-mail Address,E-mail 2 Address,E-mail 3 Address*
Phone=;Business Phone,Business Phone 2,Car Phone,Company Main Phone,Home Phone,Home Phone 2,Mobile Phone,Other Phone,Primary Phone*
Fax=;Business Fax,Home Fax,Other Fax*
'''