import os
import sys
import simplejson

def yaml_simp(yaml_string):
    table = {}
    lines = yaml_string.split('\n')
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            table[key.strip()] = value.strip()
    return table

def get_first_char(filename):
    with open(filename, 'r') as file:
        return file.read(1)

def get_file_content(filename):
    with open(filename, 'r') as file:
        return file.read()

def get_table(file):
    if not get_first_char(file) in '{[':
        return yaml_simp(get_file_content(file))
    json_data = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding="latin-1") as json_file:
            json_data = simplejson.load(json_file)
    return json_data

def load_configuration():
    if sys.platform[0] == 'w':
        figpath = os.getenv('USERPROFILE') + os.sep + '.rt' + os.sep + '.config.hash'
    else:
        figpath = os.getenv('HOME') + os.sep + '.rt' + os.sep + '.config.hash'

    fig = get_table(figpath)
    sys.path.append(os.path.join(fig['w'], 'widgets', 'python'))
    # Simulate importing modules as needed, e.g.,:
    # import your_module_here

    # Continue with other setup tasks...

# Entry point for execution when this module is run directly
if __name__ == "__main__":
    load_configuration()
