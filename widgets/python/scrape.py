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

import scrapy

# class BlogSpider(scrapy.Spider):
#     name = 'blogspider'
#     # start_urls = ['https://www.biblegateway.com/']
#     start_urls = ['https://blog.scrapinghub.com']

#     def parse(self, response):
#         for title in response.css('.post-header>h2'):
#             yield {'title': title.css('a ::text').extract_first()}

#         for next_page in response.css('div.prev-post > a'):
#             yield response.follow(next_page, self.parse)


depth = 0
parent = []
last = ''
def info(data):
	global depth
	global parent
	found = data
	try:
		exec("""
for x in dir("""+data+"""):
	if not x.startswith('_') and not 'denominator' in x:
		newData = '"""+data+""".'+x
		if check(newData):
			a = info(newData)
			if a:
				print(a)
""")
	except Exception as e:
		found = False
	return found
def check(data):
	global omitEnd
	global omitMiddle
	d = data.split('.')
	if d[len(d)-1] in omitEnd:
		result = False
	else:
		one = len(d)
		two = len(set(d))
		if one == two:
			result = True
		else:
			result = False
	if result:
		for x in d:
			if x in omitMiddle:
				result = False
	return result
omit = 'with_traceback,args,name,casefold,format,format_map,isdecimal,isidentifier,isnumeric,isprintable,capitalize,center,endswith,expandtabs,find,isalnum,isalpha,isdigit,islower,isspace,istitle,isupper,join,ljust,lower,lstrip,maketrans,partition,rfind,rindex,rjust,rpartition,rsplit,rstrip,splitlines,startswith,strip,swapcase,title,translate,upper,zfill,encode,replace,split,index,count,numerator,imag,real,bit_length,from_bytes,to_bytes,conjugate'
omitEnd = omit.split(',')
omit = 'Loop_ActionCnt,Timer,__builtins__,__cached__,__doc__,__file__,__loader__,__name__,__package__,__spec__,_dirCache,_dirCache_p,_v,addSpace,ast,attrib,buildResult,buildResultFromPipe,calculate_monthdelta,calendar,checkIfSwitch,cleanAll,cleanLastChar,columnHeaderLength,columnList,columnList_test,columnNickname1,columnNickname2,columnTab,completed,countThis,date,datetime,defaultTimeout,dirCacheGet,dirCacheSave,dirPrintColumn,dirRows,displayLine,displayLineAgo,displayLineExclude,displayLineExcludeString,displayLineFolder,displayLineInclude,displayLineIncludeString,displayLineSize,doesFieldExist,dowConvert,dt,errors,fileNameLength,folder,folderDepth,folderDepthMax,folderSizeX,folderSizeX2,formatDate,formatDateDay,formatDateMonth,formatDateYear,formatFolderName,formatSize,formatSwitchValueColumn,formatSwitchValueHelperA,formatSwitchValueHelperB,formatSwitchValueHelperC,formatSwitchValueSort,getAttribs,getExtension,getSize,getSwitchField,getSwitchValue,getSwitchValue2,getTable,getsize,glob,groupByList,groupLine,hashlib,isSwitchActive,isdir,isfile,itemgetter,join,json,lastGroup,listPrintColumn,math,maxFileNameLength,md5Gen,monthByNumber,months_between,os,pathCheck,pathCheckBase,pipeResults,printSwitches,processSwitchFormatting,processSwitches,relativedelta,removeAll,replaceAll,resolveIDs,rrule,showColumn,showColumnCSV,showColumnHeader,showColumnHeaderCSV,showPreHeader,sortThis,spaces,splitext,sqlite3,subprocess,switch,switchInput,sys,tabGetMaxSpace,tableProfile,takeAction,test,time,timedelta,timeout,timeoutKill,totalSize,unFormatSize,updateSwitchField,uuid,weeks_between,six,lxml,xmlrpclib,text,sys,os,http,urllib,asyncio,collections,concurrent,ctypes,curses,dbm,distutils,email,encodings,ensurepip,html,http,idlelib,importlib,json,lib2to3,logging,msilib,multiprocessing,pydoc_data,site-packages,sqlite3,test,tkinter,turtledemo,unittest,urllib,venv,wsgiref,xml,xmlrpc,__future__,__main__,_dummy_thread,_thread,abc,aifc,argparse,array,ast,asynchat,asyncio,asyncore,atexit,audioop,base64,bdb,binascii,binhex,bisect,builtins,bz2,calendar,cgi,cgitb,chunk,cmath,cmd,code,codecs,codeop,collections,collections.abc,colorsys,compileall,concurrent,concurrent.futures,configparser,contextlib,contextvars,copy,copyreg,cProfile,crypt,csv,ctypes,curses,curses.ascii,curses.panel,curses.textpad,dataclasses,datetime,dbm,dbm.dumb,dbm.gnu,dbm.ndbm,decimal,difflib,dis,distutils,distutils.archive_util,distutils.bcppcompiler,distutils.ccompiler,distutils.cmd,distutils.command,distutils.command.bdist,distutils.command.bdist_dumb,distutils.command.bdist_msi,distutils.command.bdist_packager,distutils.command.bdist_rpm,distutils.command.bdist_wininst,distutils.command.build,distutils.command.build_clib,distutils.command.build_ext,distutils.command.build_py,distutils.command.build_scripts,distutils.command.check,distutils.command.clean,distutils.command.config,distutils.command.install,distutils.command.install_data,distutils.command.install_headers,distutils.command.install_lib,distutils.command.install_scripts,distutils.command.register,distutils.command.sdist,distutils.core,distutils.cygwinccompiler,distutils.debug,distutils.dep_util,distutils.dir_util,distutils.dist,distutils.errors,distutils.extension,distutils.fancy_getopt,distutils.file_util,distutils.filelist,distutils.log,distutils.msvccompiler,distutils.spawn,distutils.sysconfig,distutils.text_file,distutils.unixccompiler,distutils.util,distutils.version,doctest,dummy_threading,email,email.charset,email.contentmanager,email.encoders,email.errors,email.generator,email.header,email.headerregistry,email.iterators,email.message,email.mime,email.parser,email.policy,email.utils,encodings,encodings.idna,encodings.mbcs,encodings.utf_8_sig,ensurepip,enum,errno,faulthandler,fcntl,filecmp,fileinput,fnmatch,formatter,fractions,ftplib,functools,gc,getopt,getpass,gettext,glob,grp,gzip,hashlib,heapq,hmac,html,html.entities,html.parser,http,http.client,http.cookiejar,http.cookies,http.server,imaplib,imghdr,imp,importlib,importlib.abc,importlib.machinery,importlib.resources,importlib.util,inspect,io,ipaddress,itertools,json,json.tool,keyword,lib2to3,linecache,locale,logging,logging.config,logging.handlers,lzma,macpath,mailbox,mailcap,marshal,math,mimetypes,mmap,modulefinder,msilib,msvcrt,multiprocessing,multiprocessing.connection,multiprocessing.dummy,multiprocessing.managers,multiprocessing.pool,multiprocessing.sharedctypes,netrc,nis,nntplib,numbers,operator,optparse,os,os.path,ossaudiodev,parser,pathlib,pdb,pickle,pickletools,pipes,pkgutil,platform,plistlib,poplib,posix,pprint,profile,pstats,pty,pwd,py_compile,pyclbr,pydoc,queue,quopri,random,re,readline,reprlib,resource,rlcompleter,runpy,sched,secrets,select,selectors,shelve,shlex,shutil,signal,site,smtpd,smtplib,sndhdr,socket,socketserver,spwd,sqlite3,ssl,stat,statistics,string,stringprep,struct,subprocess,sunau,symbol,symtable,sys,sysconfig,syslog,tabnanny,tarfile,telnetlib,tempfile,termios,test,test.support,test.support.script_helper,textwrap,threading,time,timeit,tkinter,tkinter.scrolledtext,tkinter.tix,tkinter.ttk,token,tokenize,trace,traceback,tracemalloc,tty,turtle,turtledemo,types,typing,unicodedata,unittest,unittest.mock,urllib,urllib.error,urllib.parse,urllib.request,urllib.response,urllib.robotparser,uu,uuid,venv,warnings,wave,weakref,webbrowser,winreg,winsound,wsgiref,wsgiref.handlers,wsgiref.headers,wsgiref.simple_server,wsgiref.util,wsgiref.validate,xdrlib,xml,xml.dom,xml.dom.minidom,xml.dom.pulldom,xml.etree.ElementTree,xml.parsers.expat,xml.parsers.expat.errors,xml.parsers.expat.model,xml.sax,xml.sax.handler,xml.sax.saxutils,xml.sax.xmlreader,xmlrpc,xmlrpc.client,xmlrpc.server,zipapp,zipfile,zipimport,zlib'
omitMiddle = omit.split(',')
info('scrapy')

# for x in help("modules"):
	# print(x)
# help("modules")

# 9158

