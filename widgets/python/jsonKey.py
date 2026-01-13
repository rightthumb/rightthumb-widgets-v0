#!/usr/bin/python3.11

def switches(): 
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.json' )
	_.switches.register( 'Keys', '-k,-key,-keys','id name' )

import requests; exec(requests.get('https://sds.sh/micro.py/').text); exec(loader);
########################################################################################
#n)--> start

import simplejson

def action():
	try:
		if __.Pipe: pass
	except:
		__.Pipe = False
	if __.Pipe and type(__.Pipe) == str:
		__.Pipe = __.Pipe.split('\n')
	
	if __.Pipe:
		_.isData(__.Pipe,save=True)
	data = ''
	if not _.switches.isActive('Files') and _.isData(r=0):
		raw = '\n'.join(_.isData(r=0))
		if raw.startswith('{') or raw.startswith('['):
			data = simplejson.loads( raw )
		else:
			data = _.fromYML(raw)


	elif _.switches.isActive('Files'):
		data = _.getJsonYaml(_.switches.values('Files')[0])

	if not data:
		_.pr('No Data',c='red')
		return

	# _.pv(data)
	for key in _.switches.values('Keys'):
		if key in data:
			print( data[key] )
	

	
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)