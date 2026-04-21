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
##################################################


def sw():
	pass
	#b)--> examples
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
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


import simplejson as json
from geopy.distance import geodesic
from itertools import combinations

# Distance threshold in miles
distance_threshold = 1.0
xref_same_brand = False

def find_brand(element):
	if isinstance(element, dict):
		for k, v in element.items():
			if k == 'brand':
				return v
			if isinstance(v, (dict, list)):
				brand = find_brand(v)
				if brand is not None:
					return brand
	elif isinstance(element, list):
		for item in element:
			brand = find_brand(item)
			if brand is not None:
				return brand
	return None

def load_json_files(files):
	locations = []
	for file in files:
		with open(file, 'r') as f:
			data = json.load(f)
			for element in data['elements']:
				lat = element.get('lat')
				lon = element.get('lon')
				tags = element.get('tags', {})
				brand = tags.get('brand', 'Unknown')
				if brand == 'Unknown': brand = find_brand(data)
				id_ = element.get('id')
				if lat and lon:
					locations.append({
						'id': id_,
						'lat': lat,
						'lon': lon,
						'brand': brand
					})
	return locations

def find_close_matches(locations):
	close_matches = []
	for loc1, loc2 in combinations(locations, 2):
		distance = geodesic((loc1['lat'], loc1['lon']), (loc2['lat'], loc2['lon'])).miles
		if distance <= distance_threshold:
			if loc1['brand'] == loc2['brand'] and not xref_same_brand:
				continue
			close_matches.append((loc1, loc2, distance))
	return close_matches



def action():
	print('this need to be fixed')
	spent=[]
	files = _.isData(r=0)
	locations = load_json_files(files)
	close_matches = find_close_matches(locations)

	for match in close_matches:
		y=[]
		y.append(str(match[0]['id']))
		y.append(str(match[1]['id']))
		y.sort()
		x=str(y)
		if not x in spent:
			spent.append(x)
			# print(f"{match[0]['brand']} at {match[0]['lat']}, {match[0]['lon']} is close to {match[1]['brand']} at {match[1]['lat']}, {match[1]['lon']} with a distance of {match[2]:.2f} miles.")
			print(f"{match[0]['brand']} at {match[0]['lat']}, {match[0]['lon']} (ID: {match[0]['id']}) is close to {match[1]['brand']} at {match[1]['lat']}, {match[1]['lon']} (ID: {match[1]['id']}) with a distance of {match[2]:.2f} miles.")



	# rest of your code...



# def action():

#     files = _.isData(r=0)
#     if not len(files) > 1:
#         _.e('specify more than 1 json file ')

#     data = load_json_files(files)
#     closest_pairs = find_closest_pairs(data)

#     for pair in closest_pairs:
#         print(f"Closest pair: {pair[0]['id']} and {pair[1]['id']}")


# https://tyrasd.github.io/overpass-turbo/?
# https://overpass-turbo.eu/

"""
[out:json][timeout:25];
// Fetch area “Tampa, Florida” to a bounding box
(
  node["name"="The Home Depot"](27.8481, -82.5439, 28.0713, -82.2747);
  way["name"="The Home Depot"](27.8481, -82.5439, 28.0713, -82.2747);
  relation["name"="The Home Depot"](27.8481, -82.5439, 28.0713, -82.2747);
);
// print results
out body;
>;
out skel qt;
"""

"""
[out:json][timeout:25];
// Fetch area “Tampa, Florida” to a bounding box
(
  node["name"="Sam's Club"](27.8481, -82.5439, 28.0713, -82.2747);
  way["name"="Sam's Club"](27.8481, -82.5439, 28.0713, -82.2747);
  relation["name"="Sam's Club"](27.8481, -82.5439, 28.0713, -82.2747);
);
// print results
out body;
>;
out skel qt;
"""
# https://chat.openai.com/c/264d9210-f934-4fb5-bc1e-b6cd6bd9969f

# this need to be fixed

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