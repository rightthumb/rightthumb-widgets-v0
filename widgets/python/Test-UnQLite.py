import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'thisApp.py',
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p thisApp -file file.txt'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
    ],
    'aliases': [],
    'relatedapps': [],
    'prerequisite': [],
    'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
    _._default_triggers_()
    _.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
    _.switches.trigger( 'DB', _.aliasesFi )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start




import json
from datetime import datetime
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'db')))
from UnQLiteMgr import UnQLiteMgr

import os
if os.path.exists('test.db'):
    if input('del test.db? (y/n)') == 'y':
        os.remove('test.db')

mgr = UnQLiteMgr('test.db')

apps = mgr.db.collection('apps')
if apps.exists():
    apps.delete_all()
else:
    apps.create()

# INSERT
insert_data = {
    'id': 'com.example.notes.2',
    'name': 'Notes App',
    'permissions': {
        'admin': False,
        'roles': []
    },
    'metadata': {
        'created': datetime.utcnow(),
        'tags': ['notes', 'productivity']
    }
}
print(f'\ninsert(table="apps", records=[{insert_data}])')
mgr.insert('apps', [insert_data])

print(json.dumps(mgr.dump(), indent=4));input(':')

# INSERT CHILD
child_data = {'name': 'tester', 'level': 3}
print(f'\ninsertChild(table="apps", parent_condition={{"id": "com.example.notes.2"}}, child_field="permissions.roles", child_data={child_data})')
mgr.insertChild(
    table='apps',
    parent_condition={'id': 'com.example.notes.2'},
    child_field='permissions.roles',
    child_data=child_data
)

print(json.dumps(mgr.dump(), indent=4));input(':')


# INSERT MULTIPLE CHILDREN
child_list = [{'name': 'qa', 'level': 2}, {'name': 'intern', 'level': 0}]
print(f'\ninsertRecordsChild(table="apps", parent_condition={{"id": "com.example.notes.2"}}, child_field="permissions.roles", child_records={child_list})')
mgr.insertRecordsChild(
    table='apps',
    parent_condition={'id': 'com.example.notes.2'},
    child_field='permissions.roles',
    child_records=child_list
)

print(json.dumps(mgr.dump(), indent=4));input(':')


# UPDATE NESTED FIELD
updated_time = datetime.utcnow().isoformat()
print(f'\nupdate_nested_field_lists(table="apps", conditions={{"id": "com.example.notes.2"}}, field_path="metadata.last_updated", value="{updated_time}")')
mgr.update_nested_field_lists(
    table='apps',
    conditions={'id': 'com.example.notes.2'},
    field_path='metadata.last_updated',
    value=updated_time
)

print(json.dumps(mgr.dump(), indent=4));input(':')


# GET NESTED FIELD
print(f'\nget_nested_field_lists(table="apps", conditions={{"id": "com.example.notes.2"}}, field_path="permissions.roles.{{name:~test}}")')
tester = mgr.get_nested_field_lists(
    table='apps',
    conditions={'id': 'com.example.notes.2'},
    field_path='permissions.roles.{name:~test}'
)
print('[GET TESTER ROLE]')
print(json.dumps(tester, indent=2))

print(json.dumps(mgr.dump(), indent=4));input(':')


# DELETE NESTED FIELD
if False:
    print(f'\ndelete_nested_field_lists(table="apps", conditions={{"id": "com.example.notes.2"}}, field_path="metadata.tags")')
    mgr.delete_nested_field_lists(
        table='apps',
        conditions={'id': 'com.example.notes.2'},
        field_path='metadata.tags'
    )
    print(json.dumps(mgr.dump(), indent=4));input(':')


# INDEX REGISTRATION
index_label = 'Field,Names:com.example.*.notes'
index_key = '/roles-|-|-|-2025-05-22'
index_value = 2
print(f'\nindex_list_add(label="{index_label}", concat_path="{index_key}", list_index={index_value})')
mgr.index_list_add(
    label=index_label,
    concat_path=index_key,
    list_index=index_value
)

print(json.dumps(mgr.dump(), indent=4));input(':')


# PRINT INDEXES
print('\n[INDEXES]')
print(json.dumps(mgr.index_list_all(), indent=4))

# FINAL DUMP
print('\n[DATABASE DUMP]')
print(json.dumps(mgr.dump(), indent=4))


"""
import os
import json
from datetime import datetime
from library.tools.db.UnQLiteMgr import UnQLiteMgr

# Optional: Reset DB for testing
if os.path.exists('test.db'):
    os.remove('test.db')

# Initialize DB
mgr = UnQLiteMgr('test.db')

# Insert main record
mgr.insert('apps', [{
    'id': 'com.example.notes',
    'name': 'Notes App',
    'permissions': {
        'admin': False,
        'roles': []
    },
    'metadata': {
        'created': datetime.utcnow(),
        'tags': ['notes', 'productivity']
    }
}])

# Insert a child record (single)
mgr.insertChild(
    'apps',
    {'id': 'com.example.notes'},
    'permissions.roles',
    {'name': 'admin', 'level': 10}
)

# Insert multiple children
mgr.insertRecordsChild(
    'apps',
    {'id': 'com.example.notes'},
    'permissions.roles',
    [
        {'name': 'editor', 'level': 5},
        {'name': 'viewer', 'level': 1}
    ]
)

# Update a child
mgr.updateChild(
    'apps',
    {'id': 'com.example.notes'},
    'permissions.roles',
    {'name': 'viewer'},
    {'level': 2}
)

# Delete a child
mgr.deleteChild(
    'apps',
    {'id': 'com.example.notes'},
    'permissions.roles',
    {'name': 'editor'}
)

# Update nested field
mgr.update_nested_field_lists(
    'apps',
    {'id': 'com.example.notes'},
    'metadata.last_modified',
    datetime.utcnow().isoformat()
)

# Get nested field
last_mod = mgr.get_nested_field_lists(
    'apps',
    {'id': 'com.example.notes'},
    'metadata.last_modified'
)
print(f'Last Modified: {last_mod}')

# Delete nested field
mgr.delete_nested_field(
    'apps',
    {'id': 'com.example.notes'},
    'metadata.last_modified'
)

# Find operations
record = mgr.findOne('apps', {'id': 'com.example.notes'})
print(f'\nFound Record:\n{json.dumps(record, indent=4, default=str)}')

roles = mgr.findChild('apps', {'id': 'com.example.notes'}, 'permissions.roles')
print(f'\nRoles:\n{json.dumps(roles, indent=4, default=str)}')

# Dump all collections
dump = mgr.dump()
print(f'\nDumped DB:\n{json.dumps(dump, indent=4, default=str)}')

# Indexing tests
mgr.index_list_add('apps_roles', 'apps.permissions.roles', [0, 1])
print('\nIndex List Get:', mgr.index_list_get('apps_roles'))

mgr.index_list_del('apps_roles')
print('\nIndex List All:', mgr.index_list_all())

# Close
mgr.close()

# Log printout
print("\n--- Logs ---")
for log in mgr.logs:
    print(log)

"""



"""
p unq
use test.db
Switched to test
export test.json
Exported to test.json
exit
cat test.json

"""


def action():
    pass

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)