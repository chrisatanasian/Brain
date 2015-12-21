from peewee import *

db = SqliteDatabase('brain.db')

class Question(Model):
    question_content = CharField()
    timestamp = DateField()
    upvotes = IntegerField()
    category = CharField()



class Answer(Model):
	answer_content = CharField()
	timestamp = DateField()
	upvotes = IntegerField()
	question_tag = ForeignKeyField('Question')
