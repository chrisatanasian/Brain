import scrapy
from selenium import webdriver
import time
import re
from datetime import datetime, timedelta

class ScraperExample(scrapy.Spider):
    name            = 'scraper_example'
    allowed_domains = ['quora.com', 'answers.yahoo.com']
    start_urls      = ['https://www.answers.yahoo.com']

    SLEEP_TIME            = 0.75
    CSS_QUESTION          = '.Fz-14.Fw-b.Clr-b.Wow-bw.title'
    CSS_BEST_ANSWER       = '.desc.Fz-13.Lh-18'
    CSS_DATE_AND_CATEGORY = '.Clr-888.Fz-12.Lh-18'

    def __init__(self):
        self.driver = webdriver.Chrome()

    def scroll_down(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_down_n_times(self, n):
        for i in range(n):
            self.scroll_down()
            time.sleep(self.SLEEP_TIME)

    def get_questions(self):
        return [q.text for q in self.driver.find_elements_by_css_selector(self.CSS_QUESTION)]

    def get_best_answers(self):
        return [ba.text for ba in self.driver.find_elements_by_css_selector(self.CSS_BEST_ANSWER)]

    def get_question_dates(self):
        return [d.text.encode('utf8').split('\xb7')[-1] for d in self.driver.find_elements_by_css_selector(self.CSS_DATE_AND_CATEGORY)]

    def get_categories(self):
        return [c.text.encode('utf8').split('\xb7')[-2] if len(c.text.encode('utf8').split('\xb7')) > 1 else '' for c in self.driver.find_elements_by_css_selector(self.CSS_DATE_AND_CATEGORY)]

    def convert_date_string_to_date(self, date_string):
        n_hours_or_minutes = int(re.findall('\d+', date_string)[0])

        if 'hours' in date_string:
            return datetime.now() - timedelta(hours = n_hours_or_minutes)
        elif 'days' in date_string:
            return datetime.now() - timedelta(days = n_hours_or_minutes)

        return datetime.now()

    def parse(self, response):
        self.driver.get(response.url)
        self.scroll_down_n_times(1)

        questions    = self.get_questions()
        time.sleep(self.SLEEP_TIME)

        best_answers = self.get_best_answers()
        time.sleep(self.SLEEP_TIME)

        dates        = self.get_question_dates()
        time.sleep(self.SLEEP_TIME)

        categories   = self.get_categories()
        time.sleep(self.SLEEP_TIME)

        assert len(questions) == len(best_answers) == len(dates) == len(categories)

        self.driver.close()
