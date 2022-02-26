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
import os, sys, time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
    global appDBA
    f = __.appName( appDBA, parentApp, childApp )
    if reg:
        __.appReg = f
    return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################
from threading import Timer
import re
try:
    import winsound
except Exception as e:
    pass
import simplejson
##################################################

def appSwitches():
    _.switches.register( 'Print-Keys', '-print' )
    _.switches.register( 'Convert-AutoText', '-autotext' )
    _.switches.register( 'Add-Text-Trigger', '-add' )
    _.switches.register( 'Add-Text-Text', '-text' )
    _.switches.register( 'Add-Text-Back', '-back' )
    _.switches.register( 'Add-Text-Note', '-note' )

#   finds the file in probable locations
#   and 
#       if  _.autoBackupData = True
#       and __.releaseAcquiredData = True
#           GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#       you can run apps on usb at a clients office
#           when you get home run: p app -loadepoch epoch 
#               backed up
#                   pipe
#                   files
#                   tables
_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs'] 
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
    'file': 'hotkeys.py',
    'liveAppName': __.thisApp( __file__ ),
    'description': 'hotkeys',
    'categories': [
                        'hotkeys',
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
                        _.hp('p hotkeys'),
                        '',
                        _.hp('p hotkeys -add ...lines -text "sum(1 for line in open(''))" -back 2 -note python-file-lines'),
                        '#      IF YOU DO NOT USE -text when -add it will take from the copied clipboard',
                        _.hp('p hotkeys -add ...lines -back 2 -note python-file-lines'),
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



def registerSwitches( argvProcessForce=False ):
    global appDBA
    if not __.appReg == appDBA and appDBA in __.appReg:

        if not __name__ == '__main__':
            _.argvProcess = argvProcessForce
        else:
            _.argvProcess = True

        _.load()
        _.appInfo[__.appReg] = _.appInfo[appDBA]
        _.appData[__.appReg] = _.appData[appDBA]
    __.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
    appSwitches()

    _.myFileLocation_Print = False
    _.switches.trigger( 'Files', _.myFileLocations, vs=True )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'URL', _.urlTrigger )
    _.switches.trigger( 'Ago', _.timeAgo )
    _.switches.trigger( 'Duration', _.timeFuture )
    # _.switches.trigger( 'Files',_.inRelevantFolder )  
    
    _.defaultScriptTriggers()
    _.switches.process()


if not __name__ == '__main__':
    _.argvProcess = False
else:
    _.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
    if not type( theFocus ) == bool:
        theFocus = theFocus
    _.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
    if not sys.stdin.isatty():
        _.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
#   os.path.abspath(path)
#                                                   if platform.system() == 'Windows':
########################################################################################
# START

from pynput.keyboard import Key, KeyCode, Controller
keyboard = Controller()

from pynput.keyboard import Listener

class HOTKEYS:
    def __init__( self ):
        pass

            

    def release_key( self, key ):
        global post_do
        global key_set
        try:
            char = str(key.char)
        except Exception as e:
            char = str(key).replace("'",'')
        try:
            key_set.remove(char)
        except Exception as e:
            key_set = set()

        if not key_set and post_do['status']:
            post_do['status'] = 0
            count = post_do['count']
            k = post_do['label']
            do = post_do['do']
            if post_do['esc']:
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)

                keyboard.press(Key.esc)
                keyboard.release(Key.esc)

                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
            
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)

            ii=0
            if ii<count:
                while not ii == count:
                    ii+=1
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
            print(k)
            exec(do)
            # beepy.simple_beep2()
         
    def process_keystroke( self, key ):
        global post_do
        global key_set
        global print_chars
        global ctrl_chars
        try:
            char = str(key.char)
        except Exception as e:
            char = str(key).replace("'",'')
        key_set.add(char)
        if print_chars:
            print('____________')
            print(key_set)
            for x in key_set:
              print(str(x).replace("'",''))
        global log
        global table
        global keyboard
        # print(key)
        key = str(key).replace("'", "")
        log.append(key)
        if _.switches.isActive('Print-Keys'):
            print(key)
        log0=log.copy()
        log0.reverse()
        esc=False

        # process set
        for k in table:
            good=True
            count=0
        
            for kk in key_set:
                found=False
                for i,t in enumerate(table[k]['test']):
                    if '.alt' in t.lower():
                        esc=True
                    if t == '\\':
                        if kk == t:
                            found=True
                    else:
                        if kk.lower().startswith(t.lower()):
                            found=True
                    if not found:
                        try:
                            # if k == 'reload':
                                # print(kk,KeyCode( char=kk ), KeyCode( char=t.lower() ))
                            if kk == ctrl_chars[t.lower()]:
                            # if kk == KeyCode( char=ctrl_chars[t.lower()] ):
                                found=True

                        except Exception as e:
                            # print(e)
                            pass
                if not found:
                    good=False
            if not len(table[k]['test']) == len(key_set):
                good=False
            if good:
                beepy.simple_beep()
                post_do['status'] = 1
                post_do['esc'] = esc
                post_do['count'] = count
                post_do['label'] = k
                post_do['do'] = table[k]['do']

                # ii=0
                # if ii<count:
                #   while not ii == count:
                #       ii+=1
                #       keyboard.press(Key.esc)
                #       keyboard.press(Key.backspace)
                #       keyboard.release(Key.backspace)
                # print(k)
                # exec(table[k]['do'])
                return None
                break

        # process history
            
        for k in table:
            good=True
            count=0
            for i,t in enumerate(table[k]['test']):
                if '.alt' in t.lower():
                    esc=True
                try:
                    if not t.startswith('Key.'):
                        count+=1
                    elif t.startswith('Key.space'):
                        count+=1

                    if t == '\\':
                        if not log0[i] == t:
                            good=False
                            break
                    else:
                        if not log0[i].startswith(t):
                            good=False
                            break

                except Exception as e:
                    good=False
                    break
            if good:
                beepy.simple_beep()
                post_do['status'] = 1
                post_do['esc'] = esc
                post_do['count'] = count
                post_do['label'] = k
                post_do['do'] = table[k]['do']

                # ii=0
                # if ii<count:
                #   while not ii == count:
                #       ii+=1
                #       keyboard.press(Key.esc)
                #       keyboard.press(Key.backspace)
                #       keyboard.release(Key.backspace)
                # print(k)
                # exec(table[k]['do'])
                break
# class Hotkeys:END


        

class BEEPS:
    def __init__( self ):
        ###
        # Notes Config
        ###

        # Set delay tempo
        self.tempo = 0.15
        # tempo = 1

        # Setup Notes
        self.notes = {}
        self.notes["pause"] = 0
        self.notes["c"] = 1
        self.notes["c#"] = 2
        self.notes["d"] = 3
        self.notes["d#"] = 4
        self.notes["e"] = 5
        self.notes["f"] = 6
        self.notes["f#"] = 7
        self.notes["g"] = 8
        self.notes["g#"] = 9
        self.notes["a"] = 10
        self.notes["a#"] = 11
        self.notes["b"] = 12

        # Note Types
        self.note_types = {}
        self.note_types["sixteenth"] = 50
        self.note_types["eigth"] = 100
        self.note_types["dotted_eigth"] = 150
        self.note_types["quarter"] = 200
        self.note_types["half"] = 400
        self.note_types["whole"] = 800
        self.note_types["triplet"] = 60
    def play_note( self, octave, note, note_type ):
        """Play a note at a certain octave by calculating the frequency of the sound it would represent on the motherboard's speaker."""

        # Match the note and note type to the dictionaries
        note = self.notes[note]
        note_type = self.note_types[note_type]

        # Chill for a bit if it's a pause
        if not note:
            time.sleep(note_type/1000)
            return

        # Calculate C for the provided octave
        frequency = 32.7032 * (2**octave)

        # Calculate the frequency of the given note
        frequency *= 1.059463094**note

        # Beep it up
        try:
            winsound.Beep(int(frequency), note_type)
            # Delay after the beep so it doesn't all run together
            time.sleep(self.tempo)
        except Exception as e:
            pass

    def simple_beep(self):
        oct = 3
        self.play_note(oct, 'g', 'half')

    def simple_beep2(self):
        oct = 3
        self.play_note(oct, 'e', 'half')


class CLIP:



    def toLower(self):
        _copy = _.regImp( __.appReg, '-copy' )
        _paste = _.regImp( __.appReg, '-paste' )
        data  = _paste.imp.paste()
        _copy.imp.copy( data.lower(), p=0 )

    def toUpper(self):
        _copy = _.regImp( __.appReg, '-copy' )
        _paste = _.regImp( __.appReg, '-paste' )
        data  = _paste.imp.paste()
        _copy.imp.copy( data.upper(), p=0 )

    def reverse_lines(self):
        _copy = _.regImp( __.appReg, '-copy' )
        _paste = _.regImp( __.appReg, '-paste' )
        data  = _paste.imp.paste()
        data = cleaner(data,1)
        result = data.split('\n')
        result.reverse()
        _copy.imp.copy(  '\n'.join(result)  , p=0 )

    def builder(self):
        global keyboard
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text = cleaner(text,1)
        if not '{}' in text:
            beepy.simple_beep2()
            return None
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('x')
            keyboard.release('x')

        time.sleep(.5)
        lines = _paste.imp.paste()
        lines = cleaner(lines,1)
        result = ''
        for line in lines.split('\n'):
            line = cleaner(line)
            result += text.replace( '{}', line ) + '\n'
        result=_str.cleanBE( result, '\n' )
        _copy.imp.copy( result, p=0 )

        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')



    def builder2(self):
        global keyboard
        def build_helper( line, base ):
            fx = '{}'
            parts = []
            fa=_.find_all( base , fx )
            i=0
            lp = line.split(',')
            for ii, pf in enumerate(fa):
                parts.append( base[i:pf] )
                try:
                    parts.append( cleaner(lp[ii]) )
                except Exception as e:
                    pass
                i=pf+len(fx)
            parts.append( base[i:] )
            return ''.join(parts)

        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text = cleaner(text,1)
        if not '{}' in text:
            beepy.simple_beep2()
            return None

        time.sleep(.5)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('x')
            keyboard.release('x')
        time.sleep(.5)
        lines = _paste.imp.paste()
        lines = cleaner(lines,1)
        result = ''
        for line in lines.split('\n'):
            line = cleaner(line)
            result += build_helper( line, text ) +'\n'
        result=_str.cleanBE( result, '\n' )
        _copy.imp.copy( result, p=0 )

        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')


    def range_first(self):
        def spliter( abc ):
            sp=','
            res = []
            if not sp in abc:
                return abc
            fa=_.find_all( abc , sp )
            a = abc[0:fa[0]]
            b = abc[fa[0]:]
            if not '-' in a:
                return abc

            aa=int(a.split('-')[0])
            bb=int(a.split('-')[1])
            res.append( str(aa)+b )
            while not aa == bb:
                aa+=1
                res.append( str(aa)+b )
            return res

        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text = cleaner(text,1)
        result = []
        for line in text.split('\n'):
            line = cleaner(line)
            tx = spliter( line )
            if type(tx) == str:
                result.append(tx)
            else:
                for kk in tx:
                    result.append(kk)

        _copy.imp.copy( '\n'.join( result ) , p=0 )







    def first(self):
        _copy = _.regImp( __.appReg, '-copy' )
        _paste = _.regImp( __.appReg, '-paste' )
        data  = _paste.imp.paste()
        data = data.replace("'",'')
        data = data.replace('"','')
        data = data.replace('`','')
        data = data.replace(':','')
        data = data.replace('$','')
        data = data.replace('=',' ')
        data = data.replace('\t',' ')
        data = cleaner(data,1)

        result = ''
        for line in data.split('\n'):
            line=_str.cleanBE( line, ' ' )
            result += line.split(' ')[0] + '\n'
        result=_str.cleanBE( result, '\n' )

        _copy.imp.copy( result, p=0 )

    def php_var(self):
        _copy = _.regImp( __.appReg, '-copy' )
        _paste = _.regImp( __.appReg, '-paste' )
        data  = _paste.imp.paste()
        data = data.replace("'",'')
        data = data.replace('"','')
        data = data.replace('`','')
        data = data.replace(':','')
        data = data.replace('$','')
        data = data.replace('=',' ')
        data = data.replace('\t',' ')
        data = cleaner(data,1)

        result = ''
        for line in data.split('\n'):
            line=_str.cleanBE( line, ' ' )
            result += '$'+line.split(' ')[0] + '\n'
        result=_str.cleanBE( result, '\n' )

        _copy.imp.copy( result, p=0 )


    def SQL_to_crud(self):

        define = {
                    'int': 'number',
                    'tinyint': 'number',
                    'smallint': 'number',
                    'mediumint': 'number',
                    'bigint': 'number',
                    'decimal': 'number',
                    'float': 'number',
                    'bit': 'number',

                    # '{}': 'spatial',
                    'char': 'text',
                    'varchar': 'text',
                    'binary': 'text',
                    'varbinary': 'text',
                    'tinyblob': 'text',
                    'blob': 'text',
                    'mediumblob': 'text',
                    'longblob': 'text',
                    'tinytext': 'text',
                    'text': 'text',
                    'mediumtext': 'text',
                    'longtext': 'text',
                    'enum': 'text',
                    'set': 'text',

                    'date': 'date',
                    'time': 'date',
                    'datetime': 'date',
                    'timestamp': 'date',
                    'year': 'date',

                    'geometry': 'spatial',
                    'point': 'spatial',
                    'linestring': 'spatial',
                    'polygon': 'spatial',
                    'geometrycollection': 'spatial',
                    'multilinestring': 'spatial',
                    'multipoint': 'spatial',
                    'multipolygon': 'spatial',
        }


        sql = """

/////////////////////////////////////////////////////////////////// START AUTO-CRUD  THETABLE


function update_one__THETABLE( $ID_label, $FIELD ){
    $FIELD =ingenuity_clean($FIELD);
    dbquery(  "UPDATE THETABLE SET FIELD='$FIELD' WHERE ID_label=ID_data ", false);
}

function add_most__THETABLE( FIELDS_MOST_var_comma ){
    $FIELD_MOST_label =ingenuity_clean($FIELD_MOST_label);
    dbquery(  " INSERT INTO THETABLE (FIELDS_MOST_comma) VALUES (FIELDS_MOST_data_comma);"  ,false);
}

function add_all__THETABLE( FIELDS_ALL_var_comma ){
    $FIELD_ALL_text_label =ingenuity_clean($FIELD_ALL_text_label);
    dbquery(  " INSERT INTO THETABLE (FIELDS_ALL_comma) VALUES (FIELDS_ALL_data_comma);"  ,false);
}

function update_most__THETABLE( $ID_label, FIELDS_MOST_var_comma ){
    $FIELD_MOST_text_label =ingenuity_clean($FIELD_MOST_text_label);
    dbquery(  "
        UPDATE THETABLE SET 
            FIELD_MOST_label=FIELD_data
        WHERE ID_label=ID_data
    ", false);
}

function update_all__THETABLE( FIELDS_ALL_var_comma ){
    $FIELD_ALL_text_label =ingenuity_clean($FIELD_ALL_text_label);
    dbquery(  "
        UPDATE THETABLE SET 
            FIELDS_ALL_label=FIELD_data
        WHERE ID_label=ID_data
    ", false);
}

function get__THETABLE( $ID_label ){
    global $theDatabase;
    $query=" SELECT * FROM THETABLE WHERE ID_label=ID_data ORDER BY ID_label DESC";
    
    $result = $theDatabase->query($query);$i=0;
    while ($row = mysqli_fetch_assoc($result)) {
    $resultArray[$i] = array(
        'FIELDS_ALL_label' => ingenuity_unclean($row['FIELDS_ALL_label']),
        );$i++;}
    if ($i === 0) $resultArray=false;
    return $resultArray;

}

/////////////////////////////////////////////////////////////////// END AUTO-CRUD  THETABLE
        """
        sq='"'
        q="'"

        invert_quotes = False

        if invert_quotes:
            q='"'
            sq="'"
            sql = sql.replace( '"', '4ED054B5666E' )
            sql = sql.replace( "'", 'E982407E' )
            sql = sql.replace( 'E982407E', '"' )
            sql = sql.replace( '4ED054B5666E', "'" )


        var='$'
        _copy = _.regImp( __.appReg, '-copy' )
        _paste = _.regImp( __.appReg, '-paste' )
        data  = _paste.imp.paste()
        data = data.replace("'",'')
        data = data.replace('"','')
        data = data.replace('`','')
        data = data.replace('\t',' ')
        data = cleaner(data,1)



        code = ''
        table = ''
        dic = {}
        fields = []
        fields_r = []
        fields_v = []
        fields_vq = []
        fields_v_a = []
        fields_vq_a = []
        skip = []
        for i,line in enumerate(data.split('\n')):
            line = cleaner(line)
            print(line)
            parts = line.split(' ')
            if i == 0:
                if 'CREATE TABLE' in line.upper():
                    line = line.replace( '(', ' (' )
                    table = parts[2]
                else:
                    beepy.simple_beep2()
                    return None
            else:
                try:
                    dic[parts[0]] = define[parts[1].split('(')[0].lower()]
                    fields.append(parts[0])
                    if 'DEFAULT 0'.lower() in line.lower() or 'DEFAULT 1'.lower() in line.lower() or 'CURRENT_TIMESTAMP'.lower() in line.lower():
                        skip.append( parts[0] )
                    elif not i == 1:

                        fields_r.append( parts[0] )


                except Exception as e:
                    pass

        # _.pv(fields)
        # _.pv(fields_r)
        # _.pv(skip)
        # _.pv(dic)
        # print( table )


        def field_data(f,t):
            if t == 'number':
                return var+f
            else:
                return q+var+f+q
                return sq+'. ingenuity_clean('+var+f+') .'+sq

        for field in fields:
            fields_v_a.append( var+field )
            fields_vq_a.append( field_data(field,dic[field]) )


        for field in fields_r:
            fields_v.append( var+field )
            fields_vq.append( field_data(field,dic[field]) )

        pass
        skip.append( fields[0] )


                
        sql = sql.replace( 'THETABLE', table )
        sql = sql.replace( 'ID_label', fields[0] )
        sql = sql.replace( 'ID_data', field_data(fields[0],dic[fields[0]]) )

        sql = sql.replace( 'FIELDS_MOST_var_comma', ', '.join(fields_v) )
        sql = sql.replace( 'FIELDS_MOST_data_comma', ', '.join(fields_vq) )
        sql = sql.replace( 'FIELDS_MOST_comma', ', '.join(fields_r) )

        sql = sql.replace( 'FIELDS_ALL_var_comma', ', '.join(fields_v_a) )
        sql = sql.replace( 'FIELDS_ALL_data_comma', ', '.join(fields_vq_a) )
        sql = sql.replace( 'FIELDS_ALL_comma', ', '.join(fields) )

        for i,line in enumerate(sql.split('\n')):
            if not 'FIELD_MOST_label' in line and not 'FIELD_data' in line and not 'FIELDS_ALL_label' in line and not 'FIELD_ALL_text_label' in line and not 'FIELD_MOST_text_label' in line:
                code += line + '\n'
            else:

                if 'FIELD_ALL_text_label' in line:
                    for field in fields:
                        if dic[field] == 'text':
                            code += line.replace( 'FIELD_ALL_text_label', field ).replace( 'FIELD_data', field_data(field,dic[field]) ) + '\n'

                elif 'FIELD_MOST_text_label' in line:
                    for field in fields:
                        if dic[field] == 'text':
                            code += line.replace( 'FIELD_MOST_text_label', field ).replace( 'FIELD_data', field_data(field,dic[field]) ) + '\n'


                elif 'FIELDS_ALL_label' in line:
                    for field in fields:
                        code += line.replace( 'FIELDS_ALL_label', field ).replace( 'FIELD_data', field_data(field,dic[field]) ) + '\n'


                else:
                    for field in fields_r:
                        code += line.replace( 'FIELD_MOST_label', field ).replace( 'FIELD_data', field_data(field,dic[field]) ) + '\n'



        pass




        # THETABLE
        # ID_label
        # ID_data

        # FIELDS_MOST_var_comma
        # FIELDS_MOST_data_comma
        # FIELDS_MOST_comma

        # FIELD_MOST_label
        # FIELD_data
        # FIELDS_ALL_label
        # FIELD_ALL_text_label
        # FIELD_MOST_text_label




        _copy.imp.copy( code, p=0 )


    #       data=_str.cleanBE( data, '\n' )
    # CREATE TABLE `meta_email_schedule` (
    #   `id` int(11) NOT NULL,
    #   `cid` varchar(40) DEFAULT NULL,
    #   `uuid` varchar(40) DEFAULT NULL,
    #   `db` varchar(40) DEFAULT NULL,
    #   `subject` varchar(40) DEFAULT NULL,
    #   `created` varchar(200) DEFAULT NULL,
    #   `sday` varchar(200) DEFAULT NULL,
    #   `stime` varchar(200) DEFAULT NULL,
    #   `last` varchar(200) DEFAULT "",
    #   `json` longblob DEFAULT "",
    #   `counter` int(6) DEFAULT 0,
    #   `expire` varchar(200) DEFAULT "",
    #   `spent` int(1) DEFAULT 0,
    #   `text` int(6) DEFAULT 0,
    #   `cnt` int(6) DEFAULT 1,
    #   `now` int(6) DEFAULT 0,
    #   `status` int(1) DEFAULT 1
    # )


    def win_path(self):
        _copy = _.regImp( __.appReg, '-copy' )
        _paste = _.regImp( __.appReg, '-paste' )
        data  = _paste.imp.paste()
        if '\\\\' in data:
            data = _str.replaceDuplicate(data,'\\')
        else:
            data = _str.replaceDuplicate(data,'\\')
            data = data.replace('\\','\\\\')
        _copy.imp.copy( data, p=0 )

    def reduction_loop(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        if ',' in text:
            par = False
        else:
            par = True
        text = text.replace( '\n', ',' )
        text = text.replace( '\t', '' )
        text = text.replace( ' ', '' )
        text = text.replace( '\r', '' )
        text = _str.cleanBE(text,',')
        text = _str.replaceAll(text,',,',',')
        numbs = []
        for n in text.split(','):
            if len(n):
                n = int(n)
                numbs.append(n)
        l=0
        done=False
        while not done:
            for n in numbs:
                if (not n%2==0):
                    done = True


            if not done:
                l+=1
                for i,n in enumerate(numbs):
                    numbs[i] = n/2
        pass
        strings = []
        strings.append( str(l)+':' )
        for n in numbs:
            strings.append(str(n).replace('.0',''))

        if par:
            bind = '\n'
        else:
            bind = ', '
        results = bind.join(strings)
        results = results.replace( ':,', ':' )
        _copy.imp.copy( results, p=0 )


    def implode(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text=_str.replaceDuplicate( text, '\n' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text = text.replace('\r','')

        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        if text.startswith('{') or text.startswith('['):
            try:
                data = simplejson.load(text)
            except Exception as e:
                data = eval(text.replace('false','False').replace('true','True'))
            result = simplejson.dumps(data, sort_keys=False)
            result=result.replace('{','{ ').replace('}',' }')
            _copy.imp.copy( result, p=0 )
            return None
        text = text.replace('\n',', ')
        text = text.replace('\r','')
        # text = text.replace('\n','')
        # text = text.replace(', ',',')
        # text = text.replace(',','\n')
        
        _copy.imp.copy( text, p=0 )

        text=_str.replaceDuplicate( text, ' ' )
        _copy.imp.copy( text, p=0 )

    def implode3(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text=_str.replaceDuplicate( text, '\n' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text = text.replace('\r','')

        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        if text.startswith('{') or text.startswith('['):
            # print(text)
            # sys.exit()
            try:
                data = simplejson.load(text)
            except Exception as e:
                data = eval(text.replace('false','False').replace('true','True'))
            result = '[\n\t'
            records = []
            for record in data:
                records.append( simplejson.dumps(record, sort_keys=False) )
            result += ',\n\t'.join(records)
            result += '\n]'
            
            result=result.replace('{','{ ').replace('}',' }')
            _copy.imp.copy( result, p=0 )
            return None

    def toString(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text=_str.replaceDuplicate( text, '\n' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text = text.replace('\r','')

        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        if text.startswith('{') or text.startswith('['):
            # print(text)
            # sys.exit()
            try:
                data = simplejson.load(text)
            except Exception as e:
                data = eval(text.replace('false','False').replace('true','True'))
            records = []
            for rec in data:
                records.append(rec.replace('\r','').replace('\n',''))

            _copy.imp.copy( '\n'.join(records), p=0 )
            return None



    def prefix(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text = text.replace( '\n', '' )
        text = text.replace( '\r', '' )
        text = text.replace( '\t', '' )
        text = _str.cleanBE( text, ' ' )

        time.sleep(1)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('x')
            keyboard.release('x')

        time.sleep(.5)
        lines = _paste.imp.paste()
        lines=_str.cleanBE( lines, '\n' )
        lines = lines.replace('\r','')

        result=''
        for line in lines.split('\n'):
            if len(line.replace(' ','').replace('\t','')):
                result += text + ' ' + line + '\n'
            else:
                result += '\n'
                
        result=_str.cleanBE( result, '\n' )
        _copy.imp.copy( result, p=0 )
        time.sleep(1)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')

    def combine_make(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text = text.replace( '\n', '' )
        text = text.replace( '\r', '' )
        text = text.replace( '\t', '' )
        text = _str.cleanBE( text, ' ' )

        time.sleep(1)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('x')
            keyboard.release('x')

        time.sleep(.5)
        lines = _paste.imp.paste()
        lines=_str.cleanBE( lines, '\n' )
        lines = lines.replace('\r','')

        a = lines.split('\n\n')[0].split('\n')
        b = lines.split('\n\n')[1].split('\n')

        result=''
        for i,line in enumerate(a):
            result += text.replace( '{1}', a[i] ).replace( '{2}', b[i] )+'\n'
                
        result=_str.cleanBE( result, '\n' )
        result=result.replace("''",'"')
        _copy.imp.copy( result, p=0 )
        time.sleep(1)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')


    def suffix(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text = text.replace( '\n', '' )
        text = text.replace( '\r', '' )
        text = text.replace( '\t', '' )
        text = _str.cleanBE( text, ' ' )
        time.sleep(1)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('x')
            keyboard.release('x')

        time.sleep(.5)
        lines = _paste.imp.paste()
        lines=_str.cleanBE( lines, '\n' )
        lines = lines.replace('\r','')
        
        project = _.genUUID()
        _.fields.register( project, 'single' )
        for line in lines.split('\n'):
            if len(line.replace(' ','').replace('\t','')):
                _.fields.register( project, 'single', line )

        result=''
        for line in lines.split('\n'):
            if len(line.replace(' ','').replace('\t','')):
                result += _.fields.value( project, 'single', line ) + ' ' + text + '\n'
            else:
                result += '\n'
        
        result=_str.cleanBE( result, '\n' )
        _copy.imp.copy( result, p=0 )
        time.sleep(1)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')


    def number(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        # text=_str.replaceDuplicate( text, '\n' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text = text.replace('\r','')
        result=''
        i_max=0
        for line in text.split('\n'):
            if len(line.replace(' ','').replace('\t','')):
                i_max+=1
        
        i_char = len(str(i_max))
        i=0
        for line in text.split('\n'):
            if len(line.replace(' ','').replace('\t','')):
                i+=1
                if i_char == 4:
                    if len(str(i)) == 4:
                        result += str(i)+' '+line+'\n'
                    elif len(str(i)) == 3:
                        result += str(i)+'  '+line+'\n'
                    elif len(str(i)) == 2:
                        result += str(i)+'   '+line+'\n'
                    elif len(str(i)) == 1:
                        result += str(i)+'    '+line+'\n'
                if i_char == 3:
                    if len(str(i)) == 3:
                        result += str(i)+' '+line+'\n'
                    elif len(str(i)) == 2:
                        result += str(i)+'  '+line+'\n'
                    elif len(str(i)) == 1:
                        result += str(i)+'   '+line+'\n'
                if i_char == 2:
                    if len(str(i)) == 2:
                        result += str(i)+' '+line+'\n'
                    elif len(str(i)) == 1:
                        result += str(i)+'  '+line+'\n'
                if i_char == 1:
                    result += str(i)+' '+line+'\n'

            else:
                result += '\n'


        result=_str.cleanBE( result, '\n' )
        # text=_str.replaceDuplicate( result, ' ' )
        _copy.imp.copy( result, p=0 )


    def numberz(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        # text=_str.replaceDuplicate( text, '\n' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text = text.replace('\r','')
        texts = text.split('\n')
        result=''
        i=0
        for line in texts:
            if len(line.replace(' ','').replace('\t','')):
                i+=1
                result += _.zeros2(i,  len(str(len(texts)))  )+' '+line+'\n'


            else:
                result += '\n'


        result=_str.cleanBE( result, '\n' )
        # text=_str.replaceDuplicate( result, ' ' )
        _copy.imp.copy( result, p=0 )


    def number_a(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        # text=_str.replaceDuplicate( text, '\n' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text = text.replace('\r','')
        result=''
        i_max=0
        for line in text.split('\n'):
            if len(line.replace(' ','').replace('\t','')):
                i_max+=1
        
        i_char = len(str(i_max))
        i=0
        for line in text.split('\n'):
            i+=1
            if i_char == 4:
                if len(str(i)) == 4:
                    result += str(i)+' '+line+'\n'
                elif len(str(i)) == 3:
                    result += str(i)+'  '+line+'\n'
                elif len(str(i)) == 2:
                    result += str(i)+'   '+line+'\n'
                elif len(str(i)) == 1:
                    result += str(i)+'    '+line+'\n'
            if i_char == 3:
                if len(str(i)) == 3:
                    result += str(i)+' '+line+'\n'
                elif len(str(i)) == 2:
                    result += str(i)+'  '+line+'\n'
                elif len(str(i)) == 1:
                    result += str(i)+'   '+line+'\n'
            if i_char == 2:
                if len(str(i)) == 2:
                    result += str(i)+' '+line+'\n'
                elif len(str(i)) == 1:
                    result += str(i)+'  '+line+'\n'
            if i_char == 1:
                result += str(i)+' '+line+'\n'



        result=_str.cleanBE( result, '\n' )
        # text=_str.replaceDuplicate( result, ' ' )
        _copy.imp.copy( result, p=0 )

    def number_b(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        # text=_str.replaceDuplicate( text, '\n' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text = text.replace('\r','')
        result=''
        i_max=0
        for line in text.split('\n'):
            if len(line.replace(' ','').replace('\t','')):
                i_max+=1
        
        i_char = len(str(i_max))
        i=0
        for line in text.split('\n'):
            line=_str.cleanBE( line, ' ' )
            if len(line.replace(' ','').replace('\t','')):
                i+=1
                if i_char == 4:
                    if len(str(i)) == 4:
                        result += str(i)+' '+line+'\n'
                    elif len(str(i)) == 3:
                        result += str(i)+'  '+line+'\n'
                    elif len(str(i)) == 2:
                        result += str(i)+'   '+line+'\n'
                    elif len(str(i)) == 1:
                        result += str(i)+'    '+line+'\n'
                if i_char == 3:
                    if len(str(i)) == 3:
                        result += str(i)+' '+line+'\n'
                    elif len(str(i)) == 2:
                        result += str(i)+'  '+line+'\n'
                    elif len(str(i)) == 1:
                        result += str(i)+'   '+line+'\n'
                if i_char == 2:
                    if len(str(i)) == 2:
                        result += str(i)+' '+line+'\n'
                    elif len(str(i)) == 1:
                        result += str(i)+'  '+line+'\n'
                if i_char == 1:
                    result += str(i)+' '+line+'\n'

            else:
                result += '\n'


        result=_str.cleanBE( result, '\n' )
        # text=_str.replaceDuplicate( result, ' ' )
        _copy.imp.copy( result, p=0 )



    def number_ba(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        # text=_str.replaceDuplicate( text, '\n' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text = text.replace('\r','')
        result=''
        i_max=0
        for line in text.split('\n'):
            if len(line.replace(' ','').replace('\t','')):
                i_max+=1
        
        i_char = len(str(i_max))
        i=0
        for line in text.split('\n'):
            line=_str.cleanBE( line, ' ' )
            i+=1
            if i_char == 4:
                if len(str(i)) == 4:
                    result += str(i)+' '+line+'\n'
                elif len(str(i)) == 3:
                    result += str(i)+'  '+line+'\n'
                elif len(str(i)) == 2:
                    result += str(i)+'   '+line+'\n'
                elif len(str(i)) == 1:
                    result += str(i)+'    '+line+'\n'
            if i_char == 3:
                if len(str(i)) == 3:
                    result += str(i)+' '+line+'\n'
                elif len(str(i)) == 2:
                    result += str(i)+'  '+line+'\n'
                elif len(str(i)) == 1:
                    result += str(i)+'   '+line+'\n'
            if i_char == 2:
                if len(str(i)) == 2:
                    result += str(i)+' '+line+'\n'
                elif len(str(i)) == 1:
                    result += str(i)+'  '+line+'\n'
            if i_char == 1:
                result += str(i)+' '+line+'\n'




        result=_str.cleanBE( result, '\n' )
        # text=_str.replaceDuplicate( result, ' ' )
        _copy.imp.copy( result, p=0 )



    def explode(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text=_str.replaceDuplicate( text, ' ' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text = text.replace('\r','')
        text = text.replace('\n','')
        if text.startswith('{') or text.startswith('['):
            try:
                data = simplejson.load(text)
            except Exception as e:
                data = eval(text)
            result = simplejson.dumps(data, indent=4, sort_keys=False)
            _copy.imp.copy( result, p=0 )
            return None
        text = text.replace(', ',',')
        text = text.replace(',','\n')
        _copy.imp.copy( text, p=0 )

    def math(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text=_str.replaceDuplicate( text, ' ' )
        text = text.replace('\t','')
        text = text.replace('\r','')
        text = text.replace('\n','')
        text = text.replace(',','')
        text = text.replace('x','*')
        text = text.replace('X','*')
        string = ''
        for x in text:
            if x in '0123456789/*-+()':
                string +=x
        result = eval(string)
        # result = sum(map(int, re.findall(r'[+-]?\d+', string)))
        _copy.imp.copy( str(_.addComma( result )), p=0 )

    def dic(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text=_str.replaceDuplicate( text, ' ' )
        text=_str.cleanBE( text, '\n' )
        text=_str.cleanBE( text, '\t' )
        text=_str.cleanBE( text, ' ' )
        text = text.replace('\r','')
        text = text.replace('\n','')
        text = text.replace(', ',',')
        text = text.replace(' ,',',')
        xXx = text.split(',')
        group=[]
        for x in xXx:
            group.append(x+':'+x)
        result = '{'+','.join(group)+'}'
        _copy.imp.copy( result, p=0 )

    def add_slash(self):
        _paste = _.regImp( __.appReg, '-paste' )
        _copy = _.regImp( __.appReg, '-copy' )
        text = _paste.imp.paste()
        text = text.replace('\r','')
        text=_str.cleanBE( text, '\n' )
        text=_str.replaceDuplicate( text, '\n' )
        newText = ''
        for line in text.split('\n'):
            newText += line + '\\\n'

        _copy.imp.copy( newText, p=0 )


    def del_activate(self):
        Timer( .001, self.del_run ).start()

    def del_run(self):
        global log
        global keyboard
        x='x'
        while not x in '123456789':
            # print('x',x)
            log0=log.copy()
            log0.reverse()
            x=log0[0]
        if x in '123456789':
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
            # print('y',x)
            x=int(x)
            _paste = _.regImp( __.appReg, '-paste' )
            text = _paste.imp.paste()
            _copy = _.regImp( __.appReg, '-copy' )
            newText = []
            for line in text.split('\n'):
                line=_str.replaceDuplicate( line, ' ' )
                line=_str.cleanBE( line, ' ' )
                parts=line.split(' ')
                i=0
                while not i == x:
                    i+=1
                    parts.pop(0)
                newLine=' '.join(parts)
                newText.append(newLine)
            _copy.imp.copy( '\n'.join(newText), p=0 )

# class CLIP:END

class TYPING:
    def __init__(self):
        pass

    def ty(self,text,back=0):
        global keyboard
        for t in text:
            self.keyboard_typing(t)

        ii=0
        while not ii == back:
            ii+=1
            keyboard.press(Key.left)
            keyboard.release(Key.left)

    def ty_h(self,k,back=0):
        global keyboard
        global hot_text

        text = hot_text[k]['text']
        text = text.replace('\r','')
        for t in text:
            self.keyboard_typing(t)

        ii=0
        while not ii == back:
            ii+=1
            keyboard.press(Key.left)
            keyboard.release(Key.left)
    def ty_a(self,k,back=0):
        global keyboard
        global auto_text

        text = auto_text[k]['text']
        text = text.replace('\r','')
        for t in text:
            self.keyboard_typing(t)


        ii=0
        while not ii == back:
            ii+=1
            keyboard.press(Key.left)
            keyboard.release(Key.left)

    def keyboard_typing(self,t):
        global keyboard
        if t == '\n':
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif t == '\t':
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            
            # keyboard.press(Key.space)
            # keyboard.release(Key.space)
            
            # keyboard.press(Key.space)
            # keyboard.release(Key.space)
            
            # keyboard.press(Key.space)
            # keyboard.release(Key.space)
            
            # keyboard.press(Key.space)
            # keyboard.release(Key.space)

        else:
            keyboard.press(t)
            keyboard.release(t)
# class TYPE:END

class LOADER:
    def __init__(self):
        pass

    def autoText(self):
        autxt = _v.dbTables  +_v.slash+ 'AutoText.csv'
        if not os.path.isfile(autxt):
            return None
        try:
            raw = _.getText( autxt, raw=True )
        except Exception as e:
            raw = ''
        if len(raw) < 5:
            return None

        table = {}

        for line in raw.split('\n'):

            c=line.count('%<')
            line = line.replace( '%<', '' )
            if not line == ';':
                if ';' in line:
                    f=_.find_all(line,';')
                    a=line[0:f[0]]
                    b=line[f[0]+1:]
                    b = b.replace( '{#crlf#}', '\n' )
                    table[a] = {}
                    table[a]['text'] = b
                    table[a]['back'] = c

        return table

    def flip_table_test(self):
        global table
        for k in table:
            table[k]['test']=[]
            for t in table[k]['raw']:
                if t.startswith('Key.') and not ',' in t:
                    table[k]['test'].append(t)
                elif t.startswith('Key.') and ',' in t:
                    p=t.split(',')
                    n=int(p[1])
                    i=0
                    while not i == n:
                        i+=1
                        table[k]['test'].append(p[0])
                else:
                    for tt in t:
                        table[k]['test'].append(tt)
            table[k]['test'].reverse()

    def add_text(self, add,text,back,note):
        hot_text  = _.getTableDB('hotkeys-Text.dex')
        hot_text[add]={
                            'text': text,
                            'back': back,
                            'note': note,
        }
        _.saveTableDB( hot_text, 'hotkeys-Text.dex' )

    def build_table(self):
        global table
        global hot_text
        global auto_text
        for k in hot_text:
            if len(hot_text[k]['note']):
                table[hot_text[k]['note']] = { 'raw': [ k ], 'do': 'Typing.ty_h("'+k+'",back='+str(hot_text[k]['back'])+')' }
            else:
                table[k] = { 'raw': [ k ], 'do': 'Typing.ty_h("'+k+'",back='+str(hot_text[k]['back'])+')' }

        for k in auto_text:
            table[k] = { 'raw': [ k ], 'do': 'Typing.ty_a("'+k+'",back='+str(auto_text[k]['back'])+')' }
# class LOADER:END

def action():

    if _.switches.isActive('Convert-AutoText'):
        table = Loader.autoText()
        if table:
            _.saveTableDB( table, 'hotkeys-AutoText.dex' )
        return None
    if _.switches.isActive('Add-Text-Trigger'):
        add  = _.switches.value('Add-Text-Trigger')
        text = _.switches.value('Add-Text-Text')
        back = _.switches.value('Add-Text-Back')
        note = _.switches.value('Add-Text-Note')
        if len(back):
            back = int(back)
        else:
            back = 0
        if len(text) < 2:
            _paste = _.regImp( __.appReg, '-paste' )
            text = _paste.imp.paste()
        text = text.replace('\r','')
        Loader.add_text(add,text,back,note)
        return None

    load()
    print( 'EXIT:   Win + esc' )
    with Listener(on_press=Hotkeys.process_keystroke,on_release=Hotkeys.release_key) as l:
        l.join()


ctrl_chars = {
    'a': '\x01',
    'b': '\x02',
    'c': '\x03',
    'd': '\x04',
    'e': '\x05',
    'f': '\x06',
    'g': '\x07',
    'h': '\x08',
    'i': '\t',
    'j': '\n',
    'k': '\x0b',
    'l': '\x0c',
    'm': '\r',
    'n': '\x0e',
    'o': '\x0f',
    'p': '\x10',
    'q': '\x11',
    'r': '\x12',
    's': '\x13',
    't': '\x14',
    'u': '\x15',
    'v': '\x16',
    'w': '\x17',
    'x': '\x18',
    'y': '\x19',
    'z': '\x1a',
}

def cleaner(subject,deep=0):
    subject=_str.cleanBE( subject, '\n' )
    subject=_str.cleanBE( subject, '\t' )
    subject=_str.cleanBE( subject, ' ' )
    subject = subject.replace('\r','')

    subject=_str.cleanBE( subject, '\n' )
    subject=_str.cleanBE( subject, '\t' )
    subject=_str.cleanBE( subject, ' ' )
    subject=_str.cleanBE( subject, '\n' )
    subject=_str.cleanBE( subject, '\t' )
    subject=_str.cleanBE( subject, ' ' )
    if deep:
        subject=_str.replaceDuplicate( subject, ' ' )
        subject=_str.replaceDuplicate( subject, '\n' )
    return subject

def load():
    global table
    global auto_text
    global hot_text
    global log
    log = []
    table = {
                'EXIT': { 'raw': [ 'Key.esc','Key.cmd' ], 'do': 'sys.exit()' },
                'tester': { 'raw': [ 'Key.ctrl,3', 'test' ], 'do': 'print("works!!")' },
                'win-path': { 'raw': [ 'Key.ctrl,2', 'win' ], 'do': 'Clip.win_path()' },
                'mom': { 'raw': [ 'Key.ctrl,2', 'mom' ], 'do': 'Typing.ty("your_mother()",back=1)' },
                'pre-clean': { 'raw': [ 'Key.ctrl,2', 'Key.space', 'del' ], 'do': 'Clip.del_activate()' },
                'implode': { 'raw': [ 'Key.ctrl,2', 'Key.space', 'i' ], 'do': 'Clip.implode()' },
                # 'reduction_loop': { 'raw': [ 'Key.alt', 'Key.shift', 'Key.cmd', 'r' ], 'do': 'Clip.reduction_loop()' },
                'implode2': { 'raw': [ 'Key.alt', 'Key.cmd', 'i' ], 'do': 'Clip.implode()' },
                'implode3': { 'raw': [ 'Key.alt', 'Key.shift', 'i' ], 'do': 'Clip.implode3()' },
                'number': { 'raw': [ 'Key.alt', 'Key.cmd', 'n' ], 'do': 'Clip.number()' },
                'number': { 'raw': [ 'Key.shift', 'Key.alt', 'n' ], 'do': 'Clip.numberz()' },
                'number-a': { 'raw': [ 'Key.alt', 'Key.cmd', 'n', 'a' ], 'do': 'Clip.number_a()' },
                'number-b': { 'raw': [ 'Key.alt', 'Key.cmd', 'n', 'b' ], 'do': 'Clip.number_b()' },
                'number-ba': { 'raw': [ 'Key.alt', 'Key.cmd', 'n', 'b', 'a' ], 'do': 'Clip.number_ba()' },
                'explode': { 'raw': [ 'Key.ctrl,2', 'Key.space', 'x' ], 'do': 'Clip.explode()' },
                'explode2': { 'raw': [ 'Key.alt', 'Key.cmd', 'x' ], 'do': 'Clip.explode()' },
                'add-slash': { 'raw': [ 'Key.shift,2',  '\\' ], 'do': 'Clip.add_slash()' },
                'comma-to-js-dic': { 'raw': [ 'Key.ctrl,2', 'Key.space', 'dic' ], 'do': 'Clip.dic()' },
                'clip-math': { 'raw': [ 'Key.alt', 'Key.cmd', 'M' ], 'do': 'Clip.math()' },
                'prefix': { 'raw': [ 'Key.alt', 'Key.cmd', 'p' ], 'do': 'Clip.prefix()' },
                'suffix': { 'raw': [ 'Key.alt', 'Key.cmd', 's' ], 'do': 'Clip.suffix()' },
                'lower': { 'raw': [ 'Key.alt', 'Key.cmd', 'l' ], 'do': 'Clip.toLower()' },
                'upper': { 'raw': [ 'Key.alt', 'Key.cmd', 'u' ], 'do': 'Clip.toUpper()' },

                'lower': { 'raw': [ 'Key.shift', 'Key.cmd', 's', 't' ], 'do': 'Clip.toString()' },
                
                'first-word': { 'raw': [ 'Key.alt', 'Key.cmd', '1' ], 'do': 'Clip.first()' },
                'sql-crud': { 'raw': [ 'Key.alt', 'Key.cmd', 'c' ], 'do': 'Clip.SQL_to_crud()' },
                'first-php-var': { 'raw': [ 'Key.alt', 'Key.cmd', '4' ], 'do': 'Clip.php_var()' },
                # 'builder-one': { 'raw': [ 'Key.alt', 'Key.cmd', 'b' ], 'do': 'Clip.builder()' },
                'builder-two': { 'raw': [ 'Key.alt', 'Key.cmd', 'y' ], 'do': 'Clip.builder2()' },
                'range-first': { 'raw': [ 'Key.alt', 'Key.cmd', '-' ], 'do': 'Clip.range_first()' },
                'reverse-lines': { 'raw': [ 'Key.alt', 'Key.shift', 'r' ], 'do': 'Clip.reverse_lines()' },
                'reverse-lines': { 'raw': [ 'Key.alt', 'Key.cmd', 'd' ], 'do': 'Clip.combine_make()' },

                'toggle-chars': { 'raw': [ 'Key.alt', 'Key.cmd', 't', 'c' ], 'do': 'toggle_chars()' },

    }
    auto_text = _.getTableDB('hotkeys-AutoText.dex')
    hot_text  = _.getTableDB('hotkeys-Text.dex')
    Loader.build_table()
    Loader.flip_table_test()
    # _.pv(table)

def toggle_chars():
    global print_chars
    if print_chars:
        print_chars = False
    else:
        print_chars = True

Hotkeys=HOTKEYS()
Typing=TYPING()
Loader=LOADER()
Clip=CLIP()
beepy=BEEPS()
key_set = set()
post_do = { 'status': 0 }
print_chars = False

########################################################################################
if __name__ == '__main__':
    action()
    __.isExit()




