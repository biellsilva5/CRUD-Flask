from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db

from app.models.forms import LoginForm, MessageForm, UserForm
from app.models.tables import User, Message

@app.route("/", methods=["GET", "POST"])
def index():

	login_form = LoginForm()
	message_form = MessageForm()
	new_user_form = UserForm()

	if login_form.validate_on_submit():
		user = User.query.filter_by(email= login_form.email.data).first()
		if user and user.password == login_form.password.data:
			login_user(user)
			flash("Logged in")
		else:
			flash("Invalid login")
	user_r = User.query.order_by(User.id).all()

	if message_form.validate_on_submit():
		message = Message(message_form.name.data,message_form.email.data,message_form.message.data)
		db.session.add(message)
		db.session.commit()
		flash("Successfully sent")

	message_r = Message.query.order_by(Message.id).all()


	return render_template('homepage.html',
						   login_form = login_form,
						   message_form = message_form,
						   new_user_form = new_user_form,
						   user_r = user_r,
						   message_r = message_r)

@app.route("/logout")
def Logout():
	logout_user()
	return redirect(url_for('index'))

@app.route("/user/new", methods=['GET', 'POST'])
def CreateUser():
	new_user_form = UserForm()

	if new_user_form.validate_on_submit():
		new_user = User(new_user_form.username.data, new_user_form.email.data, new_user_form.password.data)

		db.session.add(new_user)
		db.session.commit()

	return redirect(url_for('index'))

@app.route("/user/edit/<id>", methods=['GET', 'POST'])
def EditUser(id):
	edit_user_form = UserForm()
	user = User.query.get(id)

	if edit_user_form.validate_on_submit():

		user.username = edit_user_form.username.data
		user.email =  edit_user_form.email.data
		user.password = edit_user_form.password.data

		db.session.commit()	
		return redirect(url_for('index'))

	return render_template('user_edit.html',
		                   user = user,
		                   edit_user_form = edit_user_form)

@app.route("/message/delete/<id>", methods=['GET'])
def DeleteMessage(id):
	message = Message.query.filter_by(id=id).first()
	db.session.delete(message)
	db.session.commit()
	return redirect(url_for('index'))

@app.route("/user/delete/<id>", methods=['GET'])
def DeleteUser(id):
	user = User.query.filter_by(id=id).first()
	db.session.delete(user)
	db.session.commit()
	return redirect(url_for('index'))


