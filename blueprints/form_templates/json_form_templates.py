from flask import json,jsonify, render_template
import copy
from launch.blueprints.form_templates.TA6_part_1.TA6_part_1 import TA6_Part_1
from launch.blueprints.form_templates.micro_forms.subsidence.subsidence import subsidence
from launch.blueprints.form_templates.micro_forms.attic.attic_development.attic_development import attic_development
from launch.blueprints.form_templates import template_data_transitions as form_data

templates = {'TA6_Part_1':TA6_Part_1, 'subsidence':subsidence, 'attic_development':attic_development}

#class based template sort deprecated
"""class template_sorter:
	def init(self, template, full_q=False):
		self.flow_controls = []
		self.questions = {}
		self.sections = []
		self.template = []
		class ident_prefix:
			def __init__(self):
				self.list = []

			def find_ident_prefix(self, parent):
				if 'ident_prefix' in parent:
					#print(parent['ident_prefix'])
					self.list.append(parent['ident_prefix'])

			def pop_ident_prefix(self, parent):
				if 'ident_prefix' in parent:
					print(self.list.pop(-1))

			def calc_ident_prefix(self, ident):
				if len(self.list) == 0:
					#print(0)
					return ident
				else:
					#print(len(self.list))
					new_ident = ''
					for p in self.list:
						new_ident += p

					new_ident += ident
					return new_ident

			def reset(self):
				self.list = []

		self.ident_prefix_list = ident_prefix()

	def template_sort(self):
		for section in self.template['Sections']:
			self.sections.append(section['section_identifier'])
			self.questions[section['section_identifier']] = []
			self.section_questions = questions[section['section_identifier']]
			ident_prefix_list.find_ident_prefix(section)
			for question in section["main_questions"]:
				self.question = question
				question['identifier'] = ident_prefix_list.calc_ident_prefix(question['identifier'])
				ident_prefix_list.find_ident_prefix(question)
				questions.cur_focus = section_questions
				form_object = 'none'
				if ('question_set' in question and type(question['question_set']) == dict) or 'input_type' in question:
					if 'question_set' in question and question['question_set'] != 'true':
						form_object = question['question_set']
						question['input_type'] = 'none'
					if full_q == True:
						question['form_object'] = form_object
						questions.cur_focus.append(question);
					else:
						if 'mandatory' in question and question['mandatory'] == 'true':
							mandatory = 'true'
						else:
							mandatory = 'false'
						if 'styling' in question:
							questions.cur_focus.append({'input_type':question['input_type'],'identifier':question['identifier'], 'styling':question['styling'], 'mandatory':mandatory, 'form_object':copy.deepcopy(form_object)})
						else:
							questions.cur_focus.append({'input_type':question['input_type'],'identifier':question['identifier'], 'mandatory':mandatory, 'form_object':copy.deepcopy(form_object)})

				if 'input_type' in question and question['input_type'] == 'multi_row' and len(question['sub_questions']) > 0:
					questions.cur_focus[-1]['data_rows'] = []
					questions.cur_focus = questions.cur_focus[-1]['data_rows']
					self.question_loop(question, form_object)
				else:
					self.question_loop(question, form_object)

				display_reliance(question)
				ident_prefix_list.pop_ident_prefix(question)
			ident_prefix_list.pop_ident_prefix(section)
		ident_prefix_list.reset()

		return {'flow_controls':flow_controls, 'questions':questions, 'sections':sections, 'template':template}

	def question_loop(form_object = 'none'):
		question = self.question
		if 'sub_questions' in question:
			if 'question_set' in question and question['question_set'] != 'true':
				form_object = question['question_set']
				question['input_type'] = 'none'
			for q in question['sub_questions']:
				if 'question_set' in q:
					if q['question_set'] != 'true':
						form_object = q['question_set']
						q['input_type'] = 'none'
				q['identifier'] = ident_prefix_list.calc_ident_prefix(q['identifier'])
				ident_prefix_list.find_ident_prefix(q)

				if 'input_type' in q and ('question_set' not in q or q['question_set'] != 'true'):
					if 'element' in q:
						print(q['element'])
						form_object['element'] = q['element']
					if full_q == True:
						questions.cur_focus.append(q)
					else:
						if 'mandatory' in q and q['mandatory'] == 'true':
							mandatory = 'true'
						else:
							mandatory = 'false' 
						if 'styling' in q:
							questions.cur_focus.append({'input_type':q['input_type'],'identifier':q['identifier'], 'styling':q['styling'] ,'mandatory':mandatory, 'form_object':copy.deepcopy(form_object)})
						else:
							questions.cur_focus.append({'input_type':q['input_type'],'identifier':q['identifier'], 'mandatory':mandatory, 'form_object':copy.deepcopy(form_object)})								
				display_reliance(q, parent = question['identifier'])
				question_loop(q, form_object)
				ident_prefix_list.pop_ident_prefix(q)

	def question_loop_reliance(effector, reliance):
		question = self.question
		if 'sub_questions' in question:
			for q in question['sub_questions']:	
				if effector == q['identifier']:
					reliance['type'] = q['input_type']
				else:
					question_loop_reliance(q, effector, reliance)

	def display_reliance(question, **kwargs):
		if 'display_reliance' in question:
			full_r=[]
			ident = question['identifier']
			for reliance in question['display_reliance']:
				if reliance['identifier'] == 'parent':
					reliance['identifier'] = kwargs['parent']
				effector = reliance['identifier']
				for section in template['Sections']:
					for question in section["main_questions"]:
						if effector == question['identifier']:
							reliance['type'] = question['input_type']
						else:
							question_loop_reliance(question, effector, reliance)
				full_r.append(reliance)
			

			reliances = {'control_subject':ident, 'reliances':full_r}
			flow_controls.append(reliances)"""
def input_type_eval(question):
	print(question)
	result_options = []
	column_data = None
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
			column_data = 'ENUM ("empty",'
			opt_count = 0
			result_options = ['empty']
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
		result_options = ['none', 'value']

	elif question['input_type'] == 'detail_text':
		#details_enum.append(question['identifier'])
		column_data = 'BOOL DEFAULT FALSE'
		result_options = ['true', 'false']

	elif question['input_type'] == 'docu':
		#docu_enum.append(question['identifier'])
		column_data = 'BOOL DEFAULT FALSE'
		result_options = ['true', 'false']

	elif question['input_type'] == 'checkbox':
		column_data = 'ENUM ("empty","yes","no") NOT NULL'
		result_options = ['empty', 'yes', 'no']

	elif question['input_type'] == 'date':
		column_data = 'DATE'
		result_options = ['none', 'value']

	elif question['input_type'] == 'currency':
		column_data = 'DOUBLE PRECISION (11,2)'
		result_options = ['none', 'value']

	elif question['input_type'] == 'postcode':
		column_data = 'CHAR (8)'
		result_options = ['none', 'value']

	elif question['input_type'] == 'number':
		column_data = 'INT'
		result_options = ['none', 'value']

	else:
		column_data =  'VARCHAR (120)'
		result_options = ['none', 'value']

	return {'sql_data_type':column_data, 'result_options':result_options}

# ful q copies the full template data of a question into template sort objects for internal usage
# kwargh options = 'modifiers' (allow modifier files to be passed with templates)
def template_sort(template, full_q = False, **kwargs):
	flow_controls = []
	sections = []
	section_controls = []

	class questions:
		def __init__(self):
			self.sections={}
			self.focus =[]

		def add_sec(self, ident):
			self.sections[ident] = []

		def new_focus(self,focus):
			self.focus.append(focus)
			self.cur_focus=self.focus[-1]

		def remove_focus(self):
			self.focus.pop(-1)
			if len(self.focus) > 0:
				self.cur_focus = [-1]

	class ident_prefix:
		def __init__(self):
			self.list = []

		def find_ident_prefix(self, parent):
			if 'ident_prefix' in parent:
				#print(parent['ident_prefix'])
				self.list.append(parent['ident_prefix'])

		def pop_ident_prefix(self, parent):
			if 'ident_prefix' in parent:
				print(self.list.pop(-1))

		def calc_ident_prefix(self, ident):
			if len(self.list) == 0:
				#print(0)
				return ident
			else:
				#print(len(self.list))
				new_ident = ''
				for p in self.list:
					new_ident += p

				new_ident += ident
				return new_ident

		def reset(self):
			self.list = []

	ident_prefix_list = ident_prefix()

	def question_loop(question, form_object = 'none'):
		if 'sub_questions' in question:
			if 'question_set' in question and question['question_set'] != 'true':
				form_object = question['question_set']
				question['input_type'] = 'none'
			for q in question['sub_questions']:
				if 'modifiers' in kwargs:
					for mod in 'modifiers':
						if q['identifier'] in mod:
							for key in mod[q['identifier']]:
								q[key] = mod[q['identifier']][key]
				if 'question_set' in q:
					if q['question_set'] != 'true':
						form_object = q['question_set']
						q['input_type'] = 'none'
				q['identifier'] = ident_prefix_list.calc_ident_prefix(q['identifier'])
				ident_prefix_list.find_ident_prefix(q)

				if 'input_type' in q and ('question_set' not in q or q['question_set'] != 'true'):
					if 'element' in q:
						#print(q['element'])
						form_object['element'] = q['element']
					if full_q == True:
						questions.cur_focus.append(q)
					else:
						if 'mandatory' in q and q['mandatory'] == 'true':
							mandatory = 'true'
						else:
							mandatory = 'false' 
						if 'styling' in q:
							questions.cur_focus.append({'input_type':q['input_type'],'identifier':q['identifier'], 'styling':q['styling'] ,'mandatory':mandatory, 'form_object':copy.deepcopy(form_object)})
						else:
							questions.cur_focus.append({'input_type':q['input_type'],'identifier':q['identifier'], 'mandatory':mandatory, 'form_object':copy.deepcopy(form_object)})								
				display_reliance(q, parent = question['identifier'])
				multi_row_loop(q, form_object)
				ident_prefix_list.pop_ident_prefix(q)

	def question_loop_reliance(question, effector, reliance):
		if 'sub_questions' in question:
			for q in question['sub_questions']:	
				if effector == q['identifier']:
					reliance['type'] = q['input_type']
				else:
					question_loop_reliance(q, effector, reliance)

	def display_reliance(question, **kwargs):
		if 'display_reliance' in question:
			full_r=[]
			if 'type' in kwargs and kwargs['type'] == 'section':
				ident = question['section_identifier']
			else:
				ident = question['identifier']
			for reliance in question['display_reliance']:
				if reliance['identifier'] == 'parent':
					reliance['identifier'] = kwargs['parent']
				effector = reliance['identifier']
				for section in template['Sections']:
					for question in section["main_questions"]:
						if effector == question['identifier']:
							reliance['type'] = question['input_type']
						else:
							question_loop_reliance(question, effector, reliance)
				full_r.append(reliance)
			

			reliances = {'control_subject':ident, 'reliances':full_r}
			if 'type' in kwargs and kwargs['type'] == 'section':
				section_controls.append(reliances)
			flow_controls.append(reliances)

	#print(template)

	def multi_row_loop(question, form_object):
		if 'input_type' in question and question['input_type'] == 'multi_row' and len(question['sub_questions']) > 0:
			questions.cur_focus[-1]['data_rows'] = []
			questions.new_focus(questions.cur_focus[-1]['data_rows'])
			question_loop(question, form_object)
			questions.remove_focus()
		else:
			question_loop(question, form_object)

	questions = questions()
	for section in template['Sections']:
		if 'display_reliance' in section:
			display_reliance(section, type='section')
		sec_ident = section['section_identifier']
		sections.append(sec_ident)
		questions.add_sec(sec_ident)
		questions.new_focus(questions.sections[sec_ident])
		ident_prefix_list.find_ident_prefix(section)
		for question in section["main_questions"]:
			if 'modifiers' in kwargs:
				for mod in 'modifiers':
					if question['identifier'] in mod:
						for key in mod[question['identifier']]:
							question[key] = mod[question['identifier']][key]
			question['identifier'] = ident_prefix_list.calc_ident_prefix(question['identifier'])
			ident_prefix_list.find_ident_prefix(question)
			form_object = 'none'
			if ('question_set' in question and type(question['question_set']) == dict) or 'input_type' in question:
				if 'question_set' in question and question['question_set'] != 'true':
					form_object = question['question_set']
					question['input_type'] = 'none'
				if full_q == True:
					question['form_object'] = form_object
					questions.cur_focus.append(question);
				else:
					if 'mandatory' in question and question['mandatory'] == 'true':
						mandatory = 'true'
					else:
						mandatory = 'false'
					if 'styling' in question:
						questions.cur_focus.append({'input_type':question['input_type'],'identifier':question['identifier'], 'styling':question['styling'], 'mandatory':mandatory, 'form_object':copy.deepcopy(form_object)})
					else:
						questions.cur_focus.append({'input_type':question['input_type'],'identifier':question['identifier'], 'mandatory':mandatory, 'form_object':copy.deepcopy(form_object)})

			multi_row_loop(question, form_object)

			display_reliance(question)
			ident_prefix_list.pop_ident_prefix(question)
		ident_prefix_list.pop_ident_prefix(section)
		questions.remove_focus()
	ident_prefix_list.reset()

	return {'flow_controls':flow_controls, 'questions':questions.sections, 'sections':sections, 'template':template, 'section_controls':section_controls}

class template_form_form:
	"""docstring for ClassName"""
	def __init__(self, template_name):
		cursor = db.cursor()
		query = """SELECT {},{},{},{},{},{} FROM `template_forms`.`template_forms_data` 
		WHERE	name = {}"""

		data = {'name':template_name}
		query.format('template','query_selet','query_columns','sub_tables_list','pairings','object_links', **data)

		cursor.execute(query)
		template = cursor.fetchall()
		self.template = template[0]
		self.query_select = template[1]
		self.query_columns = template[2]
		self.sub_tables_list = template[3]
		self.pairings = template[4]
		self.pairings = object_links[5]

def basic_template_render(template, submission_sequence='sections', url='/TA6_Part_1_submit'):
	returns = template_sort(template)
	new_template = (returns['template'])
	main_form_data = {'result_send':json.dumps('none'), 'sub_tables_send':json.dumps('none'),'section_marker':0}
	for key in returns:
		main_form_data[key]=json.dumps(returns[key])
	main_form_data
	sub_forms = 0
	main_form_data['submission_sequence'] = json.dumps(submission_sequence)
	return render_template("Json_form_templating/Json_form_templating.html", main_form_data = main_form_data,template=new_template, sub_forms=sub_forms, submission_sequence=submission_sequence, submission_url=url, test='test')
	
#create meaning files or modifier files or
# current error means modifier files innacurate as they do not account for template data assigned to areas with the attribute 'question_set':'true'
def create_meaning_lists(template, typing='meanings',**kwargs):
	data_meanings = {}
	itera = 'ans'
	if typing == 'meanings':
		add_on = {'meanings':''}
	elif typing == 'duplicate':
		add_on ={
			'question_title':'',
			'extra_question_text':['']
		}
		itera = 'question'
	if 'add_on' in kwargs:
		if kwargs['add_on'] != None:
			add_on = kwargs['add_on']
	def multi_loop(result):
		if result['input_type'] == 'multi_row':
			for m in result['data_rows']:
				data_meanings[m['identifier']] ={}
				if itera == 'ans':
					result_options = input_type_eval(m)['result_options']
					for r in result_options:
						data_meanings[m['identifier']][r] = add_on
				else:
					data_meanings[m['identifier']] = add_on
					data_meanings[m['identifier']]['orig'] = copy.deepcopy(m['question_title'])
					data_meanings[m['identifier']] = copy.deepcopy(data_meanings[m['identifier']])
				multi_loop(m)

	results = template_sort(template, True)['questions']
	for section in results:
		for question in results[section]:
			if itera == 'ans':
				data_meanings[question['identifier']] = {}
				result_options = input_type_eval(question)['result_options']
				for r in result_options:
					data_meanings[question['identifier']][r] = add_on
			else:
				data_meanings[question['identifier']] =add_on
				data_meanings[question['identifier']]['orig'] = copy.deepcopy(question['question_title'])
				data_meanings[question['identifier']] = copy.deepcopy(data_meanings[question['identifier']])

			multi_loop(question)

	return data_meanings




		



	