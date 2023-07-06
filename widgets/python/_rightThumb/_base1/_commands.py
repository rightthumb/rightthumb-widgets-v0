

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


_.switches.register(name, switch, expected_input_example = None)
_.switches.register('Sort','-s,-sort', 'Asc:type, Desc:ext')


_.switches.trigger(name,script)
def fix(value):
	if value == 'n':
		value = 'name'
	return value
_.switches.trigger('Column',fix)


_.switches.print()


_.switches.fieldSet(name,column,value)
_.switches.fieldSet('Sort','active',True)
_.switches.fieldSet('Sort','value','name')



_.switches.fieldGet(name,column)
_.switches.fieldGet('Column','pos')



_.switches.isActive(name)
_.switches.isActive('Column')


_.switches.value(name)
_.switches.value('Column')


_.switches.exists(name)
if _.switches.exists('Column2'):
	print('This is a valid switch')


_.ci(string)
i = 0
for value in _.switches.value('Plus'):
	p[i] = _.ci(value)




_.tables.register(name,asset)
_.tables.register('switches',switch)

_.tables.asset('switches')



_.tables.trigger(field,script,includes = False)
def test(value):
	value = value + '_V_'
	return value
_.tables.trigger('switches','switch,name',test,True)


_.tables.registerView(table,name,fields,sort = '')
_.tables.registerView('switch','quickView','name,switch',sort)
_.tables.view('switch')



_.tables.print(name,fields)
_.tables.print('switches','name,switch,expected_input_example')

_.tables.sort(name, fields)
_.tables.sort('switch', 'name')




def test(value):
	value = value + '_V_'
	return value
_.tables.trigger('switches','switch,name',test,True)
_.tables.register('switches',switch)
_.tables.print('switches','name,switch,expected_input_example')




_.tables.fieldProfileSet('members','*','alignment','center')
_.tables.fieldProfileSet('members','email,phone','alignment','center')
_.tables.fieldProfileSet('members','_header_','alignment','center')

_.tables.alignmentMasterSupersedes('members',True)


_.formatPhone00 = 2532797392
_.formatPhone0  = (253) 279-7392
_.formatPhone1  = 253-279-7392
_.formatPhone2  = 253.279.7392

_.tables.fieldProfileSet('members','phone','trigger',_.formatPhone0)
_.tables.fieldProfileSet('members','email','trigger',_.validateEmail)



	_.tables.register('members',data)
	_.tables.fieldProfileSet('members','address1,people:first,people:email','trigger',_str.totalStrip6)
	_.tables.print('members','address1,people:first=s* n,people:email=gmail-stan')    



def saveTable(rows,theFile,tableTemp = True,printThis = True,indentCode = True):
def getTable(theFile,tableTemp = True,printThis = False):
def getTable2(theFile):
def saveTable2(rows,theFile):

def saveText(rows,theFile):
def getText(theFile):
def getSize(fileobject):
def formatSize(size):
def monthByNumber(month):
def weeks_between(start_date, end_date):
def months_between(start_date, end_date):
def calculate_monthdelta(date1, date2):
def timeout(start,t):
def processTimeout():
def showLine(string):
def positiveResults(string):
def minusResults(string):
def tempFile(rows,theFile):
def stamp2Date(ts):
def float2Date(ts):
def validateEmail(data):
def formatPhone00(data):
def formatPhone0(data):
def formatPhone1(data):
def formatPhone2(data):
def updateLine(string):
def saveTableSplitNew(rows,theFile,tableTemp = True,printThis = True):
def sort(rows, name):
def ci2(string):
def ci(string):



def formatColumns(columns):
	result = ''
	for c in columns.split(','):
		for col in _.appInfo['columns']:
			for a in col['abbreviation'].split(','):
				if a == c:
					c = col['name']
		result += c + ','
	result = result[:-1]
	return result

_.switches.trigger('Column',formatColumns)

_.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)



theJSON = _.getTable('file.json')
_.saveTable(theJSON,'file.json',True,False)


_.saveText(rows,'file.txt')
theText = _.getText('file.txt')


_.switches.isActive('Column')
_.switches.value('Column')



dict = {'Name': 'Zara', 'Age': 7}
print "Value : %s" %  dict.has_key('Age')


