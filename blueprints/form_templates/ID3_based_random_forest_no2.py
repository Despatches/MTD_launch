from launch.blueprints.form_templates import obj_form_collection
from launch.blueprints.form_templates import new_db_sql_code_writer as data_vals
from launch.blueprints.models import models
import pandas as pd
import numpy

#collect data in reference to particular selection group

class particulars_selection_group():
	def __init__(self, limit, particular_type, form_name = False):

		table = '`particulars_and_objects`.`{}`'.format(particular_type)

		if form_name != False:
			query = """SELECT `market_particulars`.`market_particulars_ID`, `{form_name}_market_particulars_relationship`.`form_id` FROM {table},
					INNER JOIN  `form_data`.`{form_name}_market_particulars_relationship`
					ON `{form_name}_market_particulars_relationship`.`market_particulars` = `market_particulars`.`market_particulars_ID`
					ORDER BY RAND()
					LIMIT {limit};""".format(table= table,limit=limit, form_name=form_name)
		self.mps_list = []
		cursor = db.cursor()
		cursor.execute(query)
		mps = cursor.fetchall()
		#self.mps_list = [market_particulars(mp[0]) for mp in mps]
		returns = template_sort(templates[form_name][template])
		for mp in mps:
			new_mp = models.market_particulars(mp[0])
			new_mp.add_form_data(form_name, mp[1])
			new_mp.add_element_relevances(self.template_set.template)
			self.mps_list.append(new_mp)
			#new_mp = repr(particular_type)(),
			#for r in self.forms




class data_catagory:
	def __init__(self, column):
		for key in column:
			self.key

class template_into_ml:
	def __init__(self, template, query_select, result_options_list):
		self.analysis_name = template['Form']

class selection_group:
	def __init__(self,form_name, limit)
		self.template_set = template_set[form_name]
		self.template = template_set['template']
		cursor = db.cursor()

		self.variants = data_vals.create_new_sql_table(template,'a', data_res = 'yes')
		self.form_set = templates[form_name]
		query = """SELECT form_id FROM {}
					ORDER BY RAND()
					LIMIT {}""".format(form_name, limit)

		cursor.execute(query)

		form_id_set = cursor.fetchall()
		self.data_set = []
		for form in form_id_set:
			form_results = obj_form_collection.form_results_collection(obj_form_collection.collect_form_data(template_set['query_columns'],form), template_set['query_select'], form, template['form_identifier'])
			form_results.add_element_relevances(template)
			form_results.exclude_irrelevants()
			form_results.value_interpret()
			self.data_set.append(form_results)

	def ID3(self, deciding_data):
		self.total_data_rows = len(self.data_set)
		self.total_entropy = 0
		def total_entropy():
			for data_piece in deciding_data:
				# area of code will vary dependant on what predictions will be made
				#end_predict_count = 0
				#for ident in 
				predict_entropy = - (end_predict_count/self.total_data_rows)
				self.total_entropy += predict_entropy

		def calculate_entropy():
			feature_count = len(self.variants)
			entropy = 0
			for c in deciding_data:
				# area of code will vary dependant on what predictions will be made
				predict_options_breakdown =
				piece_entropy = 0
				if predict_options_breakdown != 0:
					option_probability = predict_options_breakdown/feature_count
					piece_entropy =- option_probability*np.log2(option_probability)
				entropy += piece_entropy
			return entropy

		def calc_info_gain(piece_name):
			piece_options = self.variants[piece_name]
			piece_info = 0.0

			for piece_option in piece_options:

				piece_val_count = 0
				for data_set in self.data_set:
					if data_set['data'][piece_name]['relevant'] != 1:
						if data_set['data'][piece_name]['value'] == piece_option:
							piece_val_count += 1
				piece_entropy = calculate_entropy()

		def informative_piece():
			max_info_gain = max_info_piece = None

			for piece in self.variants:
				piece_info_gain = calc_info_gain(piece.key())

# sort rationalisation of options that are physically non selectable due to flow controls
# begin sequence by only only using selections that are not effected by flow controls




