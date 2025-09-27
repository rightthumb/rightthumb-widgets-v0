import _rightThumb._base3 as _
_md5 = None
_vault = None
pyAesCrypt = None
shutil = None


def saveCryptTable(rows, theFile, db=False, bank=False, index=False, temp=False, free=False, indentCode=True, sort_keys=False, archive=False, p=1, password=None, me=0):
    _.HD.chmod(theFile)
    try:
        import simplejson
        json = simplejson
    except:
        pass
    try:
        import json
    except ImportError:
        json = simplejson
    global _vault
    global shutil
    global _md5
    global pyAesCrypt
    if _md5 is None:
        import _rightThumb._md5 as _md5
    if shutil is None:
        import shutil
    if pyAesCrypt is None:
        import pyAesCrypt
    if password is None:
        if _vault is None:
            import _rightThumb._vault as _vault
        password = _md5.md5(_vault.key())
    the_temp_file = _v.stmp + _v.slash + '_-cryptTable-' + _.genUUID()
    px = ''
    if theFile.startswith('temp' + _v.slash):
        theFile = theFile.replace('temp' + _v.slash, '')
        file0 = _v.stmp + _v.slash + theFile
        px = file0
    elif db or bank:
        theFile = _v.dbTables + _v.slash + theFile
        px = theFile
    elif index:
        theFile = _v.myIndexes + _v.slash + theFile
        px = theFile
    elif free:
        file0 = theFile
        px = theFile
    elif not temp:
        file0 = _v.myTables + _v.slash + theFile
        px = theFile
    else:
        file0 = _v.stmp + _v.slash + theFile
        px = file0
    if indentCode:
        dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys, default=str)
    else:
        dataDump = simplejson.dumps(rows, sort_keys=False, default=str)
    if archive:
        import _rightThumb._md5 as _md5
        theFileLabel = theFile
        if _v.slash in theFileLabel:
            global appInfo
            tfl = theFileLabel.split(_v.slash)
            tfl.reverse()
            theFileLabel = str(appInfo[__.appReg]['liveAppName']) + '__' + tfl[0]
        theFileLabel = theFileLabel.replace('.json', '')
        theFileLabel = theFileLabel.replace('.JSON', '')
        lastMD5 = None
        if os.path.isfile(file0):
            lastMD5 = _md5.md5File(file0)
            backupFile = _v.stmp + _v.slash + '__archive_temp__' + theFileLabel + '__' + _.genUUID() + '.json'
    f = open(the_temp_file, 'w')
    f.write(str(dataDump))
    f.close()
    _.HD.chmod(theFile)
    bufferSize = 64 * 1024
    with open(the_temp_file, 'rb') as fIn:
        with open(file0, 'wb') as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
    shutil.copyfile(file0, the_temp_file)
    os.unlink(the_temp_file)
    if archive:
        shouldDocument = False
        if os.path.isfile(file0):
            thisMD5 = _md5.md5File(file0)
        if lastMD5 is None:
            shouldDocument = True
        elif not lastMD5 == thisMD5:
            shouldDocument = True
        if not shouldDocument:
            if os.path.isfile(backupFile):
                os.remove(backupFile)
        if shouldDocument:
            md5Table = _.getTable('table_archive_log.json')
            found = False
            for i, record in enumerate(md5Table):
                if theFileLabel == record['name']:
                    found = True
            theFileLabel
            theFile
            _.fileDate(theData)
    if p:
        _.printBold('Saved: ' + px, 'blue')
    if me and theFile in vv.opened_file_me:
        _.changeM(theFile, vv.opened_file_me[theFile])
    return file0