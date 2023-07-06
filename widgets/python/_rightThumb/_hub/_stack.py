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

import sys
class Subject:
	def __init__( self ):
		self.theAPP = '_rightThumb._hub'
		self.childFiles = [
								"app.py",
								"app_file.py",
								"app_files.py",
								"app_ls.py",
								"construct.py",
								"conversion.py",
								"imports.txt.py",
								"terminal.py",
								"tmp.py",
								"type",                                "_construct.py",
								"_fields.py",
								"_func.py",
								"_hub_init_example.py",
								"_hub_init_example2.py",
								"_imp.py",
								"_json.py",
								"_jsonfix.py",
								"_string.py",
								"_switches.py",
								"_switches.py.bk",
								"_tables.py",
								"_test.py",
								"_vars.py",
								"__init__.py",
							]

	def callLocation( self, data, name=None ):
		file = None
		line = None
		function = None
		data = str(data)
		path = data.split('"')[1]
		p = path.split(_v.slash)
		file = p.pop().replace('.py','')
		if file == '__init__':
			one = p.pop()
			two = p.pop()
			file = two+'.'+one

		left = data.split('"')[2].split(' ')
		line = left[len(left)-1].replace( '>', '' )
		function = data.split(' ')[2]
		if function == '<module>':
			return None
		if '_bootstrap' in function:
			return None

		if function == '__init__':
			function = 'CLASS'

		return {
					'name': name,
					'file': file,
					'line': line,
					'function': function,
		}

	def c( self, i=1, depth=0, record=False, isChild=None, callers=False, notChild=None,     r=None, c=None, d=None, nc=None ):
		if not nc is None:
			notChild = nc
		if not d is None:
			depth = d
		if not c is None:
			isChild = c
		if not r is None:
			record = r
		if not isChild is None:
			record=True

		notMatrix = True
		if not notChild is None:
			notMatrix = True
		if not isChild is None:
			notMatrix = True

		callersData = self.callers( i )
		programs = []
		for cd in callersData:
			if cd['file'] in program_registration_list:
				programs.append(cd['file'])

		result = callersData
		if True and record:
			result = {
						'file': callersData[depth]['file'],
						'function': callersData[depth]['function'],
						'line': callersData[depth]['line'],
						'programs': programs,
						'name': callersData[depth]['name'],
			}
			if notMatrix and result['file'] == self.theAPP:
				depth+=1
				if len(callersData)-1 >= depth:
					result = {
								'file': callersData[depth]['file'],
								'function': callersData[depth]['function'],
								'line': callersData[depth]['line'],
								'programs': programs,
								'name': callersData[depth]['name'],
					}
			if not notChild is None and notChild:
				error = False
				while result['file'] in self.childFiles and not error:
					depth+=1
					try:
						result = {
									'file': callersData[depth]['file'],
									'function': callersData[depth]['function'],
									'line': callersData[depth]['line'],
									'programs': programs,
									'name': callersData[depth]['name'],
						}
					except Exception as e:
						error = True
				if error:
					result['error'] = 'notChild excede i'


		if callers and type(result) == dict:
			return { 'caller': result, 'stack': callersData }
		return result

	def fn( self, i=1, var='name' ):
		callers = []
		error=False
		done=False
		i=-1
		fn=[]
		while not done:
			i+=1
			try:
				fn.append(sys._getframe(i).f_code.co_name)
			except Exception as e:
				print(e)
				return fn

	def var( self, i=1, var='name' ):
		callers = []
		error=False
		while not error:

			try:
				try:
					try:
						n = ''+sys._getframe(i).f_back.f_locals['registration']['name']+''
					except Exception as e:
						n = ''
					if n == '':
						try:
							n = ''+sys._getframe(i).f_back.f_locals[var]+''
						except Exception as e:
							n = ''
					if n == '':
						try:
							# n = sys._getframe(i).f_back.f_locals['self'].name
							n = eval( "sys._getframe(i).f_back.f_locals['self']."+var )
						except Exception as e:
							n = ''

					x = self.callLocation(  sys._getframe(i).f_back.f_code, n  )



				except Exception as e:
					x = None
					# x = dir(sys._getframe(i))
				xxx = sys._getframe(i).f_code.co_name

				if '_bootstrap' in xxx:
					error=True
				else:
					if not x is None:
						callers.append(x)

			except Exception as e:
				error=True
			i+=1
		return callers



