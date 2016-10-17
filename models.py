import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *


DATABASE = SqliteDatabase('social.db')

class User(UserMixin, MOdel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(dafault=datetime.datetime.now)
    is_admin = BooleanField(default=False)


    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)


    def get_posts(self):
        return Post.select().where(Post.user ==self)

    def get_stream(self):
        return Post.select().where(
        (Post.user == self)
        )


    @classmethod
    def create_user(cls,username,email,password,admin=False):
        try:
            with DATABASE.transaction():
                cls.create(
                    username=username,
                    email=email,
                    password= generate_password_hash(password),
                    is_admin=admin)
        except IntegrityError:
            raise ValueError("user already exists")

class Post(MOdel):
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(
    rel_model=User,
    related_name='post'
    )
    content = TextField()

    class Meta:
        database=DATABASE
        order_by= ('-timestamp',)


class Relationship(MOdel):
    from_user = ForeignKeyField(USer, related_name = 'relationships')


def initialize():
    DATABASE.Connect()
    DATABASE.create_tables([User,Post], safe=True)
    DATABASE.close()
