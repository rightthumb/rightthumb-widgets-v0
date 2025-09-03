# ⚡ Universal Terminal Framework & Automation Suite

A **cross-platform terminal framework** with **~4,000 apps** for **Windows, Linux, macOS, and PowerShell**.  
Designed for **automation, ops, provisioning, data wrangling, and rapid development**. Everything is optimized for **CLI-first workflows**, strong **switch management**, and **intelligent tables**.

**Repo:** https://github.com/rightthumb/rightthumb-widgets-v0
## 📥 Installation (Linux, Windows, PowerShell)

```bash
# From the repo root:
cd rightthumb-widgets-v0/install
python3 installer.py -rc.d h
````

* **Linux:** After install, start a new terminal (or run `bash`) so the environment refreshes and system paths/aliases load.
* **Windows (CMD):** `rr.bat` is placed in your profile root. Type:

  ```cmd
  rr
  ```

  to reload the environment.
* **PowerShell:** After installing via CMD as above, copy:

  ```
  rightthumb-widgets-v0/widgets/powershell
  ```

  to your **PowerShell** folder in **Documents**.

### `.bashrc` handling

* The installer **adds** to `.bashrc` but **never removes** anything you had.
* All inserted blocks are wrapped **between unique ID markers** (start/end) so they can be cleanly uninstalled later.

---

## 🧭 What this is

* A **terminal framework** that unifies thousands of curated CLI utilities across **Python, Bash, and PowerShell**.
* A **switch-first** philosophy: global switches, triggers, and composition make pipelines powerful and readable.
* An **adaptive table engine**: sort, group, subtotal, aggregate, and render responsive tables (fewer columns as your terminal narrows).
* **Filesystem & aliasing convenience**: file/folder/url aliases, encryption vault, site registration, and more.
* **Server automation**: extensive **auto-install / maintenance** scripts for databases, web servers, VPN, SMB, OpenVAS, WebDAV, etc. (see the bottom of this README).

---

## 🚀 Quick Start

### Create a new Python app from template

```bash
epyi base -build appName
```

This copies from the standard template and wires the app into the framework.

### Folder & file aliasing

```bash
# Create a folder alias: cd into a folder first
m aliasName

# Create a file alias
o aliasName /path/to/file
```

### Built-in encryption manager
  
```bash
# Login to your vault
p login

# Encrypt a password from clipboard and put it back encrypted
p cryptString -clip -en

# You will be prompted for pin
```

### “Site” registration via SFTP (per-folder metadata)

Create a `.folder.meta` file in the site root (JSON or YAML). Example (YAML):

```yml
url: https://site.com
sftp:
  server: site.com
  user: usernameHere
  password: AiP5bJLu9iasMXWuKhJTaHQGYLG3GFu2iDgGj9kxl/eMZ+9pCVRmHw==
  path: /home/userName/public_html/site.com
```

Drop this into **any** folder you want to control; the registration applies at that level.

Common flows:

```bash
# Upload a file or folder to the remote path
p site -f index.php -u -f fileOrFolder

# Create remote directory first, then upload file/folder
p site -f index.php -u -f fileOrFolder -mkdir

# Jump to the remote folder (defined in .folder.meta)
p site -f index.php -r

# Download a file/folder (must exist locally—touch or mkdir first)
p site -f index.php -d -f fileOrFolder
```

> On **first usage** of any `p site` commands, the website is auto-registered.

Convenience aliases:

```bash
u.   = p site -u -f %*
u..  = p site -u -f %* -mkdir
d.   = p site -d -f %*
r    = p site -remote

# Tip: run `u.` with no args to upload the last thing you opened
```

### Open anything by alias / URL / path

```bash
p cat -f file.txt
p cat -f aliasName
p cat -f https://site.com/products/ + "#login"     # auto-detects index.* pages
p cat -f https://site.com/products/search.php + login +code
# “+code” is a universal switch to show source; searching is smart (no blind greps)
```

### Stream large files

```bash
p cat2
```

### Responsive table app

```bash
p ls
# As you resize the terminal, columns reduce intelligently (most important first).
```

### Search multiple shell scripts and view all matches

```bash
p files + *.sh -has "apt install" -print                  # first instance per file
p files + *.sh -has "apt install" | p cat + "apt install" # show every match
```

### Default editor

Set a default code editor in `$HOME/.rt/.config.hash`:

```json
{
    "code_editor": "nano"
}
```

> On Windows, this can be `notepad` or any executable you prefer.

---

## 🖨 Printing Tables

The framework includes a built-in **Printed Table** function for rendering, sorting, and formatting tabular data directly in the terminal.

### Basic Usage

```python
_.pt(table)
_.pt(table, 'name,description')
```

### Function Signature

```python
_.pt(
    table,              # list of dicts or similar tabular data
    cols=None,          # columns to include (comma-separated string or list)
    sort=None,          # sort columns (comma-separated string or list)
    responsive=None,    # True = auto-hide columns based on terminal width
    focus=None,         # focus label for the current app (e.g., '__myApp__')
    c=None, s=None, r=None, t=None,  # optional shorthand column configs
    name='default',     # table profile name
    fn=None,            # function to run on table before printing
    long=False, l=None, # long format printing options
    triggers=None, t=None, # column-level triggers (transform functions)
    unique=None, u=None,# deduplicate based on given columns
    p=True              # print to terminal (False = return modified table)
)
```

### Example: With Sorting, Responsive Layout, and Triggers

```python
_.pt(
    table,
    cols='name,date',
    sort='name,d.data',
    responsive=True,
    focus='__myApp__',
    triggers={'date': _.friendlyDate},
)
```

### Returning the Modified Table Instead of Printing

```python
sortedTableWithTriggersExecuted = _.pt(
    table,
    cols='name,date',
    sort='name,d.data',
    responsive=True,
    focus='__myApp__',
    triggers={'date': _.friendlyDate},
    p=False
)
```

> **Tip:** Set `responsive=True` to automatically hide lower-priority columns as the terminal shrinks.
> Use `triggers` to preprocess column values (e.g., formatting dates, calculating derived fields).

---

## 🧠 Advanced Switches & Aggregations

The framework’s **switch engine** supports:

* **Triggers** (conditional behavior wired to switches)
* **Global aggregates** (group/subtotal/grand totals)
* **Typed columns & transforms** (e.g., `-int MemUsage`)

Example (grouped & totals via Windows Tasklist):

```bash
tasklist | p tasklist2table - svchost + .exe %* \
  -int MemUsage -s Name MemUsage -g Name -gt MemUsage \
  -aggregate " eot?mem-total=add( int(MemUsage) )); format(eot?mem-total,?size,??kb);"
```

* `-int MemUsage` → cast values
* `-s` → sort by Name & MemUsage
* `-g Name` → group by process Name
* `-gt MemUsage` → grand total
* `-aggregate` → compute + format end-of-table totals

---

### Colors & printing helpers

```python
_.pr(line=True, c='green')                         # full-width separator
_.pr(var, var2, c='red')                           # colored text
_.pr(var, var2, h='khaki')                         # hex khaki
_.pr(var, var2, h='chartreuse,cornflower_blue')    # hex fg/bg (comma-delimited)
_.pr(var, var2, h='chartreuse,#6495ED') # hex foreground + hex background

# Explore color options
p colors                 # shows available hex colors (categorized)
p colors + blue          # search for “blue” family
```

---

## 🐍 Python App Pattern (instantiated class import)

```python
appReg = __.appReg
_bk = _.regImp(__.appReg, 'fileBackup')
_bk.switch('Silent')
_bk.switch('isPreOpen')
_bk.switch('Input', path)
bkfi = _bk.action()
__.appReg = appReg
```

This preserves the global app registry, injects switches, runs the action, and restores the registry.

---

## 🧩 Example: New App Registration (Cleaned)

Below is a cleaned, consistent `_.appInfo[focus()]` block for the **`ls`** app.
Comments are minimized; duplicates removed where possible while preserving your intent.

```python
_.appInfo[focus()] = {
    'file': 'ls.py',
    'liveAppName': __.thisApp(__file__),
    'description': 'Display information about files in a folder and subfolders',
    'categories': [
        'dir', 'file', 'folder', 'db', 'file database', 'json',
        'report', 'file report', 'tool', 'tools', 'files', 'folders',
        'meta', 'meta data', 'meta report', 'meta data report'
    ],
    'relatedapps': [],
    'prerequisite': [],
    'examples': [
        'p ls',
        'p ls -ago 1d',
        'p ls -folder %pyFolder% -r -save %i%\\py.cache',
        'p ls -cache %i%\\py.cache -ago 1d',
        'p ls -r -c ext size name md cd -g ext -s ext md',
        'p ls -ext image',
        'b pys',
        'p ls -duplicates epoch -r + dir -g | p resolveIDs -replace',
        'p ls -ago 2d -invert',
        'ls.p ago -ago 1m',
        'ls.p -ago 1m',
        'ls.d',
        'p ls -s md -aggregate "isDate(me); bog?woy?week-totals=add(bytes); format(week-totals,?size);"',
        'p ls -s md -aggregate "isDate(me); bog?month?month-totals=add(bytes); format(month-totals,?size);"',
        'b txt',
        'p ls -s md -aggregate "isDate(ce); bog?woy?week-totals=add(bytes); format(week-totals,?size);" -c week-totals | p line --c',
        'p size -print',
        'p size -print g',
        'p size -print g f',
        'p ls -c g s n -s g -g g'
    ],
    'columns': [
        {'name': 'size',            'abbreviation': 's',            'sort': 'bytes'},
        {'name': 'group',           'abbreviation': 'g',            'sort': 'bytes'},
        {'name': 'path',            'abbreviation': 'p',            'sort': ''},
        {'name': 'name',            'abbreviation': 'n',            'sort': 'path'},
        {'name': 'folder',          'abbreviation': 'f',            'sort': 'path'},
        {'name': 'relative',        'abbreviation': 'r',            'sort': 'path'},
        {'name': 'parent',          'abbreviation': 'pa,par,rent',  'sort': 'path'},
        {'name': 'bytes',           'abbreviation': 'b',            'sort': ''},
        {'name': 'md5',             'abbreviation': '5',            'sort': ''},
        {'name': 'ext',             'abbreviation': 'e',            'sort': ''},
        {'name': 'year',            'abbreviation': 'y',            'sort': 'date_modified_raw'},
        {'name': 'date_modified',   'abbreviation': 'm,md,dm',      'sort': 'date_modified_raw'},
        {'name': 'date_created',    'abbreviation': 'c,cd,dc',      'sort': 'date_created_raw'},
        {'name': 'date_accessed',   'abbreviation': 'a,ad,da',      'sort': ''},
        {'name': 'week_of_year',    'abbreviation': 'woy',          'sort': 'date_modified_raw'},
        {'name': 'ago',             'abbreviation': 'ago',          'sort': 'date_modified_raw'},
        {'name': 'day_of_the_week', 'abbreviation': 'dow',          'sort': 'date_modified_raw'},
        {'name': 'header',          'abbreviation': 'h'             'sort': ''},
    ],
    'aliases': []
}
```

---

## 📚 Python Library Highlights

Paths are under:
`rightthumb-widgets-v0/widgets/python/library/`

```text
ai\gpt\__init__.py
ai\gpt.py
ai\HuggingFace.py
code\classes\CodeAnalyzer.py
code\classes\CodeColor.py
code\classes\CodeIndexer2.py
code\classes\CodeIndexerParso.py
code\classes\CodeIndexerPygments.py
code\classes\index.py
code\classes\mdFig.py
code\functions\hexColor.py
code\functions\indexText.py
code\functions\pyClassesFunctions.py
code\functions\pyColor.py
date\When.py
db\duckdbMgr.py
db\JsonDatabase.py
db\JsonDatabase2.py
db\mongoMgr.py
db\mysqlMgr.py
db\postgresMgr.py
db\postgreSQL.py
db\sqlcipherMgr.py
db\sqliteLock.py
db\sqliteMgr.py
db\tools\StemPhraseProcessor.py
db\UnQLiteMgr.py
documentation\CollectionManager.py
find\find_photos.py
gpt-test.py
har\HarTool.py
lib.py
logs\AutoLogSecurityEngine\ThreatWeaver\dump_actions.py
logs\AutoLogSecurityEngine\ThreatWeaver\FirewallEngine.py
logs\AutoLogSecurityEngine\ThreatWeaver\LogsEngine.py
logs\AutoLogSecurityEngine\ThreatWeaver\Log_Categorizer_Engine.py
logs\AutoLogSecurityEngine\ThreatWeaver\QueryVizEngine.py
logs\AutoLogSecurityEngine\ThreatWeaver\_SQL_to_QUERY__converter.py
logs\sec_logs.py
logs\sec_logs_extended_usage.py
logs\sec_logs__firewall__log_categorizer.py
modules\os\files\refine.py
os\file\bkExpire.py
os\file\create_backup_filename.py
os\file\FileAnalyzer.py
os\file\refine.py
patterns\PatternDB.py
rules_engines\RuleKit.py
rules_engines\RuleWeaver.py
security\modules\liaison.py
security\VaultWeaver\VaultWeaver.py
tables\SafeExpr.py
tables\TableTool.py
threads\MinThread.py
url\fetch_advanced.py
```

---

## 🛠 Server, Database, and Service Scripts (Index)

Paths are under:
`rightthumb-widgets-v0/widgets/bash/srv`

### APT & Package Management

* `apt/setup.sh`
* `APT_Repository/manager.sh`

### DNS

* `dns/install.sh`
* `dns/notes.md`
* `dns/NS.sh`
* `dns/SOA.sh`

### FreePBX

* `FreePBX/install.sh`

### FTP (ProFTPD & utilities)

* `ftp/add_user.sh`
* `ftp/download.sh`
* `ftp/install-client.sh`
* `ftp/install-server.sh`
* `ftp/proftpd.conf`
* `ftp/reset_password.sh`
* `ftp/status.sh`
* `ftp/upload.sh`

### Fullstack: Back-end

* `fullstack/back-end/check-uptime.sh`
* `fullstack/back-end/clean-old-logs.sh`
* `fullstack/back-end/deploy-back-end.sh`
* `fullstack/back-end/install-redis.sh`
* `fullstack/back-end/monitor-backend.sh`
* `fullstack/back-end/setup-database-backup.sh`
* `fullstack/back-end/setup-mongo.sh`
* `fullstack/back-end/setup-nginx.sh`
* `fullstack/back-end/setup-ssl.sh`
* `fullstack/back-end/update-server.sh`

### Fullstack: Front-end

* `fullstack/front-end/bundle-assets.sh`
* `fullstack/front-end/compile-css.sh`
* `fullstack/front-end/compile-js.sh`
* `fullstack/front-end/deploy-front-end.sh`
* `fullstack/front-end/generate-js-css-config-for-compile.sh`
* `fullstack/front-end/minify-css.sh`
* `fullstack/front-end/minify-js.sh`
* `fullstack/front-end/optimize-images.sh`
* `fullstack/front-end/serve-local.sh`
* `fullstack/front-end/test-linting.sh`
* `fullstack/front-end/watch-css.sh`
* `fullstack/front-end/watch-js.sh`
* `fullstack/generate-sitemap.sh`

### GPT4All

* `gpt4all/install.sh`

### HTTP/PHP

* `http_php/http_php.sh`

### LAMP

* `lamp/0_usage.md`
* `lamp/1_lamp_install.sh`
* `lamp/2_add-domain.sh`
* `lamp/3_MySQL_phpMyAdmin.sh`
* `lamp/4_email_webmail_(RainLoop).sh`
* `lamp/4_opt_ssl.sh`
* `lamp/notes.md`
* `lamp/README.md`
* `lamp/wp__cli-install-help.sh`

### Logs

* `logs/setup_log_retention.sh`

### Mail

* `mail/install.sh`
* `mail/notes.md`

### Misc

* `MISC/sync.sh`
* `MISC/__clear_temp__cleaner__.sh`

### MongoDB

* `mongoDB/99-mongodb.conf`
* `mongoDB/install.sh`
* `mongoDB/install_mongoDB_multi_local.sh`
* `mongoDB/install_mongoDB_multi_local__for_Windows.ps1`
* `mongoDB/multi.md`
* `mongoDB/setup_db_backup.sh`
* `mongoDB/setup_mongo_replica_set.sh`
* `mongoDB/sync_mongo_to_backup.sh`

### Mount Remote Folders

* `Mount_Remote_Folders/setup__openssh-server.sh`
* `Mount_Remote_Folders/setup__sshfs.sh`

### MySQL

* `mysql/1-secure.sh`
* `mysql/add_user_to_database.sh`
* `mysql/create_database.sh`
* `mysql/create_user.sh`
* `mysql/install.sh`
* `mysql/pw.txt`

### Node.js

* `node.js/manager.sh`
* `node.js/setup.sh`

### ntfy

* `ntfy/install_ntfy.sh`
* `ntfy/_start_stop.sh`

### OpenVAS

* `OpenVAS/apt_install.sh`
* `OpenVAS/dnf_install.sh`

### PostgreSQL

* `PostgreSQL/install_PostgreSQL_multi_local.sh`
* `PostgreSQL/install_PostgreSQL_multi_local__for_Windows.ps1`
* `PostgreSQL/install_Secure_PostgreSQL.sh`
* `PostgreSQL/renew_cert.sh`
* `PostgreSQL/setup_db_backup.sh`
* `PostgreSQL/setup_pg_logical_replication.sh`
* `PostgreSQL/sync_postgres_to_backup.sh`

### RustDesk

* `RustDesk/install.sh`

### Service

* `service/manage.sh`

### SMB (Samba)

* `smb/domain_install.sh`
* `smb/install.sh`
* `smb/notes.md`
* `smb/users.md`

### SMS

* `sms/install.sh`

### Temporary HTTPS PHP Server

* `Temporary_Servers/_php-https-server__Temporary.sh`

### Virtual Machines

* `VM/documentation.md`
* `VM/install.sh`
* `VM/manage.sh`

### VPN

* `vpn/byPassword/client.sh`
* `vpn/byPassword/install.sh`
* `vpn/byPassword/login_script.sh`
* `vpn/byPassword/notes.md`
* `vpn/install.sh`
* `vpn/vpn_client.sh`

### WebDAV (core + tests)

* `webdav/1234.sh`
* `webdav/1_install.sh`
* `webdav/2_ssl_install.sh`
* `webdav/3_ssl_config.sh`
* `webdav/4_add_user.sh`
* `webdav/davfs2.conf`
* `webdav/mount.md`
* `webdav/sds.db`
* `webdav/test/add_user.sh`
* `webdav/test/install.sh`
* `webdav/test/mount.md`
* `webdav/test/ssl_config.sh`
* `webdav/test/ssl_install.sh`
* `webdav/test/users.md`

### Web Tools

* `webTools/fix_permissions.sh`

### WHM / cPanel

* `WHM/Add_Repos__apt_dnf_yum_pacman.sh`
* `WHM/install_WHM_cPanel.sh`
* `WHM/post_install_notes.md`
* `WHM/recover/clean_home__post_recover_without_full_recover_just_accounts.sh`
* `WHM/whm_tunnel.sh`

### WordPress

* `WordPress/wp_harden.sh`

---

## Library Modules (single library example of ~70)

### To use library items

```sh
# use the import callable app
p ic -f rightthumb-widgets-v0/widgets/python/library/tools/tables/TableTool.py

# Generates: add this to your code to use a library class or function

class TableTool:
    def __new__(cls, *args, **kwargs):
        import importlib.util
        if 'TableTool' not in intelligent_code.classes:
            import importlib.util
            path = os.path.normpath(_v.w+'/widgets/python/library/tools/tables/TableTool.py')
            spec = importlib.util.spec_from_file_location('TableTool', path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            intelligent_code.classes['TableTool'] = module.TableTool
        return intelligent_code.classes['TableTool'](*args, **kwargs)
```

### 📊 TableTool — Advanced Table Processing Engine

`TableTool` is the framework’s **core table manipulation class**.
It powers printed tables (`_.pt`), table triggers, data transformation pipelines, and aggregation.

#### Key Features

* **Field-level operations**: register and chain operations (built-in or custom).
* **Row-level functions**: apply transformations or calculations across entire rows.
* **Custom aggregates**: group, sum, mean, min/max, counts, percentiles, or custom functions.
* **Trigger system**: queue transformations and run them in a single pass.
* **Safe expressions**: run inline formulas safely with controlled access.

---

#### Creating a TableTool

```python


rows = [
    {"sku": "abc-123", "price": 10, "qty": 2, "cost": 4},
    {"sku": "xyz-789", "price": 15, "qty": 1, "cost": 7},
]

tool = TableTool(rows)
```

---

#### Registering Custom Field Operations

Field ops run on **individual column values** and can be chained.

```python
# FIELD FUNCTION: normalize SKU
import re
def squeeze_sku(value, row, keep_dash=True):
    if not isinstance(value, str): return value
    v = re.sub(r"[^A-Za-z0-9\-]+", "", value)
    return v.upper() if keep_dash else v.replace("-", "").upper()

tool.register_field_op("squeeze_sku", squeeze_sku)
tool.add_field_trigger("sku", "squeeze_sku", keep_dash=True)
```

Built-in ops include:
`default`, `strip`, `lower`, `upper`, `title`, `replace`, `regex_extract`, `map`, `coalesce`, `cast`, `round`, and `expr`.

---

#### Registering Custom Row Functions

Row funcs operate on **entire rows** and can:

* Return a `dict` to update multiple fields
* Return a single value to assign to a target field

```python
# ROW FUNCTION: compute margin and flag profitable
def compute_margin(row, fee_rate=0.03):
    price = float(row.get("price") or 0)
    qty   = int(row.get("qty") or 0)
    cost  = float(row.get("cost") or 0)
    rev   = price * qty
    fees  = rev * fee_rate
    margin = rev - cost*qty - fees
    return {"revenue": rev, "fees": fees, "margin": margin, "profitable": margin >= 0}

tool.register_row_func("compute_margin", compute_margin)
tool.add_row_func("compute_margin", fee_rate=0.025)  # updates multiple fields

# Single-field row func
def sku_prefix(row):
    sku = row.get("sku") or ""
    return sku.split("-")[0] if "-" in sku else sku

tool.add_row_func(sku_prefix, target="sku_prefix")
```

Run all triggers:

```python
tool.run_triggers()
```

---

#### Aggregation

Group rows and compute metrics.

```python
def p95_price(rows):
    vals = sorted(float(r.get("price") or 0) for r in rows)
    if not vals: return None
    k = int(round(0.95*(len(vals)-1)))
    return vals[k]

tool.register_row_func("p95_price", p95_price)

aggregated = tool.aggregate({
    "group_by": ["region"],
    "metrics": {
        "count_rows": {"count": "*"},
        "max_price": {"max": "price"},
        "p95_price": {"func": "p95_price"},  # custom metric
    }
})
```

Built-in metrics:

* `sum`, `mean`, `min`, `max`, `count`, `nunique`, `expr`, and custom `func`.

---

#### SafeExpr — Safe Inline Expressions

`SafeExpr` lets you evaluate formulas in the context of a row.
It restricts access to a whitelist of functions, types, and modules.

Example:

```python
from TableTool import SafeExpr

row = {"qty": 2, "price": 10, "cost": 4}
expr = SafeExpr("qty * price if price and qty else 0")
total = expr.eval(row)  # 20
```

Allowed built-ins include:

* Math: `abs`, `round`, `min`, `max`, `sum`, `math` module
* Types: `int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`, `set`
* Logic and comparisons
* Date/time (`datetime`, `date`)

---

#### Example: Full Pipeline

```python
tool = TableTool(rows)

# Field trigger
tool.register_field_op("strip_upper", lambda v, r: v.strip().upper() if isinstance(v, str) else v)
tool.add_field_trigger("sku", "strip_upper")

# Row trigger
tool.register_row_func("calc_total", lambda r: {"total": r["price"] * r["qty"]})
tool.add_row_func("calc_total")

# Run and print
tool.run_triggers()
_.pt(tool.rows, cols="sku,price,qty,total", sort="total", responsive=True)
```
