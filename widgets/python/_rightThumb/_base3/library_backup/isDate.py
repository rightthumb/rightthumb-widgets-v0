
def isDate( theDate=None, record={}, tz=None, q=True, f=None,w=None,what=None ):
	if type(record) == str: e('expected: f='+record)
	# record={}
	if (type(theDate) == int or type(theDate) == float) and theDate < 1:
		return 0
	# if (type(theDate) == int or type(theDate) == float): return theDate
	if theDate is None: theDate=time.time();
	if not w is None: f=w;
	if not what is None: f=what;

	# theDate = autoDate(theDate)

	# print_(theDate)
	# sys.exit()

	global _dir
	if _dir is None:
		import _rightThumb._dir as _dir

	s = time.time()
	# slow from loading pandas
	if not tz is None and not len(tz):
		tz = None



	local_tz = str(time.strftime("%z")).replace(':','')


	hasTZ = False
	if type(theDate) == str and len(theDate) > 11:
		if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
			hasTZ = theDate[-6:].replace(':','')

	if type(theDate) == str and len(theDate) > 11 and type(hasTZ) == bool:
		if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
			hasTZ = theDate[-5:].replace(':','')
	epoch = autoDate(theDate)



	_dow_ = {
				'Sunday': 'sun',
				'Monday': 'mon',
				'Tuesday': 'tue',
				'Wednesday': 'wed',
				'Thursday': 'thu',
				'Friday': 'fri',
				'Saturday': 'sat',
	}


	def fitem(f):
		if f=='ago': return _dir.dateDiffText(epoch);
		if f=='ago-dic':
			ad=_2dates(epoch,dic=1); del ad['txt'];
			return ad;
		if f=='ago-txt': return _2dates(epoch)
		if f=='friendly': return friendlyDate( epoch );
		if f=='friendly': return friendlyDate( epoch );
		if f=='friendly3': return friendlyDate3( epoch );
		if f=='iso': return friendlyDate( epoch ).replace( ' ', 'T' ) + local_tz;
		if f=='woy': return _dir.getWeekAndYear( epoch );
		if f=='month': return _dir.getMonthFromEpoch( epoch );
		if f=='epoch': return epoch;
		if f=='ordinal': return datetime.datetime.fromtimestamp( epoch ).toordinal();
		if f=='text-date': return datetime.datetime.fromtimestamp( epoch ).strftime('%b, %d %Y');
		if f=='text-time': return datetime.datetime.fromtimestamp( epoch ).strftime('%I:%M %p');
		if f=='text-datetime': return datetime.datetime.fromtimestamp( epoch ).strftime('%b, %d %Y @ %I:%M %p');
		if f=='sdate': return friendlyDate2( epoch );
		if f=='strip': return onlyNumbers_strip(friendlyDate( epoch ).split(' ')[0]);
		if f=='strip': return onlyNumbers_strip(friendlyDate( epoch ).split(' ')[0]);
		if f=='stript': return onlyNumbers_strip(friendlyDate( epoch ));
		if f=='stripa': return onlyNumbers_strip(friendlyDate( epoch ))[:-2];
		if f=='date': return friendlyDate( epoch ).split(' ')[0];
		if f=='time': return friendlyDate2( epoch ).split(' ')[1];
		if f=='fdate': return friendlyDate( epoch );
		if f=='fdatea': return friendlyDate( epoch )[:-3];
		if f=='cmd': return friendlyDate( epoch )[:-3].replace(' ',' @ ').replace('-','.').replace(':','.');
		if f=='month': return _dir.getMonthFromEpoch( epoch );
		if f=='year': return friendlyDate( epoch ).split('-')[0]
		if f=='year2': return _dir.getYearFromEpoch( epoch ); # prioritizes week over actual year (if jan 01 and week 52 of last year)
		if f=='woy': return _dir.getWeekAndYear( epoch );
		if f=='woy2': return _dir.getWeekAndYear( epoch ).replace(str(_dir.getYearFromEpoch( epoch ))+'.','');
		if f=='ago': return _dir.dateDiffText( epoch );
		if f=='days': return daysDiff(  epoch, time.time()  );
		if f=='dow': return _dir.getDOWromEpochText( epoch );
		if f=='dow2': return _dow_[_dir.getDOWromEpochText( epoch )];
		if f=='tz': return local_tz;
		if f=='fo': return day(epoch);
		if f in 'crypt-date crypt-time crypt-epoch appID app crypt-pass'.split(' '):
			try:
				import _rightThumb._nID as _nID
				try:
					# _keychain = regImp( __.appReg, 'keychain' )
					# nID_password = _keychain.imp.key('nID')
					# _nID.mini.password( nID_password )
					_nID.mini.password( appID_nID_password() )
					isPass = 'secure'
				except Exception as e:
					_nID.mini.password( '1970' )
					isPass = 'unsecure'
				eee = ''
				try:
					ee = str(record['epoch'])
					for c in ee:
						if '.' == c:
							break
						eee+=c
				except Exception as e:
					eee=theDate
					# print_(f,1,'err:', e)
				pass

				if f=='crypt-date': return _nID.mini.gen( record['strip'] );
				if f=='crypt-time': return _nID.mini.gen( record['stript'] );
				try:
					if f=='crypt-epoch': return _nID.mini.gen( int(eee) );
					if f=='appID' or f=='app': return _nID.mini.gen( int(eee) );
				except Exception as ee:
					print_(f,2,'err:', ee)
					sys.exit()
				if f=='crypt-pass': return isPass;
			except Exception as ee:
				print_(f,3,'err:',ee)
				pass
		if f=='stardate':
			try:
				import _rightThumb._stardate as _sd
				return _sd.gen(  epoch  )
			except Exception as e:
				return None
		if f=='quarter':
			dt = friendlyDate( epoch ).split(' ')[0].split('-')
			try:
				return str(record['year']) +'.'+ str(pandas.Timestamp(datetime.date( int(dt[0]) , int(dt[1]), int(dt[2]))).quarter)
			except Exception as e:
				return None
		if f=='true': return True;
		if f=='dow':
			dow=_dir.getDOWromEpochText( epoch ).lower()
			dci = {
					'monday': 'mon',
					'tuesday': 'tue',
					'wednesday': 'wed',
					'thursday': 'thu',
					'friday': 'fri',
					'saturday': 'sat',
					'sunday': 'sun',
			}
			if dow in dci:
				return dci[dow]
			return dow
		return None



	#########################################################
	pass
	if f:
		if type(f)==list:
			f=' '.join(f)
		f=f.replace(',',' ')
		if not ' ' in f:
			return fitem(f)
		else:
			j={}
			for q in f.split(' '):
				j[q] = fitem(q)
			return j








	#########################################################

	# pv(_v.config_hash)
	if 'noarrow' in _v.config_hash:
		local_tz = ''
	else:
		global _tz
		if _tz is None:
			import _rightThumb._tz as _tz

		if not type(hasTZ) == bool:
			if not hasTZ == local_tz:
				epoch = _tz.convert( epoch, hasTZ, local_tz )
		if not tz is None and not local_tz == tz:
			epoch = _tz.convert( epoch, local_tz, tz )
			local_tz = tz

			if '/' in tz:
				global arrow
				if arrow is None:
					import arrow
				utc = arrow.utcnow()
				theDate = str(utc.to(tz))
				hasTZ = False
				if type(theDate) == str and len(theDate) > 11:
					if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
						hasTZ = theDate[-6:].replace(':','')

				if type(theDate) == str and len(theDate) > 11 and type(hasTZ) == bool:
					if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
						hasTZ = theDate[-5:].replace(':','')
				local_tz = hasTZ



	if not epoch:
		return record

	global pandas
	if pandas is None:
		if q:
			try:
				#  pandas  takes .5 seconds to load
				import pandas
			except Exception as e:
				pass

	ss = time.time()



	if type(epoch) == str:
		epoch = autoDate(epoch.replace('z',''))

	todo='ago ago-dic ago-txt epoch ordinal text-date text-time text-datetime sdate strip stript stripa date time fdate fdatea cmd month year woy woy2 dow dow2 days tz iso fo friendly friendly3'

	for k in todo.split(' '):
		record[k]=isDate(epoch,f=k)

	# record['ago'] = _dir.dateDiffText(epoch)
	# record['epoch'] = epoch
	# # print_( epoch )
	# record['ordinal'] = datetime.datetime.fromtimestamp( epoch ).toordinal()
	# # sys.exit()
	# record['text-date'] = datetime.datetime.fromtimestamp( epoch ).strftime('%b, %d %Y')
	# record['text-time'] = datetime.datetime.fromtimestamp( epoch ).strftime('%I:%M %p')
	# record['text-datetime'] = datetime.datetime.fromtimestamp( epoch ).strftime('%b, %d %Y @ %I:%M %p')
	# record['sdate'] = friendlyDate2( epoch )
	# record['strip'] = onlyNumbers_strip(friendlyDate( epoch ).split(' ')[0])
	# record['stript'] = onlyNumbers_strip(friendlyDate( epoch ))
	# record['date'] = friendlyDate( epoch ).split(' ')[0]
	# record['time'] = friendlyDate2( epoch ).split(' ')[1]
	# record['fdate'] = friendlyDate( epoch )
	# record['month'] = _dir.getMonthFromEpoch( epoch )
	# record['year'] = _dir.getYearFromEpoch( epoch )
	# record['woy'] = _dir.getWeekAndYear( epoch )
	# record['woy2'] = _dir.getWeekAndYear( epoch ).replace(str(_dir.getYearFromEpoch( epoch ))+'.','')
	# record['dow'] = _dir.getDOWromEpochText( epoch )
	# # record['ago'] = _dir.dateDiffText( epoch )
	# record['days'] = daysDiff(  epoch, time.time()  )
	# record['tz'] = local_tz
	# # record['iso'] = datetime.datetime.fromtimestamp( epoch ).isoformat()
	# # record['iso'] = datetime.datetime.fromtimestamp( epoch ).replace(microsecond=0).astimezone().isoformat()
	# record['iso'] = record['fdate'].replace( ' ', 'T' ) + record['tz']
	# --------------------------------------------------
	# __.isPass=None
	# def _en_(subject):
	#         try:
	#             import _rightThumb._nID as _nID
	#             if __.isPass is None:
	#                 try:
	#                     # _keychain = regImp( __.appReg, 'keychain' )
	#                     # nID_password = _keychain.imp.key('nID')
	#                     # _nID.mini.password( nID_password )
	#                     _nID.mini.password( appID_nID_password() )
	#                     __.isPass = 'secure'
	#                 except Exception as e:
	#                     _nID.mini.password( '1970' )
	#                     __.isPass = 'unsecure'
	#             eee = ''
	#             ee = str(record['epoch'])
	#             for c in ee:
	#                 if '.' == c:
	#                     break
	#                 eee+=c
	#             # record['crypt-password'] = nID_password
	#             return _nID.mini.gen( subject )
	#         except Exception as e:
	#             return None
	# # iso 24
	# # pv(_v.config_hash)
	# global isWin
	# if isWin:
	#     if 'nocrypt' in _v.config_hash:
	#         pass
	#     else:
	#         sub='strip';val=_en_(record[sub]);
	#         if val: record[sub] = val
	#         sub='crypt-date';val=_en_(record[sub]);
	#         if val: record[sub] = val
	#         sub='crypt-time';val=_en_(record[sub]);
	#         if val: record[sub] = val
	#         sub='crypt-pass';val=_en_(record[sub]);
	#         if val: record[sub] = val
	#         sub='appID';val=_en_(record[sub]);
	#         if val: record[sub] = val

	#         sub='crypt-epoch';val=_en_(int(eee));
	#         if val: record[sub] = val

	#         sub='';val=_en_(record[sub]);
	#         if val: record[sub] = sub

	#         # sub=_en_(record['strip'])
	#         # if sub: record['crypt-date'] = sub
	#         # record['crypt-time'] = _nID.mini.gen( record['stript'] )
	#         # record['crypt-epoch'] = _nID.mini.gen(  )
	#         # record['appID'] = _nID.mini.gen( int(eee) )
	#         # record['crypt-pass'] = __.isPass
	#         del __.isPass
	# --------------------------------------------------

	global isWin
	if isWin:
		if 'nocrypt' in _v.config_hash:
			pass
		else:
			try:
				import _rightThumb._nID as _nID
				try:
					# _keychain = regImp( __.appReg, 'keychain' )
					# nID_password = _keychain.imp.key('nID')
					# _nID.mini.password( nID_password )
					_nID.mini.password( appID_nID_password() )
					isPass = 'secure'
				except Exception as e:
					_nID.mini.password( '1970' )
					isPass = 'unsecure'
				eee = ''
				ee = str(record['epoch'])
				for c in ee:
					if '.' == c:
						break
					eee+=c
				# record['crypt-password'] = nID_password
				record['crypt-date'] = _nID.mini.gen( record['strip'] )
				record['crypt-time'] = _nID.mini.gen( record['stript'] )
				record['crypt-epoch'] = _nID.mini.gen( int(eee) )
				record['appID'] = _nID.mini.gen( int(eee) )
				record['crypt-pass'] = isPass
			except Exception as e:
				pass

		try:
			import _rightThumb._stardate as _sd
			record['stardate'] = _sd.gen(  epoch  )
		except Exception as e:
			pass

		dt = record['fdate'].split(' ')[0].split('-')
		try:
			record['quarter'] = str(record['year']) +'.'+ str(pandas.Timestamp(datetime.date( int(dt[0]) , int(dt[1]), int(dt[2]))).quarter)
		except Exception as e:
			pass

	e = time.time()
	# print_( e-s )
	# print_( e-ss )
	return record