template={
	"Form" : "Basements Residential", 
	'form_identifier':'basements_residential',
	"Sections" : [
			{
				"section_name":'Personal Details',
				'section_identifier':'surveyor_personal_details',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						"question_title":'Provide the following personal details for the Contractor / surveyor providing preliminary information', 
						"identifier":"data_providers", 
						'multi_row_guidance':'for each person who enters data fill this section out separately',
						"input_type":"multi_row",
						"sub_questions":[
							full_name({	
								'ident_prefix':'data_provider'
								"question_title":'',
								'identifier':'data_provider_name',
							}),
							contacts({	
								'ident_prefix':'data_provider'
								"question_title":'',
								'identifier':'data_provider_contacts',
							}),

						],
					},
				],
			},

			{
				"section_name":'Client Details',
				'section_identifier':'client_details',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
			
						"question_title":'Provide the following personal details of individual providing preliminary information', 
						"identifier":"data_providers", 
						'multi_row_guidance':'or each person who enters data fill this section out separately',
						"input_type":"multi_row",
						"sub_questions":[
									{
										
										"question_title":'First Name',
										"input_type":"text", 
										'identifier':'data_provider_first_name',
										'required':'true'
									},
									{
										"question_title":'Middle Name(s)',
										"input_type":"text", 
										'identifier':'data_provider_middle_name'
									},
									{
										"question_title":'surname', "sub_q_other_text":'',
										"input_type":"text", 'identifier':'data_provider_surname', 'required':'true'
									},
									{
										"question_title":'Provide details of the capacity in which you are providing preliminary information for the sale', "sub_q_other_text":'',
										"input_type":"radio", 
										'identifier':'data_provider_type',
										'required':'true', 
										'table_title':'Data Provider Type',
										'radio_options':[
											{'radio_text':'Seller','radio_value':'seller'},
											{'radio_text':'Seller’s personal representative','radio_value':'seller_rep'},
											{'radio_text':'Other','radio_value':'Other'},
										],
										"sub_questions":[
													{
														"question_title":'Specify your relationship to the property being sold, below.  For example;  seller’s family member, seller’s friend, estate agent, mortgagee in possession.',
														 "sub_q_other_text":'','table_title':'Data Provider Details',
														'identifier':"data_provider_type_details", "input_type":"detail_text", 
														'display_reliance':[{'identifier':'parent', 'value':['Other']}],
													},
												],
									},																																		
						],
					},
				],			
			},	


			{
				"section_name":'Basic Property Details',
				'section_identifier':'basic_data',


				#'question_set_data':{'set_numbering':"3.2"},

				"main_questions":[

					{
						"question_title":'Enter the full address', 
						"sub_q_other_text":'', 'question_set':'true',
						"identifier":"property_address", 
						'sub_questions':[

								{
									"question_title":'Postcode', 
									"sub_q_other_text":'',
									"identifier":"postcode", 
									"input_type":"postcode",
								},
								{
									"question_title":'Address Line 1', 
									"sub_q_other_text":'',
									"identifier":"address_line_1", 
									"input_type":"text",
								},
								{
									"question_title":'Address Line 2', 
									"sub_q_other_text":'', 
									"identifier":"address_line_2", 
									"input_type":"text",
								},															
								{
									"question_title":'Town or City', 
									"sub_q_other_text":'',
									"identifier":"address_town_or_city", 
									"input_type":"text",
								},
								{
									"question_title":'UPRN', 
									"sub_q_other_text":'',
									"identifier":"UPRN", 
									"input_type":"text",
								},
							],
						},
					],
				},




# ACCESS
			{

				"section_name":'Access',
				'section_identifier':'basic_data',
				"ident_prefix":"access_",
				"main_questions":[


							{
								"question_title":"Can the basement be accessed from another floor within the property?",
								"label":"Basement access from another floor within property",
								"input_type":"bool",
								'question_set':'true',
								"identifier":"basement_access_from_other_floor_within_property",
							}
							{
								"question_title":"How is the basement accessed from the exteriour of the property?",
								"label":"Access",
								'question_set':'true',
								"identifier":"method",
								'ident_prefix':'method_',
								'display_reliance':[{'identifier':'basement_access', 'bool':['1']}],

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
				],
			},



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
