import _rightThumb._base3 as _
import datetime
import sys
import time
_dir=None
def isDate(theDate=None, record={}, tz=None, q=True, f=None, w=None, what=None):
    if type(record) == str:
        e('expected: f=' + record)
    if (type(theDate) == int or type(theDate) == float) and theDate < 1:
        return 0
    if theDate is None:
        theDate = time.time()
    if not w is None:
        f = w
    if not what is None:
        f = what
    global _dir
    if _dir is None:
        import _rightThumb._dir as _dir
    s = time.time()
    if not tz is None and (not len(tz)):
        tz = None
    local_tz = str(time.strftime('%z')).replace(':', '')
    hasTZ = False
    if type(theDate) == str and len(theDate) > 11:
        if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
            hasTZ = theDate[-6:].replace(':', '')
    if type(theDate) == str and len(theDate) > 11 and (type(hasTZ) == bool):
        if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
            hasTZ = theDate[-5:].replace(':', '')
    epoch = _.autoDate(theDate)
    _dow_ = {'Sunday': 'sun', 'Monday': 'mon', 'Tuesday': 'tue', 'Wednesday': 'wed', 'Thursday': 'thu', 'Friday': 'fri', 'Saturday': 'sat'}
    def fitem(f):
        if f == 'ago':
            return _dir.dateDiffText(epoch)
        if f == 'ago-dic':
            ad = _._2dates(epoch, dic=1)
            del ad['txt']
            return ad
        if f == 'ago-txt':
            return _._2dates(epoch)
        if f == 'friendly':
            return _.friendlyDate(epoch)
        if f == 'friendly':
            return _.friendlyDate(epoch)
        if f == 'friendly3':
            return _.friendlyDate3(epoch)
        if f == 'iso':
            return _.friendlyDate(epoch).replace(' ', 'T') + local_tz
        if f == 'woy':
            return _dir.getWeekAndYear(epoch)
        if f == 'month':
            return _dir.getMonthFromEpoch(epoch)
        if f == 'epoch':
            return epoch
        if f == 'ordinal':
            return datetime.datetime.fromtimestamp(epoch).toordinal()
        if f == 'text-date':
            return datetime.datetime.fromtimestamp(epoch).strftime('%b, %d %Y')
        if f == 'text-time':
            return datetime.datetime.fromtimestamp(epoch).strftime('%I:%M %p')
        if f == 'text-datetime':
            return datetime.datetime.fromtimestamp(epoch).strftime('%b, %d %Y @ %I:%M %p')
        if f == 'sdate':
            return _.friendlyDate2(epoch)
        if f == 'strip':
            return _.onlyNumbers_strip(_.friendlyDate(epoch).split(' ')[0])
        if f == 'strip':
            return _.onlyNumbers_strip(_.friendlyDate(epoch).split(' ')[0])
        if f == 'stript':
            return _.onlyNumbers_strip(_.friendlyDate(epoch))
        if f == 'stripa':
            return _.onlyNumbers_strip(_.friendlyDate(epoch))[:-2]
        if f == 'date':
            return _.friendlyDate(epoch).split(' ')[0]
        if f == 'time':
            return _.friendlyDate2(epoch).split(' ')[1]
        if f == 'fdate':
            return _.friendlyDate(epoch)
        if f == 'fdatea':
            return _.friendlyDate(epoch)[:-3]
        if f == 'cmd':
            return _.friendlyDate(epoch)[:-3].replace(' ', ' @ ').replace('-', '.').replace(':', '.')
        if f == 'month':
            return _dir.getMonthFromEpoch(epoch)
        if f == 'year':
            return _.friendlyDate(epoch).split('-')[0]
        if f == 'year2':
            return _dir.getYearFromEpoch(epoch)
        if f == 'woy':
            return _dir.getWeekAndYear(epoch)
        if f == 'woy2':
            return _dir.getWeekAndYear(epoch).replace(str(_dir.getYearFromEpoch(epoch)) + '.', '')
        if f == 'ago':
            return _dir.dateDiffText(epoch)
        if f == 'days':
            return _.daysDiff(epoch, time.time())
        if f == 'dow':
            return _dir.getDOWromEpochText(epoch)
        if f == 'dow2':
            return _dow_[_dir.getDOWromEpochText(epoch)]
        if f == 'tz':
            return local_tz
        if f == 'fo':
            return _.day(epoch)
        if f in 'crypt-date crypt-time crypt-epoch appID app crypt-pass'.split(' '):
            try:
                import _rightThumb._nID as _nID
                try:
                    _nID.mini.password(_.appID_nID_password())
                    isPass = 'secure'
                except Exception as e:
                    _nID.mini.password('1970')
                    isPass = 'unsecure'
                eee = ''
                try:
                    ee = str(record['epoch'])
                    for c in ee:
                        if '.' == c:
                            break
                        eee += c
                except Exception as e:
                    eee = theDate
                pass
                if f == 'crypt-date':
                    return _nID.mini.gen(record['strip'])
                if f == 'crypt-time':
                    return _nID.mini.gen(record['stript'])
                try:
                    if f == 'crypt-epoch':
                        return _nID.mini.gen(int(eee))
                    if f == 'appID' or f == 'app':
                        return _nID.mini.gen(int(eee))
                except Exception as ee:
                    _.print_(f, 2, 'err:', ee)
                    sys.exit()
                if f == 'crypt-pass':
                    return isPass
            except Exception as ee:
                _.print_(f, 3, 'err:', ee)
                pass
        if f == 'stardate':
            try:
                import _rightThumb._stardate as _sd
                return _sd.gen(epoch)
            except Exception as e:
                return None
        if f == 'quarter':
            dt = _.friendlyDate(epoch).split(' ')[0].split('-')
            try:
                return str(record['year']) + '.' + str(pandas.Timestamp(datetime.date(int(dt[0]), int(dt[1]), int(dt[2]))).quarter)
            except Exception as e:
                return None
        if f == 'true':
            return True
        if f == 'dow':
            dow = _dir.getDOWromEpochText(epoch).lower()
            dci = {'monday': 'mon', 'tuesday': 'tue', 'wednesday': 'wed', 'thursday': 'thu', 'friday': 'fri', 'saturday': 'sat', 'sunday': 'sun'}
            if dow in dci:
                return dci[dow]
            return dow
        return None
    pass
    if f:
        if type(f) == list:
            f = ' '.join(f)
        f = f.replace(',', ' ')
        if not ' ' in f:
            return fitem(f)
        else:
            j = {}
            for q in f.split(' '):
                j[q] = fitem(q)
            return j
    if 'noarrow' in _v.config_hash:
        local_tz = ''
    else:
        global _tz
        if _tz is None:
            import _rightThumb._tz as _tz
        if not type(hasTZ) == bool:
            if not hasTZ == local_tz:
                epoch = _tz.convert(epoch, hasTZ, local_tz)
        if not tz is None and (not local_tz == tz):
            epoch = _tz.convert(epoch, local_tz, tz)
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
                        hasTZ = theDate[-6:].replace(':', '')
                if type(theDate) == str and len(theDate) > 11 and (type(hasTZ) == bool):
                    if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
                        hasTZ = theDate[-5:].replace(':', '')
                local_tz = hasTZ
    if not epoch:
        return record
    global pandas
    if pandas is None:
        if q:
            try:
                import pandas
            except Exception as e:
                pass
    ss = time.time()
    if type(epoch) == str:
        epoch = _.autoDate(epoch.replace('z', ''))
    todo = 'ago ago-dic ago-txt epoch ordinal text-date text-time text-datetime sdate strip stript stripa date time fdate fdatea cmd month year woy woy2 dow dow2 days tz iso fo friendly friendly3'
    for k in todo.split(' '):
        record[k] = _.isDate(epoch, f=k)
    global isWin
    if isWin:
        if 'nocrypt' in _v.config_hash:
            pass
        else:
            try:
                import _rightThumb._nID as _nID
                try:
                    _nID.mini.password(_.appID_nID_password())
                    isPass = 'secure'
                except Exception as e:
                    _nID.mini.password('1970')
                    isPass = 'unsecure'
                eee = ''
                ee = str(record['epoch'])
                for c in ee:
                    if '.' == c:
                        break
                    eee += c
                record['crypt-date'] = _nID.mini.gen(record['strip'])
                record['crypt-time'] = _nID.mini.gen(record['stript'])
                record['crypt-epoch'] = _nID.mini.gen(int(eee))
                record['appID'] = _nID.mini.gen(int(eee))
                record['crypt-pass'] = isPass
            except Exception as e:
                pass
        try:
            import _rightThumb._stardate as _sd
            record['stardate'] = _sd.gen(epoch)
        except Exception as e:
            pass
        dt = record['fdate'].split(' ')[0].split('-')
        try:
            record['quarter'] = str(record['year']) + '.' + str(pandas.Timestamp(datetime.date(int(dt[0]), int(dt[1]), int(dt[2]))).quarter)
        except Exception as e:
            pass
    e = time.time()
    return record