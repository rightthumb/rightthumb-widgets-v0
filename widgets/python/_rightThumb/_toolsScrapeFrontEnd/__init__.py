from __future__ import (absolute_import, division, print_function, unicode_literals)

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


import copy
import random
import socket
import sys
import time
import unicodedata
import urllib

from subprocess import call


# from selenium import webdriver
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.keys import Keys


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.chrome.options import Options
##################################################
import os
import sys
import time
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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._encryptString as _blowfish
	# _blowfish.defaultKey()
# import _rightThumb._md5 as _md5
##################################################

def appSwitches():
	pass
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': '_rightThumb._toolsScrapeFrontEnd',
	'description': 'Front end scrape tool',
	'categories': [
						'research',
						'text manipulation',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [
						'p url -url https://www.google.com/',
	],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = True

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
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

_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
# START


# from _rightThumb._toolsScrapeFrontEnd import jquery



# from browswermobproxy import Server
# from browsermobproxy import Server


class ProxyManager:

	# _BMP = "C:\\Users\\Scott\\Downloads\\browsermob-proxy-2.1.4-bin\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat"
	_BMP = "C:\\Users\\Scott\\Downloads\\browsermob-proxy-2.1.4-bin\\browsermob-proxy-2.1.4\\bin\\server.bat"

	def __init__( self ):

		# self.__server = Server( ProxyManager._BMP,  options={'port': 8080 } )
		self.__server = Server( ProxyManager._BMP )
		self.__client = None

	def start_server( self ):
		self.__server.start()
		return self.__server

	def start_client( self ):

		# self.__client = self.__server.create_proxy()
		self.__client = self.__server.create_proxy(params={'trustAllServers':'true'})
		return self.__client

	@property
	def client(self):
		return self.__client
	
	@property
	def server(self):
		return self.__server
	
	


class FrontEnd(object):

	def __init__( self ):
		self.jqueryFile = _v.myAppsJs + _v.slash+'jquery-1.11.3.js'
		# self.jquery = jquery.theCode()
		self.browser = None
		self.download_default = 'text/plain'


		self.cookies = False
		self.cookies_filename = '_toolsScrapeFrontEnd__ALL_AUTO_COOKIES.json'
		self.cookies_recent_hrs = 36
		
		self.active = False

	def is_cookie_expired( self, epoch, isCookie=False ):
		if isCookie:
			if epoch > time.time():
				return True
		elif not isCookie:
			if epoch > time.time():
				return True
		return False

	def extractDomain( self, url ):
		foundDomain = False
		for x in url.split(_v.slash):
			return x
		return None

	def preURL( self, url ):
		if self.active:
			allCookies = _.getTable( self.cookies_filename )
			cookies = {
							'epoch': time.time(),
							'domain': self.extractDomain( url ),
							'url': url,
							'cookies': self.browser.get_cookies(),
			}
			allCookies.append( cookies )
			_.saveTable( allCookies, self.cookies_filename )


	def postURL( self, url ):
		if self.cookies:
			if type(self.cookies) == str and self.cookies == 'recent':
				recent = True
			else:
				recent = False
			domain = self.extractDomain( url )
			cookies = []
			for cookieSet in _.getTable( self.cookies_filename ):
				if domain == cookieSet['domain']:
					shouldLoad = True
					if recent and self.is_cookie_expired( cookieSet['epoch'], isCookie=False ):
						shouldLoad = False

					if shouldLoad:
						for cookie in cookieSet['cookies']:
							if not 'expiry' in cookie:
								cookies.append( cookie )
							elif 'expiry' in cookie and not self.is_cookie_expired( cookie['expiry'], isCookie=True ):
								cookies.append( cookie )


			if not cookies is None:
				# keep = 'domain,httpOnly,name,path,secure,value,sameSite'
				for cookie in cookies:
					del cookie['expiry']
					self.browser.add_cookie(cookie)
					pass
			if len( cookies ):
				self.inject( 'location.reload();' )
				# self.wait()
		self.wait()
			


	def url( self, url ):
		self.preURL( url )
		self.browser.get( url )
		self.active = True
		self.postURL( url )


	"""
	def getCookies( self ):
		cookies = []
		for cookie in self.browser.get_cookies():
			# del cookie['expiry']
			cookies.append( cookie )
		return cookies
	"""

	def initialize( self ):
		if self.browser is None:
			# print( 'HERE' )

			# import chromedriver_binary
			# self.browser = webdriver.Chrome()
			# options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			# options.binary_location = "D:\\techApps\\GoogleChromePortable\\GoogleChromePortable.exe"
			# options.binary_location = "D:\\techApps\\chrome-win\\chrome.exe"
			# print( _v.chromePortable )
			options = webdriver.ChromeOptions()
			# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
			# options.add_argument('--user-agent="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
			# options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"')

			try:
				__.har
			except Exception as e:
				__.har = False
			if __.har:

				proxy = ProxyManager()
				server = proxy.start_server()
				self.client = proxy.start_client()
				self.client.new_har( "google.com" )
				print( self.client.proxy )
				# options.add_argument("--proxy-server={}".format(self.client.proxy))

			options.binary_location = _v.chromePortable
			self.browser = webdriver.Chrome( chrome_options=options, executable_path=_v.chromedriver )



			if False and not __.har:
				self.close()
			# self.browser = webdriver.Chrome(chrome_options=options, executable_path="D:\\tech\\programs\\exe\\ChromeDriver\\80.0.3987.16\\chromedriver.exe")
			# self.browser = webdriver.Chrome( _v.chromedriver )
			# self.url('http://www.google.com')
			# print( 'DONE' )



			# options = webdriver.ChromeOptions()
			# # options.add_argument('--user-agent="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
			# # prefs = { 'download.default_directory':'C:\Users\Scott\Downloads' }
			# prefs = {}
			# prefs['download.default_directory'] = 'C:\\Users\\Scott\\Downloads'
			# prefs['download.prompt_for_download'] = False
			# prefs['browser.helperApps.neverAsk.saveToDisk'] = self.download_default
			# options.add_experimental_option("prefs", prefs)
			if False and not __.har:
				self.browser = webdriver.Chrome( _v.chromedriver, chrome_options=options )



	def select( self, selector ):
		if not '.' in selector and not '#' in selector and not '[' in selector and not '=' in selector:
			elem = self.browser.find_element_by_name( selector )
		else:
			elem = self.browser.find_element_by_css_selector( selector )
		return elem
	def setField( self, data, selector, enter=False, click=False ):
		elem = self.select( selector )
		elem.send_keys( data )
		if enter:
			elem.send_keys(Keys.RETURN)
		elif not type( click ) == bool:
			elemX = self.select( click )
			elemX.click()

	def login( self, url, login, password, login_selector, password_selector, submit_selector=None ):
		self.open( url )
		email_elem = self.browser.find_element_by_css_selector( login_selector )
		email_elem.send_keys( login )
		password_elem = self.browser.find_element_by_css_selector( password_selector )
		password_elem.send_keys( password )
		if submit_selector is None:
			password_elem.send_keys(Keys.RETURN)
		else:
			button1 = self.browser.find_element_by_css_selector( submit_selector )
			button1.click()
		time.sleep( 3 )

	def loginIndividually( self, url, login, password, login_selector, password_selector, login_button='', password_button='', rawPass=False ):
		# print( 'works' )
		# print( url, login, password, login_selector, password_selector, login_button, password_button )
		# sys.exit()
		self.open( url )
		if not '.' in login_selector and not '#' in login_selector and not '[' in login_selector and not '=' in login_selector:
			email_elem = self.browser.find_element_by_name( login_selector )
		else:
			email_elem = self.browser.find_element_by_css_selector( login_selector )

		email_elem.send_keys( login )
		if login_button == '':
			email_elem.send_keys(Keys.RETURN)
		else:
			button1 = self.browser.find_element_by_css_selector( login_button )
			button1.click()
		time.sleep( 1 )

		if not '.' in password_selector and not '#' in password_selector and not '[' in password_selector and not '=' in password_selector:
			password_elem = self.browser.find_element_by_name( password_selector )
		else:
			password_elem = self.browser.find_element_by_css_selector( password_selector )
		if not rawPass:
			password = _blowfish.decrypt( password )

		if password.endswith( ' ' ):
			password = _str.cleanEnd( password, ' ' )
		password_elem.send_keys( password )
		password = ''


		if password_button == '':
			pass
			password_elem.send_keys(Keys.RETURN)
		else:
			button2 = self.browser.find_element_by_css_selector( login_button )
			button2.click()
		time.sleep( 3 )

	# def runme( self, url ):
	#   final_results = []
	#   previmages = []
	#   tries = 0
	#   try:
	#       self.url(url)
	#       while threshold > 0:
	#           try:
	#               results = []
	#               images = 
	#               if images == previmages:
	#                   tries += 1
	#               else:
	#                   tries = 0
	#               if tries > 20:
	#                   return final_results
	#               for i in images:
	#                   src = i.get_attribute("src")
	#               if src:
 #                            if src.find("/236x/") != -1 or src.find("/474x/") != 1:
 #                                print(src)
 #                                src = src.replace("/236x/", "/736x/")
 #                                src = src.replace("/474x/", "/736x/")
 #                                results.append(u_to_s(src))

 #                    previmages = copy.copy(images)
 #                    final_results = list(set(final_results + results))
 #                    dummy = self.browser.find_element_by_tag_name('a')
 #                    dummy.send_keys(Keys.PAGE_DOWN)
 #                    time.sleep( 3 )
 #                    threshold -= 1
 #                except StaleElementReferenceException:
 #                    threshold -= 1
 #        except (socket.error, socket.timeout):
 #            pass
 #        return final_results


	def open( self, url ):
		self.initialize()
		self.url( url )

		# time.sleep( 2 )

	def jqueryInject( self ):
		# self.browser.execute_script( self.jquery )
		self.injectFile( self.jqueryFile )

	def inject( self, code ):
		newCode = ''
		if type( code ) == list:
			newCode += _.flattenList( code )
		else:
			newCode += code
		# print( newCode )
		self.browser.execute_script( newCode )

	def injectReturn( self, code ):
		if not 'return ' in code:
			return self.browser.execute_script( 'return ' + code )
		else:
			return self.browser.execute_script( code )

	def injectFile( self, file ):
		with open( file, 'r' ) as item: 
			code = item.read() 
			self.browser.execute_script(code)
		time.sleep( 2 )

	# def click( self, selector ):
	#   if not '.' in selector and not '#' in selector and not '[' in selector and not '=' in selector:
	#       elem = self.browser.find_element_by_name( selector )
	#   else:
	#       elem = self.browser.find_element_by_css_selector( selector )
	#   elem.click()

	# def clickEach( self, selector ):
	#   if not '.' in selector and not '#' in selector and not '[' in selector and not '=' in selector:
	#       elem = self.browser.find_element_by_name( selector )
	#   else:
	#       elem = self.browser.find_element_by_css_selector( selector )


	#   for x,row in enumerate(elem):
	#       if elem[x].is_displayed():
	#           elem[x].click()
	#           time.sleep( .5 )


	def close( self ):
		self.active = False
		# if __.har:
		#   _.printVarSimple( self.client.har )
			# pprint.pprint( self.client.har )
			# self.proxy.new_har("myhar")
			# with open('myhar.har', 'w') as har_file:
			#   json.dump(proxy.har, har_file)
		self.browser.close()

	def wait( self ):
		time.sleep( 2 )
		# print(  )
		# print( 'Waiting for task completion' )
		ix = 0
		while not self.injectReturn('return document.readyState;') == 'complete':
			self.inject( "window.onload = function() { window.taskComplete=1; };" )
			time.sleep( 1 )
			ix+=1
			print( ix, end='\r', flush=True )

	def code( self ):
		
		return self.browser.page_source


project = FrontEnd()


# https://selenium-python.readthedocs.io/locating-elements.html
#   self.browser.find_elements_by_tag_name("img")

#   find_element_by_id
#   find_element_by_name
#   find_element_by_xpath
#   find_element_by_link_text
#   find_element_by_partial_link_text
#   find_element_by_tag_name
#   find_element_by_class_name
#   find_element_by_css_selector

# https://selenium-python.readthedocs.io/api.html
#   i.get_attribute("src")

# searches:
#   python webdriver find_element_by_css_selector


def action():
	pass
	# if _.switches.isActive('Input'):
	#   _.setPipeData( _.getText( _.switches.value('Input') ), focus() )
	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#   pass
	# print( _.d2json(_.appData) )



########################################################################################
if __name__ == '__main__':
	action()






