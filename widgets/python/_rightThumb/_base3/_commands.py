

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



saveText(rows,theFile)
getText(theFile)
getSize(fileobject)
monthByNumber(month)
weeks_between(start_date, end_date)
months_between(start_date, end_date)
calculate_monthdelta(date1, date2)
timeout(start,t)
processTimeout()
showLine(string)
positiveResults(string)
minusResults(string)
saveTable(rows,theFile,tableTemp = True,printThis = True,indentCode = True)
getTable(theFile,tableTemp = True,printThis = False)
getTable2(theFile)
saveTable2(rows,theFile)
tempFile(rows,theFile)
stamp2Date(ts)
float2Date(ts)
float2Date2(ts)
float2Date3(ts)
float2Date3B(ts,isJson = True)
expireCheck(theDate,delim)
dateDiff(theDate0,theDate1,delim)
dateAdd(theDate,delim,addDays)
dateSub(theDate,delim,addDays)
listAverage(theList)
date2epoch(theDate,delim)
validateEmail(data)
figureOutDate(theDate, theFormat)
getMonthData()
formatPhone00(data)
formatPhone0(data)
formatPhone1(data)
formatPhone2(data)
updateLine(string)
getLastTableSplit(theFile,tableTemp = 'split')
saveTableSplitNew(rows,theFile,tableTemp = True,printThis = True)
sort(rows, name)
ci2(string)
md5(fname)
formatSize(size)
unFormatSize(size)
timeAgo(do='')
epoch(string,end=False)
isNu(string)
isNu2(string)
number2Words(n)
get_size(obj, seen=None)
genLine(count,what)
ci(string)


showLine( string, plus = '', minus = '', plusOr = False )


dict = {'Name': 'Zara', 'Age': 7}
print "Value : %s" %  dict.has_key('Age')




#######################################
uuidProject = { 'input': _.switches.value('Input'), 'note': 'sample' }
_.appData[__.appReg]['uuid'] = {  'app': _.appInfo[__.appReg]['file'], 'project': uuidProject }
_.genUUID(project='')
_.genUUID('temp file')
_.genUUID({'file':'app.py'})

_.randomizeCase(_.genUUID())
_.randomizeCase(_.longID(howMany=2))
x = _.randomizeCase(_.longID(howMany=2))
print(_.onlyNumbers(x))
print(_.onlyAlpha(x))
_.onlyAlphaNumeric(_.randomizeCase(_.genUUID()))

True False same in a row
diff = int((_.randomTrueFalseSame/_.randomTrueFalseCount)*100)
#######################################




