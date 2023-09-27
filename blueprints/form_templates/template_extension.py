def extend_template(extension_temp, extend_temp, extension_point):
	extender = extension_point['identifier']
	if extension_point['extend_type'] == 'template':
		extend_temp['Sections'].append(extension_temp)

	elif extension_point['extend_type']  == 'section':
		for section in extend_temp['Sections']:
			if section['section_identifier'] == extender:
				section['section_identifier']['main_questions'].append(extension_temp)

	def q_loop(loop_set, identifier):
		for q in loop_set:
			if identifier == q['identifier']:
				if 'sub_questions' in q:
					q.append(extension_temp)
				else:
					q['sub_questions'] = [extension_temp]
				return 'match'
			else:
				if 'sub_questions' in q:
					q_loop(q['sub_questions'],identifier)
		return None


	elif extension_point['extend_type']  == 'question':
		for section in extend_temp['Sections']:
			extend_status = q_loop(section['main_questions'], extender)
			if extend_status == 'match':
				break

	return extend_temp
