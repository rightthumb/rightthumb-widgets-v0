import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
    _.switches.register( 'ShowSearchResults', '-r,-results,-ss,-ssr,-print' )
    _.switches.register( 'DebugDump', '-d,-debug,-dump' )
    _.switches.register( 'Minimal', '--c,-m,-min,-minimal', 'default' )
    _.switches.register( 'IndexDump', '-index', 'pre' )
    _.switches.register( 'JSON', '-json' )


_._default_settings_()

_.appInfo[focus()] = {
    'file': 'sql.py',
    'description': [
        'Parse large sql file to table records and fields the datamine it',
        'convert sql to json formatted same as mysql export',
        'Do a search and list every record and fields in that record that contains the search term',
        'Great for research on wordpress databases',
        'Great for manually making wordpress database changes manually',
        'Great for research on sql files',
        '',
        '',
        'Convert sql to json then use the tool json2sqlite.py',
        '',
        ],
    'categories': [
                        'sql',
                        'datamine',
                        'parse sql',
                        'sql research',
                        'research',
                        'wordpress',
                ],
    'examples': [
                        _.hp('(All results are colorized)'),
                        _.hp('cat tpn_wp.sql | p sql + "Old Company Name"'),
                        _.hp('cat tpn_wp.sql | p sql + "Old Company Name" -results'),
                        _.hp('cat tpn_wp.sql | p sql + "Old Company Name" -debug'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
    ],
    'aliases': [],
	'relatedapps': ['json2sqlite','sqlite2json','sql'],
	'prerequisite': [],
    'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
    _._default_triggers_()
    _.switches.trigger( 'Files', _.myFileLocations, vs=True )
    _.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start





# def sql(data):
#     dex = __.Meta_Namespace()
#     dex.p = _.deX.p(data, ['INSERT INTO', 'VALUES', 'CREATE TABLE'])
#     dex.o = _.deX.o(data)
#     dex.c = _.deX.c(data)
#     dex.ii = []
#     dex.ol = {}
#     # for o in dex.o: dex.ol[ _.deX.l(o,dex.c) ].append(o)
#     # for o in dex.p['index']: dex.ol[ _.deX.l(o,dex.c) ].append(o)
#     v = __.Meta_Namespace()
#     v.table = ''
#     v.tables = {}
#     v.isRec = False
#     i = 0
#     while i < len(data):
#         if i -1 in dex.c and not i in dex.p['ph']['INSERT INTO'] and not i in dex.o:
#             for ii in dex.p['ph']['INSERT INTO']:
#                 if not ii in dex.ii:
#                     i = ii
#                     dex.ii.append(ii)
#                     break
#         if i in dex.p['ph']['INSERT INTO']:
#             i = dex.p['index'][i]
#             char = data[i]
#             while not char.strip():
#                 i += 1
#                 char = data[i]
#             if i in dex.o:
#                 # modify here if table name does not have any sort of quotes
#                 c = dex.o[i]
#                 snip = data[i:c]
#                 snip = snip.strip(data[i])
#                 v.table = snip.strip()
#                 print('v.table',v.table)
#                 if not v.table in v.tables:
#                     v.tables[v.table] = {}
#                     v.tables[v.table]['fields'] = []
#                     v.tables[v.table]['records'] = []
#             while not char.strip(): i += 1; char = data[i]
#             if char == '(' and i in dex.o:
#                 c = dex.o[i]
#                 i = c
#                 snip = data[i:c]
#                 snip = snip.strip('(')
#                 snip = snip.strip(';')
#                 fields = snip.strip(')')
#                 fo = _.deX.o(fields)
#                 f = 0
#                 char = fields[f]
#                 while f < len(fields):
#                     while not char.strip(): f += 1; char = fields[f]
#                     if not f in fo:
#                         # if fields do not have quotes modify here and do by commas instead of quote jumping
#                         f += 1
#                     else:
#                         char = fields[f]
#                         v.tables[v.table]['fields'].append(fields[f:fo[f]].strip(char))
#                 v.isRec = True
            
#                 while v.isRec:
#                     char = data[i]
#                     if char == ';':
#                         v.isRec = False
#                         for ii in dex.p['ph']['INSERT INTO']:
#                             if not ii in dex.ii:
#                                 i = ii
#                                 dex.ii.append(ii)
#                                 break
#                         break
#                     while not char.strip(): i += 1; char = data[i]

#                     if char == '(' and i in dex.o:
#                         c = dex.o[i]
#                         snip = data[i:c]
#                         i = c
#                         rec = snip.strip('(')
#                         ro = _.deX.o(rec)
#                         r = 0
#                         char = rec[r]
#                         snip = ''
#                         fields = []
#                         while r < len(rec):
#                             char = rec[r]
#                             while not char.strip(): r += 1; char = rec[r]
#                             if char == ',':
#                                 fields.append(snip.strip())
#                                 snip = ''
#                                 r += 1
#                             elif r in ro:
#                                 c = ro[r]
#                                 snip = rec[r:c].strip(rec[r])
#                                 fields.append(snip.strip())
#                                 r = c
#                             else:
#                                 snip += char
#                                 r += 1
#                         pass
#                         record = {}
#                         for fi, fld in enumerate(fields):
#                             record[v.tables[v.table]['fields'][fi]] = fld
#                         v.tables[v.table]['records'].append(record)
#                     else:
#                         i += 1
#         i += 1
#     return v.tables



# def sql(data):
#     active = False
#     table = ''
#     tables = {}

#     for line in data.split('\n'):
#         line = line.strip()
#         dex = _.deX.o(line)  # Open-close index for the current line

#         # Detect start of INSERT INTO statement
#         if line.startswith('INSERT INTO'):
#             active = True
#             first = True

#             # Extract table name and fields
#             for start in dex:
#                 if line[start] == '`':  # Detect backticks around table name and fields
#                     end = dex[start]
#                     relevant = line[start + 1:end]  # Strip enclosing backticks
#                     if first:
#                         table = relevant
#                         if table not in tables:
#                             tables[table] = {'fields': [], 'records': []}
#                         first = False
#                     else:
#                         tables[table]['fields'].append(relevant)

#         elif active:
#             # Detect end of record section with semicolon
#             if line.endswith(';'):
#                 active = False  # Deactivate parsing when we reach the end

#             # Extract record values using open-close indexing
#             close = dex.get(0)
#             if close is None:
#                 continue  # Skip if no open-close found

#             rec = line[1:close].strip('()')  # Record inside parentheses
#             rDex = _.deX.o(rec)
#             fields = []
#             i = 0
#             snip = ''

#             while i < len(rec):
#                 char = rec[i]
#                 if char == ',':
#                     fields.append(snip.strip())
#                     snip = ''
#                 elif i in rDex:  # Handle values inside quotes
#                     c = rDex[i]
#                     snip = rec[i + 1:c].strip()  # Extract content between quotes
#                     fields.append(snip)
#                     i = c  # Jump to close position
#                 else:
#                     snip += char
#                 i += 1

#             if snip:
#                 fields.append(snip.strip())  # Append last field if exists

#             # Map fields to values for each record
#             record = {}
#             for fi, fld in enumerate(fields):
#                 if fi < len(tables[table]['fields']):
#                     record[tables[table]['fields'][fi]] = fld
#             tables[table]['records'].append(record)

#     return tables





import re

def sql(data):
    active = False
    table = ''
    tables = {}

    for line in data.split('\n'):
        line = line.strip()

        # Detect start of INSERT INTO statement and extract table name and fields
        if line.startswith('INSERT INTO'):
            active = True
            # print(f"Detected INSERT INTO statement: {line}")

            # Extract table name and fields
            match = re.search(r'INSERT INTO `([^`]+)` \(([^)]+)\)', line)
            if match:
                table = match.group(1)
                # print(f"Parsed table name: {table}")

                if table not in tables:
                    tables[table] = {'fields': [], 'records': []}

                # Extract fields
                fields = match.group(2).split(', ')
                fields = [field.strip('`') for field in fields]
                tables[table]['fields'].extend(fields)
                # print(f"Extracted fields: {tables[table]['fields']}")

        # Process each VALUES line
        elif active:
            if line.endswith(';'):
                active = False

            # Check if there are records in this line
            if line.startswith('('):
                # Remove the surrounding parentheses and semicolon/comma
                record_str = line[1:-1].strip()
                values = []
                current_value = ''
                in_quote = False
                quote_char = ''
                i = 0

                while i < len(record_str):
                    char = record_str[i]

                    # Handle quoted values
                    if char in {"'", '"'}:
                        if not in_quote:
                            in_quote = True
                            quote_char = char
                        elif in_quote and char == quote_char:
                            in_quote = False
                        else:
                            current_value += char
                    elif char == ',' and not in_quote:
                        # End of a value
                        values.append(current_value.strip(')').strip())
                        current_value = ''
                    else:
                        current_value += char
                    i += 1

                # Add the last value
                if current_value:
                    values.append(current_value.strip(')').strip())

                # Map values to fields
                record = {}
                for fi, value in enumerate(values):
                    if fi < len(tables[table]['fields']):
                        record[tables[table]['fields'][fi]] = value
                tables[table]['records'].append(record)

    return tables



def jsonExport(data):
    # Ensure the input is a dictionary
    if not isinstance(data, dict):
        raise TypeError("Input data should be a dictionary.")

    mysql_dump = [
        {
            "type": "header",
            "version": "5.2.1",
            "comment": "Export to JSON plugin for PHPMyAdmin"
        },
        {
            "type": "database",
            "name": "tpn_wp"
        }
    ]
    
    for table_name, table_data in data.items():
        table_entry = {
            "type": "table",
            "name": table_name,
            "database": "tpn_wp",
            "data": []
        }
        
        # Convert each record in 'records' using the field names in 'fields'
        for record in table_data["records"]:
            record_entry = {field: record.get(field, "") for field in table_data["fields"]}
            table_entry["data"].append(record_entry)
        
        mysql_dump.append(table_entry)
    
    return mysql_dump



def action():
    data = '\n'.join(_.isData(r=0))
    if _.switches.isActive('IndexDump') and 'pre' in _.switches.value('IndexDump'):
        index = _.simpleIndex(data)
        _.pv(index)
        for o in index:
            c = index[o]+1
            _.pr( data[o:c] )
        return None
    result = sql(data)

    if _.switches.isActive('JSON'):
        _.pv(jsonExport(result))
        return None
    if _.switches.isActive('IndexDump') or not _.switches.isActive('Plus'):
        _.pv(result)
        return None
        
    # _.pv(result); return False
    datamine = {
        'field_ids': {},
        'field_counts': {},
        'id_fields': {},
        'search_hits': {},
        'total': 0,
    }

    for table_name, table in result.items():
        for record in table['records']:
            first_field = next(iter(record))  # Get the first field in the record as a unique identifier
            record_id = record[first_field]

            for field, value in record.items():
                if _.showLine(value):
                    datamine['total'] += 1
                    if not table_name in datamine['field_ids']: datamine['field_ids'][table_name] = {}
                    if not table_name in datamine['field_counts']: datamine['field_counts'][table_name] = {}
                    if not table_name in datamine['id_fields']: datamine['id_fields'][table_name] = {}
                    if not table_name in datamine['search_hits']: datamine['search_hits'][table_name] = {}
                    # Initialize field-specific structures if needed
                    if field not in datamine['field_ids'][table_name]:
                        datamine['field_ids'][table_name][field] = []
                        datamine['field_counts'][table_name][field] = 0
                    datamine['field_counts'][table_name][field] += 1
                    datamine['field_ids'][table_name][field].append(record_id)

                    # Initialize search hits and ID field mappings
                    if record_id not in datamine['id_fields'][table_name]:
                        datamine['id_fields'][table_name][record_id] = []
                        datamine['search_hits'][table_name][record_id] = {}
                    if field not in datamine['id_fields'][table_name][record_id]:
                        datamine['id_fields'][table_name][record_id].append(field)
                        for plusSearchX in _.switches.values('Plus'):
                            plusSearchX = _.ci( plusSearchX )
                            for subject in _.caseUnspecificCode( value, plusSearchX ):
                                value = value.replace( subject, _.colorThis( subject, 'green', p=0 ) )
                        datamine['search_hits'][table_name][record_id][field] = value


    def searchResults(datamine):
        for table_name in datamine['search_hits']:
            _.pr(line=1, c='blue')
            _.pr(table_name, c='yellow')
            for id in datamine['search_hits'][table_name]:
                _.pr('  ',id,c='cyan')
                for field in datamine['search_hits'][table_name][id]:
                    _.pr('    ',field,c='darkcyan')
                    # print(datamine['search_hits'][table_name][id][field])
                    print('      ',datamine['search_hits'][table_name][id][field])

        _.pr('\n','',_.addComma(datamine['total']),c='Background.blue')


  
    if _.switches.isActive('DebugDump'):
        # Print outputs for debugging and verification
        color = 'Background.green'
        _.pr(line=1, c='green')
        _.pr('Count of Results in a Field by Table',c=color)
        _.pv(datamine['field_counts'])
        _.pr(line=1, c='green')
        _.pr('ID Priority and Fields by Table',c=color)
        _.pv(datamine['id_fields'])
        _.pr(line=1, c='green')
        _.pr('Field Priority and IDs by Table',c=color)
        _.pv(datamine['field_ids'])
        _.pr(line=1, c='green')
        _.pr('Search Results by Table ID and Field',c=color)
        # _.pv(datamine['search_hits'])
        searchResults(datamine)
        _.pr(line=1, c='green')

    # import simplejson
    # print( simplejson.dumps(datamine['search_hits'], indent=4) )
    elif _.switches.isActive('ShowSearchResults'):
        searchResults(datamine)
    else:
        _.pv(datamine['id_fields'])


########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__);