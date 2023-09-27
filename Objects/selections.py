#from wtforms import StringField, PasswordField, BooleanField, SubmitField
#from wtforms.validators import DataRequired
from launch import db

#class selection_set:
#	def __init__(self,)
#	type = StringField
#	particulars_ID =

class market_particular_selection:
	def __init__(self,db_row):
		self.parent_set = db_row[0]
		self.unique_selection_ID = db_row[1]
		self.parent_unique_selection_ID = db_row[2]
		self.selection_ans = db_row[3]
		self.lft = db_row[4]
		self.rgt = db_row[5]
		self.selection = db_row[6]
		self.user_validated = db_row[7]
		self.answer = db_row[8]
		self.answer_active = db_row[9]
		self.auxilliary_data = db_row[10]
		if self.auxilliary_data == "extra":
			self.ancilliary_data = db_row[17]
			self.ancilliary_data = db_row[18]
			self.previous_ancilliary_record = db_row[19]
		self.answer_meaning= db_row[11]
		self.competancy_imp= db_row[12]
		self.fraud_imp= db_row[13]
		self.inherant_risk_value= db_row[14]
		self.answer_implications= db_row[15]
		self.last_updated= db_row[16]
		return None