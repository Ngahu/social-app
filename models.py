import datetime

from peewee import *
DATABASE = SqliteDatabase('social.db')

class User(MOdel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(dafault=datetime.datetime.now)
    is_admin = BooleanField(default=False)
