from flask import json,jsonify, render_template
import copy


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


def template_sort(template, full_q = False):
	flow_controls = []
	sections = []

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
		sec_ident = section['section_identifier']
		sections.append(sec_ident)
		questions.add_sec(sec_ident)
		questions.new_focus(questions.sections[sec_ident])
		ident_prefix_list.find_ident_prefix(section)
		for question in section["main_questions"]:
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

	return {'flow_controls':flow_controls, 'questions':questions.sections, 'sections':sections, 'template':template}

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


		



	