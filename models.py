from peewee import *

db = SqliteDatabase('brain.db')

class BaseModel(Model):
    class Meta:
        database = db

class Question(BaseModel):
    content = CharField(unique=True)
    upvotes = IntegerField()
    category = CharField()
    timestamp = DateField()

class Answer(BaseModel):
    question = ForeignKeyField(Question, related_name='answers')
    content = CharField()
    upvotes = IntegerField()
    is_best_answer = BooleanField()
    timestamp = DateField()
