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
# import simplejson as json
# import shutil

import _rightThumb._construct as __
__.appReg = __name__
import _rightThumb._base2 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

# _.switches.register('Input', '-i','appIn.py')
_.switches.register('Output', '-o','1')
_.switches.register('JustVar', '-justvar')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo[__name__]=    {
	'file': 'movieTitle.py',
	'description': 'Extract title from path',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo[__name__]['examples'].append('data | p movieTitle')

# _.appInfo[__name__]['columns'].append({'name': 'name', 'abbreviation': 'n'})


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True


_.switches.process()
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f

def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

	
pipeData = ''

if not sys.stdin.isatty():
	pipeData = sys.stdin.readlines()
	try:
		if not pipeData[0][0] in _str.safeChar:
			pipeData[0] = pipeData[0][1:]
	except Exception as e:
		pass

########################################################################################
def clean( p ):
	p = p.replace('\n','')
	p = p.replace('\r','')
	p = p.replace('\t','')
	p = _str.replaceDuplicate(p,' ')
	p = _str.cleanBE(p,' ')
	# dots = p.split('.')
	# print(dots[len(dots)-1])
	# p.replace(dots[len(dots)-1],'')
	line = ''
	i=0
	for t in p.split('.'):
		i+=1
		if not i == len(p.split('.')):
			line += t + ' '
	p = line
	p = _str.replaceAll(p,'_',' ')
	# p = _str.totalStrip7(p)
	p = p.replace('_',' ')
	p = p.replace('.',' ')
	# p = line
	line = p.split('(')[0]
	line = _str.cleanBE(line,' ')
	if len(line) == 0:
		try:
			line = p.split(')')[1]
		except Exception as e:
			pass
	line = _str.cleanBE(line,' ')
	line = line.split('.')[0].split('HD-TS')[0].split('x264')[0].split('1080P')[0].split('1080p')[0].split('720p')[0].split('HDRip')[0].split('HDCLUB')[0].split('BluRay')[0].split('BluRay')[0].split('_track')[0].split(' HDTV')[0].split(' MULTI ')[0].split( '2160P' )[0].split( '2160p' )[0].split( '512Kb' )[0]
	line = line.lower()
	line = line.title()
	line = _str.cleanBE(line,' ')
	if '(' in p:
		line += ' ' + p.split('(')[1].split(')')[0]
	# print(line.encode('ascii'))
	y = False
	for l in line.split(' '):
		if len(l) == 4:
			try:
				test0 = int(l)
				test1 = str(test0)
			except Exception as e:
				test1 = ''
			if len(test1) == 4:
				year = l
				y = True
	if y:
		line = line.replace(year,'')
		# line = line + ' ' + year
		line = year + ' ' + line
	line = _str.replaceDuplicate(line,' ')
	# line = line.replace('WwW SeeHD PL','').replace('WwW SeeHD','').replace('NEW','').replace('new','').replace('New','').replace('WEB-DL','').replace('WEB-DLRip','').replace('46Gb','').replace('Rip 1  Line MegaPeer','')
	# line = line.replace('P TS','')
	line = removeStuff(line)
	line = _str.charFix( line )
	line = _str.replaceDuplicate(line,' ')
	line = _str.cleanBE(line,' ')
	return line

def action():
	global pipeData
	global theTitle
	result = []
	dataType = 'filename'
	for p in pipeData:
		# print( ( p ) )
		# sys.exit()
		if type( p ) == dict:
			dataType = 'dict'
			f = p['folder'].lower().split(_v.slash)
			folder = f[ len(f)-1 ]

			if folder == 'samples' or folder == 'extras':
				folder = f[ len(f)-2 ]
			elif folder == 'mobile movies':
				folder = ''

			line = clean( folder + ' ' + p['name'] )
		else:
			line = clean( p )
		# print( line )
		if len(line) > 0 and not 'sample' in line:
			if dataType == 'filename':
				result.append(line)
			else:
				result.append( { 'title': line, 'folder': p['folder'], 'file': p['name'], 'mod': p['date_modified_raw'], 'bytes': p['bytes'] } )
	if dataType == 'filename':
		for res in  set(result):
			if _.switches.isActive('JustVar'):
				theTitle = res.title()
			else:
				print(res.title())
	else:
		for res in  (result):
			if _.switches.isActive('JustVar'):
				theTitle = { 'title': res['title'].title(), 'folder': res['folder'], 'file': res['file'], 'mod': res['mod'], 'bytes': res['bytes'] }
			else:
				print( res['title'].title()+',', res['folder']+',', res['file'] )
	if 'sample' in theTitle.lower():
		theTitle = 'sample'
			

def removeStuff( line ):
	stuff = [
				'WwW SeeHD PL',
				'WwW SeeHD',
				'NEW',
				'new',
				'New',
				'WEB-DL',
				'WEB-DLRip',
				'46Gb',
				'Rip 1  Line MegaPeer',
				'P TS',
				'E:\\MOVIES'+_v.slash,
				'dvdrip',
				'xvid',
				'kinokopilka',
				' www ',
				' dvdrip ',
				' Hmark ',
				' Dvdrip ',
				'Xvid',
				'Bgaudio',
				'Siso',
				'-',
				'"',
				'Dvdrip',
				'Brrip',
			]
	for s in stuff:
		line = line.replace(s,' ')
	return line
theTitle = ''
########################################################################################
if __name__ == '__main__':
	action()