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
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files' )
	_.switches.register( 'Epoch', '-epoch', isRequired=True )
	_.switches.register( 'Size', '-size', isRequired=True )
	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-fi,-file,-files' )
	### EXAMPLE: END

# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('require-list',[])
__.setting('receipt-log')
__.setting('receipt-file',False)
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'pinnacle-estimate.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'estimate how long it will take to render a video',
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
						_.hp('p pinnacle-estimate -size 82gb -epoch 1653515941.548252 -f piller-dance.mp4'),
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

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
### EXAMPLE: START


	#--> make hotkey ad-description soon:  <--<w#
	#-->    - outer most typed first
	#-->    - blank pipe
	#-->    __.setting('hotkey-clip.ad_description-start1',d=False)
	#--> _________________________________
	#--> describe selection area two
	#--> 3 write a note here wrap text
	#--> two dignissim
	#--> 1 inceptos
	#--> _________________________________
	#--> describe selection area two
	#-->              |           |
	#-->              |           | - write a note here
	#-->              |           |   wrap text
	#-->              |           |
	#-->              |           | - dignissim
	#-->              |
	#-->              | - inceptos

	# if _.switches.isActive('Test'): test(); return None;
	# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
	# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
	#--> a=(1 if True else 0) <--# 
	#--> m=[[row[i] for row in matrix] for i in range(4)]
	# requests=__.imp('requests.post')
	# data=str(requests.post(url,data={}).content,'iso-8859-1')


### EXAMPLE: END
########################################################################################
# START

def tim(epoch,now=time.time()):
	try:
		import datetime
		from dateutil.relativedelta import relativedelta
	except Exception as e:
		_.pr(e)
	a = _.isDate(now,f='fdate')
	b = _.isDate(epoch,f='fdate')

	start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
	ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')

	diff = relativedelta(start, ends)
	d=diff.days
	h=diff.hours
	m=diff.minutes
	return abs(d),abs(h),abs(m)
	# >>> print "The difference is %d year %d month %d days %d hours %d minutes" % (diff.years, diff.months, diff.days, diff.hours, diff.minutes)
	# The difference is 1 year 1 month 29 days 19 hours 52 minutes

def cal(start_time,i,e):
	# for i in range(1, 101):
		# Do some work
		current_time = time.time()
		elapsed_time = current_time - start_time
		time_left = e * elapsed_time / i - elapsed_time
		return time_left
		# print(time_left)
def calcProcessTime(starttime, cur_iter, max_iter):

	telapsed = time.time() - starttime
	testimated = (telapsed/cur_iter)*(max_iter)

	finishtime = starttime + testimated
	finishtime = dt.datetime.fromtimestamp(finishtime).strftime("%H:%M:%S")  # in time

	lefttime = testimated-telapsed  # in seconds

	return (int(telapsed), int(lefttime), finishtime)


# last_times = []
# def get_remaining_time(i, total, time):
#     last_times.append(time)
#     _.saveTable(last_times,'pinnacle-estimate.list')
#     len_last_t = len(last_times)
#     if len_last_t > 5:
#         last_times.pop(0)
#     mean_t = sum(last_times) // len_last_t 
#     remain_s_tot = mean_t * (total - i + 1) 
#     remain_m = remain_s_tot // 60
#     remain_s = remain_s_tot % 60
#     # return f"{remain_m}m{remain_s}s"
#     return remain_s_tot


def action():
	# global last_times
	# last_times=_.getTable('pinnacle-estimate.list')
	epoch=float(_.switches.value('Epoch'))
	size=_.unFormatSize(_.switches.values('Size'))
	ti=time.time()-epoch

	_.pr(  'start:',_.isDate(epoch,f='fdate'), c='Background.light_blue'  )

	d,h,m=tim(epoch)
	# _.pr('done in',str(h)+':'+str(m),c='green')
	if d > 1:
		_.pr('ran:',d,'days',h,'hrs',m,'min',c='Background.light_blue')
	else:
		_.pr('ran:',h,'hrs',m,'min',c='Background.light_blue')
	# _.pr('time:',round(ti/60,2),'min')




	for path in _.switches.values('Files'):
		# _.pr(path)
		info=_dir.info(path)


		x=cal(epoch,info['bytes'],size)
		# x=get_remaining_time(info['bytes'], size, ti)
		# y=calcProcessTime(epoch,info['bytes'],size)
		# x=y[1]
		# _.pr('y:',y)
		_.pr(round(x/(60*60),2),c='red')
		# _.pr(round(y[1]/(60*60),2),c='red')
		# print(x)
		# _.pv(info)
		diff=size-info['bytes']
		#--> ti     x
		#--> diff   size
		# x=((ti/size)*diff)
		# print(x)
		# _.pr('done:',x,x/60,(x/60)/60)
		_.pr('size:',info['size'],c='Background.purple')
		_.pr('left:',_.formatSize(diff),c='Background.purple')
		fro=epoch
		fro=time.time()
		d,h,m=tim(fro+x)
		_.pr('end:',  _.isDate(fro+x,f='fdate'), c='Background.blue'  )
		# _.pr('done in',str(h)+':'+str(m),c='green')
		if d > 1:
			_.pr('left:',d,'days',h,'hrs',m,'min',c='Background.blue')
		else:
			_.pr('left:',h,'hrs',m,'min',c='Background.blue')
		d,h,m=tim(epoch,fro+x)
		if d > 1:
			_.pr('total:',d,'days',h,'hrs',m,'min',c='Background.red')
		else:
			_.pr('total:',h,'hrs',m,'min',c='Background.red')
	# _.pr(epoch)
	# _.pr(size)


import _rightThumb._dir as _dir
import datetime as dt

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()