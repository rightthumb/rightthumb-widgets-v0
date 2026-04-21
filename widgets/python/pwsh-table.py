import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Make', '-make' )
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


import re
import sys

def powershell_table_to_dict(powershell_table):
	powershell_table = powershell_table.replace('\r', '')
	lines = powershell_table.split('\n')
	cleaned_lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines

	if len(cleaned_lines) < 3:
		raise ValueError("Invalid PowerShell table format")

	# Extract column names from the first line
	headers_line = cleaned_lines[0]

	# Find the second line with underscores to identify column structure
	separator_line = cleaned_lines[1]

	if not separator_line:
		raise ValueError("Separator line not found")

	# Extract column start indices by finding the first dash in each column
	column_indices = [0]
	for i, char in enumerate(separator_line):
		if char == '-' and (i == 0 or separator_line[i - 1] == ' '):
			column_indices.append(i)

	# No need to find the end index of the last column, we'll use the end of the line

	# Extract column names
	headers = []
	for i in range(len(column_indices)):
		start = column_indices[i]
		end = len(headers_line) if i == len(column_indices) - 1 else column_indices[i + 1]
		headers.append(headers_line[start:end].strip())

	# Create a list of dictionaries for the data
	result = []
	for data_line in cleaned_lines[2:]:
		columns = []
		for i in range(len(column_indices)):
			start = column_indices[i]
			end = len(data_line) if i == len(column_indices) - 1 else column_indices[i + 1]
			columns.append(data_line[start:end].strip())
		data_dict = dict(zip(headers, columns))
		result.append(data_dict)
	records = []
	for rec in result:
		new = {}
		for k in rec:
			if k.strip():
				new[k]=rec[k]
		records.append(new)
	return records






def action():
	data = '\n'.join(_.isData())
	# print(data)
	try:
		table = powershell_table_to_dict(data)
		
	except:
		_.e('Invalid Format', 'Not a PowerShell table')
	# _.pv(table)
	if _.switches.isActive('Make'):
		text = ' '.join(_.switches.values('Make'))
		text = _.ci(text)
		for rec in table:
			t=text
			for k in rec:
				kk=k.upper()
				t=t.replace('{'+k+'}',rec[k])
				t=t.replace('{'+kk+'}',rec[k])
			if _.showLine(str(rec)):
				_.pr(t)
	else:
		_.pt(table)

# Get-WmiObject Win32_DiskDrive | Select-Object Model, DeviceID | py $p\pwsh-table.py
# Get-WmiObject Win32_DiskDrive | Select-Object Model, DeviceID | p pwsh-table

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);