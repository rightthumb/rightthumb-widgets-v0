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

import os, sys, time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register( 'Subject', '-sub,-source,-subject' )
	_.switches.register( 'Extension', '-ext' )
	_.switches.register( 'Folders', '-f,-folder,-folders' )
	_.switches.register( 'Recursive', '-r,-rec,-recursive' )
	_.switches.register( 'Restructure-Apps', '-sapp,-sapps,-structure' )
	_.switches.register( 'Var-Set-Print', '-v,-var,-vars' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'audit-terminal-variable-usage.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'scan c.bat and find how the variables are used',
	'categories': [
						'terminal',
						'variables',
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
						'copy D:\\Users\\Scott\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\scott\\.bashrc',
						_.hp('p audit-widget-variable-usage -ext .bat -folder D:\\.rightthumb-widgets\\widgets\\batch -subject D:\\.rightthumb-widgets\\widgets\\batch\\c.bat - scriptroot path stmp tmpf timestamp today Session_ID '),
						_.hp('p audit-widget-variable-usage -r -ext .sh -folder D:\\.rightthumb-widgets\\widgets\\bash -subject D:\\Users\\Scott\\.bashrc - scriptroot path stmp tmpf timestamp today Session_ID '),
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



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START

import _rightThumb._dir as _dir

def getFiles(folder,ext='.bat',rec=False):
	global results
	if not rec:
		results=[]
	for file in os.listdir( folder ):
		path=folder+os.sep+file
		if _.switches.isActive('Recursive') and os.path.isdir(path):
			getFiles(path,ext=ext,rec=True)
		if os.path.isfile(path):
			info = _dir.info(path)
			try:
				if info['name'].endswith(ext):
					results.append(path)
			except Exception as e:
				pass
	return results

def check(path=None,data=None,ext='.bat',p=True,sVars=None,suby=False):
	global table
	if sVars is None:
		global variables
		sVars=variables
	if data is None:
		data=_.getText(path,raw=True)
	if type(data) == list:
		data = ''.join(data)
	tester=data
	tester = _str.replaceDuplicate( tester, ' ' )
	while ' =' in tester:
		tester = tester.replace(' =','=')
	while '= ' in tester:
		tester = tester.replace('= ','=')
	dex={}
	# _.pr('path',path)
	# dex=_.vindex(data)
	i=0
	while True:
		eol=_.vindex(data,i,n='\n')
		# _.pr('eol',eol)
		while eol == i:
			i+=1
			# _.pr('fix',i)
			if i == len(data):
				# _.pr('break')
				break
			eol=_.vindex(data,i,n='\n')

		if not type(eol) == int:
			eol=len(data)-1
		_.updateLine( str(_.percentageDiffIntAuto(eol,len(data)))+'%' )
		if eol < 1:
			return None

		# line = _.rstr( data, i, eol )
		line = data[ i: eol+1 ].replace('\n','')
		# _.pr(line)
		# _.pr(line)
		# _.pr(i,eol,'line',line)
		pass
		test=''
		global add_s
		global add_e
		global printed

		for char in ' '+line+' ':
			if char in add_s+add_e+'_.0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
				test+=char
			else:
				test+=' '
		# _.pr('test',test)
		first=True
		for var in sVars:
			# _.pr('test',var,test)
			passed=False
			if ' '+add_s+var+add_e+' '.lower() in test.lower():
				passed=True
			if not passed and ( ext in ['.sh'] and ' '+var+' '.lower() in test ):
				passed=True
			if not suby:
				if ext in ['.bat'] and 'set '+var+'='.lower() in tester.lower():
					# _.pr('set '+var+'='.lower())
					passed=False
			if passed:
				if '=' in line and not '==' in line:
					pass
				elif var in line:
					# if var.lower() in test.lower():
					if not path in table:
						# _.cp(path,'yellow')
						table[path]={}


					if not var in table[path]:
						if not var in table[path]:
							table[path][var]=[]
						if p:
							if not str(path) in printed:
								_.cp(path,'cyan')
								printed.append(str(path))
							# if first:
							#     first=False
							# _.pr(var,_.get_supporting_line(data,i,rev=dex))
							# _.pr(var,sVars[var])
							_.updateLine('')
							_.cp([var,line],'ColorBold.gray')
							# _.pr(var)
					if not line in table[path][var]:
						l=_.get_supporting_line(data,i)
						table[path][var].append( l )
		pass
		i=eol+1
		if i == len(data):
			break
	_.updateLine('')
	return table


			

def findVariables(data,ext):
	subVars={}
	if type(data) == list:
		data = ''.join(data)
	# _.pr('data',data)
	# _.pr('ext',ext,len(ext))
	i=0
	while True:
		eol=_.vindex(data,i,n='\n')
		while eol == i:
			i+=1
			eol=_.vindex(data,i,n='\n')
		if not type(eol) == int: eol=len(data)-1;
		if eol < 1: break;
		line = data[ i: eol+1 ].replace('\n','')
		# _.pr('line67',line)
		pass
		pass
		line = _str.cleanBE( line, ' ' )
		line = _str.cleanBE( line, '\t' )
		line = _str.cleanBE( line, ' ' )
		line = _str.cleanBE( line, '\t' )
		if ext == '.bat':
			line = line.replace( 'SET ', 'set ' )
			if line.lower().startswith('set ') and '=' in line:
				# subVars.append(line.split('set ')[1].split('=')[0])
				subVars[line.split('set ')[1].split('=')[0].replace(' ','')]=_.get_supporting_line(data,i)
		elif ext == '.sh':
			if '=' in line and not '==' in line and not '>=' in line and not '<=' in line:
				# _.pr(line)
				if 'export ' in line:
					subVars[line.split('export ')[1].split('=')[0].replace(' ','')]=_.get_supporting_line(data,i)
				if 'alias ' in line:
					subVars[line.split('alias ')[1].split('=')[0].replace(' ','')]=_.get_supporting_line(data,i)
				else:
					subVars[line.split('=')[0].replace(' ','')]=_.get_supporting_line(data,i)
		elif ext == '.php':
			if '=' in line and not '==' in line and not '>=' in line and not '<=' in line:
				subVars[line.split('=')[0].replace(' ','')]=_.get_supporting_line(data,i)
		pass
		pass
		i=eol+1
		if i == len(data): break;

	# for line in data:

	return subVars

def action():
	global table
	global variables
	global toClean
	global add_s
	global add_e
	global var_pre
	global abort

	backup_log={}

	ext = _.switches.value('Extension')
	add_s=''
	add_e=''
	var_pre=''
	# _.pr(path)
	if ext.lower().endswith('.bat'):
		var_pre='set '
		add_s='%'
		add_e='%'
	elif ext.lower().endswith('.sh'):
		add_s='$'
		add_e=''
	if not _.switches.isActive('Folders'):    
		folders = [os.getcwd()]
	else:
		folders = _.switches.values('Folders')
	# _.pr('folders',folders)
	subjects = _.switches.values('Subject')
	if _.isWin:
		for i,sub in enumerate(subjects):
			subjects[i] = sub.lower()
	for path2 in _.switches.values('Subject'):
		variables = {}
		# _.pr(path2)
		root=_.getText(path2)
		all_variables=findVariables(root,ext)
		# _.pr('root',root)
		# _.pr('all_variables',all_variables)
		table = {}
		check(path=path2,data=root,ext=ext,p=False,sVars=all_variables,suby=True)
		# _.pr(table)
		if path2 in table:
			home=table[path2]
			# for v in home:
			#     while v in all_variables:
			#         del all_variables[v]
			# while True:
			#     d=0
			#     for v in home:
			#         if len(home[v]) == 1:
			#             d+=1
			#             del home[v]
			#             break
			#     if not d:
			#         break
			# _.pv(home)
			# sys.exit()
			table = {}
			# _.pr('home',home)
			for var in all_variables:
				v=all_variables[var]
				while '= ' in v or ' =' in v:
					v=v.replace('= ','=')
					v=v.replace(' =','=')
				if '='+add_s in v:
					if _.showLine(var) and not var in abort:
						shouldAdd=True
						# for v in home:
						#     # if add_s+var+add_e in home[v]:
						#     if var in home:
						#         # _.cp( ['err',var,home[v]] )
						#         shouldAdd=False

						if shouldAdd:
							variables[var]=all_variables[var]
							if not _.switches.isActive('Var-Set-Print'):
								_.cp(var,'red')

			pass
			roots=''.join(root)
			omitLines=[]
			if variables:
				for v in variables:
					roots=roots.replace(variables[v],'')
					# omitLines.append(variables[v].replace('\n',''))
					# _.pr(variables[v])
			# roots=''
			# for ik,line in enumerate(root):
			#     line=line.replace('\n','')
			#     if not line in omitLines:
			#         newFile+=line+'\n'
			#     else:
			#         if not path2 in backup_log:
			#             backup_log[path2]={}
			#         backup_log[path2][ik]=line
			#         newFile+='\n'
			if not _.switches.isActive('Var-Set-Print'):
				_.saveTable( backup_log, 'audit-widget-variable-usage_CLEANED.json' )
				backup_file(path2)
				_.saveText(roots,path2)
				_.cp( ['vars:',len(variables.keys())], 'green' )
				_.pr('<added>')
				_.pr(roots)
				_.pr('</added>')

			if _.switches.isActive('Var-Set-Print'):
				_.pr()
				_.pr()
				for v in variables:
					_.pr(variables[v])
				_.pr()
				_.pr()


				sys.exit()
			# _.pv(home)
			# _.pv(variables)
			# _.pv(toClean)
			# sys.exit()
			for folder in folders:
				files=getFiles(folder,ext)
				for path in files:
					path3=path
					if _.isWin:
						path3=path3.lower()
						path2=path2.lower()
					if not path2==path3:

						if not path3 in subjects:
							# _.cp(path,'cyan')
							data=_.getText(path)
							test=''.join(data)
							text=test
							test=_str.replaceDuplicate(test,' ')
							test=_str.replaceDuplicate(test,'\\')
							test=_str.replaceDuplicate(test,'/')
							check(path=path,data=data,ext=ext)
							if path in table:
								add=''
								inserted=False
								for v in table[path]:
									if v in variables:
										add+=variables[v]+'\n'
								if len(add) and ext == '.bat':
									if 'call %userprofile%\\cc.bat' in test.lower():
										text=''
										for line in data:
											if not inserted and 'call %userprofile%\\cc.bat' in line.lower():
												text+=line
												text+=add
												inserted=True
											else:
												text+=line
									elif '\\batch\\c.bat' in test.lower():
										text=''
										for line in data:
											if not inserted and '\\batch\\c.bat' in line.lower():
												text+=line
												text+=add
												inserted=True
											else:
												text+=line
									elif not '@echo' in test:
										text=add+text
										inserted=True
									elif '@echo' in test:
										text=''
										for line in data:
											if not inserted and '@echo' in line.lower():
												text+=line
												text+=add
												inserted=True
											else:
												text+=line
								elif len(add) and ext == '.sh':
									text=''
									if not 'source' in test:
										for ia,line in enumerate(data):
											if not ia:
												text+=line
												text+=add
											else:
												text+=line


									elif 'source' in test:
										for line in data:
											if not inserted and 'source' in line:
												inserted=True
												text+=line
												text+=add
											else:
												text+=line



								# _.pr(add)
								if len(''.join(data)) < len(text):
									try:
										_.pr('<add>')
										_.pr(add)
										_.pr('</add>')
										_.pr('<added>')
										_.pr(text)
										_.pr('</added>')
										ask=input('save?: ')
										if 'n' in ask.lower():
											backup_file(path)
											_.saveText(text,path)
									except Exception as e:
										pass




	pass
	_.cp( ['files:',len(table.keys())], 'green' )
	if _.switches.isActive('Var-Set-Print'):
		_.pr()
		_.pr()
		for v in variables:
			_.pr(variables[v])
		_.pr()
		_.pr()
	_.saveTable(table,'audit-widget-variable-usage.json')

fileBackup = _.regImp( focus(), 'fileBackup' )
fileBackup.switch( 'Silent' )
fileBackup.switch( 'Flag', 'imdb' )
fileBackup.switch( 'isRunOnce' )
fileBackup.switch( 'DoNotSchedule' )
def backup_file(path):
	fileBackup.switch( 'Input', path )
	fb = fileBackup.action()
	_.cp( [ fb, path ], 'Background.green' )



table = {}
abort=['i','n']
printed=[]

# os.getcwd()
########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()