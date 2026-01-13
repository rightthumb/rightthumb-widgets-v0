#!/usr/bin/python3
import json
import time
import threading
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import subprocess

class HouseStockWatcherScraper:
	def __init__(self):
		self.vpn_servers = [
			'aleen.sds.sh.ovpn',
			'batuu.sds.sh.ovpn',
			'lothal.sds.sh.ovpn',
			'raada.sds.sh.ovpn',
			'remote.sds.sh.ovpn',
			'rodia.sds.sh.ovpn',
			'vpn.sds.sh.ovpn',
		]
		self.no_multithreading_vps = {
			'vpn1.server.com': True,
			'vpn2.server.com': True
		}
		self.statuses = []
		self.current_vpn = 0
		self.initialize_browser()
		self.log_file = 'scrape_log.txt'
		self.scraped_data = []

	def initialize_browser(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--no-sandbox")
		chrome_options.add_argument("--disable-dev-shm-usage")
		service = Service(ChromeDriverManager().install())
		self.browser = webdriver.Chrome(service=service, options=chrome_options)

	def open_url(self, url):
		self.browser.get(url)
		WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.LINK_TEXT, 'View Summary')))

	def select_elements(self, selector):
		return self.browser.find_elements(By.CSS_SELECTOR, selector)

	def connect_to_vpn(self):
		vpn_server = self.vpn_servers[self.current_vpn]
		subprocess.run(['sudo', 'openvpn', '--config', f'{vpn_server}.ovpn'])
		time.sleep(15)  # Wait for VPN connection to establish

	def disconnect_vpn(self):
		subprocess.run(['sudo', 'killall', 'openvpn'])
		time.sleep(5)  # Wait for VPN disconnection

	def switch_vpn(self):
		self.disconnect_vpn()
		self.current_vpn = (self.current_vpn + 1) % len(self.vpn_servers)
		self.connect_to_vpn()

	def click_view_summary(self):
		self.open_url('https://housestockwatcher.com/summary_by_rep')
		view_summary_links = self.select_elements('a[href*="/summary_by_rep"]')
		threads = []

		if self.vpn_servers[self.current_vpn] in self.no_multithreading_vps:
			for link in view_summary_links:
				href = link.get_attribute('href')
				self.scrape_summary_data_thread(href)
				time.sleep(1)  # Slight delay to prevent overwhelming the server
		else:
			for link in view_summary_links:
				href = link.get_attribute('href')
				thread = threading.Thread(target=self.scrape_summary_data_thread, args=(href,))
				threads.append(thread)
				thread.start()
				time.sleep(1)  # Slight delay to prevent overwhelming the server

			for thread in threads:
				thread.join()

	def scrape_summary_data_thread(self, url):
		thread_browser = self.create_new_browser_instance()
		self.scrape_summary_data(thread_browser, url)
		thread_browser.quit()

	def create_new_browser_instance(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--no-sandbox")
		chrome_options.add_argument("--disable-dev-shm-usage")
		service = Service(ChromeDriverManager().install())
		return webdriver.Chrome(service=service, options=chrome_options)

	def scrape_summary_data(self, browser, url):
		print('scrape_summary_data', url)
		browser.get(url)
		time.sleep(2)  # Pause before scraping
		try:
			WebDriverWait(browser, 15).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr'))
			)
		except:
			self.log_status(f"Timeout when loading {url}")
			self.statuses.append('fail')
			if self.statuses[-5:] == ['fail'] * 5:
				self.switch_vpn()
				self.scrape_summary_data(browser, url)
			return

		trades = []
		rows = browser.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

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
			self.log_status(f"scrape_summary_data {url}")
			print(json.dumps(trade, indent=4))

		self.scraped_data.extend(trades)
		self.save_to_json(trades)
		self.statuses.append('success')

	def save_to_json(self, data):
		with open('trades.json', 'w') as f:
			json.dump(self.scraped_data, f, indent=4)

	def log_status(self, message):
		with open(self.log_file, 'a') as log:
			log.write(f"{message}\n")

	def close_browser(self):
		if self.browser:
			self.browser.quit()

def main():
	scraper = HouseStockWatcherScraper()
	retry_attempts = 3
	for _ in range(retry_attempts):
		try:
			scraper.click_view_summary()
			break
		except Exception as e:
			scraper.log_status(f"Main URL loading failed: {e}")
			scraper.switch_vpn()
			time.sleep(5)  # Wait before retrying
	scraper.close_browser()

if __name__ == '__main__':
	main()


















# #!/usr/bin/python3
# import json
# import time
# import threading
# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import subprocess

# class HouseStockWatcherScraper:
#     def __init__(self):
#         self.vpn_servers = [
#             'vpn1.server.com',
#             'vpn2.server.com',
#             'vpn3.server.com',
#             'vpn4.server.com',
#             'vpn5.server.com',
#             'vpn6.server.com',
#         ]
#         self.current_vpn = 0
#         self.initialize_browser()
#         self.log_file = 'scrape_log.txt'
#         self.scraped_data = []

#     def initialize_browser(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         service = Service(ChromeDriverManager().install())
#         self.browser = webdriver.Chrome(service=service, options=chrome_options)

#     def open_url(self, url):
#         self.browser.get(url)
#         WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'View Summary')))

#     def select_elements(self, selector):
#         return self.browser.find_elements(By.CSS_SELECTOR, selector)

#     def connect_to_vpn(self):
#         vpn_server = self.vpn_servers[self.current_vpn]
#         subprocess.run(['sudo', 'openvpn', '--config', f'{vpn_server}.ovpn'])
#         time.sleep(10)  # Wait for VPN connection to establish

#     def disconnect_vpn(self):
#         subprocess.run(['sudo', 'killall', 'openvpn'])
#         time.sleep(5)  # Wait for VPN disconnection

#     def switch_vpn(self):
#         self.disconnect_vpn()
#         self.current_vpn = (self.current_vpn + 1) % len(self.vpn_servers)
#         self.connect_to_vpn()

#     def click_view_summary(self):
#         self.open_url('https://housestockwatcher.com/summary_by_rep')
#         view_summary_links = self.select_elements('a[href*="/summary_by_rep"]')
#         threads = []

#         for link in view_summary_links:
#             href = link.get_attribute('href')
#             thread = threading.Thread(target=self.scrape_summary_data_thread, args=(href,))
#             threads.append(thread)
#             thread.start()
#             time.sleep(1)  # Slight delay to prevent overwhelming the server

#         for thread in threads:
#             thread.join()

#     def scrape_summary_data_thread(self, url):
#         thread_browser = self.create_new_browser_instance()
#         self.scrape_summary_data(thread_browser, url)
#         thread_browser.quit()

#     def create_new_browser_instance(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         service = Service(ChromeDriverManager().install())
#         return webdriver.Chrome(service=service, options=chrome_options)

#     def scrape_summary_data(self, browser, url):
#         print('scrape_summary_data', url)
#         browser.get(url)
#         time.sleep(2)  # Pause before scraping
#         try:
#             WebDriverWait(browser, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr'))
#             )
#         except:
#             self.log_status(f"Timeout when loading {url}")
#             return

#         trades = []
#         rows = browser.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

#         for row in rows:
#             trade = {
#                 'date': row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text,
#                 'representative': row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text,
#                 'ticker': row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text,
#                 'type': row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text,
#                 'amount': row.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text,
#                 'asset': row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text,
#                 'link': row.find_element(By.CSS_SELECTOR, 'td a').get_attribute('href')
#             }
#             trades.append(trade)
#             self.log_status(f"scrape_summary_data {url}")
#             print(json.dumps(trade, indent=4))

#         self.scraped_data.extend(trades)
#         self.save_to_json(trades)

#     def save_to_json(self, data):
#         with open('trades.json', 'w') as f:
#             json.dump(self.scraped_data, f, indent=4)

#     def log_status(self, message):
#         with open(self.log_file, 'a') as log:
#             log.write(f"{message}\n")

#     def close_browser(self):
#         if self.browser:
#             self.browser.quit()

# def main():
#     scraper = HouseStockWatcherScraper()
#     retry_attempts = 3
#     for _ in range(retry_attempts):
#         try:
#             scraper.click_view_summary()
#             break
#         except Exception as e:
#             scraper.log_status(f"Main URL loading failed: {e}")
#             scraper.switch_vpn()
#             time.sleep(5)  # Wait before retrying
#     scraper.close_browser()

# if __name__ == '__main__':
#     main()