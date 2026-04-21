#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

# http://www.idiotinside.com/2015/09/18/csv-json-pretty-print-python/
import sys, getopt
import csv
import simplejson as json
# import json
import _rightThumb._base1 as _
_.switches.register('Input', '-i')
_.switches.register('Output', '-o')
# _.switches.register('Format', '-f')

_.appInfo=  {
	'file': 'csv2json.py',
	'description': 'Convert csv to json',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p csv2json -i file.csv -o file.json')
_.appInfo['examples'].append('p  file --c + .csv | p line --c -make "p csv2json -i ;\'{};\' -o ;\'json\\{}.json;\'" | p execute')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})

_.switches.process()

# p csv2json -i data.csv -o data.json -f dump
# p csv2json -i data.csv -o data.json -f pretty


#Read CSV File
def read_csv(file, json_file, format):
	csv_rows = []
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		title = reader.fieldnames
		# print( title )
		# for t in title:
		#     print( t )
		for row in reader:
			csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
		# write_json(csv_rows, json_file, format)
		_.saveTable2(csv_rows,json_file)

#Convert csv data into json and write it
def write_json(data, json_file, format):
	with open(json_file, "w") as f:
		f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
		# if format == "pretty":
		#     f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
		# else:
		#     f.write(json.dumps(data))

if __name__ == "__main__":
	read_csv(_.switches.value('Input'), _.switches.value('Output'), _.switches.value('Format'))
   # main(sys.argv[1:])