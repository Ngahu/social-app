from flask_wtf import Form

from wtforms import StringField
from wtforms.validators import DataRequired, Regexp, ValidationError,Email
from models import User



def name_exists(form,field):
    if User.select().where(USer.username == field.data).exists():
        raise ValidationError('User with that name already exists.')


def email_exists(form,field):
    if User.select().where(USer.email == field.data).exists():
        raise ValidationError('User with that email already exists.')






class RegisterForm(Form):
    username= StringField(
    'username',
    validators={
    DataRequired(),
    Regexp(
        r'^[a-zA-Z0-9_] +$',
        message=("Username should be one word ,letters,numbers and unserscores only")
    ),
    name_exists
    ])

    email= StringField(
        'Email',
        validators= [
        DataRequired(),
        Email(),
        email_exists

        ])

    password = PasswordField(
    'Password'
    validators= [
    DataRequired(),
    Length(min=2),
    EqualTo('password2',message='Password must match')

    ])

password2 = PasswordField(
    'Confirm Password'
    validators= [DataRequired()]
)
