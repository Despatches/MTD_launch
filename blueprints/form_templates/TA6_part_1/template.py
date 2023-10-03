try:
	from launch.blueprints.form_templates import template_objects as t_ob
except:
	import sys
	sys.path.insert(0,'/Users/another/Documents/mtd/Refined_project_development/launch/blueprints/form_templates')
	import template_objects as t_ob


template={
	"Form" : "TA6 Part 1", 'form_identifier':'TA6_Part_1',"Sections" : [
			{
				"section_name":'Personal Details',
				'section_identifier':'personal_details',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						"question_title":'Provide the following personal details of individual providing preliminary information', 
						"identifier":"data_providers", 
						'multi_row_guidance':'for each person who enters data fill this section out separately',
						"input_type":"multi_row",
						"sub_questions":[
									t_ob.full_name({	
										'ident_prefix':'data_provider_',
										"question_title":'',
										'identifier':'data_provider_name',
									}),
									{
										"question_numbering":"1.3" ,"question_title":'Please provide details of the capacity in which you are providing preliminary information for the sale', "sub_q_other_text":'',
										"input_type":"radio", 'identifier':'data_provider_type',
										'required':'true', 'table_title':'Data Provider Type',
										'radio_options':[
											{'radio_text':'Seller','radio_value':'seller'},
											{'radio_text':'Seller’s personal representative','radio_value':'seller_rep'},
											{'radio_text':'Other','radio_value':'Other'},
										],"sub_questions":[
													{
														"question_numbering":"" ,"question_title":'please specify your relationship to the property being sold, below:For example, seller’s family member, seller’s friend, estate agent, mortgagee in possession.',
														 "sub_q_other_text":'','table_title':'Data Provider Details',
														'identifier':"data_provider_type_details", "input_type":"detail_text", 
														'display_reliance':[{'identifier':'parent', 'value':['Other']}]
													}
												]
									}																																		
						]
					}
				]			
			},	
			{
				"section_name":'Basic Property Details',
				'section_identifier':'basic_data',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
						t_ob.address_set({
							"question_title":'Enter the full address',
							'identifier':'disclosed_prop_address',
							'ident_prefix':'disclose_' 
						})
				]			
			},
			{
				"section_name":'Ownership',
				'section_identifier':'ownership',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					
							{
								"question_numbering":"3.1" ,
								"question_title":'Is your property freehold or leasehold?',
								"identifier":"lease_or_free", "input_type":"radio",
								'radio_options':[
										{'radio_text':'Leasehold','radio_value':'Leasehold'},
										{'radio_text':'Freehold','radio_value':'Freehold'}
									],
							},
							{
								'question_set':'true',
								"question_numbering":"3.2" ,
								"question_title":'Ground rent',
								'identifier':'ground_rent', 
								'display_reliance':[{'identifier':'lease_or_free', 'value':['Leasehold']}],
								"mandatory_guidance":[
									'You will need a copy of your lease in order to answer these questions', 
									'If you do not have a copy of your lease, ask your solicitor for help',
									'Estate agents need to be able to share the following information with the buyer'
								],						 
								"sub_q_other_text":'',
								"sub_questions":[
									{
										"question_numbering":"3.2.1" ,
										"question_title":'How many years will be left on the lease at the end of the year',
										"input_type":"number", 
										'identifier':'years_left',
										'guidance':{'text':['here is some guidance', 'here is some guidance', 'here is some guidance', 'here is some guidance', 'here is some guidance', 'here is some guidance', 'here is some guidance']}
									},								
									{
										"question_numbering":"3.2.1" ,"question_title":'How much ground rent do you pay each year? £ . year', "sub_q_other_text":'',
										"input_type":"currency", 'identifier':'rent_value', 'guidance':{'text':['here is some guidance']}
									},
									{
										"question_numbering":"3.2.2",
										"question_title":'Does your lease say when the rent is likely to be increased?', "sub_q_other_text":'',
										"input_type":"bool", 
										'identifier':'ground_rent_increase_bool'
									},
									{
										'identifier':'ground_rent_increase','question_set':'true',"question_numbering":"3.2.3", 
										"question_title":'please give details of the next increase (date, frequency, amount) - if you don’t have your lease then your solicitor will be able to obtain a copy.', 
										"sub_q_other_text":'',
										"sub_questions":[
											{
												"question_numbering":"3.2.3.1" ,"question_title":'Date of next increase', "sub_q_other_text":'',
												"input_type":"date", 'identifier':'ground_rent_increase_date'
											},
											{
												"question_numbering":"3.2.3.2" ,"question_title":'Frequency of increase:', "sub_q_other_text":'',
												'identifier':"ground_rent_increase_frequency",
												 "input_type":"text", 
												 'styling':{"stock_options":{'options':['annually','bi-annually','quarterly','every 5 years','every 10 years']}}
											},
											{
												"question_numbering":"3.2.3.3",
												"question_title":'Are the rent increases fixed, or variable?',
												"input_type":"radio", 
												'identifier':'rent_increase_type', 
												'radio_options':[
													{'radio_text':'fixed','radio_value':'Fixed'},
													{'radio_text':'variable','radio_value':'Variable'},
													{'radio_text':'other','radio_value':'Other'}

												],
												"sub_questions":[
													{
														"question_numbering":"" ,
														"question_title":'Frequency of increase:', 
														'identifier':"rent_increase_type_details", 
														"input_type":"detail_text", 
														'display_reliance':[{'identifier':'rent_increase_type', 'value':['Other']}]
													}
												]
											},																																									
										], 
										'display_reliance':[{'identifier':'ground_rent_increase_bool', 'value':['1']}]
									}									
						
								], 
							}
					]
			},
			{
				'section_name':'Service Charges',
				'section_identifier':'service_charges',
				'display_reliance':[{'identifier':'lease_or_free', 'value':['Leasehold']}],
				'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					
							{
								"question_numbering":"3.1" ,
								"question_title":'Have you paid service charges?', 
								"sub_q_other_text":'',
								"identifier":"service_charge_bool", 
								"input_type":"bool",
							},
							{
								'question_set':'true',
								'identifier':'service_charge_data' , 
								"sub_q_other_text":'',
								'display_reliance':[{'identifier':'service_charge_bool', 'value':['1']}],
								"sub_questions":[
									{
										"question_numbering":"3.2.1" ,"question_title":'How much was the service charge last year (between 1 January and 31 December in £)?', "sub_q_other_text":'',
										"input_type":"currency", 'identifier':'last_service_charge', 'guidance':{'text':['here is some guidance']}
									},
									{
										"question_numbering":"3.2.2" ,"question_title":'Is there a budget or known amount for the service charge this year?', "sub_q_other_text":'',
										"input_type":"bool", 'identifier':'service_charge_budget_bool',
										"sub_questions":[
											{
												"question_numbering":"3.2.2" ,"question_title":'upload any relevant documents, such as a service charge bill', "sub_q_other_text":'',
												"input_type":"docu", 'identifier':'service_charge_bill_docu',
												'display_reliance':[{'identifier':'parent', 'value':['1']}]
											},
										]
									},
									{
										"question_numbering":"3.2.1" ,"question_title":'When are the payments due?', "sub_q_other_text":'',
										"input_type":"date", 'identifier':'service_charge_payments_due', 'guidance':{'text':['here is some guidance']}
									},
									{
										"question_numbering":"3.2.1" ,"question_title":'Who are payments made to?', "sub_q_other_text":'',
										"input_type":"radio", 'identifier':'service_charge_pay_reciever', 'guidance':{'text':['here is some guidance']},
										'radio_options':[
												{'radio_text':'Managing agent(s)', 'radio_value':'agent'},
												{'radio_text':'Landlord(s)', 'radio_value':'landlord'},
												{'radio_text':'Freehold company', 'radio_value':'freehold_company'},
												{'radio_text':'Resident’s Association', 'radio_value':'resi_assoc'}
											]
									},
									{
										'question_set':'true',
										"question_numbering":"3.2",
										"question_title":'Please provide details of the payment receiver',
										'identifier':'service_charge_pay_reciever_data' , "sub_q_other_text":'',
										'display_reliance':[{'identifier':'service_charge_pay_reciever', 
										'value':['agent','freehold_company','resi_assoc']}],
										"sub_questions":
											[
												{
													"question_numbering":"1" ,"question_title":'Name of organisation', 
													"sub_q_other_text":'',
													"identifier":"service_charge_organisation", 
													"input_type":"text"
												},
												{
													"question_numbering":"1" ,"question_title":'Building name', 
													"sub_q_other_text":'',
													"identifier":"service_charge_Building_name", 
													"input_type":"text"
												},
												{
													"question_numbering":"1" ,"question_title":'Building.street no', 
													"sub_q_other_text":'',
													"identifier":"service_charge_street_no", 
													"input_type":"text"
												},
												{
													"question_numbering":"1" ,"question_title":'Street Name', 
													"sub_q_other_text":'',
													"identifier":"service_charge_street_name", 
													"input_type":"text"
												},
												{
													"question_numbering":"1" ,"question_title":'Town.City', 
													"sub_q_other_text":'',
													"identifier":"service_charge_town_or_city", 
													"input_type":"text"
												},
												{
													"question_numbering":"1" ,"question_title":'Postcode', 
													"sub_q_other_text":'',
													"identifier":"service_charge_postcode", 
													"input_type":"text"
												},																																																																			
											]
									}																									
								]
							}
					]
			},
			{
				"section_name":'New Builds and Conversions',
				'section_identifier':'new_builds_and_conversions',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						"question_numbering":"3.1" ,"question_title":'Were you the first person to occupy the property after it was built or converted?', 
						"sub_q_other_text":'',"identifier":"first_to_occupy", "input_type":"bool",
					},
					{
						"question_numbering":"3.1" ,
						"question_title":'When you bought the property, you may have been given the following: copies or details of the warranties and guarantees, and \
 							any planning consents or other planning documents. If available, upload or scan copies or details.', 
						"sub_q_other_text":'',
						"identifier":"warranties_docu", 
						"input_type":"docu",
					},					
				]
			},
			{
				"section_name":'Timing',
				'section_identifier':'timing',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						"question_numbering":"3.1" ,"question_title":'Does the proposed sale depend on you buying another property?', 
						"sub_q_other_text":'',"identifier":'property_dependant', "input_type":"bool",
						'sub_questions':[
							{
								"question_title":'Provide any details, such as where you are in that transaction, whether there have been any delays, and the date you expect completion to take place?',
								"identifier":"property_dependant_details","input_type":"detail_text",
								'display_reliance':[{'identifier':'property_dependant','value':['1']}]
							}
						]
					},
					{
						"question_numbering":"3.1" ,'question_title':'Are there other factors that might affect the timing of your move?', 
						"sub_q_other_text":['You can select multiple factors and should add any relevant dates, if known.'],
						"identifier":"move_factors",
						'question_set':'true','sub_questions':[
							{
								'identifier':'school_term',
								'question_title':'',
								'label':'End of school term',
								'input_type' : 'checkbox',
								'sub_questions':[
									{
										'identifier':'school_term_date',
										'question_title':'',
										'input_type' : 'date',
										'display_reliance':[{'identifier':'school_term','value':['checked']}]
									}
								]
							},
							{
								'identifier':'upcoming_holiday',
								'question_title':'',
								'label':'Upcoming holiday',
								'input_type' : 'checkbox',
								'sub_questions':[
									{
										'identifier':'upcoming_holiday_date',
										'question_title':'',
										'input_type' : 'date',
										'display_reliance':[{'identifier':'upcoming_holiday','value':['checked']}]
									}
								]
							},
							{
								'identifier':'job_move',
								'question_title':'',
								'label':'Job move',
								'input_type' : 'checkbox',
								'sub_questions':[
									{
										'identifier':'job_move_date',
										'question_title':'',
										'input_type' : 'date',
										'display_reliance':[{'identifier':'job_move','value':['checked']}]
									}
								]
							},
							{
								'identifier':'redundancy',
								'question_title':'',
								'label':'Redundancy',
								'input_type' : 'checkbox',
								'sub_questions':[
									{
										'identifier':'redundancy_date',
										'question_title':'',
										'input_type' : 'date',
										'display_reliance':[{'identifier':'redundancy','value':['checked']}]
									}
								]
							},
							{
								'identifier':'medical',
								'question_title':'',
								'label':'Medical (including pregnancy)',
								'input_type' : 'checkbox',
								'sub_questions':[
									{
										'identifier':'medical_date',
										'question_title':'',
										'input_type' : 'date',
										'display_reliance':[{'identifier':'medical','value':['checked']}]
									}
								]
							},
							{
								'identifier':'notice_to_tenant',
								'question_title':'',
								'label':'Giving notice to tenant in occupation',
								'input_type' : 'checkbox',
								'sub_questions':[
									{
										'identifier':'notice_to_tenant_date',
										'question_title':'',
										'input_type' : 'date',
										'display_reliance':[{'identifier':'notice_to_tenant','value':['checked']}]
									}
								]
							},
							{
								'identifier':'retirement',
								'question_title':'',
								'label':'Retirement',
								'input_type' : 'checkbox',
								'sub_questions':[
									{
										'identifier':'retirement_date',
										'question_title':'',
										'input_type' : 'date',
										'display_reliance':[{'identifier':'retirement','value':['checked']}]
									}
								]
							},
							{
								'identifier':'build_complete',
								'question_title':'',
								'label':'Proposed completion date, if property is a new build',
								'input_type' : 'checkbox',
								'sub_questions':[
									{
										'identifier':'build_complete_date',
										'question_title':'',
										'input_type' : 'date',
										'display_reliance':[{'identifier':'build_complete','value':['checked']}]
									}
								]
							},
							{
								'identifier':'other_move_factor',
								'question_title':'',
								'label':'Other',
								'input_type' : 'checkbox',
								'sub_questions':[
									{
										'identifier':'other_move_factor_date',
										'question_title':'',
										'input_type' : 'date',
										'display_reliance':[{'identifier':'other_move_factor','value':['checked']}]
									},
									{
										'identifier':'other_move_factor_details',
										'question_title':'please give details of this other factor.',
										'input_type' : 'detail_text',
										'display_reliance':[{'identifier':'other_move_factor','value':['checked']}]
									}									
								]
							},																																																							
						]
					},					
				]
			},
			{
				"section_name":'Property alterations and building work',
				'section_identifier':'property_alteration',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						"question_numbering":"" 
						,"question_title":'Have any of the following changes been made to the property or any part of it (including the garden), during your ownership?',
						'other_question_text':[
							'-Part of the property is has not been used for residential occupation eg commercial use',

							'-Installation of replacement windows, roof windows, roof lights, glazed doors since 1 April 2002',

							'-Garage conversion',

							'-Adding an extension',

							'-Adding a conservatory',

							'-Loft conversion',

							'-Removal of internal walls',
							'-Other building works or changes to the property',
						],
						"identifier":'works_and_alterations',
						 "input_type":"multi_row",
						 'object_type':'Property Alteration',
						'sub_questions':[
							{
								'question_title':'',
								'input_type':'radio',
								'identifier':'building_works_and_alterations',
								'table_title':'Alteration or Work',
								'styling' : 'block',
								'radio_options':[
									{'radio_text':'Part of the property is not used for residential occupation eg commercial use',
										'radio_value':'resi'
									},
									{'radio_text':'Installing replacement windows, roof windows, roof lights, glazed doors since 1 April 2002',
										'radio_value':'replace_element'
									},
									{
										'radio_value':'garage_conversion',
										'radio_text':'Garage conversion'
									},
									{
										'radio_value':'extension',
										'radio_text': 'Adding an extension'
									},
									{
										'radio_value':'conservatory',
										'radio_text': 'Adding a conservatory'
									},
									{
										'radio_value':'loft_conversion',
										'radio_text': 'Loft conversion'
									},
									{
										'radio_value':'wall_remove',
										'radio_text': 'Removal of internal walls'
									},
									{
										'radio_value':'other_change',
										'radio_text': 'Other building works or changes to the property'
									},																																										
								]
							},
							{
								'question_title':'Give details of the work carried out',
								'input_type':'detail_text',
								'identifier':'property_alterations_work_details'
							},
							{
								'question_title':'Give an indictation of the period the work occured in',
								'question_set':'true',
								'identifier':'work_period',
								'sub_questions':[
									{
										'question_title':'Work start',
										'identifier':'alterations_work_start',
										'input_type':'date'
									},
									{
										'question_title':'Work End',
										'identifier':'alterations_work_end',
										'input_type':'date'
									},
								]
							},	
							{
								'question_title':'Is this work completed',
								'input_type':'bool',
								'identifier':'property_works_completed_bool',
								'sub_questions':[
									{
										'question_title':'Give details regarding completion of the works',
										'identifier':'completion_of_work_details',
										'input_type':'detail_text'
									}
								]
							}						
						]
					}
				]
			},
			{
				"section_name":'Potential liabilities',
				'section_identifier':'liabilities',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						'question_title':'Are you aware of any of the following?',
						'question_set':'true',
						'identifier':'liabilities_set',
						'sub_questions':[
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Breaches of planning permission conditions',
								'identifier':'planning_breach',
								'sub_questions':[
								{
									'question_title':'Describe the breaches of planning permission conditions',
									'input_type':'detail_text',
									'identifier':'planning_breach_details',
									'display_reliance':[{'identifier':'planning_breach','value':['checked']}]
								}
								]
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Breaches of building regulations consent conditions',
								'identifier':'bulding_reg_breach',
								'sub_questions':[
								{
									'question_title':'Describe the breaches of building regulations consent conditions',
									'input_type':'detail_text',
									'identifier':'bulding_reg_breach_details',
									'display_reliance':[{'identifier':'bulding_reg_breach','value':['checked']}]
								}]
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Unfinished work',
								'identifier':'unfinished_work',
								'sub_questions':[
								{
									'question_title':'Describe the unfinished work',
									'input_type':'detail_text',
									'identifier':'unfinished_work_details',
									'display_reliance':[{'identifier':'unfinished_work','value':['checked']}]
								}]
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Work that does not have all necessary consents',
								'identifier':'consent_lack',
								'sub_questions':[
								{
									'question_title':'Describe works that do not have all necessary consents',
									'input_type':'detail_text',
									'identifier':'consent_lack_details',
									'display_reliance':[{'identifier':'consent_lack','value':['checked']}]
								}]
							},																					
						]
					},
				]
			},
			{
				"section_name":'Solar Panels',
				'section_identifier':'solar_panels',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						'question_title':'Have solar panels been installed at the property?',
						'input_type':'bool',
						'identifier':'solar_panels_bool'
					},
					{
						'question_set':'true',
						'identifier':'solar_panels_data',
						'display_reliance':[{'identifier':'solar_panels_bool','value':['1']}],
						'sub_questions':[
							{
								'question_title':'Which year were the solar panels installed',
								'identifier':'solar_installation_year',
								'input_type':'number',
								'input_params':[{'min':'1950'},{'max':'{{current_year}}'}]
							},
							{
								'question_title':'Do you own the solar panels outright?',
								'identifier':'solar_panels_ownership_bool',
								'input_type':'bool'
							},
							{
								'question_title':'Has a long lease of the roof . air space been granted to a solar panel provider?',
								'identifier':'solar_panels_long_lease_ownership_bool',
								'input_type':'bool',
								'other_question_text':['(A typical long lease may last 20 to 25 years.)'],
								'display_reliance':[{'identifier':'solar_panels_ownership_bool','value':['0']}]
							},
							{
								'question_title':'you’ll need to supply copies of the relevant documents, such as copies of electricity bills for feed-in tariffs (payments made for supplying electricity to the main grid).',
								'input_type':'docu',
								'identifier':'solar_electrical_tarrif_docu'
							}							
						]
					}
				]
			},
			{
				"section_name":'Protected buildings',
				'section_identifier':'protected_buildings',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						'question_title':'Is the property (or any part of it) listed in the National Heritage List for England?',
						'input_type':'bool_extra',
						'identifier':'protected_buildings_bool',
						'radio_options':[{'radio_text':'Don’t know', 'radio_value':'not_known'}],
						'sub_questions':[
							{
								'question_title':'you’ll need to supply a copy of any relevant documents eg notice of listing, letter from local authority confirming listing',
								'input_type' : 'docu',
								'identifier':'protected_buildings_docu',
								'display_reliance':[{'identifier':'protected_buildings_bool','value':['1']}]
							}
						]
					},
					{
						'question_title':'Is the property (or any part of it) in a conservation area?',
						'input_type':'bool_extra',
						'identifier':'conservation_area_bool',
						'radio_options':[{'radio_text':'Don’t know','radio_value':'not_known'}],
						'sub_questions':[
						{
							'question_title':'you’ll need to supply a copy of any relevant documents',
							'input_type':'docu',
							'identifier':'conservation_area_docu',
							'display_reliance':[{'identifier':'conservation_area_bool','value':['1']}]
						}
						]
					}
				]	
			},
			{
				"section_name":'Protected trees',
				'section_identifier':'protected_trees',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						'question_title':'Are any trees on your property subject to a Tree Preservation Order?',
						'input_type':'bool_extra',
						'identifier':'TPO_bool',
						'radio_options':[{'radio_text':'Don’t know', 'radio_value':'not_known'}],
						'sub_questions':[
							{
								'question_title':'Have the terms of the order been complied with?',
								'input_type' : 'bool_extra',
								'identifier':'order_terms_complied_with',
								'display_reliance':[{'identifier':'TPO_bool','value':['1']}],
								'radio_options':[{'radio_text':'Don’t know', 'radio_value':'not_known'}],
							},						
							{
								'question_title':' Supply a copy of any relevant documents',
								'input_type' : 'docu',
								'identifier':'TPO_docu',
								'display_reliance':[{'identifier':'TPO_bool','value':['1']}]
							}
						]
					},
				]	
			},
			{
				"section_name":'Consent',
				'section_identifier':'consent',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						'question_title':'Do you have consent for any matters that need permission?',
						'input_type':'bool_extra',
						'radio_options':[{'radio_text':'Don’t know', 'radio_value':'not_known'}],
						'identifier':'all_required_consents',
						'other_question_text':['Check with your solicitor that all necessary consents have been received.','If you are not sure if permission is needed, ask your solicitor as soon as it is practical.'],
						'sub_questions':[
							{
								'question_title':'Give details.',
								'identifier':'all_required_consents_details',
								'input_type':'detail_text',
								'display_reliance':[{'identifier':'all_required_consents', 'value':['1']}]
							}
						]
					}
				]				
			},
			{
				'section_name':'Charges',
				'section_identifier':'charges',
				"main_questions":
				[
					{
						'question_title':'Do you have to pay any charges relating to the property (apart from council tax, utility charges, and so on)?',
						'input_type':'bool',
						'identifier':'charges_bool',
						'sub_questions':
						[	
							{
								'question_title':'Give details.',
								'other_question_text':
								[
									'For example, if your property is freehold, charges might include payments to a management company or residents’ association, or for a private drainage system.',
									'If your property is leasehold, you’ll need to give details of lease expenses (such as service charges and ground rent). Your solicitor will provide you with a TA7 once the preliminary information is completed.'
								],
								'input_type':'detail_text',
								'display_reliance':[{'identifier':'charges_bool','value':['1']}],
								'identifier':'charges_details'
							}
						]
					}
				]
			},
			{
				'section_name':'Access roads and footpaths',
				'section_identifier':'access_roads',
				"main_questions":
				[
					{
						'question_title':'Do you have to pay anything towards the costs of maintaining roads, footpaths or other facilities?',
						'input_type':'bool_extra',
						'radio_options':[{'radio_text':'Not Sure', 'radio_value':'not_known'}],
						'identifier':'maintain_road_bool',
						'sub_questions':
						[
							{
								'question_title':'please give details of any payments (how much, and who payments are made to).',
								'input_type':'detail_text',
								'identifier':'maintain_road_payement_details',
								'display_reliance':[{'identifier':'maintain_road_bool','value':'1'}],
							}
						]
					},
					{
						'question_title':'Is your house on a private road or is the road that gives access to or adjoins the property a private road?',
						'input_type':'bool_extra',
						'radio_options':[{'radio_text':'Not Sure', 'radio_value':'not_known'}],
						'identifier':'private_road'
					},
					{
						'question_title':'Are the roads leading to your property maintained at public expense?',
						'input_type':'bool_extra',
						'radio_options':[{'radio_text':'Not Sure', 'radio_value':'not_known'}],
						'identifier':'public_expense_road'
					},					
				]
			},
			{
				'section_name':'Services',
				'section_identifier':'services',
				"main_questions":
				[
					{
						'question_title':'Which of the following services are connected to the property?',
						'question_set':'true',
						'identifier':'connected_services',
						'sub_questions':
						[
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Mains drainage',
								'identifier':'mains_drainage'
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Electricity',
								'identifier':'electricity'
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Water Supply',
								'identifier':'water_supply'
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Gas',
								'identifier':'gas'
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Broadband',
								'identifier':'broadband'
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Private Sewage Plant',
								'identifier':'sewage_plant'
							},	
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Telephone Landlines',
								'identifier':'telephone_landlines'
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Solar Panels',
								'identifier':'solar_panels'
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Ground and air heat pumps',
								'identifier':'heat_pumps'
							},
							{
								'question_title':'',
								'input_type':'checkbox',
								'label':'Other',
								'identifier':'other_provisioned_services',
								'sub_questions':
								[
									{
										'question_title':'please give details',
										'identifier':'other_provisioned_services_details',
										'input_type':'detail_text',
										'display_reliance':[{'identifier':'other_provisioned_services','value':['checked']}]
									}
								]
							},																																								
						]
					}
				]
			},
			{
				'section_name':'Shared facilities',
				'section_identifier':'shared_facilities',
				"main_questions":
				[
					{
						'question_title':'Are there any areas or facilities shared with neighbours (excluding common parts of a leasehold block or estate)?',
						'input_type':'bool',
						'identifier':'shared_facilities_bool',
						'sub_questions':
						[
							{
								'input_type':'detail_text',
								'identifier':'shared_facilities_text_details',
								'question_title':'give details.',
								'display_reliance':[{'identifier':'parent','value':['1']}]
							}
						]
					}	
				]
			},
			{
				'section_name':'Parking',
				'section_identifier':'parking',
				"main_questions":
				[
					{
						'question_title':'What are the parking arrangements at the property?',
						'input_type':'detail_text',
						'other_question_text':['For example, is there a garage, allocated space, permit, roadway or driveway?'],
						'identifier':'parking_arrangement_details'
					},
					{
						'question_title':'Is the property in a controlled parking zone or within a local authority parking scheme?',
						'input_type':'bool_extra',
						'identifier':'controlled_parking',
						'radio_options':[{'radio_text':'Not Sure', 'radio_value':'not_known'}],
					}					
				]
			},
			{
				'section_name':'Occupiers',
				'section_identifier':'occupiers',
				"main_questions":
				[
					{
						'question_title':'Do you live at the property?',
						'input_type':'bool',
						'identifier':'live_at_prop_bool'
					},
					{
						'question_title':'Does anyone else, aged 17 or over, live at the property?',
						'input_type':'bool',
						'identifier':'over_17_bool'
					},
					{
						'question_title':'Supply full names of any occupiers (other than yourself) aged 17 or over:',
						'input_type':'multi_row',
						'identifier':'over_17',
						'display_reliance':[{'identifier':'over_17_bool','value':['1']}],
						'sub_questions':
						[
							{
								'question_title':'First Name',
								'input_type':'text',
								'identifier':'first_name_17'
							},
							{
								'question_title':'Middle Names',
								'input_type':'text',
								'identifier':'middle_name_17'
							},
							{
								'question_title':'Surname',
								'input_type':'text',
								'identifier':'surname_17'
							},													
						]
					},
					{
						'question_title':'Are any of the occupiers who are aged 17 or over (other than yourself), tenants or lodgers?',
						'input_type':'bool',
						'identifier':'lodgers_bool',
						'display_reliance':[{'identifier':'over_17_bool','value':['1']}],
					},
					{
						'question_title':'Have all the occupiers aged 17 or over agreed to leave before completion?',
						'input_type':'bool',
						'identifier':'agree_to_leave_bool',
						'display_reliance':[{'identifier':'over_17_bool','value':['1']}],
					},
					{
						'question_title':'Have all the occupiers aged 17 or over agreed to sign the sale contract?',
						'input_type':'bool',
						'identifier':'occupiers_contract_sign_bool',
						'display_reliance':[{'identifier':'over_17_bool','value':['1']}],
					},										
					{
						'question_title':'Is the property being sold with vacant possession',
						'input_type':'bool',
						'other_question_text':['When buying or selling a property, “vacant possession” means that the property is empty and emptied of anything not contracted to remain on the day of completion eg chattels, rubbish.'],
						'identifier':'vacant_possession_bool',
						'sub_questions':
						[
							{
								'question_title':'If the property is not being sold with vacant possession, you’ll need to supply evidence that the property will be empty on the day of completion.',
								'input_type':'docu',
								'identifier':'vacant_possession_proof_docu',
								'display_reliance':[{'identifier':'vacant_possession_bool','value':['0']}],

							}
						]
					}															
				]
			},
			{
				'section_name':'Flooding',
				'section_identifier':'flooding',
				'section_text':['Flooding may take a variety of forms: it may be seasonal, irregular or simply a one-off event. Your property does not need to be near the sea or to a river for flooding to happen.','Find out more about the types of flooding and flood risk reports',"Check if you're at risk of flooding in England"],
				"main_questions":[
					{
						'api':['flood_risk'],
						'question_title':'Has any part of the property (buildings, surrounding garden or land) ever been flooded?',
						'input_type':'bool',
						'identifier':'flooding_bool'
					},				
					{
						'question_title':'give an overview of each flood event that has occured that you are aware of',
						'input_type':'multi_row',
						'identifier':'flood_events',
						'object_type':'Flood Event',
						'display_reliance':[{'identifier':'flooding_bool','value':['1']}],
						'sub_questions':[
							{
								'identifier':'flood_type',
								'question_title':'What type of flooding took place?',
								'input_type':'radio',
								'radio_options':[
									{'radio_text':'Ground water','radio_value':'Ground water'},
									{'radio_text':'Sewer flooding','radio_value':'Sewer flooding'},
									{'radio_text':'Surface water','radio_value':'Surface water'},
									{'radio_text':'Coastal flooding','radio_value':'Coastal flooding'},
									{'radio_text':'River flooding','radio_value':'River flooding'},
									{'radio_text':'Other','radio_value':'Other'}
								],
								'styling':'dropdown',
								'sub_questions':[
									{
										'question_title':'for other give details',
										'identifier':'other_flood_type_description',
										'input_type':'detail_text',
										'display_reliance':[{'identifier':'parent', 'value':['Other']}]
									}
								]
							},
							{
								'question_title':'When did the flooding take place?',
								'input_type':'date',
								'identifier':'flood_event_date'	
							},
							{
								'question_title':'Which parts flooded?',
								'input_type':'detail_text',
								'identifier':'flood_area_details'	
							}							
						]
					},
					{
						'identifier':'flood_yes_other',
						'question_set':'true',
						'display_reliance':[{'identifier':'flooding_bool','value':['1']}],
						'sub_questions':[
							{
								'question_title':'Has a flood risk report been created for the property?',
								'input_type':'bool',
								'identifier':'flood_risk_report_bool',
								'sub_questions':
								[
									{
										'question_title':'you’ll need to supply a copy of the flood risk report.',
										'identifier':'flood_risk_report_docu',
										'input_type':'docu',
										'display_reliance':[{'identifier':'flood_risk_report_bool','value':['1']}]
									}
								]
							}
						]
					}
				]
			},
			{
				'section_name':'Right to use and enjoy your property',
				'section_identifier':'right_to_enjoy',
				"main_questions":[
					{
						'question_title':'Have you been told about plans for any building or developments that might affect someone’s ability to peacefully use and enjoy the property?',
						'identifier':'nearby_development_bool',
						'input_type':'bool',
						'sub_questions':[
							{
								'question_title':'give details eg what the plans are and when they are expected to take place.',
								'identifier':'nearby_development',
								'input_type':'detail_text',
								'display_reliance':[{'identifier':'nearby_development_bool','value':['1']}]
							}
						]
					}
				]

			},
			{
				'section_name':'Disputes and complaints',
				'section_identifier':'disputes',
				"main_questions":[
					{
						'question_title':'Have there been any disputes or complaints about your property or a property nearby?',
						'identifier':'complaints_bool',
						'input_type':'bool',
						'sub_questions':[
							{
								'question_title':'give details such as when this took place and who was involved.',
								'identifier':'complaints_details',
								'input_type':'detail_text',
								'display_reliance':[{'identifier':'complaints_bool','value':['1']}]
							}
						]
					},
					{
						'question_title':'Are you aware of anything that might lead to a dispute about your property or a property nearby?',
						'identifier':'disputes_bool',
						'input_type':'bool',
						'sub_questions':[
							{
								'question_title':'give details',
								'identifier':'disputes_details',
								'input_type':'detail_text',
								'display_reliance':[{'identifier':'disputes_bool','value':['1']}]
							}
						]
					}					
				]

			},
			{
				'section_name':'Other information',
				'section_identifier':'other_info',
				"main_questions":[
					{
						'question_title':'Is the property affected by Japanese Knotweed?',
						'input_type':'bool',
						'identifier':'knotweed_bool',
						'sub_questions':[
							{
								'question_title':'give details',
								'identifier':'knotweed',
								'input_type':'detail_text',
								'display_reliance':[{'identifier':'knotweed_bool','value':['1']}]
							}
						]
					},
					{
						'question_title':'Is the property in a mining area?',
						'input_type':'bool',
						'identifier':'mining_bool',
						'sub_questions':[
							{
								'question_title':'give details',
								'identifier':'mining',
								'input_type':'detail_text',
								'display_reliance':[{'identifier':'mining_bool','value':['1']}]
							}
						]
					},
					{
						'question_title':'Has something happened in the property that a buyer would want to know about or might influence their decision to purchase?',
						'input_type':'bool',
						'identifier':'influence_decision_bool',
						'sub_questions':[
							{
								'question_title':'give details',
								'identifier':'influence_decision',
								'input_type':'detail_text',
								'display_reliance':[{'identifier':'influence_decision_bool','value':['1']}]
							}
						]
					},
					{
						'question_title':'Do any neighbours or members of the public have the right to enter your property?',
						'input_type':'bool',
						'identifier':'neighbours_access_bool',
						'sub_questions':[
							{
								'question_title':'give details',
								'identifier':'neighbours_access',
								'input_type':'detail_text',
								'display_reliance':[{'identifier':'neighbours_access_bool','value':['1']}]
							}
						]
					},
					{
						'question_title':'Is there anything else you think a buyer would want to know, or that might influence their decision to buy or that you remember about the property when you bought it?',
						'other_question_text':['For example, why are you moving?','If you are not sure if you should disclose information, ask your solicitor.'],
						'input_type':'bool',
						'identifier':'anything_else_bool',
						'sub_questions':[
							{
								'question_title':'give details',
								'identifier':'anything_else',
								'input_type':'detail_text',
								'display_reliance':[{'identifier':'anything_else_bool','value':['1']}]
							}
						]
					}									
				]
			}								
		]
	}