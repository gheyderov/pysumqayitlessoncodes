from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    company = StringField('company', validators=[DataRequired()])
    message = TextAreaField('message', validators=[DataRequired()])
    is_subscribe = BooleanField('is_subscribe')


class ReviewForm(FlaskForm):
    message = TextAreaField('message', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])


class RegisterForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired()])
    confirm_password = StringField('confirm_password', validators=[DataRequired(), EqualTo('password')])


class LoginForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
