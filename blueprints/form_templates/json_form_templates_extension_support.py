from flask import json,jsonify

def template_sort(template, full_q = False):
	multi_form = False
	flow_controls = []
	questions = {}
	sections = []

	class ident_prefix:
		def __init__(self):
			self.list = []

		def find_ident_prefix(self, parent):
			if 'ident_prefix' in parent:
				#print(parent['ident_prefix'])
				self.list.append(parent['ident_prefix'])

		def pop_ident_prefix(self, parent):
			if 'ident_prefix' in parent:
				self.list.pop(-1)

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

	def question_loop(question):
		if 'sub_questions' in question:
			for q in question['sub_questions']:
				q['identifier'] = ident_prefix_list.calc_ident_prefix(q['identifier'])
				print(q['identifier'])
				ident_prefix_list.find_ident_prefix(question['identifier'])
				if 'input_type' in q and('questions_set' not in q or q['questions_set'] != 'true'):
					if full_q == True:
						current_section.append(q)
					else:
						if 'styling' in q:
							current_section.append({'input_type':q['input_type'],'identifier':q['identifier'], 'styling':q['styling'] })
						else:
							current_section.append({'input_type':q['input_type'],'identifier':q['identifier']})								
				display_reliance(q, parent = question['identifier'])
				question_loop(q)
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

	def template_extension_loop(template, flow_controls ,questions ,sections):
		for section in template['Sections']:
			if 'form_identifier' in section:
				extend_form = section['form_identifier']
				multi_form = True
				sections.append({'form_identifier':extend_form, 'sections':[]})
				questions[section['section_identifier']] = 'extension_form'
				template_extension_loop(section, flow_controls, )
			sections.append(section['section_identifier'])
			questions[section['section_identifier']] = []
			section_questions = questions[section['section_identifier']]
			ident_prefix_list.find_ident_prefix(section)
			for question in section["main_questions"]:
				question['identifier'] = ident_prefix_list.calc_ident_prefix(question['identifier'])
				ident_prefix_list.find_ident_prefix(question)
				current_section = section_questions
				if 'input_type' in question and ('questions_set' not in question or question['questions_set'] != 'true'):
					if full_q == True:
						current_section.append(question)
					else:
						if 'styling' in question:
							current_section.append({'input_type':question['input_type'],'identifier':question['identifier'], 'styling':question['styling'] })
						else:
							current_section.append({'input_type':question['input_type'],'identifier':question['identifier']})

				if 'input_type' in question and question['input_type'] == 'multi_row' and len(question['sub_questions']) > 0:
					current_section[-1]['data_rows'] = []
					current_section = current_section[-1]['data_rows']
					question_loop(question)
				else:
					question_loop(question)

				display_reliance(question)
				ident_prefix_list.pop_ident_prefix(question)
			ident_prefix_list.pop_ident_prefix(section)
		return {'flow_controls':flow_controls, 'questions':questions, 'sections':sections, 'template':template}

	return template_extension_loop(template, flow_controls ,questions ,sections)

class template_form_form:
	"""docstring for ClassName"""
	def __init__(self, template_name):
		cursor = db.cursor()
		query = "SELECT {},{},{},{},{},{} FROM `template_forms`.`template_forms_data` WHERE\
				name = {}"
		data = {'name':template_name}
		query.format('template','query_selet','query_columns','sub_tables_list','pairings','object_links', **data)

		cursor.execute(query)
		template = cursor.fetchall()[0]
		self.template = template[0]
		self.query_select = template[1]
		self.query_columns = template[2]
		self.sub_tables_list = template[3]
		self.pairings = template[4]
		self.pairings = object_links[5]


		



	