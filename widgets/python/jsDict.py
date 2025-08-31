import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
    _.switches.register( 'Save', '-save', 'file.js', resolve=1)
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

# works with this js
'''

fn = {
    js: (namespace = null, path = '', seen = new WeakSet()) => { //fn

        if (namespace === null) namespace = window;

        if (typeof namespace === 'string') {
            path = namespace;
            try {
                namespace = eval(namespace);
            } catch (e) {
                return { [path]: `Invalid namespace string: ${e.message}` };
            }
        }

        function extractData(obj, currentPath = '', seen = new WeakSet()) {
            if (typeof obj !== 'object' && typeof obj !== 'function') {
                return { [currentPath || '<root>']: `Invalid root: ${String(obj)}` };
            }

            if (seen.has(obj)) {
                return { [currentPath || '<root>']: 'Circular reference' };
            }

            seen.add(obj);

            const result = {};

            for (const key in obj) {
                if (!Object.prototype.hasOwnProperty.call(obj, key)) continue;

                const value = obj[key];
                const fullPath = currentPath ? `${currentPath}.${key}` : key;

                try {
                    if (typeof value === 'function') {
                        result[fullPath] = value.toString();
                    } else if (typeof value === 'object' && value !== null) {
                        // Attempt to JSON stringify
                        try {
                            JSON.stringify(value); // test if serializable
                            result[fullPath] = JSON.stringify(value);
                        } catch {
                            result[fullPath] = '[Unserializable Object]';
                        }
                        Object.assign(result, extractData(value, fullPath, seen));
                    } else {
                        result[fullPath] = JSON.stringify(value);
                    }
                } catch (err) {
                    result[fullPath] = `[Error accessing: ${err.message}]`;
                }
            }

            return result;
        }

        const result = extractData(namespace, path, seen);
        if (window.ScrapeBlade?.copy) window.ScrapeBlade.copy(result);
        return result;
    },
};

'''


import json

def convert_json_to_js_code(data: dict) -> str:
    js_lines = []

    for full_path, value in data.items():
        parts = full_path.split('.')
        current_path = ''

        # Generate nested object path if needed
        for i, part in enumerate(parts[:-1]):
            current_path = '.'.join(parts[:i+1])
            js_lines.append(f"{current_path} = {current_path} || {{}};")

        final_key = parts[-1]
        full_key = '.'.join(parts)

        if isinstance(value, str):
            val = value.strip()

            # Restore function if it starts with 'function' or arrow function
            if val.startswith('function') or val.startswith('(') or val.startswith('async'):
                js_lines.append(f"{full_key} = {val};")

            # Try to restore simple JSON values
            else:
                try:
                    parsed = json.loads(val)
                    if isinstance(parsed, str):
                        js_value = json.dumps(parsed)
                    elif parsed is None:
                        js_value = 'null'
                    else:
                        js_value = json.dumps(parsed, indent=None)
                    js_lines.append(f"{full_key} = {js_value};")
                except Exception:
                    js_lines.append(f"{full_key} = {json.dumps(val)};")
        else:
            js_lines.append(f"{full_key} = {json.dumps(value)};")

    return '\n'.join(js_lines)

import json

def action():
    print(_.switches.values('Files'))
    print(_.switches.values('Save')); return
    data = '\n'.join(_.isData(2))
    dic = json.loads(data)
    code = convert_json_to_js_code(dic)
    if _.switches.isActive('Save'):
        _.saveText(code, _.switches.value('Save'))
    else:
        _.pr(code)



########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)