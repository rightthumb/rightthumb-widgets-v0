import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Trigger', '-t,-trigger,-triggers' )
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
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

# Initialize the global variable 'status'
status = False

def on_created(event):
    _.pr(f"created, {event.src_path} has been created!")

def on_deleted(event):
    _.pr(f"deleted {event.src_path}!")

def on_modified(event):
    global status
    status = False
    _.pr(f"modified, {event.src_path} has been modified")

def on_moved(event):
    _.pr(f"moved {event.src_path} to {event.dest_path}")

def action():
    global status
    status = True  # Initialize status as True

    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True

    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    # Assign event handler functions
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    # Set the path for watching
    path = "."
    if _.switches.isActive('Folder'):
        path = __.path(_.switches.values('Folder')[0])

    # Set to go recursively through the directory
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    # Start observing
    my_observer.start()

    try:
        while status:  # Continue running while status is True
            time.sleep(1)  # You can replace this with other actions or checks if needed
    except KeyboardInterrupt:
        # If interrupted, stop the observer
        _.pr("Interrupted by user")

    # Stop observer when status changes to False
    finally:
        my_observer.stop()
        my_observer.join()
        _.pr("Observer stopped")


########################################################################################
import time
import _rightThumb._dir as _dir
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);