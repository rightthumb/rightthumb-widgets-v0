import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'URLs', '-url', 'url here or leave blank to | pipe', isData='name' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt' )
	_.switches.register( 'OutputFolder', '-fo,-folder' )

__.setting('omit-switch-triggers',['Files'])
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
	# _.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start



def harBuild(har_path, output_dir='harBuild'):
    import os
    import json
    import requests # type: ignore
    from urllib.parse import urlparse
    from bs4 import BeautifulSoup # type: ignore
    os.makedirs(output_dir, exist_ok=True)
    with open(har_path, 'r', encoding='utf-8') as f:
        har = json.load(f)
    entries = har['log']['entries']
    downloaded_files = {}
    print(f"[+] Found {len(entries)} entries in HAR")
    for entry in entries:
        url = entry['request']['url']
        parsed = urlparse(url)
        path = parsed.path.lstrip('/')
        if not path or path.endswith('/'):
            path += 'index.html'
        local_path = os.path.join(output_dir, path)
        if url in downloaded_files:
            continue
        try:
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            response = requests.get(url, timeout=10)
            with open(local_path, 'wb') as f:
                f.write(response.content)
            downloaded_files[url] = os.path.relpath(local_path, output_dir)
            print(f"[✔] {url}")
        except Exception as e:
            print(f"[✘] Failed {url} -> {e}")
    html_files = [f for f in downloaded_files.values() if f.endswith('.html')]
    for file_path in html_files:
        full_path = os.path.join(output_dir, file_path)
        try:
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                soup = BeautifulSoup(f, 'html.parser')
            tag_attr = {
                'script': 'src',
                'img': 'src',
                'iframe': 'src',
                'source': 'src',
            }
            for tag, attr in tag_attr.items():
                for el in soup.find_all(tag):
                    src = el.get(attr)
                    if src and src in downloaded_files:
                        el[attr] = downloaded_files[src]
            for link in soup.find_all('link'):
                rel = link.get('rel')
                href = link.get('href')
                if href and rel and 'stylesheet' in rel:
                    if href in downloaded_files:
                        link['href'] = downloaded_files[href]
                        print(f"[↻] Rewrote CSS href: {href}")
                    else:
                        print(f"[!] Missing CSS in downloaded files: {href}")
            for el in soup.find_all(style=True):
                style = el['style']
                for url, local_path in downloaded_files.items():
                    if url in style:
                        style = style.replace(url, local_path)
                        print(f"[↻] Rewrote inline style: {url}")
                el['style'] = style
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"[✓] Rewrote paths in: {file_path}")
        except Exception as e:
            print(f"[✘] Failed to process {file_path}: {e}")
    print(f"\n[✓] Rebuild complete. View locally from: {output_dir}")






def urlBuild(start_url, output_dir='urlBuild'):
    from urllib.parse import urljoin, urlparse
    from bs4 import BeautifulSoup # type: ignore
    import mimetypes
    import requests # type: ignore
    import os
    import json

    os.makedirs(output_dir, exist_ok=True)
    downloaded_files = {}

    try:
        response = requests.get(start_url, timeout=10)
        html = response.text
    except Exception as e:
        print(f"[✘] Failed to download {start_url}: {e}")
        return

    parsed = urlparse(start_url)
    html_filename = parsed.path.strip('/').replace('/', '_') or 'index'
    html_path = os.path.join(output_dir, f"{html_filename}.html")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    soup = BeautifulSoup(html, 'html.parser')
    assets = []

    # Collect all linked asset URLs
    for tag, attr in [
        ('script', 'src'),
        ('link', 'href'),
        ('img', 'src'),
        ('iframe', 'src'),
        ('source', 'src'),
    ]:
        for el in soup.find_all(tag):
            src = el.get(attr)
            if src:
                full_url = urljoin(start_url, src)
                file_path = urlparse(full_url).path.lstrip('/')
                if not file_path or file_path.endswith('/'):
                    file_path += 'index.html'
                local_path = os.path.join(output_dir, file_path)

                assets.append((el, attr, full_url, local_path))

    # Download all missing assets
    for el, attr, url, local_path in assets:
        if os.path.exists(local_path):
            relative_path = os.path.relpath(local_path, output_dir)
            el[attr] = relative_path
            print(f"[✔] Skipped (cached): {url}")
            continue

        try:
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            r = requests.get(url, timeout=10)
            with open(local_path, 'wb') as f:
                f.write(r.content)

            relative_path = os.path.relpath(local_path, output_dir)
            el[attr] = relative_path
            downloaded_files[url] = relative_path
            print(f"[↓] Downloaded: {url}")
        except Exception as e:
            print(f"[✘] Failed {url}: {e}")

    # Rewrite inline styles
    for el in soup.find_all(style=True):
        style = el['style']
        for url, local_path in downloaded_files.items():
            if url in style:
                style = style.replace(url, local_path)
                print(f"[↻] Rewrote inline style: {url}")
        el['style'] = style

    # Save updated HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"[✓] Page saved: {html_path}")




def action():
    if _.switches.isActive('URLs'):
        for url in _.isData():
            if _.switches.isActive('OutputFolder'):
                OUTPUT_DIR = _.switches.values('OutputFolder')[0]
            else:
                OUTPUT_DIR = 'urlBuild'
            urlBuild(url, OUTPUT_DIR)
    if _.switches.isActive('Files'):
        for file in _.switches.values('Files'):
            HAR_FILE = _.switches.values('Files')
            if _.switches.isActive('OutputFolder'):
                OUTPUT_DIR = _.switches.values('OutputFolder')[0]
            else:
                OUTPUT_DIR = 'harBuild'
            harBuild(HAR_FILE, OUTPUT_DIR)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)