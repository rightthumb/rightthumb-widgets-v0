#!/usr/bin/python3
import json
import yaml
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Setup logging
logging.basicConfig(filename='scrape_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class HouseStockWatcherScraper:
    def __init__(self):
        print("Initializing scraper")
        self.initialize_browser()
        self.data_file = 'summary_by_rep.json'
        self.load_existing_data()

    def initialize_browser(self):
        print("Initializing browser")
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
        print("Browser initialized")

    def open_url(self, url):
        print(f"Opening URL: {url}")
        logging.info(f"Opening URL: {url}")
        self.browser.get(url)
        try:
            WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table')))
        except TimeoutException:
            logging.error(f"TimeoutException: {url} did not load a table in time.")
            print(f"TimeoutException: {url} did not load a table in time.")
            return False
        logging.info(f"URL opened: {url}")
        print(f"URL opened: {url}")
        return True

    def load_existing_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
            print(f"Loaded existing data with {len(self.data)} entries.")
        else:
            self.data = []
            print("No existing data found, starting fresh.")

    def save_to_json(self):
        logging.info(f"Saving data to {self.data_file}")
        print(f"Saving data to {self.data_file}")
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)
        logging.info("Data saved to JSON")
        print("Data saved to JSON")

    def scrape_page(self, url):
        if not self.open_url(url):
            return

        rows = self.browser.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

        for row in rows:
            trade = {}
            try:
                trade['date'] = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text
            except NoSuchElementException:
                trade['date'] = ''
                print("No date found")

            try:
                trade['representative'] = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
            except NoSuchElementException:
                trade['representative'] = ''
                print("No representative found")

            try:
                trade['ticker'] = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
            except NoSuchElementException:
                trade['ticker'] = ''
                print("No ticker found")

            try:
                trade['type'] = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
            except NoSuchElementException:
                trade['type'] = ''
                print("No type found")

            try:
                trade['amount'] = row.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
            except NoSuchElementException:
                trade['amount'] = ''
                print("No amount found")

            try:
                trade['asset'] = row.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text
            except NoSuchElementException:
                trade['asset'] = ''
                print("No asset found")

            try:
                trade['link'] = row.find_element(By.CSS_SELECTOR, 'td a').get_attribute('href')
            except NoSuchElementException:
                trade['link'] = ''
                print("No link found")

            self.data.append(trade)
            self.print_yaml(trade)
            self.save_to_json()

    def print_yaml(self, data):
        print(yaml.dump(data, default_flow_style=False))

    def close_browser(self):
        if self.browser:
            logging.info("Closing browser")
            print("Closing browser")
            self.browser.quit()
            logging.info("Browser closed")
            print("Browser closed")

def main():
    scraper = HouseStockWatcherScraper()
    try:
        with open('summary_by_rep.json', 'r') as f:
            links = json.load(f)
        
        for index, link in enumerate(links):
            print(f"Scraping link {index + 1}/{len(links)}: {link}")
            scraper.scrape_page(link)
    finally:
        scraper.close_browser()

if __name__ == '__main__':
    main()
