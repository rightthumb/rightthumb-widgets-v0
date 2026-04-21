#!/usr/bin/python3


##################################################
'''
 def URL
 class ProxyManager
	def __init__
	def start_server
	def start_client
	def client
	def server
 class FrontEnd(object)
	def __init__
	def is_cookie_expired
	def extractDomain
	def preURL
	def postURL
	def url
	def getCookies
	def initialize
	def select
	def setField
	def login
	def loginIndividually
	def open
	def jqueryInject
	def inject
	def injectReturn
	def injectFile
	def close
	def wait
	def code
'''
##################################################



# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##




# from selenium import webdriver
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.keys import Keys




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
# from __future__ import (absolute_import, division, print_function, unicode_literals)
import copy
import random
import socket
import unicodedata
import urllib
from subprocess import call
import re
##################################################
from selenium import webdriver # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.support.ui import Select # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.common.by import By # type: ignore
# from selenium.common.exceptions import StaleElementReferenceException

if not __.isWin:
	from selenium.webdriver.chrome.service import Service # type: ignore
	from webdriver_manager.chrome import ChromeDriverManager # type: ignore
	from selenium.webdriver.chrome.options import Options # type: ignore



import time
import copy
import socket
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.common.exceptions import StaleElementReferenceException # type: ignore
	
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
from browsermobproxy import Server  # type: ignore

def URL(url,data={}):
	return str(__.imp('requests.post').post(url, data=data).content,'iso-8859-1').replace('\\n','\n')
	return __.imp('requests.get').get(url).content.decode("utf-8").replace('\\n','\n')


class ProxyManager:
    _BMP = "D:\\.rightthumb-widgets\\widgets\\exe\\ChromeDriver\\134.0.6998.90\\browsermob-proxy-2.1.4-bin\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat"

    def __init__(self):
        self.__server = Server(ProxyManager._BMP)
        self.__client = None

    def start_server(self):
        self.__server.start()
        return self.__server

    def start_client(self):
        self.__client = self.__server.create_proxy(params={'trustAllServers': 'true'})
        return self.__client

    @property
    def client(self):
        return self.__client

    @property
    def server(self):
        return self.__server

	
	
from selenium.webdriver.chrome.service import Service # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore

import unicodedata

def u_to_s(text):
	if isinstance(text, bytes):
		text = text.decode('utf-8', errors='ignore')
	text = str(text)
	text = unicodedata.normalize('NFKC', text)  # Normalize width/formatting
	return text.strip()


########################################################################################

class FrontEnd(object):

	def __init__( self ):
		self.jqueryFile = _v.myAppsJs + os.sep+'jquery-1.12.4.min.js'
		self.jqueryFile = _v.myAppsJs + os.sep+'jquery-3.7.1.min.js'
		# self.jquery = jquery.theCode()
		self.browser = None
		self.download_default = 'text/plain'

		self.har = True
		self.harFile = 'selenium.har'
		self.cookies = False
		self.cookies_filename = '_toolsScrapeFrontEnd__ALL_AUTO_COOKIES.json'
		self.cookies_recent_hrs = 36
		self.headless = False
		
		self.active = False

	def select( self, selector ): return self.selector(selector)
	def selector( self, selector ): return self.browser.find_elements(By.CSS_SELECTOR, selector)
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
		for x in url.split(os.sep):
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
		self.initialize()
		self.preURL( url )
		# print('_______________________')
		# for x in dir(self.browser): print(x)
		# print('_______________________')
		self.browser.get( url )
		self.active = True
		self.postURL( url )


	def getCookies( self ):
		cookies = []
		for cookie in self.browser.get_cookies():
			# del cookie['expiry']
			cookies.append( cookie )
		return cookies

	def initialize( self ):
		if self.browser is None:
			if __.isWin:
				options = Options()
				if self.headless:
					options.add_argument("--headless")
				options.add_argument("--no-sandbox")
				options.add_argument("--disable-dev-shm-usage")
				service = Service(executable_path="D:\\.rightthumb-widgets\\widgets\\exe\\ChromeDriver\\134.0.6998.90\\chromedriver.exe")
				self.browser = webdriver.Chrome(service=service, options=options)
				# self.browser = webdriver.Chrome(executable_path='C:\\Users\\Scott\\.rt\\profile\\exe\\chromedriver.exe')
				
			elif not __.isWin:
				chrome_options = Options()
				chrome_options.add_argument("--headless")  # Ensure GUI is off
				chrome_options.add_argument("--no-sandbox")
				chrome_options.add_argument("--disable-dev-shm-usage")
				service = Service(ChromeDriverManager().install())
				self.browser = webdriver.Chrome(service=service, options=chrome_options)



	def select(self, selector):
		# _browser.imp.project.select('.my-button')[0].click()
		if any(x in selector for x in ['.', '#', '[', '=']):
			return self.browser.find_elements(By.CSS_SELECTOR, selector)
		else:
			return self.browser.find_elements(By.NAME, selector)



	def runme(self, url, threshold=50):
		final_results = []
		previmages = []
		tries = 0

		try:
			self.url(url)
			while threshold > 0:
				try:
					results = []
					images = self.browser.find_elements(By.TAG_NAME, 'img')

					if images == previmages:
						tries += 1
					else:
						tries = 0

					if tries > 20:
						return final_results

					for img in images:
						src = img.get_attribute("src")
						if src:
							if "/236x/" in src or "/474x/" in src:
								_.pr(src)
								src = src.replace("/236x/", "/736x/")
								src = src.replace("/474x/", "/736x/")
								results.append(u_to_s(src))  # Assumes u_to_s is defined elsewhere

					previmages = copy.copy(images)
					final_results = list(set(final_results + results))

					dummy = self.browser.find_element(By.TAG_NAME, 'a')
					dummy.send_keys(Keys.PAGE_DOWN)
					time.sleep(3)
					threshold -= 1

				except StaleElementReferenceException:
					threshold -= 1

		except (socket.error, socket.timeout):
			pass

		return final_results


	def setField(self, data, selector, enter=False, click=False):
		try:
			# Wait for element to be present & interactable
			elem = WebDriverWait(self.browser, 10).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, selector))
			)
			WebDriverWait(self.browser, 10).until(
				EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
			)

			# Debugging: Print element details
			print(f"Element found: {selector}, Tag: {elem.tag_name}, Type: {elem.get_attribute('type')}")

			# Check if inside an iframe
			if "iframe" in elem.get_attribute("outerHTML").lower():
				print("Element is inside an iframe. Switching...")
				iframe = self.browser.find_element(By.TAG_NAME, "iframe")
				self.browser.switch_to.frame(iframe)

			# Clear the field before entering new data
			elem.clear()
			elem.send_keys(data)

			if enter:
				elem.send_keys(Keys.RETURN)
			elif click and not isinstance(click, bool):
				elemX = self.select(click)
				WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, click))).click()

			# If we switched to an iframe, switch back
			self.browser.switch_to.default_content()

		except Exception as e:
			print(f"Error in setField: {e}")
			# Attempt JavaScript as a fallback
			try:
				print("Trying JavaScript-based input...")
				self.browser.execute_script("arguments[0].value = arguments[1];", elem, data)
			except Exception as js_e:
				print(f"JavaScript input failed: {js_e}")


	def login( self, url, login, password, login_selector, password_selector, submit_selector=None ):
		self.initialize()
		# for x in dir(self.browser): print(x)
		# sys.exit()
		self.open( url )



		email_elem = self.browser.find_element(By.CSS_SELECTOR,  login_selector )
		email_elem.send_keys( login )
		password_elem = self.browser.find_element(By.CSS_SELECTOR,  password_selector )
		password_elem.send_keys( password )
		if submit_selector is None:
			password_elem.send_keys(Keys.RETURN)
		else:
			button1 = self.browser.find_element(By.CSS_SELECTOR,  submit_selector )
			button1.click()
		time.sleep( 3 )
		_.pr()
		_.pr(line=1,c='yellow')
		input("Press Enter to continue...")
		input("Press Enter again...")






	def testPromptWait__This__MF__THIS(self):
		# This ---> MF THIS <---
		# This ---> MF THIS <---
		# This ---> MF THIS <---
		# This ---> MF THIS <---
		# This ---> MF THIS <---
		if not self.headless:
			# Inject a prompt after delay, so the browser has time to display it
			js = """
			setTimeout(function() {
				window.__promptValue = prompt("Manual verification required (CAPTCHA or 2FA).\\nHow many minutes should I wait?", "2");
			}, 500);
			"""

			self.browser.execute_script(js)

			# Wait for user to respond to the prompt manually
			input("⏳ Please enter response in browser prompt and press ENTER here when done...")

			# Retrieve the response from the browser
			response = self.browser.execute_script("return window.__promptValue;")
			print('response',response)
			print('response',response)
			print('response',response)
			print('response',response)
			if response is not None:
				response = str(response).strip()
				try:
					yy=float(response)
					yy+=10
					yy-=10
					valid = True
				except:
					valid = False

				# if re.match(r'^\\d*\\.?\\d+$', response):  # Valid float format
				if valid:
					wait_minutes = float(response)
					wait_seconds = int(wait_minutes * 60)
					_.pr(f'⏱️ Waiting {wait_seconds} seconds...')
					time.sleep(wait_seconds)
				else:
					_.pr("⚠️ Invalid input. No wait.")
			else:
				_.pr("🚫 Prompt canceled or no input. No wait.")
		else:
			time.sleep(10)  # Fallback wait




	def loginIndividually(self, url, login, password, login_selector, password_selector, login_button='', password_button='', rawPass=False):
		self.open(url)

		# Determine method for login field
		if any(x in login_selector for x in ['.', '#', '[', '=']):
			email_elem = self.browser.find_element(By.CSS_SELECTOR, login_selector)
		else:
			email_elem = self.browser.find_element(By.NAME, login_selector)

		email_elem.send_keys(login)

		if login_button:
			button1 = self.browser.find_element(By.CSS_SELECTOR, login_button)
			button1.click()
		else:
			email_elem.send_keys(Keys.RETURN)

		time.sleep(1)

		# Determine method for password field
		if any(x in password_selector for x in ['.', '#', '[', '=']):
			password_elem = self.browser.find_element(By.CSS_SELECTOR, password_selector)
		else:
			password_elem = self.browser.find_element(By.NAME, password_selector)

		if not rawPass:
			password = _blowfish.decrypt(password)

		if password.endswith(' '):
			password = _str.cleanEnd(password, ' ')

		password_elem.send_keys(password)
		password = ''

		if password_button:
			button2 = self.browser.find_element(By.CSS_SELECTOR, password_button)
			button2.click()
		else:
			password_elem.send_keys(Keys.RETURN)

		time.sleep(3)




	def open( self, url ):
		self.initialize()
		self.url( url )

		# time.sleep( 2 )

	def js( self, path=None ):
		if path is None:
			return self.jq()
		elif path.startswith('https://') or path.startswith('http://'):
			return self.injectURL( path )
		elif os.path.isfile(path):
			return self.injectFile( path )
		else:
			return self.injectReturn( path )

	def jq( self ): return self.jqueryInject()
	def jqueryInject( self ): return self.injectURL( 'https://rightthumb.com/apps/selenium/jquery-1.11.3.js' )

	def inject( self, code ):
		newCode = ''
		if type( code ) == list:
			newCode += _.flattenList( code )
		else:
			newCode += code
		# _.pr( newCode )
		self.browser.execute_script( newCode )

	def injectReturn( self, code ):
		if not 'return ' in code:
			return self.browser.execute_script( 'return ' + code )
		else:
			return self.browser.execute_script( code )

	def injectURL( self, url ):
		code = URL(url)
		return self.browser.execute_script(code)
	def injectFile( self, file ):
		with open( file, 'r' ) as item: 
			code = item.read() 
			return self.browser.execute_script(code)
		# time.sleep( 2 )


	def click(self, selector):
		if any(x in selector for x in ['.', '#', '[', '=']):
			elem = self.browser.find_element(By.CSS_SELECTOR, selector)
		else:
			elem = self.browser.find_element(By.NAME, selector)
		elem.click()

	def clickEach(self, selector):
		if any(x in selector for x in ['.', '#', '[', '=']):
			elems = self.browser.find_elements(By.CSS_SELECTOR, selector)
		else:
			elems = self.browser.find_elements(By.NAME, selector)

		for elem in elems:
			if elem.is_displayed():
				elem.click()
				time.sleep(0.5)



	def close(self):
		self.active = False
		if hasattr(self, 'har') and self.har:
			_.printVarSimple(self.har)
			_.pr(self.har)
			with open(self.harFile, 'w') as har_file:
				json.dump(self.har, har_file)
		if self.browser:
			self.browser.quit()


	def wait(self, max_retries=30):
		time.sleep(2)  # Initial wait to allow loading

		ix = 0
		while ix < max_retries:
			state = self.injectReturn("return document.readyState;")
			if state == "complete":
				break  # Stop waiting once the page is fully loaded

			time.sleep(1)
			ix += 1
			_.pr(f"Waiting... {ix}", end='\r', flush=True)

		_.pr("\nPage load complete.")


	def code( self ):
		return self.browser.page_source

import simplejson as json
project = FrontEnd()




def action():
	pass




########################################################################################
if __name__ == '__main__':
	action()







