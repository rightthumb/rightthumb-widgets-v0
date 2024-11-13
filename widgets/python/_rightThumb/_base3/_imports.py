_nd = _.regImp( __.appReg, 'fileNameDate' )

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

	_nd.pipe( [databaseFile] )
	_nd.do( 'action' )

_textIndex = _.regImp( __.appReg, 'words' )
	_textIndex.switch( 'Alpha' )
	_textIndex.switch( 'Unique' )
	_textIndex.switch( 'MinLength', 2 )
	_textIndex.switch( 'Stemming' )
	_textIndex.switch( 'PartsOfSpeech' )
	_textIndex.switch( 'Clean' )
	_textIndex.pipe( data )
	index = _textIndex.do( 'action' )

_bm = _.regImp( __.appReg, 'bookmarks' )
	index = _bm.imp.index()
_dirList = _.regImp( __.appReg, 'dirList' )
	_dirList.switch( 'Files' )
	_dirList.switch( 'Recursion' )
	_dirList.switch( 'Binary' )
	_dirList.switch( 'Path','D:\\Apps' )
	files = _dirList.do( 'action' )

import _rightThumb._profileVariables as _profile
	profile = _profile.records.audit( 'name', asset )
import _rightThumb._encryptString as _blowfish
	_blowfish.genPassword()
	_blowfish.genPassword( 'string' )
	en = _blowfish.encrypt( string )
	de = _blowfish.decrypt( en )
import _rightThumb._encryptFile as _blowfish
	_blowfish.encrypt( infilepath, outfilepath, key )
	_blowfish.decrypt( infilepath, outfilepath, key )
_browserX = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )

_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
	_browser.imp.project.open( url )
	code = _.getText( _v.myAppsJs + _v.slash+'Church_Directory.js' )
	_browser.imp.project.jqueryInject()
	_browser.imp.project.inject( code )
	while not _browser.imp.project.injectReturn('return window.taskComplete;'): pass
	data =_browser.imp.project.injectReturn( 'window.hack.acquire.payload()' )
	_browser.imp.project.close()

import _rightThumb._date as _date
import _rightThumb._dir as _dir
	_.printVar( _dir.info( path ) )
import _rightThumb._md5 as _hash
	.file .string .bin  ( data, h )
	md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512 shake_128 shake_256

import _rightThumb._mimetype as _mime

import _rightThumb._backupLog as _bkLog
_bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

import _rightThumb._auditCodeBase as _code
_code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
_omit = _.regImp( __.appReg, 'omitTable' )
	_omit.imp.inTable( 'the' )
_inDic = _.regImp( __.appReg, 'inDic' )
	_inDic.switch( 'All' )
	_inDic.imp.testAll( 'fight' )
	_inDic.imp.testOne( 'austen' )
_file_folder = _.regImp( __.appReg, 'file_folder' )
	_file_folder.switch( 'Save,Clean' )
	_file_folder.switch( 'Compair,Clean' )
	_file_folder.switch( 'Folder', '' )
_fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
	_fileNameDate.imp.newName( filename )
	_fileNameDate.imp.newName( filename, _dir.fileInfo( filename ) )
_filePathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
	_filePathPatterns.switch( 'NoPrint' )
	_filePathPatterns.switch( 'Files', _.switches.value( 'Files' ) )
	folderReport = _filePathPatterns.action()
fileBackup = _.regImp( __.appReg, 'fileBackup' )
	fileBackup.switch( 'Input', filename )
	fileBackup.switch( 'Flag', 'pre replaceText' )
	recoveryFile = fileBackup.do( 'action' )
_folderContent = _.regImp( __.appReg, 'file' )
	_folderContent.switch( 'Silent' )
	_folderContent.switch( 'Folder', _v.myAppsBatch )
	_folderContent.switch( 'NoExtension' )

	_folderContent.switch( 'Recursive' )

	_folderContent.switch( 'Text' )
	_folderContent.switch( 'Binary' )
	_folderContent.switch( 'Label', 'App: ' )
	_folderContent.switch( 'Prefix', ';t' )
	files = _folderContent.do( 'action' )['files']
	folders = _folderContent.do( 'action' )['folders']
_tickets = _.regImp( __.appReg, 'ticketTimeline' )
	_tickets.switch( 'ReturnFiles' )
	records = _tickets.do( 'records' )


