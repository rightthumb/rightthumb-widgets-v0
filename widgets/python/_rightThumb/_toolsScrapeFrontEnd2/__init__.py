#!/usr/bin/python3

import os
import sys
import time
import _rightThumb._construct as __
import _rightThumb._base3 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._encryptString as _blowfish
from subprocess import call
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
import simplejson as json

if not __.isWin:
    try:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.options import Options
    except ModuleNotFoundError:
        print("webdriver_manager module not found. Please install it using 'pip install webdriver-manager'.")
        sys.exit(1)

appDBA = __.clearFocus(__name__, __file__)
__.appReg = appDBA

def focus(parentApp='', childApp='', reg=True):
    global appDBA
    f = __.appName(appDBA, parentApp, childApp)
    if reg:
        __.appReg = f
    return f

__.registeredApps.append(focus())
_.load()

def appSwitches():
    pass

_.appInfo[focus()] = {
    'file': '_rightThumb._toolsScrapeFrontEnd',
    'description': 'Front end scrape tool',
    'categories': ['research', 'text manipulation'],
    'relatedapps': [],
    'prerequisite': [],
    'examples': ['p url -url https://www.google.com/'],
    'columns': [],
}

_.appData[focus()] = {
    'start': time.time(),
    'uuid': '',
    'audit': [],
    'pipe': [],
}

_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

def registerSwitches(argvProcessForce=False):
    global appDBA
    if not __.appReg == appDBA and appDBA in __.appReg:
        if not __name__ == '__main__':
            _.argvProcess = argvProcessForce
        else:
            _.argvProcess = True
        _.load()
        _.appInfo[__.appReg] = _.appInfo[appDBA]
        _.appData[__.appReg] = _.appData[appDBA]
    __.constructRegistration(_.appInfo[__.appReg]['file'], __.appReg)
    appSwitches()
    _.defaultScriptTriggers()
    _.myFileLocation_Print = True
    _.switches.process()

if not __name__ == '__main__':
    _.argvProcess = False
else:
    _.argvProcess = True

registerSwitches()

def fieldSet(switchName, switchField, switchValue, theFocus=False):
    if not type(theFocus) == bool:
        theFocus = theFocus
    _.switches.fieldSet(switchName, switchField, switchValue, theFocus)

_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
    if not sys.stdin.isatty():
        _.setPipeData(sys.stdin.readlines(), __.appReg)

class ProxyManager:
    _BMP = "C:\\Users\\Scott\\Downloads\\browsermob-proxy-2.1.4-bin\\browsermob-proxy-2.1.4\\bin\\server.bat"

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

class FrontEnd(object):
    def __init__(self):
        self.browser = None
        self.jqueryFile = _v.myAppsJs + os.sep + 'jquery-1.11.3.js'
        self.download_default = 'text/plain'
        self.cookies = False
        self.cookies_filename = '_toolsScrapeFrontEnd__ALL_AUTO_COOKIES.json'
        self.cookies_recent_hrs = 36
        self.active = False

    def select(self, selector):
        return self.selector(selector)

    def selector(self, selector):
        return self.browser.find_elements(By.CSS_SELECTOR, selector)

    def is_cookie_expired(self, epoch, isCookie=False):
        if isCookie:
            if epoch > time.time():
                return True
        elif not isCookie:
            if epoch > time.time():
                return True
        return False

    def extractDomain(self, url):
        foundDomain = False
        for x in url.split(os.sep):
            return x
        return None

    def preURL(self, url):
        if self.active:
            allCookies = _.getTable(self.cookies_filename)
            cookies = {
                'epoch': time.time(),
                'domain': self.extractDomain(url),
                'url': url,
                'cookies': self.browser.get_cookies(),
            }
            allCookies.append(cookies)
            _.saveTable(allCookies, self.cookies_filename)

    def postURL(self, url):
        if self.cookies:
            if type(self.cookies) == str and self.cookies == 'recent':
                recent = True
            else:
                recent = False
            domain = self.extractDomain(url)
            cookies = []
            for cookieSet in _.getTable(self.cookies_filename):
                if domain == cookieSet['domain']:
                    shouldLoad = True
                    if recent and self.is_cookie_expired(cookieSet['epoch'], isCookie=False):
                        shouldLoad = False

                    if shouldLoad:
                        for cookie in cookieSet['cookies']:
                            if not 'expiry' in cookie:
                                cookies.append(cookie)
                            elif 'expiry' in cookie and not self.is_cookie_expired(cookie['expiry'], isCookie=True):
                                cookies.append(cookie)

            if not cookies is None:
                for cookie in cookies:
                    del cookie['expiry']
                    self.browser.add_cookie(cookie)
            if len(cookies):
                self.inject('location.reload();')
        self.wait()

    def url(self, url):
        self.initialize()
        self.preURL(url)
        self.browser.get(url)
        self.active = True
        self.postURL(url)

    def initialize(self):
        if self.browser is None:
            if __.isWin:
                self.browser = webdriver.Chrome(executable_path='C:\\Users\\Scott\\.rt\\profile\\exe\\chromedriver.exe')
            else:
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.binary_location = "/usr/bin/google-chrome"
                try:
                    service = Service(ChromeDriverManager().install())
                    self.browser = webdriver.Chrome(service=service, options=chrome_options)
                except TypeError:
                    self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    def setField(self, data, selector, enter=False, click=False):
        elem = self.select(selector)
        elem.send_keys(data)
        if enter:
            elem.send_keys(Keys.RETURN)
        elif not type(click) == bool:
            elemX = self.select(click)
            elemX.click()

    def save_to_json(data, filename='trades.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def scrape_data(self, url, callback):
        self.url(url)
        self.wait()
        trades = []
        rows = self.select('.table.table-hover tbody tr')
        for row in rows:
            trade = {
                'date': row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text,
                'representative': row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text,
                'ticker': row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text,
                'type': row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text,
                'amount': row.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text,
                'asset': row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text,
                'link': row.find_element(By.CSS_SELECTOR, 'td a').get_attribute('href')
            }
            trades.append(trade)
        callback(trades)

    def click_view_summary(self, callback):
        self.initialize()
        view_summary_links = self.browser.find_elements(By.LINK_TEXT, 'View Summary')
        urls = [link.get_attribute('href') for link in view_summary_links]
        threads = []
        for url in urls:
            thread = Thread(target=self.scrape_summary_data, args=(url, callback))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

    def scrape_summary_data(self, url, callback):
        self.browser.get(url)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
        trades = []
        rows = self.browser.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
        for row in rows:
            trade = {
                'date': row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text,
                'representative': row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text,
                'ticker': row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text,
                'type': row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text,
                'amount': row.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text,
                'asset': row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text,
                'link': row.find_element(By.CSS_SELECTOR, 'td a').get_attribute('href')
            }
            trades.append(trade)
        callback(trades)

    def get_view_summary_links(self):
        self.initialize()
        return self.browser.find_elements(By.LINK_TEXT, 'View Summary')

    def navigate_to_url(self, url):
        print('navigate_to_url',url)
        self.initialize()
        self.browser.get(url)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'View Summary')))

    def login(self, url, login, password, login_selector, password_selector, submit_selector=None):
        self.open(url)
        email_elem = self.browser.find_element_by_css_selector(login_selector)
        email_elem.send_keys(login)
        password_elem = self.browser.find_element_by_css_selector(password_selector)
        password_elem.send_keys(password)
        if submit_selector is None:
            password_elem.send_keys(Keys.RETURN)
        else:
            button1 = self.browser.find_element_by_css_selector(submit_selector)
            button1.click()
        time.sleep(3)

    def loginIndividually(self, url, login, password, login_selector, password_selector, login_button='', password_button='', rawPass=False):
        self.open(url)
        if not '.' in login_selector and not '#' in login_selector and not '[' in login_selector and not '=' in login_selector:
            email_elem = self.browser.find_element_by_name(login_selector)
        else:
            email_elem = self.browser.find_element_by_css_selector(login_selector)
        email_elem.send_keys(login)
        if login_button == '':
            email_elem.send_keys(Keys.RETURN)
        else:
            button1 = self.browser.find_element_by_css_selector(login_button)
            button1.click()
        time.sleep(1)
        if not '.' in password_selector and not '#' in password_selector and not '[' in password_selector and not '=' in password_selector:
            password_elem = self.browser.find_element_by_name(password_selector)
        else:
            password_elem = self.browser.find_element_by_css_selector(password_selector)
        if not rawPass:
            password = _blowfish.decrypt(password)
        if password.endswith(' '):
            password = _str.cleanEnd(password, ' ')
        password_elem.send_keys(password)
        password = ''
        if password_button == '':
            password_elem.send_keys(Keys.RETURN)
        else:
            button2 = self.browser.find_element_by_css_selector(login_button)
            button2.click()
        time.sleep(3)

    def open(self, url):
        self.initialize()
        self.url(url)

    def js(self, path=None):
        if path is None:
            return self.jq()
        elif path.startwith('https://') or path.startwith('http://'):
            return self.injectURL(path)
        elif os.path.isfile(path):
            return self.injectFile(path)
        else:
            return self.injectReturn(path)

    def jq(self):
        return self.jqueryInject()

    def jqueryInject(self):
        return self.injectURL('https://rightthumb.com/apps/selenium/jquery-1.11.3.js')

    def inject(self, code):
        newCode = ''
        if type(code) == list:
            newCode += _.flattenList(code)
        else:
            newCode += code
        self.browser.execute_script(newCode)

    def injectReturn(self, code):
        if not 'return ' in code:
            return self.browser.execute_script('return ' + code)
        else:
            return self.browser.execute_script(code)

    def injectURL(self, url):
        code = URL(url)
        return self.browser.execute_script(code)

    def injectFile(self, file):
        with open(file, 'r') as item:
            code = item.read()
            return self.browser.execute_script(code)

    def close(self):
        if self.browser:
            self.browser.quit()

    def wait(self):
        time.sleep(2)
        ix = 0
        while not self.injectReturn('return document.readyState;') == 'complete':
            self.inject("window.onload = function() { window.taskComplete=1; };")
            time.sleep(1)
            ix += 1
            _.pr(ix, end='\r', flush=True)

    def code(self):
        return self.browser.page_source

project = FrontEnd()

def action():
    project = _browser.imp.FrontEnd()
    url = 'https://housestockwatcher.com/summary_by_rep'
    project.navigate_to_url(url)
    project.click_view_summary(callback=save_to_json)
    project.close()

if __name__ == '__main__':
    action()
