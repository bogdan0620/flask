from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostProblem(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired('Напиши заголовок')])
    message = TextAreaField('Проблема', validators=[DataRequired('Опиши проблему')])
    button = SubmitField('Опубликовать')