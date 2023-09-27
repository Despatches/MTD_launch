from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired

class loginform(FlaskForm):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password',validators=[DataRequired()])
	remember_me = BooleanField ('Remember Me')
	submit = SubmitField('Sign In')

#class answer_recieve(FlaskForm):
