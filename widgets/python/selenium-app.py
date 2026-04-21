import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
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
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


'''
add_cookie
add_credential
add_virtual_authenticator
application_cache
back
bidi_connection
capabilities
caps
close
command_executor
create_web_element
current_url
current_window_handle
delete_all_cookies
delete_cookie
delete_network_conditions
desired_capabilities
error_handler
execute
execute_async_script
execute_cdp_cmd
execute_script
file_detector
file_detector_context
find_element
find_elements
forward
fullscreen_window
get
get_cookie
get_cookies
get_credentials
get_issue_message
get_log
get_network_conditions
get_pinned_scripts
get_screenshot_as_base64
get_screenshot_as_file
get_screenshot_as_png
get_sinks
get_window_position
get_window_rect
get_window_size
implicitly_wait
launch_app
log_types
maximize_window
minimize_window
mobile
name
orientation
page_source
pin_script
pinned_scripts
print_page
quit
refresh
remove_all_credentials
remove_credential
remove_virtual_authenticator
save_screenshot
service
session_id
set_network_conditions
set_page_load_timeout
set_permissions
set_script_timeout
set_sink_to_use
set_user_verified
set_window_position
set_window_rect
set_window_size
start_client
start_desktop_mirroring
start_session
start_tab_mirroring
stop_casting
stop_client
switch_to
timeouts
title
unpin
vendor_prefix
virtual_authenticator_id
window_handles
'''


_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )

js = '''
let content = [];
document.querySelectorAll('.html-div').forEach(item => {
    content.push(item.textContent);
});
return content
'''




def action():
	global js
	# _browser.imp.project.login("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1", 'scott.reph@gmail.com', '21667013691424', '#email', '#pass', '#loginbutton')
	# _browser.imp.project.url("https://www.facebook.com/paul.panfilowitz")
	_browser.imp.project.url("https://eyeformeta.com/apps/DocWeaver/")

	input('Waiting...')
	_browser.imp.project.testPromptWait()
	# data = _browser.imp.project.execute_script(js)
	# _.pv(data)
	# # _browser.imp.project.
	# # _browser.imp.project.
	# # _browser.imp.project.
	_browser.imp.project.close()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# service = Service(r"D:\\.rightthumb-widgets\\widgets\\exe\\ChromeDriver\\134.0.6998.90\\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver.get('https://qa-practice.netlify.app/bugs-form.html')
# expected_title = 'Bug Report Form'
# actual_title = driver.title
# if expected_title == actual_title:
#     print('Title validation successful!')
# else:
#     print(f'Title validation failed. Expected: "{expected_title}", Actual: "{actual_title}"')
# driver.quit()

########################################################################################
if __name__ == '__main__':
	pass
	action(); _.isExit(__file__)