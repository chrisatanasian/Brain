import scrapy
from selenium import webdriver
import time


#quora login, username and password of throwaway account hardcoded
class LoginSpider(scrapy.Spider):
    name = 'quora.com login'
    start_urls = ['http://www.quora.com/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'mnakerov@gmail.com', 'password': 'thuglife12345678'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

#quora scraper adopted from chris's code
class QuoraScraper(scrapy.Spider):
    name = "quora_scraper"
    allowed_domains = ["quora.com"]
    start_urls = ["https://www.quora.com/topic/Medicine-and-Healthcare"]

    SLEEP_TIME      = 0.75
    QUORA_CSS_QUESTION    = "rendered_qtext"
    QUORA_CSS_BEST_ANSWER = "ExpandedQText.ExpandedAnswer"
    UPVOTES = "count"
    #doesn't do all answers on a question yet. only top answer + upvote


    def __init__(self):
        self.driver = webdriver.Chrome()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_down_n_times(self, n):
        for i in range(n):
            self.scroll_down()
            time.sleep(self.SLEEP_TIME)

    def get_questions(self):
        return [q.text for q in self.driver.find_elements_by_css_selector(self.CSS_QUESTION)]

    def get_best_answers(self):
        return [ba.text for ba in self.driver.find_elements_by_css_selector(self.CSS_BEST_ANSWER)]

    def get_upvote(self):
        return [u.text for u in self.driver.find_elements_by_css_selector(self.UPVOTES)]


    def parse(self, response):
        self.driver.get(response.url)
        self.scroll_down_n_times(1)

        questions    = self.get_questions()
        best_answers = self.get_best_answers()

        assert len(questions) == len(best_answers)

        self.driver.close()
