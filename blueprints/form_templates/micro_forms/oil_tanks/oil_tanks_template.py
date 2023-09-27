lft = 'liquid fuel storage tank'
not_known = {
	'input_type':'bool_extra',
	'radio_options':[
		{'radio_text':'Not Known', 'radio_value':'not_known'}
	]
}

template={
	"Form" : "Domestic Liquid Fuel Storge", 
	"form_identifier":"domestic_liquid_fuel_storage",
	"Sections" : [
		{
			"section_name":"Tank Specifictions",
			"section_identifier":"tank_specifications",
			"main_questions":[
				{
					"question_title": "What type of fuel does the liquid fuel storage tank on the property store?",
					"identifier":"fuel_type", 
					"input_type":"radio",
					'radio_options':[
						{'radio_text':'kerosene', 'radio_value':'kerosene'},
						{'radio_text':'Red Diesel', 'radio_value':'red_diesel'},
						{'radio_text':'HVO/hydrotreated vegetable oil', 'radio_value':'HVO'},
						{'radio_text':'Other', 'radio_value':'other'},
					]
				},
				{
					"question_title": "What is the volume of the liquid fuel storage tank in Litres(l)?",
					"identifier":"tank_storage_volume", 
					"input_type":"litres",
				},
				{
					"question_title": "In what year the liquid fuel storage tank installed?",
					"identifier":"tank_installation_year", 
					"input_type":"year",
				},
				{
					"question_title": "",
					"identifier":"", 
					"input_type":"",
				},
																					
			],
		},
		{
			"section_name":"Environmental Regulations",
			"section_identifier":"environmental_regulations",
			"main_questions":[
				{
					"question_title": "The following qustions regard the ",
					"identifier":"", 
					"input_type":"",
					"question_set":'true',
					'sub_questions':[
						{
							"question_title": f"Is the {lft} located within 10 meters of inland freshwaters or coastal waters",
							"identifier":"fresh_or_coastal", 
						} | not_known,
						{
							"question_title": f"is the {lft} located where spillage could run into an open drain or to a loose-fitting manhole cover",
							"identifier":"into_drain", 
						} | not_known,
							
							
					]
				},
			],
		}
	],
}
	