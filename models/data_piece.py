class data_point:
	def __init__(self, results, create='ancilliary_form'):
		if create == 'ancilliary_form':
			self.false = results['false']
			self.form_object = results['form_object']
			self.identifier = results['identifier']
			self.input_type = results['input_type']
			self.mandatory = results['mandatory']
			self.section = results['section']
			self.value = results['value']
			self.work_tasks = []
			self.documents = []


#class TA6_data_point(data_point):
