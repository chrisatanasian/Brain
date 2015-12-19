import scrapy
from selenium import webdriver

class ScraperExample(scrapy.Spider):
    name = "scraper_example"
    allowed_domains = ['quora.com', 'answers.yahoo.com']
    start_urls = ['https://www.answers.yahoo.com']

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)

        while True:
            # scroll down to the bottom of the page
            # begin scraping

        self.driver.close()
