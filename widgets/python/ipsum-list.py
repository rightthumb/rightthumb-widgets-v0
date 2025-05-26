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

##################################################
import os, sys, time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register( 'Paragraphs', '-par,-paragraph,-paragraphs' )
	_.switches.register( 'Sentences', '-sen,-sentence,-sentences' )
	_.switches.register( 'Count', '-count' )
	_.switches.register( 'Lorem', '-lorem' )
	_.switches.register( 'JSON', '-json' )
	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files' )
	### EXAMPLE: END

### EXAMPLE: START
# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
#     finds the file in probable locations
#     and 
#         if  _.autoBackupData = True
#         and __.releaseAcquiredData = True
#             GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#         you can run apps on usb at a clients office
#             when you get home run: p app -loadepoch epoch 
#                 backed up
#                     pipe
#                     files
#                     tables
### EXAMPLE: END
_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'ipsum-list.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'web ipsum tool',
	'categories': [
						'ipsum',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p ipsum-list -sentences'),
						_.hp('p ipsum-list -paragraphs'),
						_.hp('p ipsum-list -count 5 -sen'),
						_.hp('p ipsum-list -count 1 -par -lorem'),
						_.hp('p ipsum-list -count 500 -json -lorem | p -copy'),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] }, 
		},
	}
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )    
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START


ipsum = '''
Dolor sit amet, consectetur adipiscing elit. Praesent at tincidunt erat, a interdum lorem. Donec commodo suscipit lacus sit amet consectetur. Mauris aliquam ullamcorper libero, id pellentesque ex elementum et. Ut aliquam urna quis ipsum volutpat, at consectetur tortor facilisis. Sed facilisis dolor vitae mauris imperdiet iaculis. Nulla facilisi. Suspendisse potenti.

Donec metus magna, tincidunt at vulputate ut, bibendum et enim. Curabitur ornare efficitur fringilla. Praesent felis mi, ornare id dolor id, elementum tempus dolor. Phasellus varius erat nisi, pellentesque dictum dui rhoncus vel. Suspendisse viverra ligula risus, sed porttitor augue rhoncus at. Phasellus leo ex, aliquam lacinia lorem vitae, sodales porta lacus. Aenean varius massa nec lectus lacinia, vitae mollis nibh sagittis. Sed ac eros sed leo fermentum vehicula.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Duis sed molestie neque. Mauris lobortis dictum facilisis. Mauris commodo, velit id gravida condimentum, lorem lectus laoreet felis, sit amet mollis ipsum risus in dolor. Suspendisse laoreet rutrum pharetra. Integer euismod, lacus non mattis congue, nulla urna eleifend odio, at tempor ex tortor quis urna. Suspendisse malesuada ut odio et elementum. Proin at mi sed diam consectetur venenatis non at ipsum. Sed gravida ipsum ut dui eleifend, vel mattis mi dapibus. Nam a feugiat velit.

Nulla consequat lectus egestas lectus porta, non laoreet nunc egestas. Pellentesque id lorem a lacus interdum finibus sed a nibh. Nulla facilisi. Pellentesque pulvinar, magna at congue varius, mauris nisi mollis sem, sit amet varius dolor augue ut sapien. Vestibulum blandit magna vel tortor ullamcorper, nec ultricies arcu viverra. Suspendisse nec posuere orci, in tempus urna. Praesent quis lacus eu risus porttitor pharetra.

Curabitur tincidunt, lacus a tincidunt pharetra, est lorem elementum metus, ac molestie enim sem a tellus. Aenean fermentum luctus enim, ac dignissim turpis cursus ac. Sed arcu mi, euismod at varius sit amet, iaculis nec nisi. Donec bibendum risus dolor, a tempus lectus placerat a. Pellentesque quis varius dui. Nullam faucibus dignissim tincidunt. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum ullamcorper tellus mauris, nec mattis neque aliquam vitae. Nullam varius id nisi in tristique. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus in libero urna. Aenean facilisis tincidunt dui vitae aliquet.

Integer ante ipsum, ultricies sed mattis a, faucibus vel mi. Quisque congue vitae dui at pharetra. In hac habitasse platea dictumst. Proin luctus enim purus, ut dapibus ipsum laoreet in. Aenean quis nulla mauris. Cras et maximus velit. Donec vehicula, orci id accumsan imperdiet, massa metus euismod nulla, quis interdum nisi nisl a lorem. Mauris ut libero non tortor interdum mattis eget eget nisl. Morbi ac diam eget mauris lobortis porta eu vitae sem. Donec consequat tristique magna non placerat. In iaculis imperdiet velit, ut fermentum elit vulputate id.

Duis a congue enim. Integer vulputate sit amet metus vel cursus. Vestibulum at lectus et ante lobortis aliquet at id dui. Nunc at lectus elit. Pellentesque nec risus a magna commodo aliquam ut non nibh. In vestibulum sollicitudin dui, non ultricies risus molestie venenatis. Nunc tellus erat, blandit et vestibulum vel, tincidunt ac felis. Duis nisl augue, commodo et metus at, ullamcorper condimentum nulla.

Nullam non vehicula leo. Pellentesque feugiat tellus mi, sed luctus mauris tincidunt id. Ut rutrum est non dolor malesuada ultrices. In tincidunt ex neque, id ultricies augue semper ac. Fusce vitae scelerisque lectus. Vestibulum eu sem ac dui fringilla dapibus. Nullam pretium scelerisque sem id sollicitudin. Sed commodo purus vitae ex venenatis, sit amet pellentesque sapien congue. Aenean tristique tincidunt diam, non interdum augue pretium eu. Maecenas non mattis nisi. Etiam nibh tellus, blandit sed luctus vel, facilisis sed quam. Nam condimentum ornare quam, lacinia mattis felis dignissim in. Mauris egestas cursus est, in volutpat enim sodales ut. Ut id tortor luctus, accumsan magna nec, aliquet massa. Pellentesque et est tortor. Nulla vitae orci congue, condimentum erat ut, molestie magna.

Proin turpis dolor, vulputate ut justo in, mattis porta eros. Cras elementum lobortis efficitur. Integer semper dapibus pellentesque. Vestibulum sit amet dignissim felis. Morbi fringilla gravida magna, vitae sollicitudin turpis. Aliquam a dolor hendrerit, sagittis sapien in, volutpat massa. Morbi quis velit bibendum, viverra ligula id, auctor urna. In ornare magna eu convallis dignissim. Vivamus dictum nisi lectus, vel interdum libero eleifend ac. Curabitur sagittis porta diam quis vulputate. Aliquam eleifend lacinia mi eget hendrerit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Curabitur efficitur, ex a pulvinar viverra, lectus velit posuere neque, quis accumsan leo ligula sit amet sem. Nam iaculis eget ex sit amet dignissim. Donec cursus nibh ac nisi lacinia luctus. Nullam eget lacus non tortor dictum euismod. Duis quis tortor quis ex viverra vestibulum in eu massa. Curabitur in nibh eget leo tincidunt suscipit sit amet fermentum lectus. Ut quis quam porta, scelerisque orci at, dictum quam. Nullam luctus posuere elit, at convallis dolor imperdiet sit amet. Ut in molestie odio, vel finibus arcu. Integer euismod orci sit amet tincidunt euismod. Donec sit amet orci rutrum, tempus ipsum ac, dignissim libero. Pellentesque blandit congue elit sed fringilla.

Quisque venenatis risus nec justo laoreet, non aliquet orci feugiat. Donec aliquet non sapien malesuada imperdiet. Mauris at ex consequat, dignissim metus at, iaculis mi. Cras libero mauris, efficitur quis urna eu, porttitor semper ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Etiam et suscipit elit, quis mattis urna. Integer ac sem ut libero iaculis commodo. In pellentesque porttitor dignissim. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Duis in vestibulum tortor. Morbi accumsan commodo ipsum eget tristique. Ut rutrum leo id neque malesuada fermentum. Proin pulvinar gravida dolor vitae volutpat. Nam sit amet efficitur urna, a gravida tellus. Fusce rutrum commodo efficitur. Suspendisse posuere lacinia libero, ut egestas nunc molestie in. Curabitur scelerisque aliquam pulvinar. Curabitur vehicula ullamcorper maximus. Vestibulum viverra, nisl vitae commodo ornare, ex turpis luctus nibh, eu pharetra velit lectus vel nulla. Nam dolor nisi, sollicitudin nec mauris et, feugiat condimentum nunc.

Donec dignissim, elit in pretium convallis, nisi enim tincidunt eros, quis cursus odio sem a ante. Phasellus ullamcorper velit nibh, ac eleifend ligula tristique at. Nulla luctus efficitur ullamcorper. Cras sed rutrum erat. Praesent quis nisl vel elit fringilla fermentum et ac risus. Ut quis ultrices enim, vel dictum nibh. Sed et imperdiet justo, eget fermentum orci. Integer leo sem, tempor vel risus eget, pharetra sagittis quam.

Vivamus vitae ex arcu. Cras rhoncus porttitor nisi non ullamcorper. Aliquam facilisis nulla et est euismod consectetur. Nam laoreet eget nisl at gravida. Integer dapibus, leo in fringilla rhoncus, nibh lectus eleifend velit, ac malesuada orci purus dictum purus. Nulla porttitor nunc tellus, in fringilla odio aliquam vitae. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean rhoncus tincidunt malesuada. Pellentesque id erat a neque efficitur laoreet ac ut tortor.

Donec elit velit, aliquet vitae purus in, aliquet condimentum dui. Maecenas consectetur, augue ac suscipit posuere, libero augue luctus felis, ac scelerisque nulla libero vitae odio. Ut vitae dolor ac erat eleifend semper eu vel tortor. Proin fringilla, tellus commodo ullamcorper cursus, leo massa rhoncus nulla, nec ultricies massa augue quis nibh. Aliquam erat volutpat. Fusce dapibus nec purus at accumsan. Cras consequat scelerisque dui et mollis. Maecenas vel sem arcu. Praesent at dui in massa fermentum pulvinar. Nullam egestas euismod arcu, a molestie mauris faucibus a. Curabitur lobortis est justo, sed luctus sapien imperdiet ac. Quisque dapibus at nulla vel dignissim. Sed nec sodales lacus, in placerat massa. Nam vitae tellus ex.

Aenean elit ligula, vulputate sit amet elementum sit amet, accumsan eget erat. Sed tincidunt nunc at cursus sollicitudin. Maecenas dapibus a sem a feugiat. Fusce dictum nibh vel mi tempor bibendum. Cras leo velit, volutpat eget placerat eget, faucibus id diam. Integer faucibus ornare orci at laoreet. Vivamus ullamcorper nibh at bibendum laoreet. Nullam leo ligula, efficitur et mattis vitae, malesuada a risus. Nulla non vehicula urna. Praesent in ligula et ipsum condimentum consectetur a non nunc. Cras porttitor pretium felis at accumsan. Duis tempor gravida mauris, id molestie erat volutpat nec. Mauris dictum cursus metus, id lacinia leo dignissim pellentesque.

Phasellus et commodo felis. Cras vel purus non lacus dignissim facilisis sed sit amet dolor. Duis dictum, ante sit amet vestibulum aliquet, magna nisl tempus elit, et condimentum lectus lectus non ante. Vivamus interdum, arcu eu congue ornare, nisl ligula fermentum augue, ut ullamcorper ipsum magna a ipsum. Nunc sit amet dui eget mi consequat efficitur. Curabitur malesuada nec nunc a sodales. Phasellus eleifend quam varius, auctor urna at, ornare nulla.

Donec dapibus sit amet lacus nec sagittis. Pellentesque in eros nec nisi condimentum sodales quis quis lectus. Phasellus lobortis mauris et est placerat, id mollis odio sollicitudin. Praesent non elit massa. Nam placerat eleifend eros ut dapibus. Donec id rutrum ipsum, vel imperdiet ex. Nulla porta tortor quis dui lacinia elementum. Nullam convallis lorem magna, eget sollicitudin elit tincidunt sit amet.

Etiam maximus viverra tempor. Curabitur hendrerit nulla in laoreet fringilla. Sed non sem eu sem lacinia pulvinar in ac augue. Cras pharetra justo non ante vehicula fringilla. Duis volutpat eget nibh id volutpat. Pellentesque vehicula justo sit amet luctus blandit. In eu porta sem. Maecenas vel mattis nunc. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur aliquet lorem laoreet, sodales quam non, tincidunt dui. Sed ut nisl eget est semper volutpat. Nam semper elit a ipsum consectetur vestibulum.

Etiam sit amet quam dignissim, porta sapien id, tincidunt urna. Integer nec pharetra erat. Curabitur ut eleifend leo. Duis fermentum volutpat tempor. Ut eu finibus dui. Aliquam erat volutpat. Proin vel hendrerit magna, at aliquet felis. Nulla facilisi. Integer vitae neque eget velit dictum volutpat. Nam viverra, augue ut porttitor volutpat, nisl ex viverra massa, ut dignissim nunc sem non dui.

Fusce rhoncus dui at dolor aliquam, id aliquet ipsum laoreet. Donec feugiat elementum pellentesque. Nullam elit nibh, rhoncus ut accumsan quis, lobortis interdum tortor. Praesent imperdiet, dui nec elementum sodales, velit nisl mattis nibh, et volutpat nisl purus ut dolor. Donec ultrices congue eros, eu venenatis enim vehicula nec. In aliquet ante vitae mi ullamcorper, ac pellentesque nisl pellentesque. Cras blandit est fermentum orci vehicula venenatis.

Phasellus vestibulum iaculis interdum. Etiam in volutpat justo. Donec id varius tortor, bibendum ullamcorper libero. Pellentesque dapibus dapibus metus non faucibus. Phasellus placerat interdum purus. Proin condimentum, velit eu interdum scelerisque, dui dui suscipit lorem, ac accumsan purus lacus eget ipsum. Pellentesque non quam dictum, vulputate purus eget, consequat sem. Morbi metus lacus, finibus imperdiet mi in, convallis mollis libero. Ut quis velit justo. Praesent vitae euismod felis. Suspendisse augue dolor, lobortis eget ultrices non, rhoncus eu purus.

In egestas rhoncus orci in faucibus. Nam fermentum, metus et efficitur sagittis, dui tortor aliquet ligula, id sollicitudin ipsum diam ac turpis. Donec porttitor mi aliquet tortor vehicula pretium. Aenean venenatis tempor nunc in imperdiet. Suspendisse placerat placerat enim in dapibus. Maecenas sed purus tincidunt justo fermentum maximus pretium efficitur urna. Suspendisse consectetur viverra cursus. Morbi quis tincidunt nulla. Nam lacinia porttitor nulla, quis efficitur lectus elementum et. Proin tincidunt, magna sit amet finibus convallis, quam neque efficitur diam, eu lobortis arcu quam non est. Ut posuere ligula turpis, bibendum consectetur augue ultrices nec. Pellentesque in ligula felis. Duis consequat eros augue, sit amet consectetur massa dignissim at.

Quisque lobortis, eros ac rutrum congue, est elit blandit lorem, quis luctus ipsum nisi ut ipsum. Mauris tempus vestibulum semper. Donec vitae lobortis erat, at aliquet orci. Aenean euismod sagittis enim a gravida. Fusce viverra vitae nunc ac porta. Aenean sapien erat, placerat a elit id, placerat sodales neque. Suspendisse condimentum lorem augue, non scelerisque tortor porttitor nec. Sed nibh tellus, tempus id leo lacinia, rutrum dignissim diam. Vivamus rhoncus tellus leo, nec pretium mauris elementum sed.

Proin eget malesuada enim. Pellentesque nec imperdiet mi. Curabitur bibendum vehicula mi, at elementum arcu auctor convallis. Nullam aliquam egestas nulla, sed euismod nisl ultrices in. Suspendisse potenti. Nullam ac orci vel sem varius facilisis in et mi. Donec pulvinar sagittis sem. Etiam scelerisque sem neque, eget vulputate massa eleifend vel.

Nulla vel ipsum velit. Suspendisse eget massa ligula. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus tellus nisl, posuere non massa non, commodo feugiat urna. Nunc a lacinia justo. Nunc consectetur volutpat magna, at lacinia neque gravida eu. Donec at augue rhoncus, sollicitudin nisi vel, venenatis diam. Etiam venenatis suscipit magna convallis euismod. Integer convallis venenatis ex at ultricies. Etiam venenatis et libero a placerat. Nunc in nibh mollis, eleifend lectus faucibus, auctor ipsum.

Aenean id est vehicula, condimentum tellus id, mattis orci. Aliquam vulputate nisl a ex dignissim, vel eleifend mi vulputate. Proin non varius lectus. Vestibulum ullamcorper, massa ut tincidunt imperdiet, ipsum mi venenatis turpis, id rhoncus velit dolor id justo. Vestibulum sed accumsan magna, scelerisque varius turpis. Sed suscipit turpis at elit convallis scelerisque. Aliquam erat volutpat. Nunc malesuada blandit sem, non suscipit nisi volutpat sit amet. Cras dignissim mattis elit, et fermentum risus volutpat eget.

Maecenas ut lectus felis. Proin nisl lacus, accumsan nec velit nec, condimentum malesuada purus. Morbi ornare hendrerit urna, sit amet suscipit purus sodales quis. Praesent vel quam sed erat aliquam pulvinar ut eu sapien. Donec vel lorem id dolor blandit vehicula ac a felis. Integer eget purus lacus. Ut finibus, leo sed congue pharetra, nulla sem vehicula eros, id semper risus dui id ex. Sed bibendum tristique fermentum. Nunc et tortor faucibus, fringilla ipsum a, ullamcorper quam. Nam convallis sapien in sem iaculis, ac egestas risus tempor. Quisque placerat bibendum dolor blandit efficitur. Donec non tempus eros.

Donec non nunc sit amet ex imperdiet semper vel vel nibh. Pellentesque a velit sed massa eleifend porttitor non sit amet turpis. Sed ex quam, porttitor a quam quis, ornare finibus tellus. Nulla dignissim tempor elit, sit amet egestas enim sagittis a. Nunc massa nibh, convallis sed neque non, lobortis facilisis ligula. In hac habitasse platea dictumst. Quisque sit amet vestibulum orci. Pellentesque imperdiet est erat, sed tincidunt dui tempus ac. Nullam auctor neque elit, et lobortis velit viverra in. Quisque sed ante congue neque tempus imperdiet eu in lorem. Morbi volutpat imperdiet ullamcorper. Nullam tortor nibh, consequat quis nulla ac, porttitor commodo diam. Curabitur aliquam erat purus, ut porttitor dolor feugiat ac. Nulla pellentesque aliquam magna. Phasellus aliquam porttitor felis ut mattis.

Nullam eu lorem consectetur, luctus dui eget, maximus leo. Duis lacus ex, molestie ac dapibus non, mollis vestibulum lectus. Ut vitae lobortis justo, quis tempus quam. Cras posuere magna et facilisis lacinia. Fusce laoreet purus in enim egestas, non suscipit urna efficitur. Vivamus consequat ante eu ex laoreet, sed luctus tortor condimentum. Sed porttitor eros id purus pellentesque venenatis nec quis lectus. Fusce congue est placerat ex vestibulum porta. Proin sed vulputate sapien. Nunc molestie odio placerat lacus volutpat, et imperdiet ipsum luctus. Aliquam in magna quam. Fusce a purus quis ex sollicitudin varius. Duis et turpis vehicula, vehicula ante fringilla, blandit est.

Nulla tincidunt facilisis egestas. Mauris accumsan ullamcorper ullamcorper. Integer id augue at sapien mollis bibendum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Etiam vel euismod justo. Nam laoreet mi justo, vel sollicitudin quam vestibulum eget. Aenean accumsan commodo mi at scelerisque. Nam condimentum tincidunt arcu, quis ullamcorper ipsum egestas non. Cras eu tortor blandit, consectetur magna ut, fringilla eros. Aliquam id diam nec sapien bibendum lacinia vel ac eros. Sed mattis non est ac dignissim. Sed consequat luctus vestibulum. Fusce sed quam dictum, accumsan tortor eget, mattis turpis. Sed felis felis, ultrices quis auctor vitae, interdum sit amet nulla. Nam egestas turpis eget risus blandit, mollis luctus urna eleifend. Vivamus consectetur dictum felis, volutpat dictum augue bibendum sed.

Etiam faucibus erat at mi laoreet condimentum. Integer consectetur aliquet porta. Vestibulum quis luctus quam. Nulla in ex neque. Donec nec fringilla nunc. Vivamus quis nibh at arcu imperdiet malesuada quis sed tellus. Aenean fringilla erat quis felis convallis pellentesque.

Quisque porta purus ac porttitor hendrerit. Duis consectetur est lacus, quis tincidunt ipsum porttitor eget. Nulla purus nisi, luctus sit amet nulla eget, dignissim gravida metus. Sed eget semper tellus, in accumsan massa. Integer id leo accumsan, bibendum nulla at, suscipit nulla. Etiam facilisis mattis erat, sed efficitur erat ultricies at. Sed augue odio, cursus in cursus eget, scelerisque nec lorem. Quisque in eleifend ante. Aliquam metus justo, maximus non quam nec, cursus porttitor nibh. Ut quis purus et sem tempor laoreet non id velit. Integer tempus finibus metus, ut pharetra enim pellentesque sed. Nullam egestas risus diam, non ornare tortor sollicitudin et. Aenean ac commodo arcu. Ut sagittis felis non ipsum vestibulum, eget egestas ex pulvinar. Quisque lectus ex, accumsan vitae enim sed, vestibulum lobortis massa. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

Suspendisse eleifend ligula quis efficitur vestibulum. Proin consectetur varius dolor, sagittis porta felis scelerisque vitae. Aliquam aliquam mollis nulla non posuere. Phasellus quis nibh et orci aliquam tristique eu quis turpis. Nulla fermentum tellus vitae elit luctus, efficitur iaculis nisl dignissim. Fusce lectus enim, aliquam nec laoreet vel, semper non mauris. Praesent consectetur pulvinar elementum. Morbi in semper libero. Fusce eget purus eu eros vulputate scelerisque a vehicula mauris. Vivamus porttitor ullamcorper tortor sit amet ullamcorper.

Integer iaculis dolor augue, sed tincidunt neque faucibus at. Integer imperdiet nec sapien id fermentum. Quisque elit orci, malesuada a feugiat quis, suscipit id tellus. Integer fermentum neque vitae turpis laoreet, quis scelerisque nibh venenatis. Curabitur ultrices ex eu nisl pulvinar auctor. Donec et vehicula metus. Aliquam consectetur at arcu eget interdum. Nunc eget nulla eget diam mollis fermentum et ut dolor. Fusce id arcu vitae quam condimentum bibendum at ut nunc. Quisque eu ante mattis, interdum enim nec, ullamcorper nisl. Mauris in ante vel neque tincidunt vulputate nec nec augue. Curabitur fermentum sem sollicitudin, sagittis nibh a, malesuada mi. Cras et diam sapien. Maecenas tempus tincidunt dolor nec mattis. Duis eleifend elementum finibus.

Fusce id urna molestie, condimentum diam in, rhoncus sem. Nullam et sagittis ante, id tincidunt risus. In sed elementum ex, sit amet gravida arcu. Integer leo erat, elementum at justo ac, rhoncus tincidunt nunc. In erat mi, ullamcorper ac arcu id, interdum cursus leo. Nulla tincidunt rhoncus sem, congue fringilla erat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla lobortis dapibus laoreet. Phasellus eget nisl aliquet justo posuere ultricies molestie nec erat. Pellentesque consequat rhoncus leo a condimentum. Curabitur at odio vitae justo facilisis placerat sit amet at lacus.

Donec laoreet libero consequat felis iaculis posuere. Sed quis magna non libero rutrum congue ut vitae libero. Morbi dui augue, luctus at dapibus ac, porta sed arcu. Nulla vitae neque nec enim maximus placerat. Suspendisse potenti. Vivamus enim massa, aliquam fringilla iaculis sit amet, pulvinar vel felis. Morbi risus dui, luctus ac velit vitae, condimentum malesuada lacus. Donec tincidunt ac tellus eget viverra. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam ultricies vel elit eget ultrices. Praesent malesuada vel mi ac molestie. Fusce tincidunt placerat libero et finibus. Donec sodales justo vel ornare dapibus. Fusce molestie aliquet tortor, dignissim vehicula magna venenatis vitae.

Vestibulum porta enim nec justo cursus, in consequat risus malesuada. Nullam ornare orci nisi, a bibendum tellus aliquet sit amet. Pellentesque vel sollicitudin purus. Suspendisse accumsan dui ut aliquet eleifend. Praesent volutpat libero consequat, gravida nisi quis, pharetra leo. Donec feugiat velit at ante viverra viverra. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus convallis felis massa, at posuere sem suscipit et. Vivamus eu mi et metus maximus vulputate vitae non mi. Integer consequat magna eget efficitur ornare. Suspendisse potenti. Vivamus vehicula mi facilisis viverra semper.

Aliquam hendrerit massa at facilisis scelerisque. Nullam in nibh rhoncus, eleifend massa hendrerit, ullamcorper augue. Nunc nec diam sagittis, vehicula tellus sed, efficitur dui. Proin scelerisque dolor enim, tristique elementum ligula commodo quis. Mauris sed vehicula lectus. In nec varius nunc. Etiam hendrerit, ligula id tristique accumsan, lacus erat fringilla ex, sed viverra dolor dui et magna. Quisque venenatis dui id ante imperdiet, vitae porta leo interdum. Maecenas ornare eros in ipsum iaculis, at maximus leo pulvinar. Praesent efficitur, elit non rutrum fringilla, lorem odio dignissim nisl, quis convallis dolor magna ac nibh. Aliquam erat volutpat. Morbi a tortor vitae massa finibus cursus at ac turpis.

Aliquam gravida a magna at hendrerit. Nam est velit, ultrices nec laoreet sollicitudin, tincidunt non orci. Mauris egestas auctor velit non viverra. Nullam semper vulputate sodales. Vivamus vulputate quis erat sit amet imperdiet. Phasellus a nulla faucibus, mattis dolor eget, convallis mauris. Phasellus sem ante, tincidunt id lorem eu, placerat facilisis ante. Aliquam erat volutpat. Mauris et neque nulla. Mauris quis arcu consectetur, tempus neque ut, egestas dolor. In non condimentum sapien, ut imperdiet metus. Aliquam varius accumsan massa, gravida pulvinar est.

Quisque lobortis accumsan est sit amet lacinia. Nunc nisi mauris, sodales vel metus vitae, mattis feugiat massa. Nam pharetra luctus egestas. Nulla molestie quam vel mauris placerat, vel euismod sem vulputate. Pellentesque eu scelerisque turpis, at iaculis lacus. Morbi porta ligula bibendum nulla pellentesque, eget luctus nisi laoreet. Integer consequat lorem libero. Quisque et est sem. Praesent egestas nibh lacus, ut molestie lorem elementum non. Mauris volutpat eget felis sit amet finibus. Ut eleifend nisl sed porttitor ornare.

Aliquam et lacus porttitor, imperdiet quam dictum, volutpat justo. Sed accumsan neque vitae mauris iaculis, at iaculis ante porta. Phasellus sit amet metus at orci tincidunt scelerisque in nec lorem. Aliquam a enim non leo rutrum molestie sit amet eu ante. Fusce blandit metus vel lorem hendrerit, at tristique orci ornare. Cras lorem mauris, posuere at mi ultrices, venenatis laoreet elit. Nullam eget feugiat nulla. Proin a hendrerit enim. Morbi consectetur sem non nisl blandit, sed finibus elit rutrum. Cras ut dolor sed turpis viverra posuere. Aliquam sollicitudin mauris a lectus luctus ornare. Nulla facilisi. Maecenas tristique arcu sit amet auctor feugiat. Aenean vel mattis tellus. Suspendisse a purus non nisl ultrices feugiat.

Donec porttitor tristique mauris et luctus. Praesent iaculis elit et tellus venenatis, feugiat posuere est porta. Donec elementum nibh eu dui ullamcorper commodo. Nulla pretium eget nisi a bibendum. Donec consequat nisl quam, et tincidunt nulla molestie ut. Suspendisse bibendum ornare nunc. Etiam vel orci ut lorem luctus ultricies bibendum at nunc. Morbi posuere, ligula eget efficitur elementum, purus sem dignissim elit, in mollis sem massa eu odio. Morbi sem magna, placerat eu mauris sed, condimentum suscipit magna.

In vitae urna tempus, rhoncus velit at, viverra nibh. Proin sollicitudin arcu volutpat sapien consequat consectetur. Nam dignissim turpis eu nisl ultricies, et interdum nisi viverra. Etiam dapibus efficitur mi non mollis. Suspendisse nec mollis nibh. Maecenas non velit leo. Aenean tristique dignissim quam, quis accumsan risus dapibus et. Pellentesque faucibus laoreet lacus, at viverra mi malesuada vitae. Aliquam gravida purus orci, sed feugiat eros dictum sed.

Ut eget urna mollis diam tincidunt consectetur. Donec quis semper magna, ac ultricies ante. Nam dignissim a lectus et sollicitudin. Vestibulum accumsan urna in magna tempus iaculis. Fusce aliquam leo massa, vitae semper tellus blandit quis. Nam sit amet sodales lectus, at sollicitudin orci. Etiam nunc nisi, fermentum vel congue id, facilisis in nibh. Aenean vitae ligula ut mi facilisis eleifend sed a ipsum. Morbi ut dapibus mauris.

Donec condimentum turpis mauris. In consectetur felis eros, sit amet hendrerit nunc vehicula a. Aenean in neque quis ipsum auctor scelerisque. Mauris sed magna id tortor suscipit varius vel vel turpis. In nec porta odio. Donec in ornare justo, quis tincidunt magna. Nam diam metus, congue nec mauris sed, euismod fringilla justo. Vivamus vestibulum turpis vel dictum vehicula. Nunc a felis purus. Duis non eros eleifend, luctus nibh a, lobortis urna. Nunc diam mauris, ornare vitae fermentum et, dapibus a dui. Morbi est erat, mollis a tellus in, luctus commodo sapien.

Nunc fermentum velit at augue vestibulum tempor. Etiam et consequat mauris. Sed dictum velit eget orci accumsan tincidunt. Mauris ac urna in arcu blandit fermentum auctor in augue. Ut enim elit, scelerisque ac elementum eget, egestas eu mauris. Nullam mi arcu, auctor eu feugiat ut, sodales ut sapien. Vivamus gravida, nisl a tincidunt ultricies, est mi pulvinar sem, id viverra tellus tellus a nisi.

Vestibulum congue purus nulla, sit amet aliquet nisi elementum vel. Cras non egestas mi, eu feugiat tortor. In auctor quis odio in volutpat. Proin aliquet fermentum ornare. Cras aliquet ornare neque ut volutpat. Vivamus feugiat luctus tortor. Praesent rutrum dapibus dolor. Aliquam eget eleifend dolor, et pharetra tellus.

Sed congue ullamcorper ante. Aenean fermentum felis eu hendrerit euismod. Quisque facilisis felis ex, sit amet consequat neque ultrices sit amet. Maecenas tincidunt dolor justo, sit amet pellentesque est iaculis id. Vivamus viverra eros nec accumsan ornare. Aliquam varius neque non velit auctor, id egestas magna viverra. Praesent pellentesque velit ut risus fermentum, nec aliquet lectus sagittis. Donec in massa ac lorem molestie vulputate. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

Proin dolor orci, laoreet ut porttitor vel, blandit eget leo. Suspendisse semper velit at placerat sagittis. Sed ornare vitae dolor congue efficitur. Praesent finibus velit at tempus pellentesque. Nullam nec dolor magna. Nullam tincidunt eros purus, et mollis urna commodo eget. Sed faucibus ligula nec dui interdum, vitae facilisis odio scelerisque. Suspendisse fermentum porttitor ligula, et dignissim sapien bibendum ut. Etiam libero felis, euismod at quam non, sodales porttitor tortor. Vestibulum elit risus, porta eget posuere accumsan, rutrum at sapien.

Donec quis vehicula nisl, aliquam commodo augue. Interdum et malesuada fames ac ante ipsum primis in faucibus. Duis a felis in nisl rutrum vestibulum. Aliquam interdum sed augue lacinia rutrum. Sed tincidunt lacus eleifend quam molestie, nec iaculis lectus sodales. Ut fermentum sapien erat, eu volutpat eros varius vel. Quisque porttitor, neque a eleifend viverra, dui risus malesuada dolor, a molestie metus ligula quis sem. In dapibus mi et pellentesque porttitor. Quisque nec justo sit amet lectus molestie vulputate. Nam ultrices dolor ut gravida viverra. Duis fringilla augue metus, vitae dignissim tortor tristique sed. Sed eu ante vulputate, tempus ipsum vitae, egestas velit. Aenean euismod tellus a imperdiet egestas. Quisque neque nisi, sagittis non scelerisque id, fringilla blandit enim. Aliquam lobortis, libero ut mattis sodales, nibh neque malesuada ligula, vel ullamcorper sem sem nec neque.

Sed a eros nibh. Aenean id libero tellus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sodales augue a lectus condimentum iaculis. Nulla imperdiet rhoncus posuere. Donec nec facilisis sapien. Aliquam quis magna eget nisi molestie egestas. Duis at risus in sapien suscipit facilisis in eu tellus.

In hac habitasse platea dictumst. Nam aliquet dapibus libero vitae tristique. Curabitur aliquet eu urna mattis rutrum. Ut at ultricies ex, sed sagittis lacus. Donec erat eros, finibus sit amet ante ut, bibendum dapibus enim. Donec sagittis leo tellus, facilisis commodo velit rutrum ut. Praesent finibus pretium ex, vel eleifend tellus lacinia nec. Cras eget leo congue, vehicula est sed, pellentesque elit.

Maecenas tincidunt sit amet ex ac vehicula. Quisque nec varius metus. In hac habitasse platea dictumst. Aenean orci ipsum, egestas et velit sit amet, iaculis aliquam massa. Nam dignissim ipsum eget nisl pellentesque, eleifend rutrum nunc fermentum. Sed mollis ornare augue, ac bibendum tellus vehicula ut. Sed quam arcu, lacinia aliquet tincidunt vel, lacinia et libero. Vivamus in est suscipit, porttitor mi nec, molestie eros. Fusce efficitur eros nunc, quis ullamcorper mi tincidunt ac. Nullam rutrum tempor tempus. Quisque posuere interdum ante a pharetra.

Morbi quis auctor mauris. Morbi scelerisque, ligula a accumsan suscipit, sem nulla ullamcorper est, ut mollis lacus lectus at velit. Duis elit sapien, facilisis nec placerat et, lacinia nec sem. In tincidunt vehicula nibh ut tincidunt. Integer pellentesque et nisl et rhoncus. Ut pretium ac ante at tincidunt. Etiam quis feugiat est, nec convallis risus. In et nisi iaculis, sollicitudin urna eu, aliquam eros.

Maecenas lacinia massa a metus placerat, vitae iaculis leo condimentum. Pellentesque egestas efficitur lorem, quis congue arcu egestas ullamcorper. Quisque scelerisque, diam eu pretium varius, nisl lacus maximus sapien, et viverra nunc metus eu orci. Phasellus ullamcorper eu nulla a aliquam. Nullam vel finibus tellus, vel consequat magna. Vestibulum ut rhoncus magna. Nam scelerisque porta turpis. Nam iaculis urna sapien, nec porta nibh semper non.

Sed pharetra ex eu fringilla pretium. Praesent convallis, odio in mattis pharetra, ipsum augue dictum dui, quis semper erat eros a tortor. Phasellus finibus, elit a venenatis egestas, mi enim sollicitudin felis, non auctor metus tortor eget purus. Fusce pharetra et metus et tempus. Donec sollicitudin tortor a euismod laoreet. Praesent dictum neque urna, eu lobortis justo facilisis ut. Donec non nunc in tortor suscipit imperdiet id quis metus. Maecenas dignissim blandit justo ut volutpat. Praesent elementum, ante id malesuada ullamcorper, urna eros finibus turpis, nec finibus neque neque eget neque. Donec dapibus congue tortor, non viverra mi mollis quis. Nam porttitor, nulla vel auctor ultricies, sapien diam dapibus nibh, id tincidunt dolor urna eget mauris. Aenean mattis ipsum diam, eu rutrum sem aliquet id.

Nulla in fringilla est, vel semper sapien. Duis quis sapien orci. Vestibulum sit amet laoreet odio. Maecenas aliquet quam sed magna imperdiet lacinia. Praesent condimentum arcu at metus scelerisque mattis. Donec sagittis aliquam hendrerit. Ut dictum justo eget augue dapibus interdum. Cras porttitor tristique massa, vitae pulvinar urna pretium dapibus.

In eu ex sed neque accumsan suscipit. Suspendisse potenti. Sed molestie tortor ac fermentum congue. Praesent eleifend felis aliquet mollis porta. Proin odio magna, hendrerit ac velit nec, consectetur molestie nisl. Nam tempus nunc nec mattis dictum. Maecenas gravida libero nec massa fringilla blandit. Duis ante urna, aliquam non ante non, aliquam iaculis magna. Nullam elementum ultrices leo luctus volutpat. Morbi ac ex mi. Curabitur eleifend non nisl vel fermentum. Fusce at pretium dui. Aenean molestie ullamcorper ante, in pretium lorem pharetra quis. Morbi fermentum mauris quis dolor tristique condimentum.

In ultricies ornare nulla, quis venenatis risus ultrices ac. Nam tristique tempor est, in mattis erat. Cras vitae diam at magna suscipit finibus et ut orci. Donec at tellus finibus, aliquet velit vel, ultricies tellus. In euismod neque orci, nec porta felis sollicitudin placerat. Vivamus et eleifend neque. Nulla nec laoreet erat. Quisque vehicula finibus ex sed pulvinar. Vivamus mollis sapien tellus. Ut rutrum commodo dolor vel elementum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean pulvinar fringilla tellus sed placerat. Nullam eleifend suscipit feugiat. Morbi pretium tempor vehicula. Nulla ornare nibh purus, ut vulputate mi facilisis id.

Donec maximus nisi ut urna pulvinar feugiat. Vivamus nisl sem, gravida id mattis eget, suscipit accumsan sapien. Duis mattis accumsan mauris, et eleifend elit convallis eget. Curabitur non imperdiet urna, id lobortis massa. Donec fringilla hendrerit arcu molestie feugiat. Curabitur viverra feugiat pretium. Fusce et lacus at velit tincidunt vehicula at elementum tortor. Suspendisse massa leo, dignissim nec tincidunt at, faucibus sit amet quam. In tempor, tellus a lacinia pharetra, urna turpis semper ante, ut tincidunt leo nibh sit amet erat.

Sed scelerisque velit neque, et consectetur lectus eleifend id. Integer accumsan ex a felis facilisis, et lacinia diam euismod. Maecenas justo ipsum, facilisis id eros facilisis, faucibus sagittis sem. Maecenas gravida lorem pellentesque dui malesuada, at mollis mauris rhoncus. Proin auctor fermentum commodo. Mauris volutpat, nunc in pellentesque rhoncus, leo tortor suscipit nunc, at aliquet velit diam eget lectus. Sed tincidunt vel elit a efficitur. Integer at ultricies elit. Aenean porta sollicitudin sapien, eu porta metus dictum sit amet. Vivamus eleifend id sem sit amet lacinia. Duis placerat consectetur quam non sodales. Curabitur elementum mi diam. Ut eget feugiat metus. Curabitur id purus ac dolor eleifend feugiat non vel orci. In a interdum neque.

Fusce vel sollicitudin metus. Praesent porttitor, libero quis facilisis rhoncus, orci neque imperdiet risus, quis malesuada nisi nulla eget turpis. Praesent a ex nec magna pharetra euismod. Mauris et suscipit nulla. Etiam luctus nibh tellus, eget pellentesque metus faucibus vitae. Vestibulum mollis augue mauris, facilisis viverra nisl scelerisque eget. Proin faucibus sagittis dolor ut accumsan. Vestibulum quis pretium quam. Donec at ornare sem, nec imperdiet arcu. Quisque quis purus est. Nullam vestibulum libero eu est luctus, vel hendrerit nibh aliquam. Integer iaculis, est non fermentum ultricies, ligula ipsum hendrerit augue, id pellentesque ligula lorem a diam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

Maecenas volutpat sem ac odio vehicula eleifend. Nunc diam lacus, euismod ut hendrerit tincidunt, venenatis sed elit. Etiam blandit neque ex. Nunc in lorem in orci ornare sagittis. Praesent ac tellus bibendum, interdum ipsum eu, congue nibh. Aliquam fringilla condimentum augue vel hendrerit. Nullam metus est, porta id justo vitae, cursus sollicitudin nisl. Mauris tincidunt vestibulum augue, sed imperdiet felis sagittis non. Curabitur maximus turpis pulvinar sem ultricies, sed pulvinar erat pharetra. Vivamus ut lacinia nisl. Mauris dictum, purus eu molestie lobortis, leo nisi vulputate risus, sed commodo nulla enim vitae nisi. Nullam ut lectus vel ligula facilisis pretium. Sed sit amet ligula quam. Donec convallis vitae tortor eget viverra.

Cras ex elit, posuere id fringilla quis, finibus nec arcu. Integer laoreet eget diam ut consequat. Proin elementum ac urna eu venenatis. Vivamus cursus justo quis quam tempor blandit. Cras convallis nec mauris at ornare. Proin dapibus porta consequat. Nunc volutpat consequat sem eget viverra.

Vestibulum vestibulum vel sapien eu tempor. Morbi non magna malesuada, aliquam odio eget, posuere neque. Donec ut hendrerit odio, non bibendum libero. Maecenas tempus pretium ligula id volutpat. Sed nec suscipit nunc. Maecenas vulputate risus urna, at vestibulum est varius id. Aenean leo nulla, porta in ante sed, auctor bibendum nisi. Nam nec tristique justo. Donec finibus ac eros ac pretium. Aenean imperdiet pretium purus, quis ultricies metus porttitor ut. Quisque odio eros, efficitur ut pretium vel, ornare at erat. Fusce gravida risus vitae turpis hendrerit, non placerat justo tincidunt.

Maecenas et porttitor nulla, in finibus eros. Nulla tincidunt ex sit amet velit suscipit laoreet. Aliquam tempor blandit elit nec mattis. Phasellus nibh lorem, laoreet id lorem eu, rhoncus rutrum eros. Nulla imperdiet tortor in lacus malesuada, vel fermentum erat placerat. Vivamus non fringilla velit, a scelerisque sem. Suspendisse malesuada sapien neque, sed tristique arcu maximus eget. Donec augue dolor, aliquam ut ligula ac, aliquam mollis arcu. Nulla vehicula euismod aliquet. Proin vitae semper eros, ac laoreet lacus. Donec consequat consequat volutpat. Donec fermentum, metus vel viverra posuere, metus est dapibus nibh, nec ultricies neque orci non orci. Vivamus dapibus mattis consequat. Proin blandit maximus sollicitudin.

Mauris aliquet feugiat nulla vel vehicula. Phasellus vitae porttitor nisl, a pulvinar libero. Morbi condimentum eu orci at fringilla. Donec faucibus consequat faucibus. Mauris nec ipsum risus. Morbi eleifend dictum est vel tristique. In aliquam sollicitudin augue quis scelerisque. Integer porta lectus in eleifend imperdiet. Vivamus mollis ligula non ligula tincidunt gravida. Cras pharetra nunc sed orci commodo, id rhoncus erat maximus. Donec convallis est sed maximus vulputate. Interdum et malesuada fames ac ante ipsum primis in faucibus.

In eu dictum diam. Mauris lacinia, eros vel tincidunt placerat, mauris justo venenatis ante, ut elementum metus massa blandit justo. In non sem quis tellus interdum vehicula eu et massa. Nunc facilisis metus sed neque condimentum euismod. Sed quis accumsan velit. Mauris eget dolor maximus, tempor lorem ac, aliquet risus. Integer porta ornare leo. Ut dignissim lorem turpis, vel ultrices dui laoreet vel.

Curabitur porttitor in lacus et porta. Nullam sed risus efficitur, bibendum tellus ut, malesuada lectus. Nulla sed mi a nisi porttitor porta. Nunc sed nisi mollis quam mollis lobortis maximus sit amet nibh. Phasellus vehicula diam consequat eleifend lobortis. Donec feugiat nisl vel sodales ultrices. Nunc dolor magna, semper eget tincidunt ut, luctus vitae risus. Proin lacinia leo eget ipsum venenatis dapibus.

Sed turpis tellus, convallis non euismod sit amet, vehicula non ante. In hac habitasse platea dictumst. Maecenas placerat ex in dignissim dignissim. Aliquam erat volutpat. Aliquam sed varius risus. In in ligula ex. Curabitur convallis dapibus mi, sed vehicula magna pellentesque vitae. Vestibulum lacinia, augue et euismod accumsan, lacus tellus pulvinar eros, sit amet mollis dui ipsum commodo lacus. Morbi convallis elit metus. Donec non tellus eget risus bibendum luctus eu et ex. Curabitur vitae vehicula mauris. In vestibulum venenatis sapien eget hendrerit. Etiam interdum ex sapien, non placerat metus rutrum vitae. Proin finibus faucibus lacus in faucibus.

In rhoncus fermentum malesuada. Nunc ac sapien eget neque faucibus eleifend sit amet laoreet nisi. Etiam rhoncus lobortis dui, sit amet ultrices orci hendrerit sed. Nulla tellus enim, ultricies at mattis ac, malesuada id tortor. Nulla sed ante eros. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Proin in purus a lorem pulvinar ullamcorper. Etiam a hendrerit justo. Suspendisse orci mi, blandit sit amet quam vel, consequat posuere neque. Cras tempor vestibulum magna ut laoreet. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed condimentum nisl ligula, non rhoncus ante tincidunt id. Sed at sodales tellus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Nullam ultrices, mauris eget cursus molestie, libero felis tempor dolor, consectetur scelerisque arcu libero ut turpis. Donec at nulla tincidunt, feugiat turpis ut, tempus erat. Mauris quis magna accumsan, accumsan sapien id, tempus turpis. Aenean ornare et nunc nec mollis. Nulla auctor vulputate turpis id imperdiet. Vestibulum neque tortor, dictum vitae tincidunt in, venenatis quis lectus. Donec facilisis malesuada sem, at gravida turpis posuere in. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam at erat et metus condimentum molestie sed ut est. Quisque ac tincidunt arcu, ut tempor est. Nunc vitae tellus bibendum, laoreet metus id, lobortis ipsum. Cras eu augue accumsan, volutpat lacus at, congue mauris. Mauris in orci suscipit, vestibulum enim et, fringilla risus. Vivamus eu leo vitae nunc egestas suscipit. Integer volutpat dui sed quam facilisis aliquet. Donec pulvinar, diam in vulputate tempor, diam est efficitur ex, vel sagittis mauris turpis id felis.

In condimentum convallis magna, in bibendum urna sodales vitae. Pellentesque interdum turpis eu tempus rutrum. Ut semper rhoncus tempor. Sed egestas, ante id efficitur ultricies, arcu dui ullamcorper eros, et malesuada sem est eget diam. Sed a enim cursus, pharetra nunc ultrices, scelerisque sem. Vestibulum sed ultrices est. Donec urna ante, pulvinar non odio eget, tempor venenatis augue. Phasellus euismod libero sed lectus lacinia, eu volutpat erat viverra. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed ornare lacus id tincidunt lobortis. Cras vel posuere ante, eu sagittis ipsum. Donec hendrerit ex massa, sit amet molestie augue pretium quis. Nam tincidunt facilisis mauris, volutpat imperdiet urna venenatis vel.

Duis iaculis pharetra tempus. Cras vitae dignissim augue. Nulla mattis malesuada suscipit. Etiam tincidunt egestas elit nec cursus. Ut convallis ipsum a vulputate convallis. Mauris dapibus egestas turpis ut malesuada. Ut bibendum et nisi nec tempor. Etiam libero nisi, viverra ac lectus pharetra, ornare lobortis lorem. In semper imperdiet nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; In et justo turpis. Donec in tellus quis magna iaculis commodo. Pellentesque volutpat laoreet consectetur. In sodales nisi maximus lectus pellentesque, a varius erat fermentum.

Aliquam erat volutpat. Morbi egestas efficitur commodo. Sed placerat nec massa eu mattis. Donec mattis mauris ac risus vestibulum vulputate. Maecenas tempor sapien vel mattis pharetra. Nam ultricies nisl consectetur dolor luctus pellentesque. Quisque malesuada orci at nulla consequat pulvinar. Donec dignissim, erat sed malesuada cursus, orci nibh aliquam justo, non interdum libero dui in libero. Donec sit amet libero rutrum dolor mollis vestibulum ac at risus. Morbi blandit euismod pretium.

Cras consequat eros vel efficitur mollis. Proin molestie lobortis dui, in malesuada augue convallis sed. Etiam ac ex vitae nisl scelerisque venenatis. Vestibulum et elementum lorem, at ultricies ligula. Mauris sit amet magna in libero viverra pulvinar vel et libero. Proin sed metus et arcu ullamcorper dapibus sit amet et quam. Morbi fermentum vitae ipsum id pharetra.

Curabitur finibus sodales mollis. Nam maximus neque accumsan, vulputate felis ac, porta nunc. Pellentesque sed mi eu quam condimentum egestas in a urna. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut sed consectetur neque. Sed vitae arcu sit amet sem lobortis rutrum. Curabitur ac accumsan leo. Nunc maximus ipsum et nibh consectetur, quis semper nisi pellentesque. Integer luctus elit blandit dignissim dictum. Nulla volutpat sed quam ut fermentum. Quisque dignissim quam id dolor efficitur, sit amet maximus lacus tristique. Donec erat diam, tincidunt in convallis at, blandit ac mauris.

Cras ullamcorper consectetur leo ac fringilla. Curabitur at pellentesque lectus, vitae vehicula sapien. Quisque varius tincidunt justo ut ultrices. Curabitur quam est, maximus sed pretium id, posuere vitae tortor. Integer commodo, libero non porta tincidunt, erat lacus congue massa, semper malesuada ante risus eu quam. Cras vitae scelerisque nunc. Pellentesque metus mi, posuere at gravida vel, iaculis vitae ante. Quisque sed ipsum sit amet ante feugiat fringilla. Aenean vitae metus eget ligula finibus dapibus. Vivamus faucibus justo sit amet sapien consequat tincidunt. Mauris dapibus at quam interdum fringilla. Phasellus sit amet ex facilisis, congue ligula at, commodo arcu. Vestibulum pulvinar consequat ultrices. Pellentesque facilisis scelerisque velit, sit amet posuere enim finibus euismod. Vestibulum a felis vitae justo blandit rhoncus ac quis tellus. Proin tincidunt felis diam, commodo scelerisque lorem finibus quis.

Donec eros augue, mollis et dui ac, pulvinar dapibus tellus. Ut laoreet lorem ut ultricies laoreet. Sed imperdiet libero urna. Vivamus dignissim erat eget turpis egestas, id sollicitudin lacus suscipit. Pellentesque blandit accumsan augue, nec molestie felis tincidunt non. Nulla risus mi, sollicitudin dapibus nisi et, faucibus ultrices erat. Sed ac sodales justo, in tincidunt felis. Nunc sodales a ligula sit amet maximus. Vestibulum malesuada felis ut ipsum imperdiet, id dictum purus auctor. Nullam a sem sollicitudin, laoreet erat id, auctor velit. Sed mollis, magna in pretium interdum, mi urna vulputate purus, et suscipit mi erat vitae massa. Vestibulum augue odio, dictum ac est non, venenatis hendrerit sapien. Mauris tincidunt arcu arcu, a hendrerit lacus tempor nec. Sed at erat libero. Duis convallis pretium nisi, ut tempus dolor molestie quis. In ac ipsum accumsan, fermentum augue ac, posuere magna.

Morbi rutrum lorem ante, in feugiat quam semper at. Suspendisse ex dui, posuere id tellus quis, maximus ornare dui. Mauris ultrices ante aliquet lorem molestie suscipit. Nam rhoncus nulla ut nibh laoreet, semper congue mi ornare. Cras quis dui eget magna bibendum sollicitudin id in eros. Phasellus fermentum arcu ac augue dignissim, nec luctus massa tempus. Morbi sit amet risus fringilla, auctor dolor tincidunt, commodo turpis. Morbi quis turpis eleifend, bibendum orci condimentum, iaculis leo. Ut scelerisque erat id risus lacinia viverra. Maecenas quis hendrerit turpis, id congue ligula. Ut tellus ligula, sodales quis venenatis venenatis, vehicula ac felis. Suspendisse posuere hendrerit mi vitae fermentum. Curabitur cursus, nisl vel pharetra vulputate, velit neque malesuada massa, vitae aliquet purus nisl vel dui. Aenean id efficitur velit.

Etiam viverra est ut tortor consectetur, quis dignissim dolor euismod. Aliquam euismod quam at commodo convallis. Aenean sagittis efficitur tellus. Vestibulum nec porttitor eros, et pellentesque ante. Phasellus ut convallis metus. Integer tempor eu felis pellentesque mollis. Nunc ut ultricies lorem. Pellentesque malesuada interdum lectus, vel viverra mi pretium facilisis. Mauris eu massa eleifend, viverra lacus ut, faucibus est. Vivamus ac posuere mi, a ultrices lorem.

Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed neque libero, posuere et enim eu, laoreet facilisis enim. Nunc eleifend lectus vitae tortor dapibus faucibus. Donec quam urna, interdum sed lobortis vel, feugiat ac diam. Curabitur rutrum est eget magna dignissim feugiat. Sed felis augue, lacinia a eros non, efficitur mollis odio. Nullam ac placerat orci, at tempor dui. Pellentesque erat quam, vulputate vel tellus at, gravida fringilla quam. Curabitur ac leo eu lorem lacinia tristique. Morbi et urna et purus dictum imperdiet.

Ut fringilla blandit lectus, non finibus turpis dignissim et. Proin vitae orci nec justo consectetur porttitor. Quisque consectetur felis a purus rutrum, eu maximus nisi rutrum. Donec dignissim, velit ac efficitur condimentum, nulla tortor placerat augue, in eleifend arcu purus in lectus. Aliquam mollis mollis nibh, sed pretium ex. In nec urna arcu. Nunc hendrerit lectus ut auctor posuere. Praesent suscipit ante ut tellus porttitor sagittis. In hac habitasse platea dictumst. Nunc sagittis ligula neque, sed lobortis sapien convallis ac. Pellentesque porttitor justo lacus, eu vehicula odio condimentum ac. Fusce porttitor convallis venenatis. Nullam dolor eros, tincidunt malesuada felis vitae, commodo gravida lorem. Fusce libero ligula, viverra ac quam ut, finibus tempus tellus.

Suspendisse in rutrum arcu. Nam maximus, lorem at interdum maximus, erat diam faucibus nisi, nec pulvinar eros tellus et tortor. Nunc sagittis sem id ultricies ultricies. Sed euismod, tortor a condimentum pellentesque, sapien tortor tempus tellus, sed iaculis augue neque vel velit. Ut non sem blandit quam condimentum placerat eu a neque. Phasellus suscipit ipsum nibh, eu aliquet nunc sollicitudin eu. Cras tristique enim odio, id interdum metus vulputate vitae. Curabitur erat sem, dictum id arcu nec, aliquam maximus metus. Sed suscipit condimentum velit ullamcorper pharetra. Cras pulvinar, lacus non maximus porttitor, urna sapien tempus magna, id fermentum erat orci vel magna. Ut id auctor turpis. Proin eget nunc dui. Proin placerat cursus orci sit amet aliquet. Fusce molestie eu diam quis lobortis. Pellentesque dictum nisl hendrerit sapien tempor tristique. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Maecenas faucibus non magna id feugiat. Praesent bibendum lorem eget ex pulvinar efficitur. Curabitur tristique metus quis ipsum finibus egestas. Sed urna tellus, mattis sed turpis non, feugiat fermentum ligula. Ut quis ex vitae erat auctor pharetra. Nulla posuere sapien sed aliquam auctor. Praesent nec dapibus arcu. Quisque ultrices fringilla ante ut sodales. Quisque iaculis sit amet urna ut pulvinar. Donec non ultrices augue, eget accumsan augue. Nulla ac ex a orci vehicula vehicula. Aliquam vitae sollicitudin magna, in auctor metus. Nam malesuada a erat sit amet suscipit. Sed interdum neque at mollis fermentum.

Duis velit ligula, semper eu lorem in, scelerisque aliquam eros. In tempus nibh quam, ac consequat mauris aliquam pellentesque. Vivamus a placerat turpis, sed pretium neque. Etiam convallis, felis sed eleifend facilisis, tortor ipsum pellentesque libero, eu tristique eros risus tempor tortor. Donec ac cursus nisi, at tincidunt arcu. Aliquam eu sem efficitur, euismod urna ac, condimentum magna. Fusce suscipit placerat nisl ut ullamcorper. Vestibulum dapibus fermentum diam, nec euismod nulla placerat a. Nam sit amet risus eros. Etiam volutpat sit amet felis ac vehicula. Praesent vitae lobortis enim. Phasellus augue lorem, consectetur sit amet nisi in, sollicitudin feugiat justo. Nulla in sodales ligula. Fusce gravida ultrices semper. Integer condimentum condimentum lorem ut luctus. Curabitur vulputate lobortis lorem, et iaculis neque convallis quis.

Etiam eu turpis luctus, venenatis neque id, laoreet sem. Donec posuere dignissim dui, tristique pulvinar urna aliquet quis. Vivamus nisl nunc, sagittis et libero a, euismod faucibus erat. Ut sit amet tempor ligula. Nulla eleifend lacus sit amet nisi gravida, eu viverra sem imperdiet. Quisque ac tortor diam. Phasellus elit ex, euismod at nisl ac, fermentum mattis lorem. Proin placerat fermentum massa, vel sagittis urna mattis ut. Curabitur fermentum purus vel justo tristique, sed pulvinar ligula feugiat. Donec sit amet lorem ut dolor pellentesque sagittis sit amet in erat.

Integer ac sem turpis. Proin mollis blandit nunc, imperdiet finibus neque hendrerit in. Nunc at facilisis felis, nec tempus augue. Maecenas finibus gravida magna, eu egestas leo semper eu. Mauris ullamcorper a ante in gravida. Vivamus libero neque, bibendum quis velit in, hendrerit dictum nulla. Nam sit amet mollis nibh. Nunc tempor, ex sit amet finibus luctus, tellus elit bibendum purus, ac dictum sem ex a turpis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dictum hendrerit facilisis. Nullam placerat enim nec dolor vulputate, et tempor nulla pharetra. Etiam sagittis sem vitae elit dictum finibus. Donec non venenatis dui, nec rhoncus mi. In justo erat, elementum sit amet ligula in, aliquet consequat nunc. Pellentesque ut ante nec odio porta iaculis quis sed turpis.

Praesent lacus nibh, vestibulum at risus sed, lacinia maximus augue. Etiam nec est ut tellus pretium ultricies ac quis orci. Vivamus aliquam molestie ante. Aliquam condimentum tristique nibh, eu pulvinar tortor posuere sed. Nunc non magna id turpis finibus condimentum. Pellentesque in elit aliquet, fringilla erat eget, ultrices sapien. Integer sed iaculis purus. Vivamus et urna nisl. Morbi interdum nunc nec urna bibendum tempus. Morbi ut luctus ante, eget ultrices libero. Nunc velit nisl, varius ac scelerisque vel, dapibus a risus.

Sed blandit tortor dui. Quisque venenatis enim ipsum, sit amet fringilla lectus rutrum nec. Nam id consequat elit. Cras vel dignissim arcu. Nulla vitae tellus nulla. Donec sed urna sit amet justo tempor luctus. Vestibulum sem ante, mollis eu laoreet sed, aliquet ac mi. Nunc varius nisi nec blandit tincidunt. Quisque sed ullamcorper justo. Vestibulum luctus tempor quam ut tempor. Fusce varius orci vitae elit interdum, eget aliquet mauris sollicitudin.

Etiam quis risus eros. Suspendisse at libero facilisis quam posuere condimentum. Quisque rutrum ornare odio sit amet ultricies. Nulla mi velit, dictum vitae ipsum eget, bibendum convallis ex. Praesent at aliquet purus, nec iaculis ligula. Suspendisse vel augue non lacus ornare placerat. Duis ac auctor ligula, posuere tempor eros. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam et ipsum ligula. Sed eu nisl odio. Cras sit amet massa sed ipsum varius condimentum id eu elit. Mauris interdum velit magna, vel lobortis lorem commodo a. Morbi augue nisl, ultrices vel ipsum nec, eleifend consectetur lorem. Aliquam ullamcorper pharetra suscipit.

Integer pharetra accumsan nisi eu dictum. Donec euismod pulvinar elit, molestie hendrerit dolor ultrices ut. Aenean nulla elit, blandit eu est ut, laoreet malesuada mauris. Nulla facilisi. Vestibulum commodo sit amet ante eu mattis. Vestibulum id leo eu nulla sodales rutrum non id tellus. Aenean porta efficitur arcu eget consequat. Phasellus quis mauris ut tellus suscipit interdum. Aliquam gravida ipsum enim, sed eleifend nisl gravida id. Praesent vulputate ligula quis libero efficitur vestibulum.

Curabitur sit amet nisl ultricies massa imperdiet ullamcorper. In dignissim, velit id tempus facilisis, ligula sapien porttitor nisi, ut imperdiet ex nunc vel sem. Etiam pretium, ipsum ac mollis tempus, nulla ligula aliquam nibh, rhoncus pretium sapien mauris eu enim. Nulla facilisis orci a tellus maximus, sed feugiat lacus rhoncus. Sed finibus imperdiet libero vel rhoncus. Curabitur fermentum risus malesuada, eleifend quam et, accumsan dui. Proin pharetra eu orci ut auctor.

Aenean sollicitudin orci nec lobortis pulvinar. Nulla facilisi. Mauris viverra urna et dolor maximus elementum. Aenean et dolor elementum, molestie eros a, tempor tortor. Praesent porta tincidunt neque. Vivamus consequat odio nisl, ac faucibus dui vestibulum porta. Donec sagittis mauris id condimentum facilisis. Sed vel neque mattis, pulvinar nunc tempor, imperdiet metus. Nam fringilla purus nec neque blandit aliquet. Praesent lacinia vestibulum nisl quis vulputate. Nunc nulla ante, imperdiet et turpis sed, fringilla sagittis dui. Curabitur dignissim, urna sit amet dapibus facilisis, ante ligula aliquam ligula, in sagittis tellus nunc id ipsum.

Donec libero nisi, interdum non quam id, vehicula luctus quam. Sed lacinia, purus eget eleifend vehicula, mi tortor laoreet mauris, et convallis ligula ipsum quis diam. Suspendisse ac convallis lacus, quis rhoncus eros. Vestibulum tincidunt porta sapien sit amet commodo. Vivamus eu nibh neque. Suspendisse potenti. In luctus vehicula eleifend. Maecenas eget lorem consequat, egestas felis nec, sodales lacus. Praesent a facilisis neque. Vestibulum eu accumsan velit. Sed gravida posuere mauris, eu placerat metus. Maecenas id tortor vitae massa pretium faucibus eu id eros. Integer id hendrerit sem. Sed lectus leo, interdum quis dui nec, ullamcorper cursus ex.

Phasellus pharetra scelerisque ligula, a accumsan turpis euismod eu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec a feugiat metus, non hendrerit ante. Mauris tincidunt id urna sit amet vehicula. Nulla rutrum, nisi non dapibus bibendum, nunc massa tristique ante, eget dapibus ex metus vitae lorem. Aenean vestibulum leo ac augue aliquet gravida. Phasellus euismod sem neque, ut pharetra tellus tincidunt vitae. Nulla facilisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse tempor condimentum auctor. Sed eu sapien arcu.

Praesent odio dolor, scelerisque eget eleifend eu, faucibus ut libero. Fusce pulvinar sollicitudin eleifend. Curabitur pharetra semper mauris, et tempus sapien viverra at. Donec aliquam congue auctor. Nulla sit amet iaculis urna. Aenean sagittis ultrices magna, et mollis ligula blandit vitae. Sed sodales dapibus consequat. Aenean et lectus elementum, vulputate urna ut, aliquam metus. Etiam eget sapien sit amet felis feugiat molestie. Sed et est vel urna lobortis imperdiet vitae in mi. Cras dictum magna in libero pulvinar, sed feugiat odio malesuada.

Donec consequat ipsum orci, ut congue velit pharetra eget. Nunc commodo diam diam, ut laoreet justo feugiat id. Vestibulum sit amet mauris in leo iaculis porttitor. Fusce tempus libero et erat consequat vehicula. Aliquam ultrices ex auctor enim accumsan, elementum finibus sem elementum. Donec quis commodo quam, sit amet imperdiet urna. Nam eget mi eget augue tempus blandit a in velit. Fusce dapibus nisi in dui facilisis, sit amet porta orci aliquam. Ut magna lectus, feugiat quis arcu eu, scelerisque auctor dui. Maecenas lobortis, nisi a bibendum bibendum, tortor tortor rhoncus nisl, nec luctus dolor augue sed eros.

Vestibulum elementum, ligula sed dapibus luctus, est nibh sollicitudin orci, ac venenatis elit elit accumsan lacus. Fusce pretium, risus cursus porta placerat, sapien nisi luctus neque, in commodo quam leo pulvinar neque. Aliquam volutpat porta augue, sed vestibulum ipsum placerat et. Donec fermentum commodo odio eu luctus. In hac habitasse platea dictumst. Vivamus tristique eros neque, posuere pellentesque urna iaculis quis. Etiam ut mi mollis turpis aliquam tempor et sit amet justo. Integer pharetra varius volutpat. Phasellus nisl ex, elementum in mattis a, pharetra et orci.

Morbi volutpat bibendum bibendum. In et congue est. Integer ultrices diam in sapien egestas, et tincidunt lorem congue. Aenean vel massa sed eros commodo faucibus. Ut condimentum feugiat est, nec semper diam sollicitudin nec. Sed pellentesque sed mi at elementum. Integer faucibus, neque in luctus vehicula, risus odio imperdiet velit, imperdiet hendrerit arcu eros id dui. Praesent dignissim mollis magna, sed sodales nisl. Nulla et porta eros. In vel urna id ligula tristique congue. Proin purus diam, mollis at tortor sit amet, auctor dignissim massa. Integer varius elit sit amet est fringilla porttitor. Aliquam a iaculis dolor, quis porttitor enim. Donec sagittis sem id vehicula venenatis.

Morbi tincidunt mi risus, id pellentesque nulla fringilla ut. Donec dapibus nunc ut nulla vehicula aliquet. Fusce faucibus laoreet libero, ac dapibus arcu tincidunt et. Vivamus non sapien non turpis tristique mollis vel ut ligula. Praesent justo lacus, scelerisque ut consectetur feugiat, tristique ac urna. In consequat, ligula sit amet pretium ullamcorper, tellus magna luctus diam, non porta ante orci nec magna. Sed tempor vehicula malesuada. Morbi semper sem ipsum, eu volutpat mi venenatis sit amet. Maecenas lobortis et sem egestas mollis. Sed lobortis risus ut velit pharetra vulputate. Nam faucibus odio vitae lacus consectetur pellentesque. Proin eleifend, libero eget pharetra faucibus, mi nisl molestie justo, id pellentesque enim orci eu erat. Praesent laoreet libero mi, in lacinia purus porta vitae. Nullam vel augue id urna dignissim ornare sit amet sit amet quam. In diam nibh, aliquet non mi eget, aliquet viverra augue.

Suspendisse quis lacus auctor, pretium erat vel, aliquet est. Quisque leo nisl, sollicitudin a dictum aliquet, ultrices ac arcu. Nullam facilisis ultrices felis, sit amet pulvinar nunc sagittis in. In id magna ac massa consequat fringilla. Nunc efficitur hendrerit molestie. Donec vitae luctus mi. Suspendisse maximus est at justo tempus molestie. Aenean eleifend, felis at ullamcorper cursus, tellus augue commodo lacus, nec ornare felis dui ut est.

Phasellus vulputate, dolor at viverra molestie, velit magna aliquet purus, id pulvinar diam erat non ipsum. Etiam bibendum sagittis dui a varius. In vehicula tristique arcu vel tincidunt. Sed feugiat efficitur tellus sed ullamcorper. Suspendisse facilisis, eros sit amet tristique faucibus, neque libero tincidunt tellus, nec pulvinar nulla elit vitae lectus. Nullam ut convallis sapien. Praesent elementum molestie scelerisque. Nullam aliquet convallis magna ac fringilla. Pellentesque auctor dapibus dictum. Nulla sit amet sapien vel turpis posuere fringilla a sed erat. Duis sollicitudin non quam ac rhoncus. Ut vulputate molestie efficitur. Proin posuere risus et ipsum dictum ornare.

Fusce blandit purus sed magna viverra, in vulputate nulla pretium. Aliquam vitae diam magna. Etiam consectetur, massa ac venenatis tempus, nisi nisi varius magna, ut venenatis lectus ipsum eget risus. Pellentesque vel lacus velit. Suspendisse molestie congue velit, gravida aliquam ipsum. Etiam et magna condimentum, feugiat lorem sit amet, blandit nulla. Maecenas posuere fringilla aliquam. Suspendisse laoreet suscipit ante ut rutrum. Curabitur eget finibus metus. Donec eleifend venenatis sem, non laoreet enim tristique eu. Aliquam sodales orci a pulvinar aliquam.

Proin tincidunt, nulla eu vehicula dapibus, ex elit interdum turpis, eu tempor erat ante vitae est. Suspendisse quis ligula nisi. Mauris neque ipsum, sagittis at vehicula et, placerat nec nibh. Suspendisse id hendrerit lorem. Pellentesque ut quam euismod, eleifend diam non, auctor magna. Proin risus urna, vestibulum in tortor ut, pharetra maximus mi. Sed arcu quam, volutpat rutrum feugiat eu, luctus a magna. Phasellus ipsum tortor, finibus sit amet euismod eu, tristique sed ipsum. Vivamus eget ligula eleifend, fermentum sem sit amet, consectetur magna. Nam nec vulputate justo.

Integer scelerisque ipsum vel sapien commodo, sed suscipit odio porta. Mauris ante libero, varius sit amet nisl ac, tincidunt tincidunt tellus. Fusce non leo vitae enim mattis cursus sed non purus. Donec id tortor semper, egestas enim at, mollis nisi. Phasellus feugiat porta pharetra. Fusce sodales luctus urna et mattis. Mauris bibendum pretium elit, at pulvinar libero rutrum ac.

Mauris ac posuere ex. Maecenas auctor tristique tellus, tincidunt lacinia odio mattis sit amet. Donec aliquam ullamcorper nisl ut scelerisque. Pellentesque tincidunt neque ultricies, convallis nisi a, suscipit ex. Praesent dictum sed nisi vitae mattis. In sollicitudin sagittis tristique. Nam rutrum, tortor ut bibendum auctor, nisi urna fringilla odio, sed gravida mauris neque eu risus. Morbi tempor nisl nisi, a mollis odio vehicula sed. Aliquam mattis fringilla velit, vel aliquam justo dapibus scelerisque. Nam elementum aliquam tortor non sollicitudin.

Mauris semper euismod quam, at luctus tortor eleifend quis. Vestibulum faucibus est finibus lectus venenatis pellentesque. Etiam est enim, malesuada sit amet feugiat sed, facilisis non mi. Aenean pretium suscipit imperdiet. Nulla massa odio, ultrices eu auctor sed, suscipit in dui. Suspendisse ac vestibulum sem. Morbi vestibulum porttitor massa, eget sagittis purus luctus ac. Integer vel faucibus tortor. Integer ac nibh ac augue vulputate maximus. Etiam id elit quam.

Aliquam ut dui et felis pellentesque condimentum eget et justo. Pellentesque pharetra, urna eu varius vulputate, nisi urna accumsan augue, id tristique arcu dui a augue. Integer id feugiat ante. Mauris ullamcorper vestibulum cursus. Sed eu enim laoreet felis suscipit egestas. Vestibulum malesuada pellentesque varius. Vivamus sed felis mi. Cras suscipit dolor tellus, at ultrices enim facilisis sit amet. Curabitur lacinia mauris nec elementum semper. Vivamus varius leo a nisi finibus, sit amet ornare elit mattis. Integer quam turpis, placerat vel pretium sed, molestie in mi. Integer tempor tellus at auctor consectetur. Pellentesque in vulputate dolor, at blandit odio. Nunc at tincidunt libero.

Vestibulum sed magna mattis, consectetur ipsum sed, pretium neque. Aliquam fringilla, ante ut vestibulum ultricies, tortor enim aliquam mauris, at euismod turpis lacus sit amet nisl. Maecenas volutpat est sit amet tristique tempor. Phasellus sit amet purus sit amet lorem convallis maximus a ac nunc. Vestibulum augue ipsum, congue sit amet magna sit amet, elementum euismod arcu. Vivamus sed nisi diam. Donec nulla nibh, mollis sed risus eget, scelerisque interdum felis. Maecenas dignissim scelerisque neque eget pharetra. Duis congue lacinia turpis, at dapibus nibh hendrerit sit amet.

Mauris pharetra ornare tempor. Nulla ultricies accumsan arcu in gravida. Etiam elit leo, posuere at lacus vel, mattis vulputate nisi. Vivamus tincidunt justo libero, ac ullamcorper purus viverra et. Vivamus at magna a nisl rutrum ullamcorper eget ac nisl. Maecenas viverra ligula non nisl malesuada accumsan. Integer ullamcorper, felis et iaculis hendrerit, lectus neque maximus eros, id gravida enim augue vitae felis. Quisque sed odio neque. Pellentesque sed nibh eu elit pretium ultrices. Nunc non mattis nibh. Vestibulum quis nisi a lorem rhoncus fringilla sed nec lorem.

Proin id erat et nulla hendrerit dapibus et eu dui. Mauris turpis risus, hendrerit et enim sit amet, mattis blandit nulla. Etiam auctor semper suscipit. Aliquam erat volutpat. Fusce vestibulum tellus sit amet diam finibus, non imperdiet justo suscipit. Phasellus ullamcorper vestibulum arcu non viverra. Donec felis ante, sagittis eu mi sit amet, blandit feugiat metus. Sed mauris lectus, vestibulum ac dignissim sit amet, egestas sed nisi. Proin lacinia lacus ut nisl congue rutrum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam tellus ipsum, pellentesque quis nunc ac, elementum vehicula dolor. Aliquam ac varius nibh. Aliquam rutrum orci nec lobortis tristique. Donec aliquet turpis ex, ut pellentesque metus finibus nec. Proin ac augue arcu.

Morbi non mi nisl. Donec ac tortor accumsan, interdum odio sed, scelerisque diam. Praesent porttitor lacus a elit lobortis, at tristique mauris faucibus. Curabitur varius risus mi, ultrices tristique magna rhoncus viverra. Aliquam posuere, quam quis elementum lobortis, felis enim pulvinar turpis, in pretium nisi leo aliquam leo. Aliquam magna turpis, tincidunt et gravida at, mollis in leo. Quisque interdum, diam sit amet congue rhoncus, tellus sapien porta arcu, id ullamcorper enim eros vitae eros. Suspendisse eros felis, aliquet quis commodo et, bibendum non arcu. Pellentesque semper ipsum nunc, ac maximus dui egestas eu. Etiam lacinia erat eget lorem hendrerit, nec mattis justo gravida. Nullam et finibus tellus, non feugiat mi. Sed elementum turpis massa, sit amet tincidunt risus convallis a. Curabitur gravida erat lorem. Suspendisse potenti.

Vestibulum ut est quis sapien iaculis placerat. Cras mollis mattis feugiat. Pellentesque cursus, turpis ac cursus pulvinar, odio felis molestie risus, id fermentum ipsum libero sit amet velit. Quisque posuere convallis leo, nec fermentum augue sagittis id. Aliquam pretium turpis a pretium interdum. Curabitur sapien massa, convallis ac lectus a, imperdiet molestie ligula. Donec ut orci ut lorem pharetra viverra. Suspendisse auctor urna nisl, sed dignissim purus maximus vel. Phasellus rutrum ligula non mauris laoreet, et suscipit mi sollicitudin. Mauris ornare lectus nec congue cursus. Praesent tempus, ligula dictum gravida iaculis, ante velit tempus mauris, quis volutpat augue dui non velit. Pellentesque volutpat a nulla ac mattis. Proin cursus quam nisl, eu tincidunt neque semper finibus. Cras nec egestas magna, in molestie lectus.

Nullam congue felis mollis, molestie metus vitae, finibus nisl. Nunc egestas nulla ullamcorper neque faucibus, quis mollis ante egestas. Fusce sit amet sapien pretium, tempus augue id, mattis leo. Mauris volutpat quam in justo condimentum, eu pellentesque tortor vehicula. In dictum leo erat, nec congue magna euismod nec. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur non augue blandit, pellentesque est nec, viverra tellus. Sed ac dapibus diam, quis viverra lacus. Aliquam consectetur, est ut efficitur finibus, est libero gravida lorem, id dictum lorem eros non dolor. Duis sed orci at ex ultricies facilisis.

Aenean varius erat sit amet arcu ultrices ornare. Vivamus fermentum vitae neque a dapibus. Morbi rutrum tincidunt elit quis molestie. In vel dignissim urna, eget dictum justo. Morbi volutpat est non libero interdum hendrerit. Nam odio tortor, suscipit at viverra ac, tempor vel turpis. Quisque vulputate est varius, dictum risus ac, scelerisque magna. Suspendisse pharetra, leo sed commodo viverra, elit turpis cursus ligula, in ultrices risus nulla a metus. Mauris fringilla sagittis lacus ut blandit. Donec vitae ornare lorem. Praesent dui erat, lobortis vel est id, imperdiet rutrum magna. Fusce aliquet mattis justo, non mollis nibh imperdiet eu. Morbi convallis ante tortor, ut fringilla erat dictum non. Suspendisse ut elit nec lectus pulvinar imperdiet. Morbi bibendum scelerisque pretium.

Donec turpis sapien, sodales sed congue in, porttitor ac orci. Aliquam pretium condimentum sapien sed sollicitudin. Mauris hendrerit, diam vitae commodo viverra, justo urna gravida sem, vel tincidunt erat lacus ut mauris. Ut tempor quam eget massa consectetur scelerisque. Nam ac tempor orci, vitae congue odio. Nunc faucibus fringilla lorem nec vehicula. Vivamus luctus, neque quis suscipit elementum, mi nibh sodales quam, eget aliquet nisi tellus in metus.

Sed justo lectus, vestibulum sit amet ullamcorper a, sollicitudin ut nulla. Sed malesuada lacus ac lacus scelerisque auctor. Vestibulum sit amet sem finibus, maximus arcu sit amet, sollicitudin enim. Aenean a ultrices libero, quis tempor nulla. Quisque consequat odio eget urna convallis mattis. Donec sit amet dapibus odio. Maecenas aliquet metus odio. Vestibulum venenatis molestie diam vel elementum. Suspendisse ullamcorper tristique elit, id euismod tortor scelerisque a. Vivamus sodales odio vitae mi semper luctus eget id risus. Sed quis ex aliquet erat commodo pharetra. Praesent porta ipsum at erat ullamcorper varius. Mauris eget congue urna. Curabitur aliquet ligula eros, sed rhoncus turpis pulvinar quis. Quisque et consequat ipsum, id tincidunt dolor. Suspendisse et maximus orci, ac finibus nibh.

Aenean pellentesque est a est commodo, eu lacinia ante consequat. Nam volutpat tempor velit, in luctus erat luctus eu. Vestibulum egestas, diam quis hendrerit iaculis, magna mi dictum sem, quis aliquam dui nibh non neque. Duis euismod neque euismod ipsum tristique tincidunt. Maecenas hendrerit felis vitae turpis aliquet, et rutrum nibh fermentum. Curabitur ac elementum orci. Integer vel ipsum elit. Nullam eu vehicula enim, sit amet hendrerit ligula. Vivamus at volutpat urna. Donec eu pulvinar dolor. Ut quam orci, mattis sed elit sed, efficitur volutpat eros. Morbi tristique lorem a augue tempus venenatis. Maecenas nec orci massa. Phasellus eleifend sapien purus, id mollis sapien luctus quis. Ut laoreet volutpat sem quis vehicula.

Nulla fringilla ante metus, a suscipit nisi lobortis sed. Fusce venenatis varius ultrices. Quisque et lectus congue, rutrum nunc in, malesuada mauris. Donec eu eleifend est, vitae suscipit diam. Suspendisse viverra, turpis a gravida facilisis, nisi mauris finibus magna, sed finibus lorem tellus quis nulla. Vestibulum dignissim erat sed sapien fermentum hendrerit. Vivamus porttitor scelerisque pharetra. Mauris ac elit et risus varius ultrices non id nunc. Vivamus aliquam bibendum est. Nunc molestie a tortor ac lobortis. Integer malesuada nisi felis, vitae lobortis risus vulputate et. Donec feugiat pulvinar justo eu accumsan. Sed suscipit est vitae urna porta pulvinar. Praesent imperdiet auctor lectus vel pretium. Duis ornare quam a mollis interdum. In nec turpis ornare, lobortis lorem vitae, semper mauris.

Suspendisse sed finibus dolor, sit amet ultricies enim. Suspendisse potenti. Fusce varius viverra mattis. Pellentesque nec euismod tortor. Maecenas tincidunt posuere augue vitae faucibus. Morbi lobortis magna leo, quis facilisis libero congue et. Aenean facilisis cursus lacus ac pulvinar. Donec viverra urna non dui ultricies consequat. Maecenas blandit at orci id lobortis. Ut condimentum nisl tempor dignissim dignissim. Aliquam magna lacus, euismod consectetur augue eu, efficitur congue sapien. Maecenas auctor tincidunt erat, sit amet pretium velit malesuada volutpat. Cras at euismod purus, sit amet viverra erat. Pellentesque convallis ac nunc vitae accumsan. Mauris tristique, tortor ac sagittis varius, enim eros lobortis sapien, sed porta nisl leo et velit. Morbi rutrum vulputate mattis.

Vestibulum porttitor nec massa ac tempor. Maecenas eu urna eu tellus dapibus porta et vel nulla. Praesent pharetra suscipit nunc, at sodales ex laoreet ac. Proin in nisi feugiat, consectetur arcu in, pellentesque quam. Nullam metus risus, rhoncus in porta eu, cursus sed est. Duis pretium tortor eu nulla volutpat pulvinar. Quisque eu leo venenatis, tempor tortor in, auctor nisi. Cras convallis ipsum vel efficitur vehicula. Nunc ut ex magna. Nam egestas, nisl vel tristique posuere, urna tellus iaculis orci, sit amet rutrum turpis libero a nunc.

Praesent egestas, nisl porttitor sodales tempus, felis nulla malesuada ante, non mattis felis nunc sed est. Maecenas accumsan condimentum porta. Phasellus volutpat massa et mauris maximus, non lacinia nunc imperdiet. Sed facilisis nisl mauris. Nunc a elementum orci. In accumsan tincidunt justo, et porta diam aliquet eget. Donec sit amet quam vitae sem dapibus auctor vestibulum at purus. Aenean pellentesque quam eu suscipit blandit. Morbi aliquam vulputate tortor, quis convallis tellus laoreet vitae. Aliquam blandit felis nec velit aliquet aliquet. Aenean mattis placerat mi a malesuada. Suspendisse aliquam a neque ultrices efficitur. Nulla in ultrices mauris, sed varius massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus volutpat tempor nisl, et accumsan quam dapibus quis.

Phasellus eget massa ex. Aenean sodales lectus ac dapibus condimentum. Pellentesque posuere sodales purus, a laoreet nunc molestie quis. Fusce efficitur diam nisi, at commodo lacus dictum vitae. Sed tincidunt arcu lacus, sit amet efficitur nisl maximus eu. Donec sed tempus tortor. Cras dapibus feugiat lacus convallis elementum. Sed vulputate, dui nec ultrices tempor, leo nisl porta felis, vitae mollis neque nunc ac nibh. Pellentesque vitae eros malesuada, convallis erat sed, ullamcorper est.

Nunc volutpat elit in venenatis iaculis. Quisque euismod lorem vehicula leo placerat, eget convallis diam consectetur. Duis nec rutrum nunc, eget luctus quam. Nullam congue a urna ac vehicula. Vestibulum enim dui, eleifend a magna non, cursus placerat turpis. Vivamus eu odio justo. Nulla finibus, eros eu pellentesque rhoncus, mauris velit volutpat lectus, at ornare eros nulla sed nisi. Fusce efficitur mattis egestas. Pellentesque dignissim, dolor at porttitor fringilla, sem libero tincidunt erat, et hendrerit tellus ex sollicitudin nibh. Fusce convallis nunc a lacus tempus convallis. Sed et augue mi. Aliquam non faucibus est.

Phasellus volutpat maximus cursus. In hac habitasse platea dictumst. Proin nunc ante, finibus et massa eu, vehicula lobortis erat. Proin vel mi commodo, porttitor enim vitae, malesuada erat. Proin commodo dictum consectetur. Phasellus hendrerit ac odio non accumsan. Nam vehicula varius laoreet. Nunc tincidunt purus in feugiat pharetra. In finibus, lacus vitae lobortis posuere, metus velit dictum tellus, a accumsan neque tellus vel justo. Praesent id egestas justo, eget tincidunt urna. Proin sit amet ullamcorper lacus, et laoreet purus.

Etiam ullamcorper ex a ultrices euismod. In volutpat, est eu imperdiet condimentum, diam augue fringilla felis, non faucibus nunc eros at metus. Fusce quis purus vel arcu placerat tincidunt vel sed libero. Suspendisse potenti. Aenean sed sem diam. Aenean sagittis diam orci, id aliquam neque molestie non. Ut luctus efficitur lobortis.

Integer faucibus suscipit turpis, euismod maximus nunc. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam consectetur sem risus, non lacinia lectus lobortis id. Pellentesque nec aliquet tortor. In pellentesque dolor odio, ac consectetur lacus condimentum at. Vivamus auctor arcu non justo finibus, sit amet tristique massa accumsan. Donec elementum tristique mauris non placerat. Ut congue, turpis id fermentum molestie, lectus libero auctor diam, id gravida mi tortor eu mauris. Ut cursus commodo libero, et hendrerit orci consectetur a.

Integer egestas malesuada nulla a aliquam. Sed libero felis, malesuada eget purus luctus, aliquet fringilla risus. Etiam tempus ligula id est dictum, quis accumsan est tristique. In hac habitasse platea dictumst. Cras quis venenatis elit, posuere ultrices justo. Sed ultricies nulla in libero faucibus viverra. Nulla suscipit, nunc et hendrerit lacinia, augue ligula posuere est, ut efficitur dolor neque et mi. Donec ac ipsum lacinia diam feugiat ornare vitae sed dolor. Donec rutrum volutpat purus, tincidunt tempor massa placerat nec. Sed tortor ligula, vehicula ut malesuada vel, hendrerit vitae metus. Ut maximus nibh a eros porta vulputate. Vivamus augue felis, mattis quis porttitor sed, gravida molestie magna. Proin vel dui nibh. Nullam aliquet finibus commodo.

Nulla eget turpis sed tellus tincidunt pretium. Etiam tincidunt volutpat massa vel tristique. Duis euismod consectetur elit. Aliquam a felis nisi. Integer non neque eu tortor pulvinar consectetur. Nam laoreet, nisl id porta fermentum, metus leo finibus velit, nec ullamcorper ante dui nec turpis. Donec tempus interdum odio, ac imperdiet tellus euismod quis. Donec sem mi, dignissim id nulla vitae, cursus rutrum libero. Fusce rutrum volutpat hendrerit. Integer quis quam tristique, hendrerit ex sit amet, faucibus felis. Vestibulum velit enim, interdum eget nulla vitae, faucibus aliquam enim. Morbi dignissim molestie lorem ut sollicitudin. Quisque tincidunt venenatis finibus. Donec molestie eu orci eu hendrerit. Sed interdum nibh nisl, sit amet sodales elit ultrices ac. Phasellus quis augue elit.

Praesent in ante egestas, eleifend sem nec, euismod sapien. Praesent risus ante, maximus faucibus urna porttitor, iaculis gravida tortor. Suspendisse sed pulvinar risus. Nullam vel dictum massa, sed fringilla ipsum. Phasellus nisl lectus, eleifend quis magna a, posuere tincidunt lorem. Curabitur eu laoreet magna, at molestie risus. Pellentesque iaculis finibus bibendum. Mauris et sodales sapien, at posuere nibh. Nam at egestas purus.

Maecenas commodo tellus at pulvinar porttitor. Etiam commodo dapibus ex ac vehicula. Donec viverra ante nibh, id vulputate orci venenatis vel. Quisque dapibus, erat nec lobortis placerat, massa est pellentesque ex, non fermentum odio ipsum nec lorem. Donec condimentum nulla lobortis orci laoreet, eget mollis dui aliquam. Nam aliquet et orci quis dapibus. Fusce malesuada porttitor justo, vel commodo tellus tempor in. Vestibulum magna eros, auctor nec libero vel, facilisis tempor dui. Vestibulum tempus ornare elementum. Nullam nec enim at ante vulputate fringilla. Nulla feugiat magna ac ipsum vestibulum bibendum et nec arcu. Nulla ullamcorper arcu volutpat congue lacinia. Cras mollis consequat dolor ac accumsan. Aliquam nec mollis dui, nec semper odio. Maecenas aliquet finibus risus in lobortis.

Maecenas tempus est eu neque condimentum, nec facilisis eros ultricies. Phasellus nisl dui, gravida id libero vitae, imperdiet aliquet leo. Duis vitae lorem pretium, facilisis diam suscipit, porttitor nisl. Vestibulum tempor elit magna, eget tempus arcu efficitur consequat. Quisque ligula orci, commodo ac vehicula ac, accumsan id mauris. Duis venenatis neque sit amet lorem pretium, eu suscipit dui laoreet. Aenean gravida iaculis lorem eu euismod. Fusce consequat, sapien nec ornare rhoncus, nibh ante aliquet lectus, et cursus lacus nibh non orci. Fusce malesuada sit amet mauris molestie imperdiet. Duis at facilisis eros, a dictum libero. Morbi malesuada leo sed felis vulputate, a elementum purus facilisis.

Nam molestie rhoncus felis sit amet volutpat. Aenean quis felis leo. Phasellus eget efficitur odio. Proin lectus eros, luctus ut dictum sed, aliquet vel erat. Aliquam varius maximus faucibus. Integer sed velit purus. Suspendisse nec euismod metus, a imperdiet lacus. Pellentesque nec finibus justo.

Morbi varius at elit nec pulvinar. Quisque eget massa vel eros ultricies varius. Aliquam ut turpis et tortor consequat consectetur ac non nisl. Phasellus id lorem id metus egestas maximus nec a nulla. Duis a risus maximus velit auctor pellentesque. Curabitur ut ante lacinia, congue enim sit amet, congue ante. Cras ultricies lorem nec odio congue, eu aliquam dolor iaculis. Ut fringilla bibendum justo, sed interdum orci vestibulum et. Aliquam ut lacus fringilla, vulputate nunc ut, facilisis metus.

Pellentesque vehicula quis metus eu porta. Vestibulum condimentum diam ac augue aliquam efficitur. Ut aliquam justo quam, ac consectetur tortor molestie et. Suspendisse tempor egestas magna, vitae facilisis mi. Ut elit est, lobortis viverra justo sed, scelerisque porta lorem. Nam sit amet tortor urna. Proin sit amet augue id augue semper egestas ut at tortor. Nullam tincidunt ante at magna dictum pulvinar. Vestibulum quis libero diam. Morbi id libero vel arcu gravida condimentum. Sed tempor fermentum magna sit amet vestibulum. Nam malesuada neque nec dignissim euismod. Morbi orci dui, euismod ac nibh non, condimentum hendrerit ante. Proin vitae sapien purus. Maecenas rhoncus, risus sed fringilla consectetur, massa nibh aliquam quam, vel malesuada justo ligula a ligula.

Nunc ut ornare lacus. Duis venenatis faucibus mi in tempus. Suspendisse ac mi convallis, dictum massa in, ultricies urna. Nullam ipsum leo, dictum vitae convallis sed, sollicitudin a tellus. Maecenas pretium tempor egestas. Sed pulvinar dui est. Nulla porttitor risus libero, dignissim porttitor tortor dignissim sit amet. Sed vestibulum dignissim felis, ut commodo turpis condimentum ut. Nullam luctus eleifend augue, a rutrum nunc aliquam ut. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse sapien neque, lobortis quis cursus id, consectetur sit amet arcu. Quisque sagittis lorem sed viverra mattis. Sed est eros, tincidunt eu imperdiet quis, cursus et lacus.

Ut ultricies ex eget ex vulputate, id euismod tellus feugiat. Sed gravida pharetra suscipit. Nullam ultrices porttitor viverra. Quisque accumsan nulla eu nunc placerat, at facilisis erat laoreet. Mauris dignissim urna at diam fringilla malesuada. Suspendisse eu semper magna. Aliquam ut accumsan nunc. Proin egestas lacinia elit eget sollicitudin. Suspendisse venenatis mattis purus vitae ornare. Etiam et tincidunt ex, et dapibus risus. Vivamus elementum nulla metus, vel ornare nisi gravida viverra.

Nam rutrum sodales lacus, sed sodales risus placerat sed. Vestibulum sed ultricies massa. Phasellus tincidunt mollis sem ac pretium. Nulla convallis tempus lectus eget luctus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus non purus egestas, condimentum lorem eu, mollis magna. Phasellus convallis quam auctor eleifend placerat. Vivamus sed odio vel velit sagittis luctus. Fusce iaculis viverra nisi eu feugiat. Duis neque nunc, euismod sit amet ex non, lobortis commodo risus. Etiam ipsum purus, eleifend ut neque vel, molestie mattis neque. Curabitur elementum consectetur nisi, in sagittis ligula scelerisque iaculis. In lobortis odio eu nisi vehicula tempor. Maecenas vulputate neque eget dui fermentum vestibulum.

Pellentesque nunc libero, feugiat in erat eget, condimentum laoreet ante. Aliquam nec vehicula leo. Sed tincidunt sapien vel efficitur vestibulum. Nulla et auctor risus. Ut id odio non ex imperdiet sagittis non sit amet diam. Praesent euismod lectus sodales tempor elementum. Proin eget ligula gravida, porta metus vel, pharetra augue. Donec imperdiet maximus feugiat. Maecenas tempus pellentesque aliquam. Cras tincidunt nibh dolor, quis vulputate lorem blandit at. In vitae porta velit. Quisque id sollicitudin orci. Donec fermentum lectus sem, eu aliquam sapien pellentesque a. Phasellus volutpat metus nulla, malesuada feugiat purus pulvinar a. Integer eget lectus cursus, ullamcorper orci eget, scelerisque tellus. Aliquam enim justo, imperdiet eget bibendum quis, sollicitudin sed est.

Nulla nec auctor lorem, ut interdum lectus. Integer et maximus metus. Duis quis erat et lectus pellentesque egestas vel quis turpis. Nullam quis tortor at leo congue semper non eu felis. Nam a orci sit amet justo facilisis laoreet. Morbi nec tortor sit amet tellus dictum aliquam. Sed sit amet lectus vitae lectus mollis tincidunt et eget ligula. Aliquam a leo fermentum, venenatis nibh nec, malesuada libero. Fusce volutpat, nulla sit amet rutrum ultricies, massa est sodales turpis, in porta urna est ornare dui. Vestibulum tincidunt tortor vel risus vulputate tempus ut interdum lectus. Praesent eget tortor vitae ipsum porttitor bibendum. Nullam vitae ornare erat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;

Mauris quis efficitur nulla. Maecenas vel justo sed lorem elementum tincidunt et et ipsum. Nam convallis elit vel quam suscipit, a aliquet eros dignissim. Quisque lacinia nisl libero, id accumsan orci dignissim in. Vestibulum hendrerit fermentum felis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean sagittis pellentesque leo.

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla facilisi. Cras venenatis ornare sapien, a mattis tortor luctus consectetur. Vestibulum pulvinar turpis eu ipsum gravida, feugiat elementum sapien cursus. Aliquam ultrices rhoncus dui at vehicula. Cras erat urna, placerat nec nisi a, sollicitudin aliquam mauris. Fusce lectus quam, dapibus in dui nec, gravida tincidunt augue.

Donec vel felis volutpat, auctor eros in, vestibulum leo. Sed vehicula vestibulum risus, quis hendrerit risus feugiat ac. Nam rutrum iaculis dui, a dapibus leo accumsan nec. Aliquam cursus lacus a est bibendum auctor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum vitae felis eget neque tempus viverra vel non turpis. Cras vitae est eu dolor dignissim porta vitae id ex. Nullam condimentum ornare magna, sed aliquet ex posuere vitae. Sed aliquet libero ac dapibus vulputate. Etiam eget ultricies massa, ut viverra arcu. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed volutpat mauris vel eros ullamcorper, nec aliquet quam ullamcorper.
'''
from random import randint
import random

def action():
	global ipsum
	lorem = 'Lorem ipsum '
	ipsum = ipsum.replace( '\r', '' )
	ipsum = ipsum.replace( '\t', ' ' )
	ipsum = _str.cleanBE(ipsum,'\n')
	sample = []


	if not _.switches.isActive('Paragraphs') and not _.switches.isActive('Sentences'):
		config = 'Sentences'
	if _.switches.isActive('Paragraphs'):
		config = 'Paragraphs'
	if _.switches.isActive('Sentences'):
		config = 'Sentences'

	if not _.switches.isActive('Count'):
		count = randint(1, 5)
	else:
		count = int(_.switches.value('Count'))


	if config == 'Paragraphs':
		total = ipsum.split('\n\n')

	if config == 'Sentences':
		ipsum = ipsum.replace( '\n', ' ' )
		ipsum = _str.replaceDuplicate(ipsum,' ')
		total = ipsum.split('.')




	random.shuffle(total)

	sample = total[0:count]

	for i,item in enumerate(sample):
		sample[i] = _str.cleanBE(sample[i],' ')
		sample[i] = result = _str.replaceDuplicate(sample[i],' ')
		if config == 'Sentences':
			sample[i]+='.'
		if _.switches.isActive('Lorem') and _.switches.isActive('JSON'):
			sample[i] = lorem + sample[i][:1].lower()+sample[i][1:]



	if _.switches.isActive('JSON'):
		import simplejson
		_.pr( simplejson.dumps(sample, indent=4, sort_keys=False) )


	elif not _.switches.isActive('JSON'):
		if config == 'Paragraphs':
			result = '\n\n'.join(sample)
		if config == 'Sentences':
			result = ' '.join(sample)
		result = _str.replaceDuplicate(result,' ')

		if _.switches.isActive('Lorem'):
			result = lorem + result[:1].lower()+result[1:]

		_.pr( result )




########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()






