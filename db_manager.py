import peewee
from datetime import datetime
from models import *

class DbManager:
    @staticmethod
    def create_tables(models):
        for model in models:
            if not model.table_exists():
                db.create_tables([model])

if __name__ == '__main__':
    DbManager.create_tables([Question, Answer])
