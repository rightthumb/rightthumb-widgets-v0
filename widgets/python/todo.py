import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Table', '-table', 'daily, weekly, monthly, todo' )
	_.switches.register( 'SaveToTemplate', '-t,-template', '' )
	_.switches.register( 'Add', '-a,-add', 'Cancel Trial Subscription' )

	_.switches.register( 'Prepend', '-p,-prepend' )
	_.switches.register( 'Delete', '-d,-del,-delete', '' )
	_.switches.register( 'Day', '-day', '15: '+_.pr0('day of month') )
	_.switches.register( 'Order', '-o,-order' )
	_.switches.register( 'ChangeAt', '-at', '15: '+_.pr0('day of month') )
	_.switches.register( 'ChangeToDo', '-u,-update,-change' )
	_.switches.register( 'Recover', '-r,-recover' )
	_.switches.register( 'RecoverJust', '-just', 'global or current' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'todo.py',
	'description': 'ToDo list manager',
	'categories': [
						'todo',
				],
	'examples': [
						_.hp('p todo -add Buy Groceries'),
						_.hp('p todo -add Cancel Trial Subscription -day 15 -prepend'),
						_.pr0('\t-prepend will add to TOP of the list'),
						_.hp(''),
						_.hp('p todo -delete'),
						_.pr0('\t1 3 5'),
						_.pr0('\tSelect one or multiple items to delete'),
						_.hp(''),
						_.hp('p todo -change Buy Groceries dont forget milk'),
						_.pr0('\t7'),
						_.pr0('\tSelect one item and it will be changed'),
						_.hp(''),
						_.hp('p todo -order'),
						_.pr0('\t1 3 5'),
						_.pr0('\tSelect one or multiple. Selected items at top. In that order'),
						_.pr0('\t\tUnselected items will be at the below selected in the order they were in'),
						_.hp(''),
						_.hp('p todo -at 15'),
						_.pr0('\t3'),
						_.pr0('\tSelect one item and change the day of month'),
						_.hp(''),
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

from shutil import copyfile
def action():
	if _.switches.isActive('Recover'):
		just = ''
		import simplejson as json
		if len(_.switches.value('Recover')):
			data = _.getTable2(_.switches.value('Recover'))
		else:
			data = _.getTable('todo'+__.os.sep+'todo.json')
		if _.switches.isActive('Table'):
			newData = {}
			for table in _.switches.values('Table'):
					newData[table] = data[table]
			data = newData
			
			if _.switches.isActive('RecoverJust'):
				if 'g' in _.switches.value('RecoverJust').lower():
					just = '&just=g'
				elif 'c' in _.switches.value('RecoverJust').lower():
					just = '&just=c'
				else:
					just = ''
		data = {'data': data}
		result = _.URL(f'{_v.fig["todoURL"]}?api={_v.fig["todo"]}&recover=1{just}',{'data':json.dumps(data)})
		_.pr()
		if 'success' in result:
			_.pr(' ','Success',c='green')
		else:
			_.pr(' ','Error',c='red')
			_.pr(result)
		return

	table = 'todo'
	if _.switches.isActive('Table'):
		table = _.switches.value('Table')
	import simplejson as json
	if not 'todo' in _v.fig: _.e('No todo configured')
	if not 'todoURL' in _v.fig: _.e('No todo configured')
	todo = _.URL(f'{_v.fig["todoURL"]}?api={_v.fig["todo"]}')
	todo = json.loads(todo)
	# bk = _.backupName('todo.json')
	_.saveTable(todo,'todo'+__.os.sep+'todo.json')
	bk = _v.tt + __.os.sep + 'todo'+ __.os.sep +'todo.json'
	nBK = _.backupName(bk)
	copyfile(bk, nBK)
	# _.pv(todo)
	todo = todo[table]

	def send(todo):
		templateGet = ''
		if _.switches.isActive('SaveToTemplate'):
			templateGet = '&template=true'
		data = {'data': todo}
		result = _.URL(f'{_v.fig["todoURL"]}?api={_v.fig["todo"]}&save=1&{table}=true{templateGet}',{'data':json.dumps(data)})
		_.pr()
		if 'success' in result:
			_.pr(' ','Success',c='green')
		else:
			_.pr(' ','Error',c='red')
			_.pr(result)
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
		elif _.switches.isActive('ChangeAt'):
			doAt = _.switches.value('ChangeAt')
		rec = {
			"at": doAt,
			"todo": name,
			"type": table,
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
		_.pr('\tx to exit',c='yellow')
		select = input('Select: ').strip()
		if select == 'x':
			return False
		IDs = []
		for i in select.replace('  ',' ').replace('  ',' ').replace('  ',' ').split(' '):
			IDs.append(int(i))
		IDs.sort()
		IDs.reverse()
		for i in IDs:
			todo.pop(i)
		listTodo(todo)
		send(todo)
	elif _.switches.isActive('ChangeAt'):
		listTodo(todo)
		_.pr('\tx to exit',c='yellow')
		select = input('Select: ').strip()
		if select == 'x':
			return False
		if _.switches.isActive('Day'):
			newAt = _.switches.value('Day')
		elif not len(_.switches.value('ChangeAt')):
			newAt = input('New at: ').strip()
		else:
			newAt = _.switches.value('ChangeAt')
		todo[int(select)]['at'] = newAt
		listTodo(todo)
		send(todo)
	elif _.switches.isActive('ChangeToDo'):
		listTodo(todo)
		_.pr('\tx to exit',c='yellow')
		select = input('Select: ').strip()
		if select == 'x':
			return False
		newToDo = ''
		while not len(newToDo):
			if _.switches.isActive('Day'):
				newAt = _.switches.value('Day')
			elif _.switches.isActive('ChangeAt'):
				newAt = _.switches.value('ChangeAt')
			else:
				newAt = input('(optional) New at: ').strip()
				if newAt == 'x': return False
				if not len(newAt):
					newAt = todo[int(select)]['at']
				else:
					newAt = newAt
			if _.switches.isActive('Add'):
				newToDo = ' '.join(_.switches.values('Add'))
			elif not len(_.switches.value('ChangeToDo')):
				newToDo = input('Updated ToDo: ').strip()
			else:
				newToDo = ' '.join(_.switches.values('ChangeToDo'))
		if newToDo == 'x': return False

		todo[int(select)]['todo'] = newToDo
		todo[int(select)]['at'] = newAt
		listTodo(todo)
		send(todo)
	elif _.switches.isActive('Order'):
		listTodo(todo)
		_.pr('\tx to exit',c='yellow')
		select = input('Select: ').strip()
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