import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    _.switches.register('Action', '--a,-action')
    _.switches.register('Collection', '-col,-collection')
    _.switches.register('Language', '-lan,-language')
    _.switches.register('Description', '-d,-description')
    _.switches.register('Snippet', '-sn,-snippet','Blank for clipboard')
    _.switches.register('Tags', '--t,-tags')
    _.switches.register('Tag', '-t,-tag')
    _.switches.register('Text', '-txt,-text')
    _.switches.register('DB', '-db')
actions = '''
listAllTags
addSnippet -sn -lan markdown 
updateSnippet
deleteSnippet
advancedSearch
showAll
searchAll
'''.strip().split('\n')
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

import sys
if len(_.yFig('Snippets')) < 3: _.pr('Missing required configuration: api and snippet', c='red'); sys.exit(1)

import requests # type: ignore
import argparse
import json

class SnippetAPI:
    def __init__(self, base_url="https://snippet.sds.sh/api.php"):
        self.base_url = base_url

    def _request(self, action, collection, params=None, db='snippets'):
        try:
            payload = {
                'action': action,
                'collection': collection,
                'params': params or {},
                'db': db
            }
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def add_snippet(self, language, description, snippet, tags):
        tag_string = ','.join(tags)
        return self._request('addSnippet', 'documentation', {
            'language': language,
            'description': description,
            'snippet': snippet,
            'tags': tag_string
        })

    def list_tags(self):
        return self._request('listTags', 'tags')

    def search_by_tag(self, tag):
        return self._request('searchByTag', 'documentation', {'tag': tag})

    def search_by_language(self, language):
        return self._request('searchByLanguage', 'documentation', {'language': language})

    def search_description(self, text):
        return self._request('searchDescription', 'documentation', {'text': text})

    def search_all(self, text):
        return self._request('searchAll', 'documentation', {'text': text})


def print_json(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))



import requests # type: ignore
import json

# Assuming this is within your framework
def action():
    collection = 'documentation'
    if _.switches.isActive('Coll'):
        collection = _.switches.value('Collection')

    if not _.switches.isActive('Action'):
        _.pr('Missing required switches: Action', c='red')
        for action in actions:
            _.pr(f'  -action {action}', c='yellow')

        return
    
    api = _.yFig('Snippets','api')
    base_url = _.yFig('Snippets','url')
    action = _.switches.value('Action')
    params = {}
    db = _.switches.value('DB') if _.switches.isActive('DB') else 'snippets'

    if action == 'addSnippet':
        language = _.switches.value('Language')
        description = _.switches.value('Description')
        snippet = _.switches.value('Snippet')
        if not snippet: snippet = '\n'.join(_.pp())
        tags = _.switches.values('Tags')
        if not language or not snippet:
            _.pr('Missing required: --Language and --Snippet', c='red')
            return
        params = {
            'language': language,
            'description': description,
            'snippet': snippet,
            'tags': ','.join(tags)
        }

    elif action in ['searchByTag', 'searchByLanguage', 'searchDescription', 'searchAll']:
        key = {
            'searchByTag': 'tag',
            'searchByLanguage': 'language',
            'searchDescription': 'text',
            'searchAll': 'text'
        }[action]
        value = _.switches.value(key.capitalize())
        if not value:
            _.pr(f'Missing required switch: --{key.capitalize()}', c='red')
            return
        params = {key: value}

    payload = {
        'action': action,
        'collection': collection,
        'params': params,
        'db': db
    }

    payload['key'] = _.yFig('Snippets','key')
    
    try:
        response = requests.post(base_url, json=payload)
        response.raise_for_status()
        data = json.loads(response.text)
        _.pv(data)
    except Exception as e:
        _.pr({'error': str(e)}, c='red')


'''
listAllTags
addSnippet
updateSnippet
deleteSnippet
advancedSearch
showAll
searchAll


searchByTag
searchByLanguage
searchCLI
searchDescription
searchConstantinople
listTags
c
i
r
get
read
u
ui
d
update
delete
'''



########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)