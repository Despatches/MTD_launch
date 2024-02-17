from launch.blueprints.form_templates import obj_form_collection
from launch.blueprints.form_templates import new_db_sql_code_writer as data_vals
from launch.blueprints.models.models import market_particulars
import pandas as pd
import numpy
"""def input_types_section_loop(sections)
	def input_type_eval(question):
		result_options = []
		if question['input_type'] == 'bool':
			column_data = 'ENUM ("empty","yes","no") NOT NULL'
			result_options = ['empty', 'yes', 'no']

		elif question['input_type'] == 'bool_extra':
			column_data = 'enum ("empty","yes","no"'
			result_options = ['empty', 'yes', 'no']
			if 'radio_options' in question and len(question['radio_options']) > 0:
				for opt in question['radio_options']:
					result_options.append(opt['radio_value'])
					radio_value = opt['radio_value']
					column_data += f',"{radio_value}"'
				column_data += ') NOT NULL'

		elif question['input_type'] == 'radio':
			result_options = []
			if 'radio_options' in question and len(question['radio_options']) > 0:
				column_data = 'ENUM ('
				opt_count = 0
				for opt in question['radio_options']:
					if opt_count > 0:
						column_data += ','
					radio_value = opt['radio_value']
					column_data += f'"{radio_value}"'
					opt_count += 1

					result_options.append(opt['radio_value'])
				column_data += ') NOT NULL'

		elif question['input_type'] == 'text':
			column_data =  'VARCHAR (120)'
			result_options = ['true', 'false']

		elif question['input_type'] == 'detail_text':
			details_enum.append(question['identifier'])
			column_data = 'BOOL DEFAULT FALSE'
			result_options = ['true', 'false']

		elif question['input_type'] == 'docu':
			column_data = 'BOOL DEFAULT FALSE'
			result_options = ['true', 'false']

		elif question['input_type'] == 'checkbox':
			column_data = 'ENUM ("empty","yes","no") NOT NULL'
			result_options = ['empty', 'yes', 'no']

		elif question['input_type'] == 'date':
			column_data = 'DATE'

		elif question['input_type'] == 'currency':
			column_data = 'DOUBLE PRECISION (11,2)'

		elif question['input_type'] == 'postcode':
			column_data = 'CHAR (8)'

		elif question['input_type'] == 'number':
			column_data = 'INT'

		else:
			column_data =  'VARCHAR (120)'		
	def input_types_question_loop(loop_item):
		for question in loop_item:
			if 'question_set' not in question:
				if 'input_type' in question:
					if question['input_type'] != 'multi_row':
						row = question['identifier']

	for section in sections:
		input_types_question_loop(section['main_questions'])"""

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


class particulars_selection_group():
	def __init__(self, limit, particular_type):
		table = '`particulars_and_objects`.`{}`'.format(particular_type)
		query = """SELECT market_particulars_ID FROM {}
					ORDER BY RAND()
					LIMIT {}""".format(table, limit)

		cursor = db.cursor()
		cursor.execute(query)
		mps = cursor.fetchall()
		for mp in mps:
			new_mp = repr(particular_type)(),
			new_mp.form_status()
			#for r in self.forms




