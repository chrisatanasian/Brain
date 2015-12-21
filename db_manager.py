import peewee
from datetime import datetime
from models import *

class DbManager:
    @staticmethod
    def create_tables(models):
        for model in models:
            if not model.table_exists():
                db.create_tables([model])

    @staticmethod
    def add_question(question):
        try:
            db_question = Question.create(content=question.content,
                                          upvotes=question.upvotes,
                                          category=question.category,
                                          timestamp=datetime.fromtimestamp(question.created_utc))
            db_question.save()
        except peewee.IntegrityError:
            print question.content + ' already in database'

if __name__ == '__main__':
    DbManager.create_tables([Question, Answer])
