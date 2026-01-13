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
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log',True)
__.setting('receipt-file',True)
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
# columns used for
# 	- abbreviation in switches
#		- ex: -column n s
#			- instead of: -column name size
#		- ex: -sort n
#		- ex: -group n
# 	- sort is used for things like size sort by bytes
# 	- responsiveness to terminal width
# 		- order is important
# 		- most important on top
		
		# this is used for personal usage to programmatically generate columns
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



from jdcal import gcal2jd
from jdcal import jd2gcal


def to_jdn(year, month, day):
    return sum(gcal2jd(year, month, day))

def from_jdn(jdn):
    year, month, day, fraction = jd2gcal(jdn, 0)
    return {'year': year, 'month': month, 'day': day}


# AD Date
jdn = to_jdn(2023, 9, 29)
print("Julian Day Number:", jdn)
date = from_jdn(jdn)
print("Date:", date)

print()
# BC Date (Remember: There is no year 0 in this calendar, -1 corresponds to 1 BC)
jdn_bc = to_jdn(-1000, 1, 1)
print("BC Julian Day Number:", jdn_bc)
date_bc = from_jdn(jdn_bc)
print("BC Date:", date_bc)

print()
print()
print()

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def date_time_to_float(date_time_str, epoch_str="1970-01-01 00:00:00"):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    year, month, day, hour, minute, second = map(int, date_time_str.replace("-", " ").replace(":", " ").split())
    epoch_year, epoch_month, epoch_day, _, _, _ = map(int, epoch_str.replace("-", " ").replace(":", " ").split())
    
    days = day - epoch_day
    for y in range(epoch_year, year):
        days += 365 + is_leap_year(y)
    for m in range(1, month):
        days += days_in_month[m - 1] + (m == 2 and is_leap_year(year))
    for m in range(1, epoch_month):
        days -= days_in_month[m - 1] + (m == 2 and is_leap_year(epoch_year))
    
    time = ((hour * 3600) + (minute * 60) + second) / (24 * 3600)
    
    return days + time

def float_to_date_time(date_time_float, epoch_str="1970-01-01 00:00:00"):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    days = int(date_time_float)
    seconds = int((date_time_float - days) * 24 * 3600)
    
    epoch_year, epoch_month, epoch_day, _, _, _ = map(int, epoch_str.replace("-", " ").replace(":", " ").split())
    
    year = epoch_year
    month = epoch_month
    day = epoch_day + days
    while day > (days_in_month[month - 1] + (month == 2 and is_leap_year(year))):
        day -= days_in_month[month - 1] + (month == 2 and is_leap_year(year))
        month += 1
        if month > 12:
            month = 1
            year += 1
    
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    second = seconds % 60
    
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"


# Test with the date "2023-09-29 14:37:28" and a custom epoch "2000-01-01 00:00:00"
date_time_str = "1560-09-29 14:37:28"
epoch_str = "0001-01-01 00:00:00"

date_time_float = date_time_to_float(date_time_str, epoch_str)
print("Float Representation:", date_time_float)

converted_date_time_str = float_to_date_time(date_time_float, epoch_str)
print("Date-time String:", converted_date_time_str)

# url
# M2ITwl3r2+/F9DpD40R3lKQ6K5EW4gzd6yhJ9BtZk2QZTtMg5LqAFX5jltgtPd+NruWbjqnc4mjR0x3cgqQqDQ==

def action():
	pass

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

