import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Add', '-a,-add', 'Do this thing' )
	_.switches.register( 'Delete', '-d,-del,-delete', '' )
	_.switches.register( 'Day', '-day', '15: day of month' )
	_.switches.register( 'Order', '-o,-order' )
	_.switches.register( 'Prepend', '-p,-prepend' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'vps-todo.py',
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

def action():
	import simplejson as json
	if not 'todo' in _v.fig:
		_.e('No todo configured')
	todo = _.URL(f'https://r.etc.ac/routine.php?api={_v.fig["todo"]}')
	todo = json.loads(todo)
	todo = todo['todo']

	def send(todo):
		data = {'data': todo}
		result = _.URL(f'https://r.etc.ac/routine.php?api={_v.fig["todo"]}&todo=true',{'data':json.dumps(data)})
		_.pr()
		_.pr('\t',result)
	def listTodo(todo):
		for i,item in enumerate(todo):
			name = item['todo']
			if item['status']:
				color = 'Background.green'
			else:
				color = 'Background.red'
			_.pr(_.pr0(i,c='cyan')+'  '+_.pr0(item['at'],c='ColorBold.blue')+'  '+_.pr0(name,c=color))

	if _.switches.isActive('Add'):
		name = ' '.join(_.switches.values('Add'))
		doAt = '-'
		if _.switches.isActive('Day'):
			doAt = _.switches.value('Day')
		rec = {
			"at": doAt,
			"todo": name,
			"type": "todo",
			"status": False
		}
		if _.switches.isActive('Prepend'):
			todo = [rec] + todo
		else:
			todo.append(rec)
		listTodo(todo)
		send(todo)

	elif _.switches.isActive('Delete'):
		listTodo(todo)
		select = input('Select: ')
		if select == 'x':
			return False
		todo.pop(int(select))
		send(todo)
	elif _.switches.isActive('Order'):
		listTodo(todo)
		select = input('Select: ')
		if select == 'x':
			return False
		newOrder = []
		IDs = []
		for i in select.replace('  ',' ').replace('  ',' ').replace('  ',' ').split(' '):
			IDs.append(int(i))
		for i in IDs:
			newOrder.append(todo[int(i)])
		for i,item in enumerate(todo):
			if i in IDs:
				continue
			newOrder.append(item)
		todo = newOrder
		listTodo(todo)
		send(todo)
	else:
		listTodo(todo)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);