import _rightThumb._base3 as _
import _rightThumb._construct as __
import _rightThumb._dir as _dir


_.switches.postRegister('Text', '-t,-text,-txt')
_.switches.postRegister('Binary', '-bin')
_.switches.postRegister('Encrypted', '-en,-crypt,-encryption,-encrypted,-isCrypt')
_.switches.postRegister('Size', '-size',' g 10mb, L 2kb ')
_.switches.postRegister('Ago', '-ago', '1min 1h 1d 1w 1m 1y')
_.switches.postRegister('Extensions', '-ext', 'db image graphic video app audio doc script archive')
_.switches.postRegister('Ago-Create-Date', '-cd')

import os
def refine(path,trigger=None,failTrigger=None):
    if not os.path.isfile(path):
        return False
    path = __.path(path)
    isValid = False
    if _.showLine(path):
        
        if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
            isValid = True
        else:
            if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
                isValid = True
            if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
                isValid = True
            if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
                isValid = True
            if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
                isValid = True
        pass
        pass
        if _.switches.isActive('Ago'):
            record = _dir.fileInfo( path )
            isValid = False
            run = 'default'
            if len( _.switches.values('Ago') ) > 2:
                if 'a' in _.switches.values('Ago')[2]:
                    run = 'a'
                elif 'md' in _.switches.values('Ago')[2]:
                    run = 'md'
                elif _.switches.isActive('Ago-Create-Date'):
                    run = 'cd'
                elif 'resent' in _.switches.values('Ago')[2]:
                    run = 'resent'
                elif 'm' in _.switches.values('Ago')[2]:
                    run = 'md'
            elif len( _.switches.values('Ago') ) > 1 and type(_.switches.values('Ago')[1]) == str:
                if 'a' in _.switches.values('Ago')[1]:
                    run = 'a'
                elif 'md' in _.switches.values('Ago')[1]:
                    run = 'md'
                elif _.switches.isActive('Ago-Create-Date'):
                    run = 'cd'
                elif 'resent' in _.switches.values('Ago')[1]:
                    run = 'resent'
                elif 'm' in _.switches.values('Ago')[1]:
                    run = 'md'
            agoRange = False
            if len( _.switches.values('Ago') ) > 1 and type(_.switches.values('Ago')[1]) == float:
                agoRange = True
            if not agoRange:
                if run == 'default':
                    if record['date_modified_raw'] > _.switches.values('Ago')[0]:
                        isValid = True
                elif run == 'resent':
                    if record['date_modified_raw'] > _.switches.values('Ago')[0]:
                        isValid = True
                elif run == 'a':
                    if record['accessed_raw'] > _.switches.values('Ago')[0]:
                        isValid = True
                elif run == 'cd':
                    if record['date_created_raw'] > _.switches.values('Ago')[0]:
                        isValid = True
                elif run == 'md':
                    if record['date_modified_raw'] > _.switches.values('Ago')[0]:
                        isValid = True
            elif agoRange:
                if run == 'default':
                    if (record['date_modified_raw'] < _.switches.values('Ago')[0] or record['date_created_raw'] < _.switches.values('Ago')[0]) and (record['date_modified_raw'] > _.switches.values('Ago')[1] or record['date_created_raw'] > _.switches.values('Ago')[1]):
                            isValid = True
                elif run == 'resent':
                    if (record['date_modified_raw'] < _.switches.values('Ago')[0] or record['date_created_raw'] < _.switches.values('Ago')[0] or record['accessed_raw'] < _.switches.values('Ago')[0]) and (record['date_modified_raw'] > _.switches.values('Ago')[1] or record['date_created_raw'] > _.switches.values('Ago')[1] or record['accessed_raw'] > _.switches.values('Ago')[1]):
                            isValid = True
                elif run == 'a':
                    if (record['accessed_raw'] < _.switches.values('Ago')[0]) and (record['accessed_raw'] > _.switches.values('Ago')[1]):
                            isValid = True
                elif run == 'cd':
                    if (record['date_created_raw'] < _.switches.values('Ago')[0]) and (record['date_created_raw'] > _.switches.values('Ago')[1]):
                            isValid = True
                elif run == 'md':
                    if (record['date_modified_raw'] < _.switches.values('Ago')[0]) and (record['date_modified_raw'] > _.switches.values('Ago')[1]):
                            isValid = True
        pass
        pass
        if isValid:
            if _.switches.isActive('Size'):
                isValid = False
                isValid_2 = False
                stat = os.stat(path)
                size = stat.st_size
                if 'l' in _.switches.values('Size')[0]:
                    if size < _.switches.values('Size')[1]:
                        isValid_2 = True
                if 'g' in _.switches.values('Size')[0]:
                    if size > _.switches.values('Size')[1]:
                        isValid_2 = True
                if isValid_2:
                    isValid = False
                    if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
                        isValid = True
                    else:
                        if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
                            isValid = True
                        if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
                            isValid = True
                        if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
                            isValid = True
                        if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
                            isValid = True

        
        if isValid :
            global extensionList
            try: record
            except Exception as ee: record = None
            if len( extensionList ):
                if record is None:
                    record = _dir.info( path )
                if not len( record['ext'] ):
                    isValid = False
                else:
                    record['ext'] = record['ext'].lower()
                    if not '.'+record['ext'] in extensionList:
                        isValid = False
        if isValid and _.switches.isActive('Encrypted') and not _.isCrypt(path): isValid = False
        if isValid:
            if path.endswith('.pyc'): isValid=False
    if isValid and trigger:
        trigger(path)
    if not isValid and failTrigger:
        failTrigger(path)
    
    return isValid



extensionList = []
def extensionsDatabank():
	global extensionList
	_db = _.regImp( __.appReg, 'databank' )
	_db.switch( 'JustReturn' )
	_db.switch( 'Tables', [ 'file', 'extensions' ] )
	useDB=True
	for index in _.switches.values('Extensions'):
		if index.startswith('.'):
			useDB=False
			extensionList.append(index)
	if useDB:
		for index in _.switches.values('Extensions'):
			_db.switch( 'Plus', [index] )
			for i,x in enumerate(_db.action()):
				# print(x)
				x = x.replace('.','')
				if not x.startswith('.'):
					x = '.'+x
				if not x in extensionList:
					extensionList.append( x.lower() )
                         
if _.switches.isActive('Extensions'): extensionsDatabank()