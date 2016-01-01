import peewee
import re
from datetime import datetime, timedelta
from models import *

class DbManager:
    @staticmethod
    def convert_date_string_to_datetime(date_string):
        num_regex = re.findall('\d+', date_string)
        if (len(num_regex) == 0):
            return datetime.now()

        n_hours_or_minutes = int(num_regex[0])

        if 'hours' in date_string:
            return datetime.now() - timedelta(hours = n_hours_or_minutes)
        elif 'days' in date_string:
            return datetime.now() - timedelta(days = n_hours_or_minutes)

        return datetime.now()

    @staticmethod
    def create_tables(models):
        for model in models:
            if not model.table_exists():
                db.create_tables([model])

    @staticmethod
    def add_question(question):
        try:
            db_question = Question.create(content=question['content'],
                                          upvotes=question['upvotes'],
                                          category=question['category'],
                                          timestamp=question['timestamp'])
            db_question.save()
        except peewee.IntegrityError:
            print question['content'] + ' already in database'

    @staticmethod
    def add_answer(answer):
        db_answer = Answer.create(content=answer['content'],
                                  upvotes=answer['upvotes'],
                                  is_best_answer=answer['is_best_answer'],
                                  timestamp=answer['timestamp'])
        db_answer.save()

if __name__ == '__main__':
    DbManager.create_tables([Question, Answer])
