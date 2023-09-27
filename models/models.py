from launch import db, templates
from flask import redirect, url_for
from flask_login import UserMixin
from launch.blueprints.form_templates import template_data_transitions as form_data
from launch.blueprints.form_templates.templates import templates
from launch.models.stamps import stamps
import re

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

#class title_derivative():
#	def __init__(data_list,pair_set):
#		self.X_location_point = 


#class cns(title_derivative):

basic_deriv_data_pair = [('reference_name','Name'), ('date_first_specified', 'Date First Specified'), 
						('ID',), ('parent_object_type',),
						('provisioned_ID',), ('parent_ID',),('creating_user',),('verified',),('verified_id',),
						('X_location_point',), ('Y_location_point',)]

cns = basic_deriv_data_pair[0:-2]
cns += [('registry_name', 'Name At registered at Registry'),('percentage', 'Share Percentage')]

mp_title_derivatives = {
					'c_n_s':{
						'table':"`companies_and_shares`.`company_share`",
						'columns':cns
					},
					'freehold_shares':{
						'table':"`title_derivatives`.`freehold_share`",
						'columns':basic_deriv_data_pair +[('percentage', 'Share Percentage'),]
					},
					'leaseholds':{
						'table':'`title_derivatives`.`leasehold`',
						'columns':basic_deriv_data_pair + [('sub_lease',),('material_parent',)]
					},
					'commonholds':{
						'table':'`title_derivatives`.`common_hold`',
						'columns':basic_deriv_data_pair +[('percentage_ownership', 'Share Percentage'), ('percentage_vote', 'Vote Percentage')]
					},
					'freeholds':{
						'table':'`title_derivatives`.`freehold`',
						'columns':basic_deriv_data_pair
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
    		`market_particulars`.`last_data_change`,\
    		`market_particulars`.`single_point_loci_lat`,\
    		`market_particulars`.`single_point_loci_lng`\
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
		self.last_user_to_change = mp[11]
		self.last_data_change = mp[12]
		self.single_point_x = mp[13]
		self.single_point_y = mp[14]
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
			for sub in self.TA6.sub_forms:
				self.forms[sub] = self.TA6.sub_forms[sub]
			self.forms['TA6_Part_1'] = self.TA6.__dict__
		else:
			self.TA6 = None

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

			query = "SELECT {} FROM {} WHERE parent_ID = %s AND parent_object_type = 'market_particular'".format(query_columns,td[key]['table'])
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

	#outmoded pre objectg orientated stamp_evaluation
	"""def stamp_evaluation(self):
		self.stamps ={}
		for stamp in stamps:
			cur_stamp =  stamps[stamp]
			stamp_attr = {}
			stamp_value = True
			for stamp_key in cur_stamp['identifiers']:
				print(stamp_key)
				x = re.search("\.", stamp_key)
				if not x == None:
					deci = x.start()
					form_loci = stamp_key[0:deci]
					identifier = stamp_key[deci+1:]
					print(form_loci,identifier)
					if form_loci in self.forms:
						form = self.forms[form_loci]
						if identifier in form['data']:
							match = False
							for val in cur_stamp['identifiers'][stamp_key]['values']:
								print(val, form['data'][identifier]['value'])
								if form['data'][identifier]['value'] ==  val:
									stamp_attr[stamp_key] = {'value':val}
									match = True
									break
							if match == False and cur_stamp['identifiers'][stamp_key]['status'] ==  'required':
								stamp_value = False
								break
			self.stamps[stamp] = stamp_value"""

	def stamp_evaluation(self):
		self.stamps = stamps.stamp_set(stamps.stamps,self.forms)

	def auto_objects(self):
		if self.total_derivatives != 0:
			return 0
		if self.TA6 != None:
			lease_or_free = self.TA6.data['lease_or_free']['value']
			if lease_or_free  != 'empty':
				if lease_or_free == 'Freehold':
					self.new_freehold_derivative()
				elif lease_or_free == 'Leasehold':
					self.new_leasehold_derivative()

	def new_freehold_derivative(self):
		cursor = db.cursor()
		query = """INSERT INTO `title_derivatives`.`freehold`
					(
					`creating_user`,
					`reference_name`,
					`parent_object_type`,
					`parent_ID`,
					`verified`,
					`x_location_point`,
					`y_location_point`,
					`other_data`,
					`date_first_specified`)
					VALUES
					(%s,
					%s,
					%s,
					%s,
					%s,
					%s,
					%s,
					%s,
					NOW());
					"""
		params = (None, self.sudo_name+ ' Freehold', 'market_particular', self.id, self.single_point_x, self.single_point_y,'')

		cursor.execute(query, params)
		db.commit()
		cursor.close()
		return 0

	def new_leasehold_derivative(self):
		cursor = db.cursor()
		query = """INSERT INTO `title_derivatives`.`leasehold`
					(
					`parent_object_type`,
					`creating_user`,
					`reference_name`,
					`parent_ID`,
					`x_location_point`,
					`y_location_point`,
					`other_data`,
					`date_first_specified`)
					VALUES
					(
					%s,
					%s,
					%s,
					%s,
					%s,
					%s,
					%s,
					NOW());

					"""
		params = ('market_particular', None, self.sudo_name+ ' Leasehold', self.id, self.single_point_x, self.single_point_y,'')

		cursor.execute(query, params)
		print('works')
		db.commit()
		cursor.close()
		return 0

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








