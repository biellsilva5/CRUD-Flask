from flask_login import UserMixin
from app import db, lm

@lm.user_loader
def load_user(user_id):
	return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.username

class Message(db.Model):
	__tablename__ = "messages"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	message = db.Column(db.Text, nullable=False)

	def __init__(self, name, email, message):
		self.name = name
		self.email = email
		self.message = message

	def __repr__(self):
		return '<User %r>' % self.name