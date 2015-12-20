import scrapy
from selenium import webdriver
import time

class ScraperExample(scrapy.Spider):
    name = "scraper_example"
    allowed_domains = ["quora.com", "answers.yahoo.com"]
    start_urls = ["https://www.answers.yahoo.com"]

    SLEEP_TIME = 0.75
    CSS_QUESTION = ".Fz-14.Fw-b.Clr-b.Wow-bw.title"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_down_n_times(self, n):
        for i in range(n):
            self.scroll_down()
            time.sleep(self.SLEEP_TIME)

    def get_questions(self):
        return [i.get_attribute('text') for i in self.driver.find_elements_by_css_selector(self.CSS_QUESTION)]

    def parse(self, response):
        self.driver.get(response.url)
        self.scroll_down_n_times(1)

        self.get_questions()

        self.driver.close()
