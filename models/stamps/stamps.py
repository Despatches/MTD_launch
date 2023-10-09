import re

stamps  = {
	'off_grid_sewage':{
		'identifiers':{
			'TA6_Part_1.mains_drainage':{'values':['no'], 'status':'required', 'marks':[True]},
			#'TA6_Part_1.mains_drainage':{'values':['yes'], 'status':'secondary'}
		},
		'marks':{
			'default':{'text':['this property has no mains sewage connection']},
			'new_disclose':{'text':[
					"undertake the small sewage disclosure module to determine if this system is compliant with the current sewage discharge regulations",
					"if non complaint a despatches stratified mortgages may lend to cover the cost of bringing the property in addition to the purchase.",
					"cover for any non compliant damage done can be appended to conveyance indemnity "
				],
				"new_disclose_name":"Small Sewage",
				"linkage":"",
				"action":""
			},
			'loan_opp':{'text':['Loan Funding may be possible in order to enable installation of either mains sewage connection or a small sewage treatment plant']},
			'indem_opp':{'text':['An indemnity may be available in order to mitigate this risk']},
			'esg':{'text':['some esg text']}
			},
		'info_type':['']
	},
	'sewage_general_binding_rules_compliant':{
		'identifiers':{

		}
	},
	'permitted_development':{
		'identifiers':{
			'TA6_Part_1.conservation_area_bool':{'values':['yes'], 'status':'minimum.1', 'marks':['limited']},
			'TA6_Part_1.protected_buildings_bool':{'values':['yes'], 'status':'minimum.1', 'marks':['limited']},
		},
		'marks':{
			'default':'This property may have limitations effecting it\'s permitted development rights',
			'new_disclose':{'permitted_develop_status':{'':''},},
			'loan_opp':{},
			'indem_opp':{},
		},
		'info_type':{'legal_concern':True, 'estate_agent':'negative'}
	},
	'permitted_development_limitation':{
		'identifiers':{
			'TA6_Part_1.conservation_area_bool':{'values':['yes'], 'status':'minimum.1', 'marks':['limited']},
			'TA6_Part_1.protected_buildings_bool':{'values':['yes'], 'status':'minimum.1', 'marks':['limited']},
		},
	},
	'without_major_utility':{
		'identifiers':{
			'TA6_Part_1.mains_drainage':{'values':['no'], 'status':'minimum.1', 'marks':[True]},
			'TA6_Part_1.electricity':{'values':['no'], 'status':'minimum.1', 'marks':[True]},
			'TA6_Part_1.water_supply':{'values':['no'], 'status':'minimum.1', 'marks':[True]},	
		},
		'marks':{
			'default':'This does not have a mains connection to at least one major utility',
			'new_disclose':{'permitted_develop_status':{'':''},},
			'loan_opp':{},
			'indem_opp':{},
		}		
	},
	'off_grid_power':{
		'identifiers':{
			'TA6_Part_1.solar_panels':{'values':['yes'],'status':'minimum.1'}
		}
	},
	'eco_property':{
		'identifiers':{
			'TA6_Part_1.solar_panels':{'values':['yes'],'status':'minimum.2'},
			'TA6_Part_1.heat_pumps':{'values':['yes'],'status':'minimum.2'},
		},
		"marks":{"default":{"text":["This property is ideal for people interested in a more sustainable way of living or are interested in a low carbon lifestyle"]}}
	},
	'without_sewage':{
		'identifiers':{
			'TA6_Part_1.sewage_plant':{'values':['yes'], 'status':'required', 'marks':[True]},
			'TA6_Part_1.mains_drainage':{'values':['yes'], 'status':'required', 'marks':[True]}
		}
	},
	'not_suitable_For_habitation':{
		'identifiers':{
			'stamp.without_sewage':{'values':[True], 'status':'minimum.1', 'marks':[True]}
		},
		'marks':{
			'default':{'text':['this property is missing a major utilit and is therfore uninhabitable']},
			'new_disclose':{'permitted_develop_status':{'':''},},
			'loan_opp':{},
			'indem_opp':{},
		}		
	}
}

#evaluated individual data peices that make up a stamp
class stamp_identifier:
	def __init__(self, name, identifier):
		self.values = identifier['values']
		self.status = identifier['status']
		if 'marks' in identifier:
			self.marks = identifier['marks']
		else:self.marks = None
		self.name = name
		self.match = False
		self.finished =  False
		#find out subdivisions denoting which form the identifier belongs to
		x = re.search("\.", self.name)
		if not x == None:
			deci = x.start()
			self.form_loci = name[0:deci]
			self.identifier = name[deci+1:]
		x = re.search("\.", self.status)
		if not x == None:
			deci = x.start()
			primary = self.status[0:deci]
			secondary = self.status[deci+1:]
			if primary == 'minimum':
				self.minimum = int(secondary, 10)

	def truth(self, form):
		if self.identifier in form:
			for val in self.values:
				if form[self.identifier]['value'] ==  val:
					self.match = True
					break


#main body of stamp data
class stamp:
	def __init__(self, name, stamp):
		self.name = name
		self.identifiers = []
		self.outcomes = []
		self.bool = False
		self.mini_count = 0
		self.mini_threshold = 0
		self.marks = None
		if 'marks' in stamp:
			self.marks = stamp['marks']
		#for mark in stamp['marks']:
		#	continue
		for ident in stamp['identifiers']:
			self.identifiers.append( stamp_identifier(ident,stamp['identifiers'][ident]))
			if 'minimum' in self.identifiers[-1].__dict__:
				if self.mini_threshold == 0:
					self.mini_threshold = self.identifiers[-1].minimum
				self.mini_count += 1

	def test_threshold(self):
		if self.mini_threshold >0:
			if self.mini_count < self.mini_threshold:
				self.bool = False



	"""def test_status(self, form_Set):
		for ident in self.identifier:
			if ident.form_loci in form_Set:
				ident.truth(self.forms[ident.form_loci])
			if ident.match == False and ident.status == 'required':
				self.bool = False
				return False"""

class stamp_set:
	def __init__(self, stamp_list, forms):
		self.stamps = {}
		for s in stamp_list:
			cur_stamp = stamp(s, stamps[s])
			for ident in cur_stamp.identifiers:
				if ident.form_loci != stamp:
					if ident.form_loci in forms:
						ident.truth(forms[ident.form_loci]['data'])
					if ident.match == False and ident.status == 'required':
						cur_stamp.bool = False
						ident.finished = True
						break
					elif ident.match == False:
						cur_stamp.bool = False
					elif ident.match == True:
						cur_stamp.bool = True

			cur_stamp.test_threshold()
			if cur_stamp.bool != False:
				cur_stamp.identifiers = None
				self.stamps[s] = cur_stamp



