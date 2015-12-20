import scrapy
from selenium import webdriver
import time

class ScraperExample(scrapy.Spider):
    name = "scraper_example"
    allowed_domains = ['quora.com', 'answers.yahoo.com']
    start_urls = ['https://www.answers.yahoo.com']

    SLEEP_TIME = 0.75

    def __init__(self):
        self.driver = webdriver.Chrome()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_down_n_times(self, n):
        for i in range(n):
            self.scroll_down()
            time.sleep(self.SLEEP_TIME)

    def parse(self, response):
        self.driver.get(response.url)
        self.scroll_down_n_times(25)

        # begin scraping

        self.driver.close()
