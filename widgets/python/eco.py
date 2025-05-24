

import sys

# import requests; exec(requests.get('https://sds.sh/micro.py/?app=eco').text); exec(loader);
# import files
# for x in _.appInfo:
#     print(x)
#     _.pv(_.appInfo[x])

# sys.exit()



import shutil
import os

def RemoveFolder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and all its contents have been removed.")
    else:
        print(f"Folder '{folder_path}' does not exist.")






def SaveFile(content, filename, mode='w', encoding='utf-8'):
    with open(filename, mode, encoding=encoding) as file:
        file.write(content)





import importlib.util
import os

def Import(module_name, path):
    """Dynamically import a module from a path"""
    if os.path.isdir(path):
        init_file = os.path.join(path, '__init__.py')
    else:
        init_file = path
    spec = importlib.util.spec_from_file_location(module_name, init_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

















class MetaNamespace:
    def __init__(self):
        pass

ππ = MetaNamespace()
ππ.p = MetaNamespace()
ππ.p.db = MetaNamespace()

if os.name == 'nt':
    ππ.p.app = "C:/ProgramData/eco".replace('/', os.sep)
else:
    ππ.p.app = "/opt/eco"
os.makedirs(ππ.p.app, exist_ok=True)

ππ.p.eco = os.path.join(ππ.p.app, "eco")
ππ.p.py = os.path.join(ππ.p.eco, "py")
ππ.p.apps = os.path.join(ππ.p.eco, "apps")+os.sep
ππ.p.call = os.path.join(ππ.p.eco, "callable")+os.sep
ππ.p.db.cli = os.path.join(ππ.p.app, "eco.db")
ππ.p.db.private = os.path.join(ππ.p.app, "private.db")

sys.path.append(ππ.p.py)


import os

ππ.p.home = os.path.expanduser('~/.eco'.replace('/', os.sep)) + os.sep
if not os.path.exists(ππ.p.home):
    os.mkdir(ππ.p.home)

if os.name == 'nt':
    ππ.p.app = "C:/ProgramData/eco".replace('/', os.sep)
else:
    ππ.p.app = "/opt/eco"
os.makedirs(ππ.p.app, exist_ok=True)


def EnsureDB():
    if not os.path.exists(ππ.p.db.cli):
        import urllib.request
        try:
            urllib.request.urlretrieve("https://ecocli.xyz/eco.db", ππ.p.db.cli)
        except Exception as e:
            print(f"[EcoCLI] ❌ {e}")

EnsureDB()

import sqlite3

def loader(db, table='py', cond={'usage': 'ecocli'}, saveTo='py'):
    folder = os.path.join(ππ.p.eco, saveTo)
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    where = 'WHERE ' + ' AND '.join(f'"{k}"=?' for k in cond) if cond else ''
    sql = f'SELECT * FROM {table} {where}'
    cursor = conn.execute(sql, tuple(cond.values()))
    res = cursor.fetchall()
    cols = [desc[0] for desc in cursor.description]
    conn.close()
    out = {}
    imports = []
    files = []
    for r in res:
        d = dict(zip(cols, r))
        name = d.get('name', '').strip()
        code = d.get('content', '').strip()
        


        file = os.path.join(folder, name)+'.py'
        file = file.replace('/', os.sep).replace('\\', os.sep).replace('.py.py', '.py')
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        if not os.path.exists(file):
            print(name)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(code)
        files.append(os.path.basename(file))
    return files



loader(ππ.p.db.cli, 'py', {'usage': 'ecocli'})
π = Import('construct',ππ.p.py)






π.cli = ππ.p.db.cli
π.apps = ππ.p.apps
π.ππ = ππ
π.Import = Import
loader(ππ.p.db.cli, 'apps', {'usage': 'general'}, saveTo='apps')
# loader(ππ.p.db.cli, 'callables', {'usage': 'general'}, saveTo='callable')

π.load()




π.π = MetaNamespace()
ππ = MetaNamespace()
π.l = MetaNamespace()
import sys




# Switch Actions
import sys
def Label(val):
    os.environ['ECO_LABEL'] = val
    print(f"[eco] 🏷️  EcoCLI session label set to '{val}'")

def Salt(val):
    os.environ['ECO_SALT'] = val
    print(f"[eco] 🧂  EcoCLI session salt set to '{val}'")

def Parent(val):
    os.environ['ECO_PARENT'] = val
    print(f"[eco] 🧂  EcoCLI session parent set to '{val}'")

switches = {
    'Save': '-save',
    'Label': '-label',
    'Salt': '-salt',
    'Parent': '-parent',
    'Update': '-update',
    'View-Modules': '-view',
}
triggers = {
    'Label': Label,
    'Salt': Salt,
    'Parent': Parent,
}
Switches = π.e.SwitchManager(0, switches, triggers)

if Switches.isActive('View-Modules'):
    fn = []
    for key in list(π.l.collables.keys()):
        t = π.l.collables[key].replace('function', 'fn').strip()
        if t == 'fn':
            fn.append(key)
        else:
            print( t+ '  ', key.replace('pi.', 'π.'))
    for key in fn:
        t = π.l.collables[key].replace('function', 'fn').strip()
        if t == 'fn':
            print( t+ '     ', key.replace('pi.', 'π.'))
    sys.exit(0)
if Switches.isActive('Update'):
    if os.path.exists(ππ.p.db.cli):
        os.remove( ππ.p.db.cli)
    EnsureDB()
    print('[eco] 🔄 EcoCLI database updated.   Exiting')
    sys.exit(0)



def action():
    π.e.TerminalProxy()

########################################################################################
if not Switches.isActive('Save'):
    if __name__ == '__main__':
        action()



subject = '''
π.e.EcoSSL=EcoSSL
'''
# π.db.cli.insert('py', [{'name': 'EcoSSL', 'usage': 'ecocli', 'content': subject}])