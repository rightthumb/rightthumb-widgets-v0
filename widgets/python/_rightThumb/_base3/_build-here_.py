#!/usr/bin/python3
import os,sys,time,importlib,simplejson
if sys.platform[0] == 'w': figpath=os.getenv('USERPROFILE') +os.sep+'.rt'+os.sep+ '.config.hash'
else: figpath=os.getenv('HOME') +os.sep+'.rt'+os.sep+ '.config.hash'
def getTable( file ):
		json_data={}
		if os.path.isfile(file):
				with open(file,'r', encoding="latin-1") as json_file: json_data = simplejson.load(json_file)
		return json_data
fig=getTable(figpath)
sys.path.append( fig['w']+'/widgets/python'.replace('/',os.sep) )
