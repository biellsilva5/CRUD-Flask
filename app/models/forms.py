from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	email = StringField("email", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	remember_me = BooleanField("remember_me")

class MessageForm(FlaskForm):
	name = StringField("name", validators=[DataRequired()])
	email = StringField("email", validators=[DataRequired()])
	message = TextAreaField("message", validators=[DataRequired()])

class UserForm(FlaskForm):
	username = StringField("username", validators=[DataRequired()])
	email = StringField("email", validators=[DataRequired()])
	password =PasswordField("password", validators=[DataRequired()])

