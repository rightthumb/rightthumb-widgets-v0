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
    _.switches.register( 'Folders', '-fo,-folder,-fos,-folders' )
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
    for field_name in _.v.records[0].keys():
        column_type = None
        for row in _.v.records:
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
    conn = sqlite3.connect(_.v.db)
    c = conn.cursor()
    column_names = ','.join(field_names)
    column_defs = ','.join([f'{name} {column_types[i]}' for i, name in enumerate(field_names)])
    create_table_query = f'CREATE TABLE {_.v.table} ({column_defs})'
    c.execute(create_table_query)
    conn.commit()
    conn.close()

def import_json_data():
    conn = sqlite3.connect(_.v.db)
    c = conn.cursor()

    for row in _.v.records:
        values = [row[field_name] for field_name in row]
        insert_query = f'INSERT INTO {_.v.table} VALUES ({",".join(["?" for _ in range(len(values))])})'
        c.execute(insert_query, values)
    conn.commit()
    conn.close()






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
    _.pr(path)

    if path.endswith('.pdf'):
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
    _.v.records.append({'file': path, 'content': fi})


def action():
    load(); global documents;

    for path in documents:
        process(path)
    
    create_sqlite_table(clean_field_names(_.v.records[0].keys()), determine_column_types())
    import_json_data()

def load():
    global documents
    if _.switches.isActive('Folders'):
        folders=_.switches.values('Folders')
    else:
        folders=[os.getcwd()]

    documents=[]
    for folder in folders:
        for path in _.fo(folder):
            if path.endswith('.doc') or path.endswith('.docx') or path.endswith('.pdf'):
                if not '\\~' in path:
                    if _.showLine(path):
                        documents.append(path)
_.v.records=[]
_.v.db='documents.db'
_.v.table = 'documents'
os=__.imp('os.getcwd')
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

