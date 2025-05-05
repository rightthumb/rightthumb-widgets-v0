





import shutil
import os

def remove_folder_recursive(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and all its contents have been removed.")
    else:
        print(f"Folder '{folder_path}' does not exist.")




























class Meta_Namespace:
    def __init__(self):
        pass

π = Meta_Namespace()
π.π = Meta_Namespace()
π.e = Meta_Namespace()
ππ = Meta_Namespace()
π.p = Meta_Namespace()
π.p.db = Meta_Namespace()
π.db = Meta_Namespace()
π.l = Meta_Namespace()

import os

π.p.home = os.path.expanduser('~/.eco'.replace('/', os.sep)) + os.sep
if not os.path.exists(π.p.home):
    os.mkdir(π.p.home)

if os.name == 'nt':
    π.p.app = "C:/ProgramData/eco".replace('/', os.sep)
else:
    π.p.app = "/opt/eco"
os.makedirs(π.p.app, exist_ok=True)

π.p.db.cli = os.path.join(π.p.app, "eco.db")
π.p.db.private = os.path.join(π.p.app, "private.db")

def ensure_db():
    if not os.path.exists(π.p.db.cli):
        import urllib.request
        try:
            urllib.request.urlretrieve("https://ecocli.xyz/eco.db", π.p.db.cli)
        except Exception as e:
            print(f"[EcoCLI] ❌ {e}")

ensure_db()

import sqlite3

def loader(db, table='py', cond={'usage': 'ecocli'}):
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
    for r in res:
        d = dict(zip(cols, r))
        code = d.get('content', '').strip()
        name = d.get('name', '').strip()
        print(name)
        if not code:
            continue
        lines = []
        for line in code.split('\n'):
            if line.startswith('import ') or line.startswith('from '):
                if line not in imports:
                    imports.append(line)
            else:
                lines.append(line)
        code = '\n'.join(lines)
        try:
            exec(code, globals(), locals())
            for line in code.split('\n'):
                if '=' in line and 'π.e.' in line:
                    key = line.split('=')[0].strip()
                    out[key.replace('π', 'pi')] = str(eval(key)).split(' ')[0].replace('<', '')
        except Exception as e:
            print(f"[EcoCLI] ⚠️ {name} Error loading {key}: {e}")
    return out, imports



π.l.collables, imports = loader(π.p.db.cli, 'py', {'usage': 'ecocli'})

for imp in imports:
    # if not 'nt' == os.name and 'readline' in imp:
    #     continue

    exec(imp)  # GLOBAL

π.db.cli = π.e.sqliteMgr(π.p.db.cli)
# π.db.cli.delete('py', {'name': 'SwitchManager'})






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
    if os.path.exists(π.p.db.cli):
        os.remove(π.p.db.cli)
    ensure_db()
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