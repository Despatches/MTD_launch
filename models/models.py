from launch import db, templates
from flask import redirect, url_for
from flask_login import UserMixin
from launch.blueprints.form_templates import template_data_transitions as form_data
from launch.blueprints.form_templates.templates import templates

class User(UserMixin):
	def __init__(self,ID):
		user_get=db.cursor()
		user_data=f"""SELECT `user`.`user_ID`,
			    `user`.`first_name`,
			    `user`.`last_name`,
			    `user`.`other_names`,
			    `user`.`join_date`,
			    `user`.`user_email`,
			    `user`.`standard_user`,
			    `user`.`user_is_freeholder`,
			    `user`.`user_is_leaseholder`,
			    `user`.`user_password`,
			    `user`.`user_is_estate_agent`
				FROM `user_data`.`user`;"""

		user_get.execute(user_data)
		user=user_get.fetchone()
		if user == None or 0:
			self.id=None
			return None
		self.id = ID
		self.first_name = user[1]
		self.last_name = user[2]
		self.other_names = user[3]
		self.join_date = user[4]
		self.user_email = user[5]
		self.standard_user = user[6]
		self.user_is_freeholder = user[7]
		self.user_is_leaseholder = user[8]
		self.agent = user[10]
		if user[10] == 1:
			user_get.fetchall()
			user_data="select agency_ID from user_data.estate_agency_members where agency_member = %s"
			params= (ID,)
			user_get.execute(user_data,params)
			agency = user_get.fetchone()
			self.agency= agency[0]
		else:
			self.agency = False
		user_get.fetchall()
		user_get.close()
		return None

mp_title_derivatives = {
					'c_n_s':{
						'table':"`selection_routines`.`cns_within_market_partics`",
						'columns':[('reference_name',),('registered_at_companies_house',)]
					},
					'freehold_shares':{
						'table':"`selection_routines`.`unassigned_freehold_share`",
						'columns':[('provisioned_ID',),('reference_name',),]
					},
					'leaseholds':{
						'table':'`selection_routines`.`unassigned_leasehold`',
						'columns':[('reference_name','Name'), ('freehold_type', 'Freehold'), ('freehold_ID','Parent Freehold'), ('holding_ID',), ('X_location_point',), ('Y_location_point',)]
					},
					'commonholds':{
						'table':'`selection_routines`.`commonhold_within_market_partics`',
						'columns':[('reference_name',)]
					},
					'freeholds':{
						'table':'`selection_routines`.`unassigned_freehold`',
						'columns':[('reference_name','Name'), ('provisioned_ID', 'ID'), ('date_first_specified', 'Date First Specified'),('holding_ID',), ('x_location_point',), ('y_location_point',)]
					}
				}

def new_form_object(template_set,form_id):
	form_results = collect_form_data(template_set['query_columns'],form_id)

	new_ob = form_results_collection(form_results, template_set['query_select'], form_id, template['form_identifier'])
	return new_ob

class market_particulars:
	def __init__(self, market_particulars_id):
		market_partics_get = db.cursor()
		#mp_data = "select * from particulars_and_objects.market_particulars where market_particulars_ID = %s"
		mp_data = "SELECT \
			`market_particulars`.`market_particulars_ID`,\
    		`market_particulars`.`user_creator`,\
    		`market_particulars`.`vendor_ID`,\
    		`market_particulars`.`active_offers`,\
    		`market_particulars`.`assigned_agency`,\
    		`market_particulars`.`validated_vendor_lawyer`,\
    		`market_particulars`.`particulars_proceed_to_sale`,\
    		`market_particulars`.`optional_componants`,\
   		 	`market_particulars`.`confirmed_on_the_market`,\
    		`market_particulars`.`sudo_name`,\
    		`market_particulars`.`creation`,\
    		`market_particulars`.`last_user_to_change`,\
    		`market_particulars`.`last_data_change`\
		FROM `particulars_and_objects`.`market_particulars`\
		where`market_particulars_ID` = %s;"\

		params = (market_particulars_id,)
		market_partics_get.execute(mp_data,params)
		mp =market_partics_get.fetchone()
		self.id = mp[0]
		self.user_creator  = mp[1]
		self.vendor  = mp[2]
		self.active_offers  = mp[3]
		self.assigned_agency = mp[4]
		self.validated_vendor_lawyer = mp[5]
		self.particulars_proceed_to_sale = mp[6]
		self.optional_componants = mp[7]
		self.confirmed_on_the_market = mp[8]
		self.sudo_name = mp[9]
		self.creation = mp[10]
		self.forms={}

		market_partics_get.close()
		return None

	def add_form_data(self, form_name, form_id =False):
		if form_id != False:
			self.template_set = templates[form_name]
			self.forms[form_name] = new_form_object(template_set,form_id)

	def TA6_collection(self):
		self.TA6 = form_data.evaluate_form_mp_relation('TA6_Part_1', 'market_particulars',self.id)

	def TA6_subs_collection(self):
		if self.TA6[0] != None:
			form = self.TA6[0]
			template_set = templates['TA6_Part_1']
			self.TA6 = form_data.form_results_collection(form_data.collect_form_data(template_set['query_columns'],form), form, 'TA6_Part_1')
			#TA6_part_1_set.fraud_risk_comp(templates)
			self.TA6.append_data_group(template_set['comp_risk_fraud'])
			self.TA6.add_element_relevances()
			self.TA6.exclude_irrelevants()
			self.TA6.sub_forms_gather(True)

	def TA6_and_subs(self):
		self.TA6_collection()
		self.TA6_subs_collection()


	#Find forms that have been started or initiated for given market particular
	def form_status(self):
		self.forms = {}
		cursor = db.cursor()
		query = 'SELECT `form_name`, `form` FROM `particulars_and_objects`.`cur_forms`\
			WHERE market_particulars = %s'
		params = (self.id,)
		cursor.execute(query,params)
		results = cursor.fetchall()
		if len(results) != 0:
			for r in results:
				self.forms[r[0]] = {'id':r[1]}

	#def evaluate_Work_tasks(selef)

	def fetch_market_particular_components(self, td = mp_title_derivatives):
		cursor = db.cursor()
		query_columns = ''
		self.total_derivatives = 0
		self.title_derivatives={}
		for key in td:
			columns = td[key]['columns']
			max_cols = len(columns)
			self.title_derivatives[key] = {'data':[],'headings':[]}
			query_columns = '`{}`'.format(columns[0][0])
			for col in columns[1:]:
				query_columns += ',`{}`'.format(col[0])

			query = 'SELECT {} FROM {} WHERE market_particulars = %s'.format(query_columns,td[key]['table'])
			params = (self.id,)
			cursor.execute(query,params)
			results = cursor.fetchall()
			print(results)
			if results != 0:
				col_count = 0
				while col_count < max_cols:
					if len(columns[col_count]) == 2:
						print(columns[col_count])
						self.title_derivatives[key]['headings'].append(columns[col_count])
					col_count += 1
				for r in results:
					self.total_derivatives +=1
					new_ob = {}
					col_count = 0
					while col_count < max_cols:
						new_ob[columns[col_count][0]] = r[col_count]
						col_count += 1

					self.title_derivatives[key]['data'].append(new_ob)
		cursor.close()



class selection_set_mp:
	def __init__(self, market_particulars,selections_owner):
		mp_selections_get = db.cursor()
		query = f"select * from market_particulars_selection_set where market_particulars_selections_set_ID = {market_particulars} and selections_owner = {selections_owner}"
		mp_selections_get.execute(query)
		select_set = mp_selections_get.fetchone()
		self.market_particulars_selections_set_ID =[0]
		self.market_particulars_ID =[1]
		self.selections_owner =[2]
		self.selection_ID_counter =[3]
		self.creation_moment = [4]
		self.time_of_last_data_entry = [5]
		mp_selections_get.close()

class question:
	def __init__(self, Q_ID):
		get_q_data =db.cursor()
		query = f"select question_meaning from questions_answers.questions where Q_ID = {Q_ID}"
		get_q_data.execute(query)
		q_data = get_q_data.fetchone()
		self.Q_ID = Q_ID
		self.question_meaning = q_data
		get_q_data.close()

class answer:
	def __init__(self,data,Q_ID):
		self.parent_q = Q_ID
		self.answer = data[0]
		self.full_code = data[1]
		self.auxilliary_data = data[2]

	def add_to_selections_with_parents(abc, selec_set_ID, parent_selec_ID):
		answer = self['full_code']
		ans_type = self['type']
		answer_input = db.cursor()

		query = "select max(`lft`) into @lftmove from selection_routines.market_particulars_selections where market_particulars_selections.parent_set = %s and market_particulars_selections.unique_selection_ID=%s;"
		params = (f"{selec_set_ID}",f"{parent_selec_ID}")
		answer_input.execute(query,params)
		answer_input.execute("select @lftmove;")
		max_lft = answer_input.fetchone()
		if max_lft[0] == None or 0:
			add_to_selections_without_parents(answer,selec_set_ID)
			#query ='select max(`rgt`) into @lftmove from selection_routines.market_particulars_selections where market_particulars_selections.parent_set = %s;'
			#params = (selec_set_ID,)
			#answer_input.execute(query,params)
			#parent_selec_ID=None

		else:
			query = "update selection_routines.market_particulars_selections SET `rgt` := (`rgt`+2) where `rgt`>=@lftmove AND `parent_set`= %s;"
			params = (selec_set_ID,)
			answer_input.execute(query,params)

			query = "update selection_routines.market_particulars_selections SET `lft` := (`lft`+2) where `lft`>@lftmove and market_particulars_selections.parent_set = %s;"
			answer_input.execute(query,params)

	#update the counter to keep track of entries in selection sets
		#counter(selec_set_ID)
			count = counter(selec_set_ID)

			query ="select @lftmove"
			answer_input.execute(query)
			lftmove=answer_input.fetchone()
			if not lftmove[0]==None:

				query = "insert into selection_routines.market_particulars_selections(parent_set, unique_selection_ID, parent_unique_selection_ID, selection_ans,lft,rgt,selection) values (%s,@ID_counter, %s,%s,@lftmove + 1,@lftmove + 2,curdate())"
				params = (selec_set_ID,parent_selec_ID,answer)
				answer_input.execute(query,params)

	# end add_to_selections_with_parents procedure
				db.commit()
				answer_input.close()

			else:
				query = "insert into selection_routines.market_particulars_selections(parent_set, unique_selection_ID, parent_unique_selection_ID, selection_ans,lft,rgt,selection) values (%s,@ID_counter, %s,%s,1,2,curdate())"
				params = (selec_set_ID,parent_selec_ID,answer)
				answer_input.execute(query,params)

	#add extra data if extra type answer
		if ans["type"] == "extra":
			extra_data_store( ans,selec_set_ID)

	# end add_to_selections_with_parents procedure
		db.commit()
		answer_input.close()
		return None

class selection_set_queue:
	def __init__ (self):
		self.queue =[]

class answer_mp_data:
	def __init__(self,row):
		self.Q_ID = row[0]
		self.propagating_ID = row[1]
		self.full_code =  row[2]
		self.glossary_identifier = row[3]
		self.auxilliary_data = row[4]
		self.answer_text = row[5]
		self.question_meaning = row[6]
		self.glossary_term = row[7]

class title_derivative():
	def __init__(self,):
		return 0

class freehold(title_derivative):
	def __init__(self, row):
		self.holding_ID = row[0]
		self.market_particulars = row[1]
		self.creating_user = row[2]
		self.reference_name = row[3]
		self.provisioned_ID = row[4]
		self.date_first_specified = row[5]
		self.location_point ={"lat": row[6], "long": row[7]}

class offer:
	def __init__(self):
		return 0








