lft = 'liquid fuel storage tank'
not_known = {
	'input_type':'bool_extra',
	'radio_options':[
		{'radio_text':'Not Known', 'radio_value':'not_known'}
	]
}

template={
	"Form" : "Domestic Liquid Fuel Storage", 
	"form_identifier":"domestic_liquid_fuel_storage",
	"Sections" : [
		{
			"section_name":"Tank Specifictions",
			"section_identifier":"tank_specifications",
			"main_questions":[
				{
					"question_title": "What type of fuel is contained in the liquid fuel storage tank on this property?",
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
					"question_title": "What volume of fuel can be held in the liquid fuel storage tank (in Litres)?",
					"identifier":"tank_storage_volume", 
					"input_type":"litres",
				},
				{
					"question_title": "In what year was the liquid fuel storage tank installed?",
					"identifier":"tank_installation_year", 
					"input_type":"year",
				},
				{
					"question_title": "Is the fuel storage tank bunded? ",
					'other question text': ['a bund is a secondary protective containment capable of retaining the tank content in the event that the primary tank were to fail.'],
					"identifier":"is_tank_bunded", 
					"input_type":"bool",
				},
																					
			],
		},
		
		{
			"section_name":"Environmental Regulations",
			"section_identifier":"environmental_regulations",
			"main_questions":[
				{
					"question_title": "The following questions regard statutory Environmental Regulations ",
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
		{
			"section_name":"Tank Proximities",
			"section_identifier":"tank_proximities",
			"main_questions":[
				{
					"question_title": "Is the tank located within 100m of a drainage ditch, culvert or watercourse?",
					"identifier":"fuel_type", 
					"input_type":"radio",
					'radio_options':[
						{'radio_text':'kerosene', 'radio_value':'kerosene'},xs
						{'radio_text':'Red Diesel', 'radio_value':'red_diesel'},
						{'radio_text':'HVO/hydrotreated vegetable oil', 'radio_value':'HVO'},
						{'radio_text':'Other', 'radio_value':'other'},
					]
				},
				{
					"question_title": "Is the tank located within 10m of any flamable structure or building?",
					"identifier":"proximity_flamables", 
					"input_type":"bool",
				},
				{
					"question_title": "Had a fireproof barrier been installed between the {ltf} and the building / flamable structure?",
					"identifier":"flamable_barrier",
					"input_type":"bool",
					'display_reliance':{'identifier':'proximity_flamables','display_value':['1']},
				},
			],
		},
		{
			"section_name":"Tank Condition",
			"section_identifier":"tank_proximities",
			"main_questions":[
				{
					"question_title": "Has the exteriour of the {lft} been thoroughly inspected and confirmed to be free of any material defect within the last 3 months?",
					"identifier":"inspected", 
					"input_type":"radio",
					'radio_options':[
						{'radio_text':'Not inspected in the last 3 months', 'radio_value':'not_3month_inspected'},xs
						{'radio_text':'Occupier inspected', 'radio_value':'occupier_inspection'},
						{'radio_text':'Inspected by Professional ', 'radio_value':'pro-inspection'},
						{'radio_text':'Other', 'radio_value':'other'},
					]
				},
				{
					"question_title": "Hads a fire-proof barrier been installed between the {ltf} and the identified building / flamable structure?",
					"identifier":"flamable_barrier",
					"input_type":"bool",
					'display_reliance':{'identifier':'proximity_flamables','display_value':['1']},
				},
			],	
		},
	],
}
	