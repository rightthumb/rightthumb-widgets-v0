#!/usr/bin/python3
import json
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

    def scrape_links(self):
        self.open_url('https://housestockwatcher.com/summary_by_rep')
        view_summary_links = self.select_elements('a[href*="/summary_by_rep"]')
        links = []
        for link in view_summary_links:
            try:
                href = link.get_attribute('href')
                links.append(href)
                logging.info(f"Found link: {href}")
            except StaleElementReferenceException as e:
                logging.error(f"StaleElementReferenceException: {e}")
                continue
        return links

    def save_to_json(self, data, filename):
        logging.info(f"Saving data to {filename}")
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info("Data saved to JSON")

    def close_browser(self):
        if self.browser:
            logging.info("Closing browser")
            self.browser.quit()
            logging.info("Browser closed")

def main():
    scraper = HouseStockWatcherScraper()
    try:
        links = scraper.scrape_links()
        for index, link in enumerate(links, start=1):
            print(f"{index}: {link}")
        scraper.save_to_json(links, 'summary_by_rep.json')
    finally:
        scraper.close_browser()

if __name__ == '__main__':
    main()
