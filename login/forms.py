from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RegisterLogin(FlaskForm):
    name = StringField('Имя')
    password = StringField('Пароль')
    button = SubmitField('Вход')
