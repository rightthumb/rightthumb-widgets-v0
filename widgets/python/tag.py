import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

# app_navigator: switches
def sw():
    _.switches.register( 'Search', '-ss,-search', group=[1,'Search'] )

    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', group=[2,'Files and Folders'] )
    _.switches.register( 'Folders', '-fo,-folder,-folders', group=[2] )

    _.switches.register( 'Tags', '-t,-tag,-tags', 'tag1 tag2 tag3', group=[3,'Add Records'] )
    _.switches.register( 'Note', '-n,-note', 'hello world', isData='raw', group=[3] )
    _.switches.register( 'Subject', '-sub,-subject', 'function fnName | _ this all goes under general', group=[3] )
    _.switches.register( 'RelatedFiles', '-r,-rel,-related', 'subject.txt related1.txt r2.txt r3.txt', group=[3] )
    _.switches.register( 'Trigger', '-tr,-trigger', 'expires 1w', group=[3] )

    _.switches.register( 'Rename', '-rename', 'file1.txt file2.txt | tag1 tag2 | folder1 folder2', group=[4,'Modify Records'] ) # renames file or folder or tag 
    _.switches.register( 'Delete', '-del,-delete', group=[4] ) # dumps files or folders data with numbers and can choose multiple
    _.switches.register( 'Recover', '-recover', group=[4] ) # dumps transactions with numbers and can choose multiple

    _.switches.register( 'Dump', '-d,-dump', group=[5,'Utilities'] )
    _.switches.register( 'InitializeDatabase', '-i,-initialize', group=[5] )
    _.switches.register( 'Clean', '--c', group=[5] )


_._default_settings_()

_.appInfo[focus()] = {
    'file': 'tag.py',
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p tag -file file.txt '),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
    ],
    'aliases': [],
    'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
    _._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

# structure = {
# 	'folders': {
# 		'/opt/rightthumb-widgets-v0/widgets/python': {
# 			'tags': ['programming','py','python'],
# 			'notes': [{'epoch': 1727293603, 'note': 'hello world', 'subject': {'function': 'fnName'}},],
# 		},
# 	},
# 	'files': {
# 		'/opt/rightthumb-widgets-v0/widgets/python/files.py': {
# 			'tags': ['os','files','research'],
# 			'notes': [{'epoch': 1727293603, 'note': 'hello world', 'subject': {'function': 'fnName'}},],
# 		},
# 	},
# 	'tags': {
# 		'os': [
# 			'/opt/rightthumb-widgets-v0/widgets/python/files.py',
# 		],
# 	},
# 	'transactions': [{},],
# }


# structure = {}
# def action():
# 	global structure


# def load():
# 	global structure
# 	if not 'files' in structure:
# 		structure['folders'] = {}
# 		structure['files'] = {}
# 		structure['tags'] = {}
# 		structure['transactions'] = []

# '''
# Framework notes:

# 	Switches used:
# 		_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt' )
# 		_.switches.register( 'Folders', '-fo,-folder,-folders' )

# 		_.switches.register( 'Tags', '-t,-tag,-tags', 'tag1 tag2 tag3' )

# 		_.switches.register( 'Note', '-n,-note', 'hello world', isData='raw' )
# 		_.switches.register( 'Subject', '-sub,-subject', 'function fnName' )

# 		_.switches.register( 'Rename', '-r,-rename', 'file1.txt file2.txt | tag1 tag2 | folder1 folder2' ) # renames file or folder or tag 
# 		_.switches.register( 'Delete', '-del,-delete' ) # dumps files or folders data with numbers and can choose multiple
# 		_.switches.register( 'Recover', '-r,-recover' ) # dumps transactions with numbers and can choose multiple

# 	How switches work:
# 		if _.switches.isActive('Tags'):
        
# 		Data types:
# 			_.switches.value('Tags') = 'tag1,tag2,tag3'
# 			_.switches.values('Tags') = ['tag1','tag2','tag3']

# 	Note switch:
# 		if len(_.switches.value('Tags')):
# 			note = ' '.join( _.switches.values('Tags') )
# 		else:
# 			note = ' '.join( _.isData() )
    
# 	Subject switch:
# 		subject is used with the Note switch
# 		if _.switches.isActive('Subject') and len(_.switches.values('Subject')) > 0:
# 			if len(_.switches.values('Subject')) > 1:
# 				key = '_'
# 				value = _.switches.value('Subject')
# 			else:
# 				key = _.switches.values('Subject')[0]
# 				values = []
# 				for i, data in enumerate( _.isData(_.switches.values('Subject')) ):
# 					if i:
# 						values.append( data )
# 				value = ' '.join( values )
            
# '''
########################################################################################

import os
import json
import time

# This will store the structure of folders, files, tags, and transactions
structure = {}




def save_structure():
    _.saveTable(structure,'tag.json',p=0)
    if not _.switches.isActive('Clean'):
        _.pr('Structure saved.',c='darkcyan')
    # Save structure to a file (for persistent state)
    # with open('structure.json', 'w') as f:
    # 	json.dump(structure, f)

def load_structure():
    global structure
    # # Load structure from file
    # if os.path.exists('structure.json'):
    # 	with open('structure.json', 'r') as f:
    # 		structure = json.load(f)
    # else:
    # 	load()  # If the file doesn't exist, initialize the structure








# app_navigator: create

def create_folder(path):
    if not os.path.isdir(path): return
    if path not in structure['folders']:
        structure['folders'][path] = {'tags': [], 'notes': [],'related':[]}
        log_transaction('create_folder', {'path': path})
        _.pr(f"Folder created: {path}",c='green')
    else:
        _.pr(f"Folder already exists: {path}",c='green')

def create_file(path):
    if not os.path.isfile(path): return
    if path not in structure['files']:
        structure['files'][path] = {'tags': [], 'notes': [],'related':[]}
        log_transaction('create_file', {'path': path})
        if not _.switches.isActive('Clean'):
            _.pr(f"File created: {path}",c='green')
    else:
        if not _.switches.isActive('Clean'):
            _.pr(f"File already exists: {path}",c='green')

def rename_item(old_path, new_path, item_type='file'):
    key = item_type + 's'

    # Check if item type is valid (file, folder, or tag)
    if item_type in ['file', 'folder']:
        if old_path in structure[key]:
            # Renaming file or folder
            structure[key][new_path] = structure[key].pop(old_path)
            _.pr(f"{item_type.capitalize()} renamed from {old_path} to {new_path}",c='green')
        else:
            _.pr(f"{item_type.capitalize()} does not exist: {old_path}",c='green')

    elif item_type == 'tag':
        # Renaming a tag, affecting files and folders
        if old_path in structure['tags']:
            structure['tags'][new_path] = structure['tags'].pop(old_path)
            # Update the tag in files
            for file_path, file_data in structure['files'].items():
                if old_path in file_data['tags']:
                    file_data['tags'].remove(old_path)
                    file_data['tags'].append(new_path)
            # Update the tag in folders
            for folder_path, folder_data in structure['folders'].items():
                if old_path in folder_data['tags']:
                    folder_data['tags'].remove(old_path)
                    folder_data['tags'].append(new_path)
            _.pr(f"Tag renamed from {old_path} to {new_path}",c='green')
        else:
            _.pr(f"Tag does not exist: {old_path}",c='green')

    else:
        _.pr(f"Unknown item type: {item_type}",c='green')
        return False

    # Log the transaction
    log_transaction('rename_' + item_type, {'old': old_path, 'new': new_path})




def delete_item(path, item_type='file'):
    key = item_type+'s'
    if item_type == key and path in structure[key]:
        log_transaction('delete_'+item_type, path)
        del structure[key][path]
        _.pr(f"File deleted: {path}",c='green')
    else:
        _.pr(f"{item_type.capitalize()} does not exist: {path}",c='green')

def log_transaction(action, record):
    timestamp = int(time.time())
    rec = {'epoch': timestamp, 'action': action, 'record': record}
    structure['transactions'].append(rec)

def recover_transaction():
    global structure

    # Iterate over the recorded transactions with enumeration
    for i, rec in enumerate(structure['transactions']):
        if 'add_tag' in rec['action']:
            continue
        _.pr(i, rec,c='cyan')

    try:
        selection = int(input('Selection: '))
        record = structure['transactions'][selection]
        action = record['action']

        # Check if Files switch is active
        if _.switches.isActive('Files'):
            if action == 'create_file':
                create_file(record['record']['path'])
            elif action == 'rename_file':
                rename_item(record['record']['old'], record['record']['new'], item_type='file')
            elif action == 'delete_file':
                delete_item(record['record'], item_type='file')
            elif action == 'add_tag':
                add_tag(record['record']['path'], record['record']['tag'], item_type='file')
            elif action == 'remove_tag':
                remove_tag(record['record']['path'], record['record']['tag'], item_type='file')
            elif action == 'add_note':
                add_note(record['record']['path'], record['record']['note'], item_type='file')
            elif action == 'remove_note':
                remove_note(record['record']['path'], record['record']['note'], item_type='file')

        # Check if Folders switch is active
        if _.switches.isActive('Folders'):
            if action == 'create_folder':
                create_folder(record['record']['path'])
            elif action == 'rename_folder':
                rename_item(record['record']['old'], record['record']['new'], item_type='folder')
            elif action == 'delete_folder':
                delete_item(record['record'], item_type='folder')
            elif action == 'add_tag':
                add_tag(record['record']['path'], record['record']['tag'], item_type='folder')
            elif action == 'remove_tag':
                remove_tag(record['record']['path'], record['record']['tag'], item_type='folder')

        # Check if Tags switch is active
        if _.switches.isActive('Tags'):
            if action == 'rename_tag':
                rename_item(record['record']['old'], record['record']['new'], item_type='tag')

    except Exception as e:
        _.pr(f'Error processing transaction: {e}', c='red')








# app_navigator: process

def add_tag(path, tag, item_type='file'):
    global structure
    key = item_type+'s'
    if not path in structure[key]: structure[key][path] = {'tags': [], 'notes': [],'related':[]}
    if not tag in structure[key][path]['tags']: structure[key][path]['tags'].append(tag)
    if not tag in structure['tags'][key]: structure['tags'][key][tag] = []
    structure['tags'][key][tag].append(path)
    log_transaction('add_tag', path)
    _.pr(f"Tag '{tag}' added to {item_type}: {path}",c='green')

def remove_tag(path, tag, item_type='file'):
    global structure
    if item_type == 'file' and path in structure['files'] and tag in structure['files'][path]['tags']:
        structure['files'][path]['tags'].remove(tag)
    elif item_type == 'folder' and path in structure['folders'] and tag in structure['folders'][path]['tags']:
        structure['folders'][path]['tags'].remove(tag)
    if tag in structure['tags']:
        structure['tags'][tag].remove(path)
        if not structure['tags'][tag]:
            del structure['tags'][tag]
    log_transaction('remove_tag', path)
    _.pr(f"Tag '{tag}' removed from {item_type}: {path}",c='green')

def related_files():
    global structure
    if len(_.switches.values('Files')) == 1:
        subject = _.switches.values('Files')[0]
        files = _.isData()
        if subject in files: files.remove(subject)
        subject = os.path.abspath(subject)
        _.pr(f"Subject: {subject}",c='green')
        for i,file in enumerate(files):
            files[i] = os.path.abspath(file)
            _.pr(f"Related file added: {files[i]}",c='green')
    else:
        files = _.switches.values('Files')
        for i,file in enumerate(files): files[i] = os.path.abspath(file)
        subject = files.pop(0)
    if not subject in structure['related']: structure['related'][subject] = []
    for file in files:
        if not file in structure['related'][subject]:
            structure['related'][subject].append(file)
    if subject not in structure['files']: structure['files'][subject] = {'tags': [], 'notes': [],'related':[]}
    structure['files'][subject]['related'].append({'subject':  ' '.join(_.switches.values('Subject'))  ,'file':files})
    _.pr(f"Related file added: {file}",c='green')
    log_transaction('related_files', subject)



def add_trigger(path, item_type='file'):
    global structure
    global trigger
    test = 0
    # test += 1; print('trigger',test)
    key = item_type+'s'
    key2 = item_type+'s'

    if os.path.isfile(path):
        key = 'files'
    elif os.path.isdir(path):
        key = 'folders'
    else:
        _.pr('Invalid path',c='red')
        return
    
    config = _.switches.values('Trigger')
    subject = config.pop(0)
    # config = ' '.join( config )
    # print('config',config)
    continuity = {
        'expir':'expires',
        'save':'onSave',
    }

    for k in continuity:
        if k in subject:
            subject = continuity[k]

    deleted = False
    wasDeleted = False
    deleted = _.switches.isActive('Delete')
    # test += 1; print('trigger',test)
    if _.switches.isActive('Delete'):
        # print('delete')
        try:
            del structure['triggers'][key][path][subject]
            pp = path.split(os.sep)
            pp.pop()
            path2 = os.sep.join(pp)
            structure['triggers']['fileFolders'][path2][path] = structure['triggers'][key][path]
            if not structure['triggers'][key][path]:
                del structure['triggers'][key][path]
            if not structure['triggers']['fileFolders'][path2][path]:
                del structure['triggers']['fileFolders'][path2][path]
            for file in structure['triggers']['fileFolders'][path2]:
                if not structure['triggers']['fileFolders'][path2]:
                    del structure['triggers']['fileFolders'][path2][file]
            for folder in structure['triggers']['fileFolders']:
                if not structure['triggers']['fileFolders'][folder]:
                    del structure['triggers']['fileFolders'][folder]
            log_transaction('remove_trigger', path)
        except Exception as e:
            pass
            # _.pr(f"Trigger did not exist: {path} : {e}",c='red')
        return

    # test += 1; print('trigger',test)
    if config[0] == '_': deleted = True
    if not path in structure['triggers'][key]: structure['triggers'][key][path] = {}
    structure['triggers'][key][path][subject] = {}
    if subject in structure['triggers'][key][path]:
        if config[0] == '_':
            del structure['triggers'][key][path][subject]
            _.pr(f"Trigger deleted: {path}",c='red')
        else:
            if not _.switches.isActive('Clean'):
                _.pr(f"Trigger updated: {path}",c='yellow')
    else:
        if not deleted:
            if not _.switches.isActive('Clean'):
                _.pr(f"Trigger added: {path}",c='green')
        else:
            wasDeleted = True
            _.pr(f"Trigger did not exist: {path}",c='red')
    if not deleted:
        structure['triggers'][key][path][subject] = config
        log_transaction('add_trigger', path)
    else:
        if path in structure['triggers'][key]:
            if not structure['triggers'][key][path]: del structure['triggers'][key][path]
        if not wasDeleted:
            log_transaction('remove_trigger', path)

    if key == 'files':
        key = 'fileFolders'
        path2 = path
        wasDeleted = False

        path = os.path.dirname(path2)
        if not path in structure['triggers'][key]: structure['triggers'][key][path] = {}
        structure['triggers'][key][path][path2] = structure['triggers']['files'][path2]
        log_transaction('add_trigger', path)




def add_note(path, note, subject=None, item_type='file'):
    key = 'NA'
    value = 'NA'
    if _.switches.isActive('Subject') and len(_.switches.values('Subject')) > 0:
        if _.switches.values('Subject')[0] == '.':
            key = '_'
            values = []
            for i, data in enumerate( _.isData(_.switches.values('Subject')) ):
                if i:
                    values.append( data )
            value = ' '.join( values )
        else:
            values = _.switches.values('Subject')
            key = values.pop(0)
            if values[0] == '.':
                key = '_'
            value = ' '.join( values )

    note_entry = {'epoch': int(time.time()), 'note': note, 'subject': {key: value}}
    if subject:
        note_entry['subject'] = subject
    if item_type == 'file' and path in structure['files']:
        structure['files'][path]['notes'].append(note_entry)
    elif item_type == 'folder' and path in structure['folders']:
        structure['folders'][path]['notes'].append(note_entry)
    log_transaction('add_note', path)
    _.pr(f"Note added to {item_type}: {path}",c='green')

def remove_note(path, note, item_type='file'):
    if item_type == 'file' and path in structure['files']:
        notes = structure['files'][path]['notes']
        for n in notes:
            if n['note'] == note:
                notes.remove(n)
                log_transaction('remove_note', path)
                _.pr(f"Note removed from {item_type}: {path}",c='green')
                return
    elif item_type == 'folder' and path in structure['folders']:
        notes = structure['folders'][path]['notes']
        for n in notes:
            if n['note'] == note:
                notes.remove(n)
                log_transaction('remove_note', path)
                _.pr(f"Note removed from {item_type}: {path}",c='green')
                return
    _.pr(f"Note not found in {item_type}: {path}",c='green')















def action(switches=None):
    if not switches is None:
        appReg=__.appReg
        __.appReg=focus()
        for switch in switches:
            _.switches.fieldSet(switch,'active',True)
            if switches[switch]:
                _.switches.fieldSet(switch,'value',switches[switch])
                _.switches.fieldSet(switch,'values',switches[switch].split(','))


    load()
    subF = []
    fiFo = ''
    do = ''


    # app_navigator: routing
    if _.switches.isActive('Recover'):
        recover_transaction()
        return
    if _.switches.isActive('RelatedFiles'):
        if not _.switches.isActive('Files') or len(_.switches.values('Files')) < 0:
            _.pr('Need at least two files',c='red')
        if not _.switches.isActive('Subject'):
            _.switches.fieldSet('Subject','active',True)
            _.switches.fieldSet('Subject','values',['_'])
        related_files()

    if _.switches.isActive('Files') and not _.switches.isActive('RelatedFiles'):
        fiFo = 'file'
        if not len(_.switches.values('Files')):
            file_paths = _.isData()
        else:
            file_paths = _.switches.values('Files')
        
        for path in file_paths:
            path = __.path(path)
            create_file(os.path.abspath(path))
            subF.append(os.path.abspath(path))
    
    if _.switches.isActive('Folders'):
        fiFo = 'folder'
        folder_paths = _.switches.values('Folders')
        for path in folder_paths:
            path = __.path(path)
            create_folder(os.path.abspath(path))
            subF.append(os.path.abspath(path))

    if _.switches.isActive('Trigger'):
        do = 'trigger'
        tags = _.switches.values('Tags')
        if _.switches.isActive('Files'):
            if not len(_.switches.values('Files')):
                file_paths = _.isData()
            else:
                file_paths = _.switches.values('Files')
            for path in file_paths: add_trigger(os.path.abspath(path), fiFo)
        elif _.switches.isActive('Folders'):
            if not len(_.switches.values('Folders')):
                file_paths = _.isData()
            else:
                file_paths = _.switches.values('Folders')
            for path in file_paths: add_trigger(os.path.abspath(path), fiFo)
        else:
            for sub in subF: add_trigger(os.path.abspath(path), fiFo)

    if _.switches.isActive('Tags'):
        do = 'tag'
        tags = _.switches.values('Tags')
        for tag in tags:
            if _.switches.isActive('Files'):
                if not len(_.switches.values('Files')):
                    file_paths = _.isData()
                else:
                    file_paths = _.switches.values('Files')
                for path in file_paths: add_tag(os.path.abspath(path), tag, fiFo)
            elif _.switches.isActive('Folders'):
                if not len(_.switches.values('Folders')):
                    file_paths = _.isData()
                else:
                    file_paths = _.switches.values('Folders')
                for path in file_paths: add_tag(os.path.abspath(path), tag, fiFo)
            else:
                for sub in subF: add_tag(os.path.abspath(path), tag, fiFo)

    if _.switches.isActive('Note'):
        do = 'note'
        if len(_.switches.value('Note')):
            note = ' '.join( _.switches.values('Note') )
        else:
            note = ' '.join( _.isData() )
        for sub in subF: add_note(os.path.abspath(path), note)

    if _.switches.isActive('Rename'):
        old_path, new_path = _.switches.values('Rename')
        rename_item(old_path, new_path, item_type=do)

    if _.switches.isActive('Delete'):
        file_paths = _.switches.values('Delete')
        for path in file_paths:
            delete_item(os.path.abspath(path))
    
    if _.switches.isActive('Recover'):
        recover_transaction()
    
    # Save the state of the structure after actions
    save_structure()





# app_navigator: load
def load():
    global structure
    global trigger
    trigger = _.switches.values('Trigger')
    structure = _.getTable('tag.json')
    # Check if structure is not loaded or is empty
    if not structure or _.switches.isActive('InitializeDatabase'):
        # Initialize structure with necessary keys if it's not loaded or if we're initializing
        structure = {
            'folders': {},
            'files': {},
            'related': {},
            'tags': {'files': {}, 'folders': {}},
            'triggers': {'files': {}, 'folders': {}, 'fileFolders': {}},
            'transactions': []
        }
    if not _.switches.isActive('Clean'):
        _.pr("Structure loaded or initialized.", c='darkcyan')




# def load():
# 	global structure
# 	structure = _.getTable('tag.json')
# 	# Check if the structure exists, initialize if not
# 	# if not 'files' in structure:
# 	#     structure['folders'] = {}
# 	#     structure['files'] = {}
# 	#     structure['tags'] = {}
# 	#     structure['transactions'] = []
# 	if _.switches.isActive('InitializeDatabase'):
# 		structure = {}

# 	if structure:
# 		structure= {}
# 		structure['folders'] = {}
# 		structure['folders'] = {}
# 		structure['files'] = {}
# 		structure['related'] = {}
# 		structure['tags'] = {}
# 		structure['transactions'] = []
# 	_.pr("Structure loaded or initialized.",c='darkcyan')







########################################################################################
import os
########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__);