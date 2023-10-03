template={
	"Form" : "Basements", 
	'form_identifier':'basement',
	"Sections" : [
# ACCESS
			{

				"section_name":'Access',
				'section_identifier':'basic_data',
				"ident_prefix":"access_",
				"main_questions":[


							{
								"question_title":"Can the basement be accessed directly from the outside of the property?",
								"label":"Basement access from another floor within property",
								"input_type":"bool",
								'question_set':'true',
								"identifier":"exteriour_basement_access",
							}

							{
								"question_title":"How is the basement accessed from the exteriour of the property?",
								"label":"Access",
								'question_set':'true',
								"identifier":"method",
								'ident_prefix':'method_',
								'display_reliance':[{'identifier':'exteriour_basement_access', 'bool':['1']}],

								'radio_options':[
										{'checkbox':'stairs', 'radio_text':'Staircase'},
										{'checkbox':'ramp', 'radio_text':'Ramp'},
										{'checkbox':'hatch', 'radio_text':'Hatch'},
										{'checkbox':'elevator', 'radio_text':'Elevator'},
										{'checkbox':'escalator', 'radio_text':'Escallator'},
										{'checkbox':'garage','radio_text':'Garage'},

									],
								"other_question_text" : "Select all of the forms of access",
								"sub_questions":[
									{
										'input_type':'checkbox',
										'label':'Staircase',
										'identifier':'staircase'
									},
									{
										'input_type':'checkbox',
										'label':'Ramp',
										'identifier':'ramp'
									},
									{
										'input_type':'checkbox',
										'label':'Hatch',
										'identifier':'hatch'
									},
									{
										'input_type':'checkbox',
										'label':'Elevator',
										'identifier':'elevator'
									},	
									{
										'input_type':'checkbox',
										'label':'Escalator',
										'identifier':'escalator'
									},
									{
										'input_type':'checkbox',
										'label':'Garage',
										'identifier':'garage'
									},					
								],
							},
							{
								"question_title":"Can the basement be accessed from another floor within the property?",
								"label":"Basement access from another floor within property",
								"input_type":"bool",
								'question_set':'true',
								"identifier":"basement_access_within_property",
							}	
							{
								"question_title":"How is the basement accessed from the interiour of the property?",
								"label":"Access",
								'question_set':'true',
								"identifier":"method",
								'ident_prefix':'method_',
								'display_reliance':[{'identifier':'interiour_basement_access', 'bool':['1']}],

								'radio_options':[
										{'checkbox':'stairs', 'radio_text':'Staircase'},
										{'checkbox':'ramp', 'radio_text':'Ramp'},
										{'checkbox':'hatch', 'radio_text':'Hatch'},
										{'checkbox':'elevator', 'radio_text':'Elevator'},
										{'checkbox':'escalator', 'radio_text':'Escallator'},
										{'checkbox':'garage','radio_text':'Garage'},
										{'checkbox':'main hall','radio_text':'Main reception hall or entrance'},

									],
								"other_question_text" : "Select all of the forms of access",
								"sub_questions":[
									{
										'input_type':'checkbox',
										'label':'Staircase',
										'identifier':'staircase'
									},
									{
										'input_type':'checkbox',
										'label':'Ramp',
										'identifier':'ramp'
									},
									{
										'input_type':'checkbox',
										'label':'Elevator',
										'identifier':'elevator'
									},	
									{
										'input_type':'checkbox',
										'label':'Escalator',
										'identifier':'escalator'
									},
									{
										'input_type':'checkbox',
										'label':'Garage',
										'identifier':'garage'
									},		

				],
			},
							{
								"question_title":"Is the basement access and it's internal floor levels accessible and navigable by a wheelchair without further modification?",
								"label":"wheelchair_mobility_access",
								"input_type":"bool",
								'question_set':'true',
								"identifier":"basement_access_within_property",
							}	


			{
				"section_name":'Flood Risk and Protection',
				'section_identifier':'flood_risk_protection',


				"main_questions":[

					{
						"question_numbering":"1" ,"question_title":'Has the basement ever flooded?', 
						"sub_q_other_text":'', 'question_set':'true',
						"identifier":"basement_flooding", 
						'sub_questions':[
						
							{
								"question_numbering":"1" ,"question_title":'What was the source of the water that caused the flooding?', 
								"sub_q_other_text":'', 
								"identifier":"source_of_flood", 
								"input_type":"text",
							},

							{
								"question_numbering":"1" ,
								"question_title":"Is the basement situated below the mean level of any captive water body, reservoir or watercourse located within 500m of the property" , 
								"sub_q_other_text":'', 
								"identifier":"basement_level", 
								"input_type":"text",
							},

							{
								"question_numbering":"1" ,
								"question_title":"Is the basement curtiledge protected by a flood sump with an operational water pump to prevent flood water entering the basement?", 
								"sub_q_other_text":'', 
								"identifier":"basement_level", 
								"input_type":"text",
							},

							{
								"question_numbering":"1" ,
								"question_title":"Will the pump operate in the event of a mains power cut?",
								"sub_q_other_text":'', 
								"identifier":"basement_level", 
								"input_type":"text",
							},

							{
								"question_numbering":"1" ,
								"question_title":"Has a flood mitigation barrier been installed to prevent a minimum of 9' / 220mm of water depth breaching the basement wall or access?",
								"sub_q_other_text":'', 
								"identifier":"basement_level", 
								"input_type":"text",
							},

						],
					},	
				],

			},	# "endpoint_actor":"",

			{
				"section_name":'Flood Risk and Protection',
				'section_identifier':'flood_risk_protection',


				"main_questions":[

					{
						"question_numbering":"1" ,"question_title":'Has the basement ever flooded?', 
						"sub_q_other_text":'', 'question_set':'true',
						"identifier":"basement_flooding", 
						'sub_questions':[
						
							{
								"question_title":'What was the source of the water that caused the flooding?', 
								"sub_q_other_text":'', 
								"identifier":"source_of_flood", 
								"input_type":"text",
							},

							{

								"question_title":'Is the basement curtiledge now protected by a flood sump with an operational water pump to prevent flood water entering the basement?',
								"sub_q_other_text":'', 
								"identifier":"source_of_flood", 
								"input_type":"text",
							},
						],
					},
				],
			},
		],
	}
