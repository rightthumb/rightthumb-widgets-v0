import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext
from datetime import datetime as dt, timedelta
import datetime
from datetime import date
try:
	import dateutil.relativedelta
except Exception as e:
	pass
import time
from pathlib import Path
import _rightThumb._construct as __
import _rightThumb._vars as _v
import _rightThumb._md5 as _md5
import _rightThumb._mimetype as _mime
import hashlib
try:
	import simplejson as json
except:
	try:
		import json
	except:
		pass
import _rightThumb._base3 as _
__.dir=_.dot()
__.dir.print=False
print_fields = 'path, name, parent, bytes, size, date_created, date_modified, ext, week_of_year, day_of_the_week, md5, sha256, date_accessed, ce, me, ae, ago, header, lines'.split(', ')
def _lines_(filename):

	try:
		with open(filename) as f:
			for i, asdf in enumerate(f): pass
		return i + 1
	except Exception as e:
		_.pr(e,c='red')
		return 1

"""
[
	{
		"path": "D:\\tech\\programs\\python\\src\\windows\\5e.py",
		"name_": "5e.py",
		"name": "5e.py",
		"folder": "D:\\tech\\programs\\python\\src\\windows",
		"stat": [
			33206,
			562949953429741,
			1319441880,
			1,
			0,
			0,
			7361,
			1606402282,
			1603981112,
			1606402282
		],
		"bytes": 7361,
		"size": "7.19 KB",
		"date_created_raw": 1606402282.416147,
		"date_modified_raw": 1603981112.0,
		"date_created": "2020-11-26 07:51:22",
		"date_modified": "2020-10-29 08:18:32",
		"type": "File",
		"typesort": 1,
		"ext": "py",
		"week_of_year": "2020.44",
		"week_of_year_": 44,
		"day_of_the_week": "Thursday",
		"month": "2020.10",
		"friendly_week": "",
		"friendly_month": "",
		"md5": "",
		"year": 2020,
		"accessed_raw": 1606402282.416147,
		"date_accessed": "2020-11-26 07:51:22",
		"ce": 1606402282.416147,
		"me": 1603981112.0,
		"ae": 1606402282.416147
	}
]
"""

def size_group(s):
	if type(s) == str:
		s = unFormatSize(s)
	if s == 0:
		return 0
	groups = [{"l": "1", "s": "500", "x": "kb"}, {"l": "2", "s": "1", "x": "mb"}, {"l": "3", "s": "5", "x": "mb"}, {"l": "4", "s": "10", "x": "mb"}, {"l": "5", "s": "20", "x": "mb"}, {"l": "6", "s": "50", "x": "mb"}, {"l": "7", "s": "200", "x": "mb"}, {"l": "8", "s": "500", "x": "mb"}, {"l": "9", "s": "1", "x": "gb"}, {"l": "10", "s": "5", "x": "gb"}, {"l": "11", "s": "10", "x": "gb"}, {"l": "12", "s": "20", "x": "gb"}, {"l": "13", "s": "50", "x": "gb"}, {"l": "14", "s": "200", "x": "gb"}, {"l": "15", "s": "500", "x": "gb"}, {"l": "16", "s": "1", "x": "tb"}, {"l": "17", "s": "5", "x": "tb"}, {"l": "18", "s": "10", "x": "tb"}, {"l": "19", "s": "20", "x": "tb"}, {"l": "20", "s": "50", "x": "tb"}, {"l": "21", "s": "200", "x": "tb"}, {"l": "22", "s": "500", "x": "tb"}, {"l": "23", "s": "1", "x": "pb"}, {"l": "24", "s": "5", "x": "pb"}, {"l": "25", "s": "10", "x": "pb"}, {"l": "26", "s": "20", "x": "pb"}, {"l": "27", "s": "50", "x": "pb"}, {"l": "28", "s": "200", "x": "pb"}, {"l": "29", "s": "500", "x": "pb"}, {"l": "30", "s": "1", "x": "eb"}, {"l": "31", "s": "5", "x": "eb"}, {"l": "32", "s": "10", "x": "eb"}, {"l": "33", "s": "20", "x": "eb"}, {"l": "34", "s": "50", "x": "eb"}, {"l": "35", "s": "200", "x": "eb"}, {"l": "36", "s": "500", "x": "eb"}, {"l": "37", "s": "1", "x": "zb"}, {"l": "38", "s": "5", "x": "zb"}, {"l": "39", "s": "10", "x": "zb"}, {"l": "40", "s": "20", "x": "zb"}, {"l": "41", "s": "50", "x": "zb"}, {"l": "42", "s": "200", "x": "zb"}, {"l": "43", "s": "500", "x": "zb"}, {"l": "44", "s": "1", "x": "yb"}, {"l": "45", "s": "5", "x": "yb"}, {"l": "46", "s": "10", "x": "yb"}, {"l": "47", "s": "20", "x": "yb"}, {"l": "48", "s": "50", "x": "yb"}, {"l": "49", "s": "200", "x": "yb"}, {"l": "50", "s": "500", "x": "yb"}]
	groups.reverse()
	last = 0
	for rec in groups:
		un = rec['s']+rec['x']
		fo = unFormatSize(un)
		print
		if s >= fo:
			return int(rec['l'])
	return 1

def size_group2(s):
	if s < 10:
		return '0'+str(s)
	else:
		return str(s)
touch_meta = None
timeAudit = []
timeAuditCollect = False
commitPer = 46285
maxFileNameLength = 35
dateCalcByModified = True
if not os.path.isdir( _v.exif_temp ):
	os.mkdir( _v.exif_temp )

def fileAge( file ):
	md = fileInfo( file )['date_modified_raw']
	return time.time() - md

def acquireExif( info ):
	try:
		do = 'exiftool "THEFILE" -json > MOD_BYTES.json'
		MOD_BYTES = 'MOD_BYTES.json'
		doThis = do.replace( 'THEFILE', info['path'] )
		doThis = doThis.replace( 'MOD_BYTES', _v.exif_temp +_v.slash+ str(info['date_modified_raw'])+'_'+str(info['bytes']) )
		MOD_BYTES = MOD_BYTES.replace( 'MOD_BYTES', _v.exif_temp +_v.slash+ str(info['date_modified_raw'])+'_'+str(info['bytes']) )
		os.system('"' + doThis + '"')
		return getTable2( MOD_BYTES )
	except Exception as e:
		return [{}]

def getTable2( theFile ):
	if os.path.isfile( theFile ):
		with open( theFile,'r', encoding='latin-1' ) as json_file:
			json_data = json.load( json_file )
		return json_data
	else:
		return [{}]

def epoch( path ):
	return os.path.getmtime( path )

def getSize(path):
	stat = os.stat(path)
	size = stat.st_size
	return size
conn = None
cursor = None
total_records = 0

def sqlCreateTable( db, deleteDBFirst=False, close=False, asset=None, length=None, delete=None ):
	global total_records
	global conn
	global cursor
	import sqlite3
	if not length is None:
		if type(length) == int:
			total_records = length
	if not asset is None:
		if type(asset) == int:
			total_records = asset
		elif type(asset) == list:
			total_records = len(asset)
	if not delete is None:
		deleteDBFirst = delete
	# if deleteDBFirst:
	if os.path.isfile(db) and not deleteDBFirst:
		if 'y' in input(' delete db? ').lower(): os.unlink(db); print('deleted');
	# if os.path.isfile(db) and deleteDBFirst:
	#     try: os.unlink(db)
	#     except: pass
	conn = sqlite3.connect(db)
	cursor = conn.cursor()
	sql =  'CREATE TABLE files (path text, name_ text, name text, folder text, stat text, attrib text, bytes int, size text, date_created_raw double, date_modified_raw double, date_created text, date_modified text, type text, typesort text, ext text, week_of_year text, week_of_year_ text, day_of_the_week text, month text, friendly_week text, friendly_month text, accessed_raw double, date_accessed text                        , ce double, me double, ae double, meta text, header text, err int        )'
	cursor.execute( sql )
	if close:
		conn.close()
	else:
		return conn, cursor
commit_count = 0
processed_count = 0

def info( path, sql=False, md5=False, exif=0,   attrib=None, mime=None, db_connection=None, db_cursor=None, count=None, insert=None, last=False, sdate=None, meta=True, err=False,       subject=None, k=None, f=None, s=None, sub=None, field=None, mini=False, sha256=False, lines=False ):
	if not field is None: subject=field;
	if not sub is None: subject=sub;
	if not s is None: subject=s;
	if not k is None: subject=k;
	if not f is None: subject=f;
	sub=subject
	mrec=fileInfo( path=path, sql=sql, md5=md5, exif=exif,   attrib=attrib, mime=mime, db_connection=db_connection, db_cursor=db_cursor, count=count, insert=insert, last=last, sdate=sdate, meta=meta, err=err, subject=subject, sha256=sha256, _lines=lines )
	if mini and mrec:
		del mrec['stat']
		del mrec['date_created_raw']
		del mrec['date_modified_raw']
		del mrec['type']
		del mrec['typesort']
		del mrec['md5']
		del mrec['week_of_year']
		del mrec['week_of_year_']
		del mrec['month']
		del mrec['friendly_week']
		del mrec['friendly_month']
		del mrec['group']
		del mrec['header']
		del mrec['error']
		del mrec['accessed_raw']
		del mrec['meta']
		del mrec['ago']
		del mrec['day_of_the_week']
		mrec['created']=mrec['date_created']
		mrec['modified']=mrec['date_modified']
		mrec['accessed']=mrec['date_accessed']
		del mrec['date_created']
		del mrec['date_modified']
		del mrec['date_accessed']
	return mrec

def fileInfo( path, sql=False, md5=False, exif=0,   attrib=None, mime=None, db_connection=None, db_cursor=None, count=None, insert=None, last=False, sdate=None, meta=True, err=False, subject=None, sha256=False, _lines=False ):
	global processed_count
	global total_records
	processed_count += 1
	if processed_count == total_records:
		last = True
	if not insert is None:
		if insert:
			global conn
			global cursor
			db_connection = conn
			db_cursor = cursor
			count = processed_count
	if err:
		return fileInfoAction( path, sql, md5, exif, attrib, mime, db_connection, db_cursor, count, insert, last, sdate, meta, subject, sha256, _lines )
	else:
		try:
			return fileInfoAction( path, sql, md5, exif, attrib, mime, db_connection, db_cursor, count, insert, last, sdate, meta, subject, sha256, _lines )
		except Exception as e:
			return False

def _woy_(epoch):
	weekAndYear=round(getWOYFromEpoch(epoch) * 0.01,2) + getYearFromEpoch(epoch); weekAndYear = str(weekAndYear);
	if len(weekAndYear) == 6: weekAndYear += '0';
	return weekAndYear

def _header_(path):
		global header
		theHeader = ''
		if header:
			theHeader = " ".join(['{:02X}'.format(byte) for byte in     open( path, 'rb' ).read(32)    ])
			if type(header) == int:
				theHeader = theHeader[0:header*3]
		return theHeader

def individual(path,subject,forceDic=False):
	path=__.path(path)
	dic={}
	if ' path ' in ' '+subject+' ': dic['path'] =  __.path(path);
	if ' file ' in ' '+subject+' ': dic['name'] =  Path(path).name;
	if ' name ' in ' '+subject+' ': dic['name'] =  Path(path).name;
	if ' folder ' in ' '+subject+' ': dic['folder'] =  os.path.dirname(path);
	if ' stat ' in ' '+subject+' ': dic['stat'] =  os.stat(path);
	if ' bytes ' in ' '+subject+' ': dic['bytes'] =  os.stat(path).st_size;
	if ' size ' in ' '+subject+' ': dic['size'] = formatSize(os.stat(path).st_size) ;
	if ' date_created_raw ' in ' '+subject+' ': dic['date_created_raw'] =  os.path.getctime(path);
	if ' date_modified_raw ' in ' '+subject+' ': dic['date_modified_raw'] =  os.path.getmtime(path);
	if ' date_created ' in ' '+subject+' ': dic['date_created'] =  formatDate(os.path.getctime(path));
	if ' created ' in ' '+subject+' ': dic['date_created'] =  formatDate(os.path.getctime(path));
	if ' date_modified ' in ' '+subject+' ': dic['date_modified'] =  formatDate(os.path.getmtime(path));
	if ' modified ' in ' '+subject+' ': dic['date_modified'] =  formatDate(os.path.getmtime(path));
	if ' fd ' in ' '+subject+' ': dic['date_modified'] =  formatDate(os.path.getmtime(path));
	if ' type ' in ' '+subject+' ': dic['type'] = ('File' if os.path.isfile(path) else 'Folder');
	if ' typesort ' in ' '+subject+' ': dic['typesort'] =  (1 if os.path.isfile(path) else 0);
	if ' ext ' in ' '+subject+' ': dic['ext'] =  getExtension(Path(path).name);
	if ' week_of_year ' in ' '+subject+' ': dic['week_of_year'] =  _woy_(os.path.getmtime(path));
	if ' day_of_the_week ' in ' '+subject+' ': dic['day_of_the_week'] =  getDOWromEpochText(os.path.getmtime(path));
	if ' dow ' in ' '+subject+' ': dic['dow'] =  getDOWromEpochText(os.path.getmtime(path));
	if ' month ' in ' '+subject+' ': dic['month'] =  str(getYearFromEpoch(os.path.getmtime(path))) + '.' + str(formatDateMonth(os.path.getmtime(path)))
	if ' friendly_week ' in ' '+subject+' ': dic['friendly_week'] =  friendlyWeekNew(os.path.getmtime(path));
	if ' fw ' in ' '+subject+' ': dic['fw'] =  friendlyWeekNew(os.path.getmtime(path));
	if ' friendly_month ' in ' '+subject+' ': dic['friendly_month'] =  friendlyMonthNew(os.path.getmtime(path));
	if ' fm ' in ' '+subject+' ': dic['fm'] =  friendlyMonthNew(os.path.getmtime(path));
	if ' md5 ' in ' '+subject+' ': dic['md5'] =  _md5.md5File(path);
	if ' sha ' in ' '+subject+' ': dic['md5'] =  _md5.sha256File(path);
	if ' sha256 ' in ' '+subject+' ': dic['md5'] =  _md5.sha256File(path);
	if ' year ' in ' '+subject+' ': dic['year'] =  getYearFromEpoch(os.path.getmtime(path));
	if ' accessed_raw ' in ' '+subject+' ': dic['accessed_raw'] =  os.path.getatime(path);
	if ' date_accessed ' in ' '+subject+' ': dic['date_accessed'] =  formatDate(os.path.getatime(path));
	if ' accessed ' in ' '+subject+' ': dic['accessed'] =  formatDate(os.path.getatime(path));
	if ' ce ' in ' '+subject+' ': dic['ce'] =  os.path.getctime(path);
	if ' cef ' in ' '+subject+' ': dic['ce'] =  formatDate(os.path.getctime(path));
	if ' me ' in ' '+subject+' ': dic['me'] =  os.path.getmtime(path);
	if ' mef ' in ' '+subject+' ': dic['me'] =  formatDate(os.path.getmtime(path));
	if ' ae ' in ' '+subject+' ': dic['ae'] =  os.path.getatime(path);
	if ' aef ' in ' '+subject+' ': dic['ae'] =  formatDate(os.path.getatime(path));
	if ' woy ' in ' '+subject+' ': dic['me'] =  _woy_(os.path.getmtime(path));
	if ' me-woy ' in ' '+subject+' ': dic['me'] =  _woy_(os.path.getmtime(path));
	if ' mwoy ' in ' '+subject+' ': dic['me'] =  _woy_(os.path.getmtime(path));
	if ' ce-woy ' in ' '+subject+' ': dic['me'] =  _woy_(os.path.getctime(path));
	if ' cwoy ' in ' '+subject+' ': dic['me'] =  _woy_(os.path.getctime(path));
	if ' awoy ' in ' '+subject+' ': dic['me'] =  _woy_(os.path.getatime(path));
	if ' ae-woy ' in ' '+subject+' ': dic['me'] =  _woy_(os.path.getatime(path));
	if ' ae-woy ' in ' '+subject+' ': dic['me'] =  _woy_(os.path.getatime(path));
	if ' ago ' in ' '+subject+' ': dic['ago'] =  dateDiffText(os.path.getmtime(path));
	if ' me-ago ' in ' '+subject+' ': dic['ago'] =  dateDiffText(os.path.getmtime(path));
	if ' ce-ago ' in ' '+subject+' ': dic['ago'] =  dateDiffText(os.path.getctime(path));
	if ' header ' in ' '+subject+' ': dic['header'] =  _header_(path);
	if ' head ' in ' '+subject+' ': dic['head'] =  _header_(path);
	if ' group ' in ' '+subject+' ': dic['group'] =  size_group(os.stat(path).st_size);
	if ' sg ' in ' '+subject+' ': dic['group'] =  size_group(os.stat(path).st_size);
	if ' sha1 ' in ' '+subject+' ': dic['sha1'] =  _md5.string(path,'sha1');
	if ' sha256 ' in ' '+subject+' ': dic['sha256'] =  _md5.string(path,'sha256');
	if ' sha512 ' in ' '+subject+' ': dic['sha512'] =  _md5.string(path,'sha512');
	if not dic: return info(path);
	k=list(dic.keys())
	if not forceDic:
		if len(k) == 1: return dic[k[0]];
	return dic

def fileInfoAction( path, sql=False, md5=False, exif=0, getAttrib=None, getMime=None, db_connection=None, db_cursor=None, count=None, insert=None, last=False, sdate=None, meta=True, subject=None, sha256=False, _lines=False ):
	global touch_meta
	global dateCalcByModified
	global timeAudit
	global timeAuditCollect
	if not subject is None: return individual(path,subject);
	hasError = 0
	error = False
	epoch = []
	epoch.append({ 'label': 'start', 'epoch': time.time() })
	md5
	aPath = os.path.abspath(path)
	if os.path.isfile(aPath):
		ty = 'File'
		typesort = 1
	elif os.path.isdir(aPath):
		ty = 'Folder'
		typesort = 0
	else:
		error = True
	epoch.append({ 'label': 'pre', 'epoch': time.time() })
	if not error:
		if not getAttrib is None:
			attri = attrib(aPath)
			epoch.append({ 'label': 'attrib', 'epoch': time.time() })
			attribs = getAttribs(attri)
			epoch.append({ 'label': 'getAttribs', 'epoch': time.time() })
		name = Path(path).name
		epoch.append({ 'label': 'Path', 'epoch': time.time() })
		path2 = __.path(aPath)
		epoch.append({ 'label': 'realpath', 'epoch': time.time() })
		createdRaw = os.path.getctime(aPath)
		modifiedRaw = os.path.getmtime(aPath)
		if modifiedRaw == 0:
			modifiedRaw = time.time()
			hasError = 1
		if createdRaw == 0:
			createdRaw = time.time()
			hasError = 2
		epoch.append({ 'label': 'get_time', 'epoch': time.time() })
		stat = os.stat(aPath)
		size = stat.st_size
		sizeF = formatSize(size)
		epoch.append({ 'label': 'size', 'epoch': time.time() })
		ext = getExtension(name)
		folder = os.path.dirname(aPath)
		epoch.append({ 'label': 'dirname', 'epoch': time.time() })
		mwoy = getWOYFromEpoch(modifiedRaw)
		myear = getYearFromEpoch(modifiedRaw)
		cwoy = getWOYFromEpoch(createdRaw)
		cyear = getYearFromEpoch(createdRaw)
		accessed_raw = os.path.getatime(aPath)
		if not sdate is None:
			sdate_raw = createdRaw
			if 'o' in sdate:
				if modifiedRaw > sdate_raw:
					sdate_raw = modifiedRaw
				if accessed_raw > sdate_raw:
					sdate_raw = accessed_raw
			elif 'n' in sdate:
				if modifiedRaw < sdate_raw:
					sdate_raw = modifiedRaw
				if accessed_raw < sdate_raw:
					sdate_raw = accessed_raw
		if dateCalcByModified:
			woy = mwoy
			year = myear
			calcBy = modifiedRaw
			woyBY = '.m'
		else:
			woyBY = '.c'
			woy = cwoy
			year = cyear
			calcBy = createdRaw
		thisweek = getWOYFromEpoch(time.time())
		weekAndYear = round(woy * 0.01,2) + year
		dow = getDOWromEpochText(calcBy)
		friendlyWeek1 = friendlyWeekNew(calcBy)
		friendlyMonth1 = friendlyMonthNew(calcBy)
		month = str(year) + '.' + str(formatDateMonth(calcBy))
		epoch.append({ 'label': 'week_and_year', 'epoch': time.time() })
		md5Data = ''
		sha256Data = ''
		shouldMD5 = False
		if type( md5 ) == bool:
			if md5:
				shouldMD5 = True
		else:
			shouldMD5 = True
			if modifiedRaw > float(md5[0]):
				shouldMD5 = True
			else:
				shouldMD5 = False
				md5Data = md5[1]
		if sha256:
			try: sha256Data = _md5.sha256File( path2 )
			except Exception as e: pass
		if shouldMD5:
			try: md5Data = _md5.md5File( path2 )
			except Exception as e: pass
		epoch.append({ 'label': 'md5:'+str(shouldMD5), 'epoch': time.time() })
		if not getMime is None:
			try:
				if _mime.isText(path2):
					mime = 'Text'
				else:
					mime = 'Binary'
			except Exception as e:
				mime = ''
			epoch.append({ 'label': 'mime', 'epoch': time.time() })
		weekAndYear = str(weekAndYear)
		if len(weekAndYear) == 6:
			weekAndYear += '0' 
		global header
		theHeader = ''
		if header:
			theHeader = " ".join(['{:02X}'.format(byte) for byte in     open( aPath, 'rb' ).read(32)    ])
			if type(header) == int:
				theHeader = theHeader[0:header*3]
		# print(_lines_(path2))
		__lines=0
		try:
			if _lines:
				__lines=_lines_(path2)
			else:
				__lines=0
		except Exception as e:
			_.pr(e,c='red')
			pass

		obj = {
				'path': path2,
				'name_': fileNameLength(name,ext),
				'name': name,
				'parent': path2.split(os.sep)[-2],
				'folder': folder,
				'relative': '',
				'stat': stat,
				'bytes': size,
				'size': sizeF,
				'date_created_raw': createdRaw,
				'date_modified_raw': modifiedRaw,
				'date_accessed_raw': accessed_raw,
				'date_created': formatDate(createdRaw),
				'date_modified': formatDate(modifiedRaw),
				'date_accessed': formatDate(accessed_raw),
				'type': ty,
				'typesort': typesort,
				'ext': ext,
				'week_of_year': weekAndYear,
				'week_of_year_': woy,
				'day_of_the_week': dow,
				'month': month,
				'friendly_week': friendlyWeek1,
				'friendly_month': friendlyMonth1,
				'md5': md5Data,
				'sha256': sha256Data,
				'year': year,
				'ce': createdRaw,
				'me': modifiedRaw,
				'ae': accessed_raw,
				'meta': {},
				'ago': dateDiffText(calcBy),
				'header': _header_(path2),
				'error': hasError,
				'group': size_group(size),
				'lines': __lines,
		}


		_cwd=os.getcwd()
		if _cwd+os.sep in path2:
			obj['relative'] = path2[ len(_cwd)+1: ]

		if not type(obj['bytes']) == int:
			obj['bytes'] = 0
		if not sdate is None:
			obj['sdate'] = formatDate(sdate_raw)
			obj['sdate_raw'] = sdate_raw
			obj['de'] = sdate_raw
			obj['cps'] = ps_timestamp(createdRaw)
			obj['mps'] = ps_timestamp(modifiedRaw)
			obj['aps'] = ps_timestamp(accessed_raw)
			obj['dps'] = ps_timestamp(sdate_raw)
		if touch_meta is None:
			touch_meta = getTable('touch.meta')
		if path2 in touch_meta:
			touch_meta[path2]
			obj['meta'] = touch_meta[path2]
			if meta:
				if 'epoch' in obj['meta']:
					obj['meta']['epoch-bk'] = {}
					if 'ce' in obj['meta']['epoch']:
						obj['meta']['epoch-bk']['ce'] = obj['ce']
						obj['meta']['epoch-bk']['date_created'] = obj['date_created']
						obj['ce'] = obj['meta']['epoch']['ce']
						obj['date_created_raw'] = obj['ce']
						obj['date_created'] = formatDate(obj['ce'])
					if 'me' in obj['meta']['epoch']:
						obj['meta']['epoch-bk']['me'] = obj['me']
						obj['meta']['epoch-bk']['date_modified'] = obj['date_modified']
						obj['me'] = obj['meta']['epoch']['me']
						obj['date_modified_raw'] = obj['me']
						obj['date_modified'] = formatDate(obj['me'])
					if 'ae' in obj['meta']['epoch']:
						obj['meta']['epoch-bk']['ae'] = obj['ae']
						obj['meta']['epoch-bk']['date_accessed'] = obj['date_accessed']
						obj['ae'] = touch_meta[path2]['epoch']['ae']
						obj['accessed_raw'] = obj['ae']
						obj['date_accessed'] = formatDate(obj['ae'])
		pass
		if __.dir.print:
			global print_fields
			oj={}
			for k in obj:
				keep=True
				if k in obj and not obj[k]: keep=False
				if k in obj and not k in print_fields: keep=False
				if keep: oj[k]=obj[k]
			obj=oj
		pass
		if not getAttrib is None:
			obj['attrib'] = attribs
		if not getMime is None:
			obj['mime'] = mime
		epoch.append({ 'label': 'obj', 'epoch': time.time() })
	if exif == 1:
		obj['exif'] = acquireExif( obj )
	if exif == 2:
		exifData = acquireExif( obj )
		for key in exifData[0].keys():
			try:
				try:
					if not str( obj[key] ) > 0:
						obj[key] = exifData[0][key]
				except Exception as e:
					obj[key] = exifData[0][key]
			except Exception as e:
				pass
	if sql:
		path = obj['path']
		name_ = obj['name_']
		name = obj['name']
		folder = obj['folder']
		bytesx = obj['bytes']
		sizeF = obj['size']
		createdRaw = obj['date_created_raw']
		modifiedRaw = obj['date_modified_raw']
		date_created = obj['date_created']
		date_modified = obj['date_modified']
		week_of_year = obj['week_of_year']
		week_of_year_ = obj['week_of_year_']
		day_of_the_week = obj['day_of_the_week']
		month = obj['month']
		friendly_week = obj['friendly_week']
		friendly_month = obj['friendly_month']
		sqlInsert = 'INSERT INTO files VALUES ("{}","{}","{}","{}","", "",{},"{}",{},{},"{}","{}","File", "1", "{}","{}","{}","{}","{}","{}","{}"  ,{},"{}"         , {}, {}, {}, "{}", "{}", {}        )'.format(path, name_, name, folder, bytesx, sizeF, createdRaw, modifiedRaw, date_created, date_modified, ext, week_of_year, week_of_year_, day_of_the_week, month, friendly_week, friendly_month, accessed_raw, formatDate(accessed_raw)                          , obj['ce'], obj['me'], obj['ae'], obj['meta'], obj['header'], obj['error']       )
		obj = sqlInsert
	if error:
		obj = False
	epoch.append({ 'label': 'sql', 'epoch': time.time() })
	if not db_cursor is None:
		global commitPer
		global commit_count
		if not type(obj) == bool:
			db_cursor.execute(obj)
			epoch.append({ 'label': 'sql_execute', 'epoch': time.time() })
			if not count is None and count % commitPer == 0:
				db_connection.commit()
				commit_count+=1
			if last:
				db_connection.commit()
				commit_count+=1
			epoch.append({ 'label': 'sql_commit', 'epoch': time.time() })
		else:
			_.pr( 'error:', path )
	if timeAuditCollect:
		timeAudit.append(epoch)
	return obj

def commit():
	global conn
	global cursor
	global commit_count
	db_connection = conn
	db_cursor = cursor
	db_connection.commit()
	commit_count+=1

def ps_timestamp( stamp ):
	d = formatDate(stamp)
	parts = d.split(' ')
	day = parts[0]
	tip = parts[1].split(':')
	if int(tip[0]) > 12:
		tip[0] = int(tip[0]) - 12
		ap = 'PM'
	else:
		ap = 'AM'
	if not len(tip)> 2:
		f = day + ' ' + str(tip[0])+':'+str(tip[1])+ ' '+ ap
	else:
		f = day + ' ' + str(tip[0])+':'+str(tip[1])+':'+str(tip[2])+ ' '+ ap
	return f

def formatDate(theDate):
	result = datetime.datetime.fromtimestamp( int(theDate) ).strftime('%Y-%m-%d %H:%M:%S')
	result = str(result)
	return result

def formatDateYear(theDate):
	result = datetime.datetime.fromtimestamp( int(theDate) ).strftime('%Y')
	return result

def formatDateDay(theDate):
	result = datetime.datetime.fromtimestamp( int(theDate) ).strftime('%d')
	return result

def formatDateMonth(theDate):
	result = datetime.datetime.fromtimestamp( int(theDate) ).strftime('%m')
	result = str(result)
	return result

def friendlyMonthNew(theDate):
	friendlyMonth1 = ''
	currentDate = time.time()
	currentYear = formatDateYear(currentDate)
	try:
		theDate = int(theDate)
		testYear = formatDateYear(theDate)
		friendlyMonth0 = months_between(theDate, currentDate)
		littleMonth = monthByNumber(formatDateMonth(theDate))
		testMonth = formatDateMonth(theDate)
		testMonthThis = formatDateMonth(currentDate)
		if currentYear == testYear and testMonth == testMonthThis:
			friendlyMonth1 = '( This month: ' + littleMonth + ' )'
		elif currentYear == testYear and testMonth == lastMonth(testMonthThis):
			friendlyMonth1 = '( Last month: ' + littleMonth + ' )'
		else:
			if int(friendlyMonth0) > 12:
				years = math.floor(int(friendlyMonth0)/12)
				months = int(friendlyMonth0) - (years * 12)
				friendlyMonth1 = str(years) + ' years ' + str(months) + ' months ago: ' + littleMonth 
			else:
				friendlyMonth1 = str(friendlyMonth0) + ' months ago: ' + littleMonth
	except Exception as e:
		pass
	return friendlyMonth1

def friendlyWeekNew(theDate):
	friendlyWeek1 = ''
	currentDate = time.time()
	currentYear = formatDateYear(currentDate)
	currentWeek = datetime.datetime.fromtimestamp(currentDate).isocalendar()[1]
	try:
		theDate = int(theDate)
		testYear = formatDateYear(theDate)
		woy = datetime.datetime.fromtimestamp(theDate).isocalendar()[1]
		friendlyWeek0 = weeks_between(theDate, currentDate)
		if currentYear == testYear and currentWeek == woy:
			friendlyWeek1 = '( This week )'
		elif (currentYear == testYear and currentWeek == lastWeek(woy)) or str(friendlyWeek0) == '1':
			friendlyWeek1 = '( Last week )'
		else:
			friendlyWeek1 = str(friendlyWeek0) + ' weeks ago'
	except Exception as e:
		pass
	return friendlyWeek1

def getWeekAndYear(theDate):
	y = getYearFromEpoch(theDate)
	w = getWOYFromEpoch(theDate)
	if w < 10:
		w = '0'+str(w)
	else:
		w = str(w)
	return str(y) +'.'+ w

def getMonthFromEpoch(theDate):
	return str( getYearFromEpoch(theDate) ) + '.' + str(formatDateMonth(theDate))

def getYearFromEpoch(theDate):
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[0]

def getWOYFromEpoch(theDate):
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[1]

def getDOWromEpoch(theDate):
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[2]

def getDOWromEpochText(theDate):
	return dowConvert(getDOWromEpoch(theDate))

def dowConvert(dow):
	result = ''
	if dow == 1:
		result = 'Monday'
	if dow == 2:
		result = 'Tuesday'
	if dow == 3:
		result = 'Wednesday'
	if dow == 4:
		result = 'Thursday'
	if dow == 5:
		result = 'Friday'
	if dow == 6:
		result = 'Saturday'
	if dow == 7:
		result = 'Sunday'
	return result

def formatSize(size):
	result = ''
	if size == None:
		result = ''
	elif size < 1024:
		result = str(size) + ' B'
	elif size > 1024 and size < 1048576:
		num = round(size / 1024, 2)
		result = str(num) + ' KB'
	elif size > 1048576 and size < 1073741824:
		num = round(size / 1048576, 2)
		result = str(num) + ' MB'
	elif size > 1073741824 and size < 1099511627776    :
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	else:
		num = round(size / 1099511627776, 2)
		result = str(num) + ' TB'
	return result

def unFormatSize(size):
	size = str(size)
	size = size.upper()
	factor = ''
	if False:
		pass
	elif 'YB' in size:
		factor = 1208925819614629174706176
	elif 'ZB' in size:
		factor = 1180591620717411303424
	elif 'EB' in size:
		factor = 1152921504606847000
	elif 'PB' in size:
		factor = 1125899906842624
	elif 'TB' in size:
		factor = 1099511627776
	elif 'GB' in size:
		factor = 1073741824
	elif 'MB' in size:
		factor = 1048576
	elif 'KB' in size:
		factor = 1024
	else:
		factor = 1
	size = size.replace('X','')
	size = size.replace('Y','')
	size = size.replace('Z','')
	size = size.replace('E','')
	size = size.replace('P','')
	size = size.replace('T','')
	size = size.replace('B','')
	size = size.replace('M','')
	size = size.replace('K','')
	size = size.replace('G','')
	size = float(size)
	if str(size).endswith('.0'):
		size = int(size)
	result = round(size * factor,0)
	return result

def fileNameLength(string,ext,l=0):
	global maxFileNameLength
	if l == 0:
		theLength = maxFileNameLength
	else:
		theLength = l
	result = ''
	toLong = False
	try:
		i = 0
		for L in string:
			if i <= theLength:
				result += L
			else:
				toLong = True
			i += 1
		if toLong == True:
			result += '...'
			if len(ext) > 0:
				result += '  .' + ext
	except Exception as e:
		result = string
	return result

def attrib(path, a=None, s=None, h=None, r=None, i=None):
	attrs=[]
	if r==True:    attrs.append('+R')
	elif r==False: attrs.append('-R')
	if a==True:    attrs.append('+A')
	elif a==False: attrs.append('-A')
	if s==True:    attrs.append('+S')
	elif s==False: attrs.append('-S')
	if h==True:    attrs.append('+H')
	elif h==False: attrs.append('-H')
	if i==True:    attrs.append('+I')
	elif i==False: attrs.append('-I')
	if attrs: 
		cmd = attrs
		cmd.insert(0,'attrib')
		cmd.append(path)
		cmd.append('/L')
		return subprocess.call(cmd, shell=False)
	else: 
		output = subprocess.check_output(
			['attrib', path, '/L'],
			shell=False, universal_newlines=True
		)[:9]
		attrs = {'A':False, 'S':False, 'H':False, 'R':False, 'I':False}
		for char in output:
			if char in attrs:
				attrs[char] = True
		return attrs

def getAttribs(rows):
	result = ''
	if rows['A'] == True:
		result += 'A' 
	if rows['S'] == True:
		result += 'S' 
	if rows['H'] == True:
		result += 'H' 
	if rows['R'] == True:
		result += 'R' 
	if rows['I'] == True:
		result += 'I' 
	return result

def getExtension(string):
	if not '.' in string:
		return ''
	ext = string.split('.')
	ext.reverse()
	return ext[0]

def getTable( theFile, tableTemp=False,      isDic=None, isList=None,      tmp=None ):
	if not type( tableTemp ) == bool:
		if tableTemp == 'split':
			file0 = _v.myTables + _v.slash+'tablesets'+_v.slash + theFile
	else:
		if tableTemp == True:
			file0 = _v.stmp + _v.slash + theFile
		else:
			file0 = _v.myTables + _v.slash + theFile
	if not os.path.isfile(file0):
		file0 = theFile
	if os.path.isfile(file0):
		with open(file0,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()

def gen_days_ago(days=1):
	now = _.autoDate( _.friendlyDate( time.time() ).split(' ')[0] ) - (  86400*days  )
	tdy0 = _.friendlyDate( now ).split(' ')[0]
	return tdy0

def gen_days_2be(days=1):
	now = _.autoDate( _.friendlyDate( time.time() ).split(' ')[0] ) + (  86400*days  )
	tdy0 = _.friendlyDate( now ).split(' ')[0]
	return tdy0

def gen_days_ago(days=1):
	now = _.autoDate( _.friendlyDate( time.time() ).split(' ')[0] ) - (  86400*days  )
	tdy0 = _.friendlyDate( now ).split(' ')[0]
	return tdy0

def dateDiffText( theDate ):
	y=0
	m=0
	w=0
	epoch = time.time()
	days = int( str( (epoch - theDate)/86400 ).split('.')[0] )
	msDiff = epoch - theDate
	if abs(msDiff) <= 86402:
		return 'today'
	if theDate < epoch:
		end = '<'
	else:
		end = '>'
	if days == 0:
		return 'today'
	elif theDate < epoch:
		if days == 1:
			return 'yesterday'
		elif days < 7:
			return 'this week'
	elif theDate > epoch:
		if days == 1:
			return 'tommorow'
		elif days < 7:
			return 'next week'
	if days >= 365:
		tmp = float(days / 365)
		y = int(str(tmp).split('.')[0])
		days = days - ( y*365 )
	if days >= 30:
		tmp = float(days / 30)
		m = int(str(tmp).split('.')[0])
		days = days - ( m*30 )
	if days >= 7:
		tmp = float(days / 7)
		w = int(str(tmp).split('.')[0])
		days = days - ( w*7 )
	result = []
	if y:
		result.append( str(y)+'y' )
	if m:
		result.append( str(m)+'m' )
	if w:
		result.append( str(w)+'w' )
	result.append( end )
	return ' '.join( result )

def daysDiff( one, two ):
	_.pr(one, two)
	_.pr(type(one), type(two))
	if one == two:
		return 0
	elif one > two:
		one = datetime.datetime.fromtimestamp( int(one) )
		two = datetime.datetime.fromtimestamp( int(two) )
	else:
		two = datetime.datetime.fromtimestamp( int(one) )
		one = datetime.datetime.fromtimestamp( int(two) )
	delta = one - two
	return delta.days
header = 0
"""
changes
____
2023-06-27 11:31:44
accessed_raw to date_accessed_raw
____
"""
# __.dir.print