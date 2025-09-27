### EXAMPLE: START
# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
#   finds the file in probable locations
#   and 
#       if  _.autoBackupData = True
#       and __.releaseAcquiredData = True
#           GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#       you can run apps on usb at a clients office
#           when you get home run: p app -loadepoch epoch 
#               backed up
#                   pipe
#                   files
#                   tables
### EXAMPLE: END


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
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
#   os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                   if platform.system() == 'Windows':
### EXAMPLE: END

# def triggers():
#     _.myFileLocation_Print = False
#     _.switches.trigger( 'Files', _.myFileLocations, vs=True )
#     _.switches.trigger( 'Folder', _.myFolderLocations )
#     _.switches.trigger( 'URL', _.urlTrigger )
#     _.switches.trigger( 'Ago', _.timeAgo )
#     _.switches.trigger( 'Duration', _.timeFuture )
#     ### EXAMPLE: START
#     # _.default_switch_trigger('Plus', trigger_plus)
#     # _.switches.trigger( 'Files',_.inRelevantFolder )  
#     # _.switches.trigger( 'Watched', _.txt2Date )
#     # _.switches.trigger( 'Input',_.formatColumns )
#     # _.switches.trigger( 'Franchise',_.triggerSpace )
#     ### EXAMPLE: END

# l.conf('myFileLocation_Print',False)