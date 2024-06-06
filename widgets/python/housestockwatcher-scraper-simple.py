#!/usr/bin/python3
import json
import time
import subprocess
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Setup logging
logging.basicConfig(filename='scrape_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
        self.scraped_data = []
        self.initialize_browser()

    def initialize_browser(self):
        logging.info("Initializing browser")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=chrome_options)
        logging.info("Browser initialized")

    def open_url(self, url):
        logging.info(f"Opening URL: {url}")
        self.browser.get(url)
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.LINK_TEXT, 'View Summary')))
        logging.info(f"URL opened: {url}")

    def select_elements(self, selector):
        logging.info(f"Selecting elements with selector: {selector}")
        elements = self.browser.find_elements(By.CSS_SELECTOR, selector)
        logging.info(f"Found {len(elements)} elements")
        return elements

    def connect_to_vpn(self):
        vpn_server = self.vpn_servers[self.current_vpn]
        logging.info(f"Connecting to VPN: {vpn_server}")
        subprocess.run(['sudo', 'openvpn', '--config', vpn_server])
        time.sleep(15)  # Wait for VPN connection to establish
        logging.info(f"Connected to VPN: {vpn_server}")

    def disconnect_vpn(self):
        vpn_server = self.vpn_servers[self.current_vpn]
        logging.info(f"Disconnecting from VPN: {vpn_server}")
        subprocess.run(['sudo', 'killall', 'openvpn'])
        time.sleep(5)  # Wait for VPN disconnection
        logging.info(f"Disconnected from VPN: {vpn_server}")

    def switch_vpn(self):
        logging.info("Switching VPN")
        self.disconnect_vpn()
        self.current_vpn = (self.current_vpn + 1) % len(self.vpn_servers)
        self.connect_to_vpn()
        logging.info("VPN switched")

    def click_view_summary(self):
        self.open_url('https://housestockwatcher.com/summary_by_rep')
        view_summary_links = self.select_elements('a[href*="/summary_by_rep"]')

        for link in view_summary_links:
            try:
                href = link.get_attribute('href')
                logging.info(f"Found link: {href}")
                self.scrape_summary_data(href)
                time.sleep(1)  # Slight delay to prevent overwhelming the server
            except StaleElementReferenceException as e:
                logging.error(f"StaleElementReferenceException: {e}")
                continue

    def scrape_summary_data(self, url):
        logging.info(f"Scraping data from: {url}")
        time.sleep(3)  # Pause to minimize firewall blocking
        self.browser.get(url)
        time.sleep(2)  # Pause before scraping
        try:
            WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr'))
            )
        except TimeoutException:
            self.log_status(f"Timeout when loading {url}")
            self.statuses.append('fail')
            logging.warning(f"Timeout when loading {url}")
            if self.statuses[-5:] == ['fail'] * 5:  
                logging.info("Switching VPN due to repeated failures")
                self.switch_vpn()
                self.scrape_summary_data(url)
            return

        trades = []
        rows = self.retry_find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

        for row in rows:
            try:
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
                logging.info(f"Scraped trade: {json.dumps(trade, indent=4)}")
            except StaleElementReferenceException as e:
                logging.error(f"Error scraping row: {e}")
                continue

        self.scraped_data.extend(trades)
        self.save_to_json(trades)
        self.statuses.append('success')

    def retry_find_elements(self, by, value, retries=3, delay=2):
        for attempt in range(retries):
            try:
                return self.browser.find_elements(by, value)
            except StaleElementReferenceException:
                logging.warning(f"Retry {attempt + 1}/{retries} for finding elements by {by} with value {value}")
                time.sleep(delay)
        return []

    def save_to_json(self, data):
        logging.info("Saving scraped data to JSON")
        with open('trades.json', 'w') as f:
            json.dump(self.scraped_data, f, indent=4)
        logging.info("Data saved to JSON")

    def log_status(self, message):
        logging.info(f"Logging status: {message}")
        with open('scrape_log.txt', 'a') as log:
            log.write(f"{message}\n")

    def close_browser(self):
        if self.browser:
            logging.info("Closing browser")
            self.browser.quit()
            logging.info("Browser closed")

def main():
    scraper = HouseStockWatcherScraper()
    retry_attempts = 3
    for attempt in range(retry_attempts):
        try:
            logging.info(f"Attempt {attempt + 1} to scrape data")
            scraper.click_view_summary()
            break
        except Exception as e:
            scraper.log_status(f"Main URL loading failed: {e}")
            logging.error(f"Main URL loading failed: {e}")
            scraper.switch_vpn()
            time.sleep(5)  # Wait before retrying
    scraper.close_browser()

if __name__ == '__main__':
    main()
