from flask import render_template, flash, redirect

@launch.route("/login")
def login():
	form = loginform()
	return render_template('login.html',title='Sign In', form=form)