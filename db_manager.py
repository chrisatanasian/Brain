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

    @staticmethod
    def add_answer(answer):
        db_answer = Answer.create(content=answer.content,
                                  upvotes=answer.upvotes,
                                  is_best_answer=answer.is_best_answer,
                                  timestamp=answer.fromtimestamp(answer.created_utc))
        db_answer.save()

if __name__ == '__main__':
    DbManager.create_tables([Question, Answer])
