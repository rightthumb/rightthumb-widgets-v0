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
    _.switches.register( 'Build', '-re,-rebuild,-build' )
    _.switches.register( 'Folders', '-fo,-folder,-fos,-folders' )
    _.switches.register( 'ZipFolder', '-zip', 'C:\\tech\\document-database' )
    # _.switches.register( 'URL', '-u,-url,-urls', 'https://efm.cx/', isData='raw' )
    #e)--> examples
    # _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

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

# text = textract.process("path/to/file.extension")

import textract
import docx2txt
import win32com.client
from PyPDF2 import PdfReader
import PyPDF2

########################################################################################




import simplejson
import sqlite3

def clean_field_names(field_names):
    cleaned_names = []
    for field_name in field_names:
        cleaned_name = ''.join(char for char in field_name if char.isalnum()).lower()
        cleaned_names.append(cleaned_name)
    return cleaned_names

def determine_column_types():
    column_types = []
    for field_name in _.v.dd.records[0].keys():
        column_type = None
        for row in _.v.dd.records:
            if isinstance(row[field_name], (int, float)):
                column_type = 'REAL'
                break
            elif isinstance(row[field_name], str):
                column_type = 'TEXT'
        if column_type is None:
            column_type = 'TEXT'
        column_types.append(column_type)
    return column_types

def create_sqlite_table(field_names, column_types):
    if _.switches.isActive('Build'):
        if os.path.isfile(_.v.dd.db):
            os.unlink(_.v.dd.db)
    else:
        if os.path.isfile(_.v.dd.db): return None
    _.switches.fieldSet( 'Build', 'active', True )
    conn = sqlite3.connect(_.v.dd.db)
    c = conn.cursor()
    column_names = ','.join(field_names)
    column_defs = ','.join([f'{name} {column_types[i]}' for i, name in enumerate(field_names)])
    create_table_query = f'CREATE TABLE {_.v.dd.table} ({column_defs})'
    c.execute(create_table_query)
    conn.commit()
    conn.close()



import sqlite3

def import_json_data(key='path'):


    def insert_all():
        conn = sqlite3.connect(_.v.dd.db)
        c = conn.cursor()

        for row in _.v.dd.records:
            values = [row[field_name] for field_name in row]
            print('INSERT',row[key])
            insert_query = f'INSERT INTO {_.v.dd.table} VALUES ({",".join(["?" for _ in range(len(values))])})'
            c.execute(insert_query, values)
        conn.commit()
        conn.close()


    if _.switches.isActive('Build'):
        insert_all()
        return None
    conn = sqlite3.connect(_.v.dd.db)
    c = conn.cursor()

    for row in _.v.dd.records:
        key_value = row.get(key, None)
        if key_value:
            c.execute(f"SELECT COUNT(*) FROM {_.v.dd.table} WHERE {key}=?", (key_value,))
            record_count = c.fetchone()[0]
            if record_count > 0:
                # Record exists, update it
                print('UPDATE',row[key])
                update_query = f'UPDATE {_.v.dd.table} SET {",".join([f"{field_name} = ?" for field_name in row])} WHERE {key}=?'
                values = [row[field_name] for field_name in row] + [key_value]
                c.execute(update_query, values)
                continue

        # Record doesn't exist or key is not set, insert it
        values = [row[field_name] for field_name in row]
        print('INSERT',row[key])
        insert_query = f'INSERT INTO {_.v.dd.table} VALUES ({",".join(["?" for _ in range(len(values))])})'
        c.execute(insert_query, values)

    conn.commit()
    conn.close()







os=__.imp('os.path.isfile')


########################################################################################
# pip install textract
# pip install docx2txt
# pip install PyPDF2
# pip install pdfminer.six


def cleaner(data):
    data = data.replace('\r','\n')
    data = data.replace('\t','    ')
    # while '     ' in data: data = data.replace('     ','    ')
    while '  ' in data: data = data.replace('  ',' ')
    lines=data.split('\n') 
    for i,line in enumerate(lines): lines[i] = line.strip()
    data = '\n'.join(lines)
    while '\n\n' in data: data = data.replace('\n\n','\n')
    return data.lower()


def process(path):
    path = __.path(path)
    shouldRun=True
    if path in _.v.dd.date:
        shouldRun=False
        if _.mod(path) > _.v.dd.date[path]:
            shouldRun=True


    if shouldRun:
        _.pr(path)
        
        elif path.endswith('.txt') or path.endswith('.md'):
            fi = _.getText(path,raw=True)
        elif path.endswith('.pdf'):
            fi = ''
            try:
                pdf_file = open(path, 'rb')
                reader = PyPDF2.PdfReader(pdf_file)
                for page in reader.pages: fi += page.extract_text()+'\n'
            except:
                pass
        else:
            try:
                if path.endswith('.doc'):
                    fi = textract.process(path)
                else:
                    fi = docx2txt.process(path)
            except:
                word = win32com.client.Dispatch("Word.Application")
                word.visible = False
                wb = word.Documents.Open(path)
                doc = word.ActiveDocument
                fi = doc.Range().Text
                doc.Close()
                word.Quit()

        # _.pr(path)
        fi = cleaner(fi)
        print(len(fi.split('\n')),len(fi.split(' ')))
        info = _dir.info(path)
        _info={}
        for k in info:
            if k in 'path name parent folder bytes size date_created date_modified date_accessed ce me ae ext week_of_year day_of_the_week month year ago'.split(' '):
                if type(info[k]) == float:
                    _info[k]=int(str(info[k]).split('.')[0])
                else:
                    _info[k]=info[k]
        _info['content']=fi
        global api
        for k in api: _info[k]=api[k]
        _info['machine']=_v.getMachineID().replace('{','').replace('}','')
        _info['uuid']=_v.md5(str(uuid.UUID(int=uuid.getnode())),True).replace('{','').replace('}','')
        # _.pv(_info)
        # sys.exit()
        _.v.dd.records.append(_info)
        # _.v.dd.records.append({'file': path, 'content': fi})
        _.v.dd.date[path]=__.startTime
        _.v.dd.files.append(path)


def upload():

    import requests

    url = "https://eyeformeta.com/apps/piller/documents/u/"

    zip_file_path = _.v.dd.zip
    db_file_path = _.v.dd.db

    zip_file_name = __.path(zip_file_path).split(os.sep)[-1]
    db_file_name = __.path(db_file_path).split(os.sep)[-1]

    headers = {
        "User-Agent": "Mozilla/5.0",
        "APP-API-KEY": "e861e4f6",
    }

    files = {
        "zip_file": (zip_file_name, open(zip_file_path, "rb"), "application/zip"),
        "db_file": (db_file_name, open(db_file_path, "rb"), "application/octet-stream"),
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        print("Files uploaded successfully.")
    else:
        print(f"Error uploading files: {response.status_code} {response.reason}")



def action():
    load(); global documents;

    for path in documents:
        process(path)
    if _.v.dd.records:
        create_sqlite_table(clean_field_names(_.v.dd.records[0].keys()), determine_column_types())
        import_json_data()
        _.saveTable(_.v.dd.date,'document-database.meta')
        if _.switches.isActive('ZipFolder'):
            import shutil
            epoch = int(str(__.startTime).split('.')[0])
            fo = _.switches.values('ZipFolder')[0]+os.sep+str(epoch)
            _v.mkdir(fo)
            for path in _.v.dd.files:
                md = _hash.string( path )
                os.link(path,fo+os.sep+'__'+md+'.'+path.split('.')[-1].lower())
            shutil.make_archive(fo, 'zip', fo)
            _.v.dd.zip = fo+'.zip'
            upload()




def load():
    global api
    global documents

    gk = _v.tt+os.sep+'gatekeeper.api'
    if not os.path.isfile(gk):
        _gk = _.regImp( __.appReg, 'gatekeeper' )
        _gk.switch('Register')
        _gk.action()
        input('Hit ENTER when done.')

    _gk_ = _.getText(gk,clean=2,raw=True).split('\n')
    api = {
            'app': _gk_[0],
            'api': _gk_[1],
    }

    if not _.switches.isActive('ZipFolder'):
        _.switches.fieldSet( 'ZipFolder', 'active', True )
        _.switches.fieldSet( 'ZipFolder', 'value', 'C:\\tech\\document-database' )
        _.switches.fieldSet( 'ZipFolder', 'values', ['C:\\tech\\document-database'] )

    
    if _.switches.isActive('ZipFolder'):
        _.v.dd.db = _.switches.values('ZipFolder')[0]+os.sep+'documents.db'
    else:
        _.v.dd.db='documents.db'

    if _.switches.isActive('Folders'):
        folders=_.switches.values('Folders')
    else:
        folders=[os.getcwd()]

    if _.switches.isActive('Build'):
        _.v.dd.date = {}
    else:
        _.v.dd.date = _.getTable('document-database.meta')
    documents=[]
    for folder in folders:
        for path in _.fo(folder):
            if path.endswith('.doc') or path.endswith('.docx') or path.endswith('.pdf') or path.endswith('.md'):
                if not '\\~' in path:
                    if _.showLine(path):
                        documents.append(path)
_.v.dd = _.dot()
_.v.dd.records=[]

_.v.dd.table = 'documents'
_.v.dd.files = []
_.v.dd.date = {}
os=__.imp('os.getcwd')
os=__.imp('os.unlink')
os=__.imp('os.link')


import uuid
import _rightThumb._dir as _dir
import _rightThumb._md5 as _hash
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

