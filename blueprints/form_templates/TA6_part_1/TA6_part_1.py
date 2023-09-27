
from launch.blueprints.form_templates.TA6_part_1.TA6_part_1_comp_risk_fraud import comp_risk_fraud as comp_risk_fraud
from launch.blueprints.form_templates.TA6_part_1.TA6_part_1_meanings import meanings as meanings
from launch.blueprints.form_templates.TA6_part_1.pro_tasks import meanings as pro_meanings

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
									{
										"question_title":'First Name',
										"input_type":"text", 
										'identifier':'data_provider_first_name',
										'required':'true'
									},
									{
										"question_numbering":"1.2" ,
										"question_title":'Middle Name(s)',
										"input_type":"text", 
										'identifier':'data_provider_middle_name'
									},
									{
										"question_numbering":"1.2" ,
										"question_title":'surname',
										"sub_q_other_text":'',
										"input_type":"text", 
										'identifier':'data_provider_surname', 
										'required':'true'
									},
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

					{
						"question_numbering":"1" ,
						"question_title":'Enter the full address', 
						"sub_q_other_text":'', 
						'question_set': {'type':'address', 'identifier':'disclosure_address'},
						"identifier":"property_address",
						'object_set':'disclosure_address',
						'sub_questions':[
							{
								"question_numbering":"1" ,"question_title":'Address Line 1', 
								"sub_q_other_text":'',
								"identifier":"address_line_1", 
								"input_type":"text",
								'element':'line_1'
							},
							{
								"question_numbering":"1" ,
								"question_title":'Address Line 2', 
								"sub_q_other_text":'', 
								"identifier":"address_line_2", 
								"input_type":"text",
								'element':'line_2'
							},
							{
								"question_numbering":"1" ,
								"question_title":'Address Line 3', 
								"sub_q_other_text":'', 
								"identifier":"address_line_3", 
								"input_type":"text",
								'element':'line_3'
							},																						
							{
								"question_numbering":"1" ,
								"question_title":'Town or City', 
								"sub_q_other_text":'',
								"identifier":"address_town_or_city", 
								"input_type":"text",
								'element':'post_town'
							},
							{
								"question_numbering":"1" ,
								"question_title":'Postcode', 
								"sub_q_other_text":'',
								"identifier":"postcode", 
								"input_type":"postcode",
								'element':'postcode'
							},							
							{
								"question_numbering":"1" ,"question_title":'UPRN', 
								"sub_q_other_text":'',
								"identifier":"UPRN", 
								"input_type":"text",
								'element':'UPRN'
							},							
						]		
					}
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
									'You’ll need a copy of your lease in order to answer these questions. If you do not have a copy of your lease, ask your solicitor for help. Estate agents need to be able to share the following information with the buyer.'
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
										"question_numbering":"3.2.1" ,"question_title":'How much ground rent do you pay each year? £ / year', "sub_q_other_text":'',
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
													"question_numbering":"1" ,"question_title":'Building/street no', 
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
													"question_numbering":"1" ,"question_title":'Town/City', 
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
								"question_title":'provide any details, such as where you are in that transaction, whether there have been any hold-ups, and what your expected completion date is?',
								"identifier":"property_dependant_details","input_type":"detail_text",
								'display_reliance':[{'identifier':'property_dependant','value':['1']}]
							}
						]
					},
					{
						"question_numbering":"3.1" ,'question_title':'Are there other factors that might affect the timing of your move?', 
						"sub_q_other_text":['You can select multiple factors and add any relevant dates, if known.'],
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
								'question_title':'Has a long lease of the roof / air space been granted to a solar panel provider?',
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

query_select = {
'data_providers_count' : {'db_position': 0, 'input_type': 'multi_row'} , 

'address_line_1' : {'db_position': 1, 'input_type': 'text'} , 

'address_line_2' : {'db_position': 2, 'input_type': 'text'} , 

'address_line_3' : {'db_position': 3, 'input_type': 'text'} , 

'address_town_or_city' : {'db_position': 4, 'input_type': 'text'} , 

'postcode' : {'db_position': 5, 'input_type': 'postcode'} , 

'UPRN' : {'db_position': 6, 'input_type': 'text'} , 

'lease_or_free' : {'db_position': 7, 'input_type': 'radio'} , 

'years_left' : {'db_position': 8, 'input_type': 'number'} , 

'rent_value' : {'db_position': 9, 'input_type': 'currency'} , 

'ground_rent_increase_bool' : {'db_position': 10, 'input_type': 'bool'} , 

'ground_rent_increase_date' : {'db_position': 11, 'input_type': 'date'} , 

'ground_rent_increase_frequency' : {'db_position': 12, 'input_type': 'text'} , 

'rent_increase_type' : {'db_position': 13, 'input_type': 'radio'} , 

'rent_increase_type_details' : {'db_position': 14, 'input_type': 'detail_text'} , 

'service_charge_bool' : {'db_position': 15, 'input_type': 'bool'} , 

'last_service_charge' : {'db_position': 16, 'input_type': 'currency'} , 

'service_charge_budget_bool' : {'db_position': 17, 'input_type': 'bool'} , 

'service_charge_bill_docu' : {'db_position': 18, 'input_type': 'docu'} , 

'service_charge_payments_due' : {'db_position': 19, 'input_type': 'date'} , 

'service_charge_pay_reciever' : {'db_position': 20, 'input_type': 'radio'} , 

'service_charge_organisation' : {'db_position': 21, 'input_type': 'text'} , 

'service_charge_Building_name' : {'db_position': 22, 'input_type': 'text'} , 

'service_charge_street_no' : {'db_position': 23, 'input_type': 'text'} , 

'service_charge_street_name' : {'db_position': 24, 'input_type': 'text'} , 

'service_charge_town_or_city' : {'db_position': 25, 'input_type': 'text'} , 

'service_charge_postcode' : {'db_position': 26, 'input_type': 'text'} , 

'first_to_occupy' : {'db_position': 27, 'input_type': 'bool'} , 

'warranties_docu' : {'db_position': 28, 'input_type': 'docu'} , 

'property_dependant' : {'db_position': 29, 'input_type': 'bool'} , 

'property_dependant_details' : {'db_position': 30, 'input_type': 'detail_text'} , 

'school_term' : {'db_position': 31, 'input_type': 'checkbox'} , 

'school_term_date' : {'db_position': 32, 'input_type': 'date'} , 

'upcoming_holiday' : {'db_position': 33, 'input_type': 'checkbox'} , 

'upcoming_holiday_date' : {'db_position': 34, 'input_type': 'date'} , 

'job_move' : {'db_position': 35, 'input_type': 'checkbox'} , 

'job_move_date' : {'db_position': 36, 'input_type': 'date'} , 

'redundancy' : {'db_position': 37, 'input_type': 'checkbox'} , 

'redundancy_date' : {'db_position': 38, 'input_type': 'date'} , 

'medical' : {'db_position': 39, 'input_type': 'checkbox'} , 

'medical_date' : {'db_position': 40, 'input_type': 'date'} , 

'notice_to_tenant' : {'db_position': 41, 'input_type': 'checkbox'} , 

'notice_to_tenant_date' : {'db_position': 42, 'input_type': 'date'} , 

'retirement' : {'db_position': 43, 'input_type': 'checkbox'} , 

'retirement_date' : {'db_position': 44, 'input_type': 'date'} , 

'build_complete' : {'db_position': 45, 'input_type': 'checkbox'} , 

'build_complete_date' : {'db_position': 46, 'input_type': 'date'} , 

'other_move_factor' : {'db_position': 47, 'input_type': 'checkbox'} , 

'other_move_factor_date' : {'db_position': 48, 'input_type': 'date'} , 

'other_move_factor_details' : {'db_position': 49, 'input_type': 'detail_text'} , 

'works_and_alterations_count' : {'db_position': 50, 'input_type': 'multi_row'} , 

'planning_breach' : {'db_position': 51, 'input_type': 'checkbox'} , 

'planning_breach_details' : {'db_position': 52, 'input_type': 'detail_text'} , 

'bulding_reg_breach' : {'db_position': 53, 'input_type': 'checkbox'} , 

'bulding_reg_breach_details' : {'db_position': 54, 'input_type': 'detail_text'} , 

'unfinished_work' : {'db_position': 55, 'input_type': 'checkbox'} , 

'unfinished_work_details' : {'db_position': 56, 'input_type': 'detail_text'} , 

'consent_lack' : {'db_position': 57, 'input_type': 'checkbox'} , 

'consent_lack_details' : {'db_position': 58, 'input_type': 'detail_text'} , 

'solar_panels_bool' : {'db_position': 59, 'input_type': 'bool'} , 

'solar_installation_year' : {'db_position': 60, 'input_type': 'number'} , 

'solar_panels_ownership_bool' : {'db_position': 61, 'input_type': 'bool'} , 

'solar_panels_long_lease_ownership_bool' : {'db_position': 62, 'input_type': 'bool'} , 

'solar_electrical_tarrif_docu' : {'db_position': 63, 'input_type': 'docu'} , 

'protected_buildings_bool' : {'db_position': 64, 'input_type': 'bool_extra'} , 

'protected_buildings_docu' : {'db_position': 65, 'input_type': 'docu'} , 

'conservation_area_bool' : {'db_position': 66, 'input_type': 'bool_extra'} , 

'conservation_area_docu' : {'db_position': 67, 'input_type': 'docu'} , 

'TPO_bool' : {'db_position': 68, 'input_type': 'bool_extra'} , 

'order_terms_complied_with' : {'db_position': 69, 'input_type': 'bool_extra'} , 

'TPO_docu' : {'db_position': 70, 'input_type': 'docu'} , 

'all_required_consents' : {'db_position': 71, 'input_type': 'bool_extra'} , 

'all_required_consents_details' : {'db_position': 72, 'input_type': 'detail_text'} , 

'charges_bool' : {'db_position': 73, 'input_type': 'bool'} , 

'charges_details' : {'db_position': 74, 'input_type': 'detail_text'} , 

'maintain_road_bool' : {'db_position': 75, 'input_type': 'bool_extra'} , 

'maintain_road_payement_details' : {'db_position': 76, 'input_type': 'detail_text'} , 

'private_road' : {'db_position': 77, 'input_type': 'bool_extra'} , 

'public_expense_road' : {'db_position': 78, 'input_type': 'bool_extra'} , 

'mains_drainage' : {'db_position': 79, 'input_type': 'checkbox'} , 

'electricity' : {'db_position': 80, 'input_type': 'checkbox'} , 

'water_supply' : {'db_position': 81, 'input_type': 'checkbox'} , 

'gas' : {'db_position': 82, 'input_type': 'checkbox'} , 

'broadband' : {'db_position': 83, 'input_type': 'checkbox'} , 

'sewage_plant' : {'db_position': 84, 'input_type': 'checkbox'} , 

'telephone_landlines' : {'db_position': 85, 'input_type': 'checkbox'} , 

'solar_panels' : {'db_position': 86, 'input_type': 'checkbox'} , 

'heat_pumps' : {'db_position': 87, 'input_type': 'checkbox'} , 

'other_provisioned_services' : {'db_position': 88, 'input_type': 'checkbox'} , 

'other_provisioned_services_details' : {'db_position': 89, 'input_type': 'detail_text'} , 

'shared_facilities_bool' : {'db_position': 90, 'input_type': 'bool'} , 

'shared_facilities_text_details' : {'db_position': 91, 'input_type': 'detail_text'} , 

'parking_arrangement_details' : {'db_position': 92, 'input_type': 'detail_text'} , 

'controlled_parking' : {'db_position': 93, 'input_type': 'bool_extra'} , 

'live_at_prop_bool' : {'db_position': 94, 'input_type': 'bool'} , 

'over_17_bool' : {'db_position': 95, 'input_type': 'bool'} , 

'over_17_count' : {'db_position': 96, 'input_type': 'multi_row'} , 

'lodgers_bool' : {'db_position': 97, 'input_type': 'bool'} , 

'agree_to_leave_bool' : {'db_position': 98, 'input_type': 'bool'} , 

'occupiers_contract_sign_bool' : {'db_position': 99, 'input_type': 'bool'} , 

'vacant_possession_bool' : {'db_position': 100, 'input_type': 'bool'} , 

'vacant_possession_proof_docu' : {'db_position': 101, 'input_type': 'docu'} , 

'flooding_bool' : {'db_position': 102, 'input_type': 'bool'} , 

'flood_events_count' : {'db_position': 103, 'input_type': 'multi_row'} , 

'flood_risk_report_bool' : {'db_position': 104, 'input_type': 'bool'} , 

'flood_risk_report_docu' : {'db_position': 105, 'input_type': 'docu'} , 

'nearby_development_bool' : {'db_position': 106, 'input_type': 'bool'} , 

'nearby_development' : {'db_position': 107, 'input_type': 'detail_text'} , 

'complaints_bool' : {'db_position': 108, 'input_type': 'bool'} , 

'complaints_details' : {'db_position': 109, 'input_type': 'detail_text'} , 

'disputes_bool' : {'db_position': 110, 'input_type': 'bool'} , 

'disputes_details' : {'db_position': 111, 'input_type': 'detail_text'} , 

'knotweed_bool' : {'db_position': 112, 'input_type': 'bool'} , 

'knotweed' : {'db_position': 113, 'input_type': 'detail_text'} , 

'mining_bool' : {'db_position': 114, 'input_type': 'bool'} , 

'mining' : {'db_position': 115, 'input_type': 'detail_text'} , 

'influence_decision_bool' : {'db_position': 116, 'input_type': 'bool'} , 

'influence_decision' : {'db_position': 117, 'input_type': 'detail_text'} , 

'neighbours_access_bool' : {'db_position': 118, 'input_type': 'bool'} , 

'neighbours_access' : {'db_position': 119, 'input_type': 'detail_text'} , 

'anything_else_bool' : {'db_position': 120, 'input_type': 'bool'} , 

'anything_else' : {'db_position': 121, 'input_type': 'detail_text'}
}

query_columns = 'data_providers_count,address_line_1,address_line_2,address_line_3,address_town_or_city,postcode,UPRN,lease_or_free,years_left,rent_value,ground_rent_increase_bool,ground_rent_increase_date,ground_rent_increase_frequency,rent_increase_type,rent_increase_type_details,service_charge_bool,last_service_charge,service_charge_budget_bool,service_charge_bill_docu,service_charge_payments_due,service_charge_pay_reciever,service_charge_organisation,service_charge_Building_name,service_charge_street_no,service_charge_street_name,service_charge_town_or_city,service_charge_postcode,first_to_occupy,warranties_docu,property_dependant,property_dependant_details,school_term,school_term_date,upcoming_holiday,upcoming_holiday_date,job_move,job_move_date,redundancy,redundancy_date,medical,medical_date,notice_to_tenant,notice_to_tenant_date,retirement,retirement_date,build_complete,build_complete_date,other_move_factor,other_move_factor_date,other_move_factor_details,works_and_alterations_count,planning_breach,planning_breach_details,bulding_reg_breach,bulding_reg_breach_details,unfinished_work,unfinished_work_details,consent_lack,consent_lack_details,solar_panels_bool,solar_installation_year,solar_panels_ownership_bool,solar_panels_long_lease_ownership_bool,solar_electrical_tarrif_docu,protected_buildings_bool,protected_buildings_docu,conservation_area_bool,conservation_area_docu,TPO_bool,order_terms_complied_with,TPO_docu,all_required_consents,all_required_consents_details,charges_bool,charges_details,maintain_road_bool,maintain_road_payement_details,private_road,public_expense_road,mains_drainage,electricity,water_supply,gas,broadband,sewage_plant,telephone_landlines,solar_panels,heat_pumps,other_provisioned_services,other_provisioned_services_details,shared_facilities_bool,shared_facilities_text_details,parking_arrangement_details,controlled_parking,live_at_prop_bool,over_17_bool,over_17_count,lodgers_bool,agree_to_leave_bool,occupiers_contract_sign_bool,vacant_possession_bool,vacant_possession_proof_docu,flooding_bool,flood_events_count,flood_risk_report_bool,flood_risk_report_docu,nearby_development_bool,nearby_development,complaints_bool,complaints_details,disputes_bool,disputes_details,knotweed_bool,knotweed,mining_bool,mining,influence_decision_bool,influence_decision,neighbours_access_bool,neighbours_access,anything_else_bool,anything_else'

# more than likely all options covered by most concern are covered by risk markers
most_concern = {
				'years_left':{ 'value':10},
				'ground_rent_increase_bool':{'value':'yes'},
				'rent_increase_type': {'value':['Variable','Other']},
				'service_charge_bool':{'value':['yes','empty']},
				'service_charge_budget_bool':{'value':['empty','yes']},
				'property_dependant':{'value':'yes'},
				'job_move':{'value':'yes'},
				'redundancy':{'value':'yes'},
				'medical':{'value':'yes'},
				'notice_to_tenant':{'value':'yes'}, 
				'build_complete':{'value':'yes'},
				'other_move_factor':{'value':'yes'},
				'planning_breach':{'value':'yes'},
				'bulding_reg_breach':{'value':'yes'},
				'unfinished_work':{'value':'yes'},
				'consent_lack':{'value':'yes'},
				'order_terms_complied_with':{'value':['yes','not_known']},
				'all_required_consents':{'value':['yes']},
				'charges_bool':{'value':['yes','empty']},
				'maintain_road_payement_details':{'value':['not_known','empty','yes']},
				'agree_to_leave_bool':{'value':['empty','yes']},
				'vacant_possession_bool':{'value':['empty','yes']},
				'flooding_bool':{'value':['empty','yes']},
				'flood_events_count':{'value':1},
				'knotweed_bool':{'value':['empty','yes']},
				'mining_bool':{'value':['empty','yes']},
				'influence_decision_bool':{'value':['empty','yes']},
				'neighbours_access_bool':{'value':['empty','yes']},
				'anything_else_bool':{'value':['empty','yes']},
				}

highest_risk = []

sub_tables_list = ['`form_data`.`TA6_Part_1_data_providers`', '`form_data`.`TA6_Part_1_works_and_alterations`', '`form_data`.`TA6_Part_1_over_17`', '`form_data`.`TA6_Part_1_flood_events`']
#obligations_burdens_and_negtive
obn = []

sub_tables = [{'table_route': '`form_data`.`TA6_Part_1_data_providers`', 'table_key': {'data_provider_first_name': {'db_position': 0, 'input_type': 'text'}, 'data_provider_middle_name': {'db_position': 1, 'input_type': 'text'}, 'data_provider_surname': {'db_position': 2, 'input_type': 'text'}, 'data_provider_type': {'db_position': 3, 'input_type': 'radio'}, 'data_provider_type_details': {'db_position': 4, 'input_type': 'detail_text'}}, 'table_collector': 'data_provider_first_name,data_provider_middle_name,data_provider_surname,data_provider_type,data_provider_type_details,'}, {'table_route': '`form_data`.`TA6_Part_1_works_and_alterations`', 'table_key': {'building_works_and_alterations': {'db_position': 0, 'input_type': 'radio'}, 'property_alterations_work_details': {'db_position': 1, 'input_type': 'detail_text'}, 'alterations_work_start': {'db_position': 2, 'input_type': 'date'}, 'alterations_work_end': {'db_position': 3, 'input_type': 'date'}, 'property_works_completed_bool': {'db_position': 4, 'input_type': 'bool'}, 'completion_of_work_details': {'db_position': 5, 'input_type': 'detail_text'}}, 'table_collector': 'building_works_and_alterations,property_alterations_work_details,alterations_work_start,alterations_work_end,property_works_completed_bool,completion_of_work_details,'}, {'table_route': '`form_data`.`TA6_Part_1_over_17`', 'table_key': {'first_name_17': {'db_position': 0, 'input_type': 'text'}, 'middle_name_17': {'db_position': 1, 'input_type': 'text'}, 'surname_17': {'db_position': 2, 'input_type': 'text'}}, 'table_collector': 'first_name_17,middle_name_17,surname_17,'}, {'table_route': '`form_data`.`TA6_Part_1_flood_events`', 'table_key': {'flood_type': {'db_position': 0, 'input_type': 'radio'}, 'other_flood_type_description': {'db_position': 1, 'input_type': 'detail_text'}, 'flood_event_date': {'db_position': 2, 'input_type': 'date'}, 'flood_area_details': {'db_position': 3, 'input_type': 'detail_text'}}, 'table_collector': 'flood_type,other_flood_type_description,flood_event_date,flood_area_details,'}]
monetary_outputs = []

third_party_rights = []

pairings = {'personal_details': [{'database': 'data_providers_count', 'form': 'data_providers', 'table': '`form_data`.`TA6_Part_1_data_providers`', 'rows': [{'database': 'data_provider_first_name', 'form': 'data_provider_first_name'}, {'database': 'data_provider_middle_name', 'form': 'data_provider_middle_name'}, {'database': 'data_provider_surname', 'form': 'data_provider_surname'}, {'database': 'data_provider_type', 'form': 'data_provider_type'}, {'database': 'data_provider_type_details', 'form': 'data_provider_type_details'}]}], 'basic_data': [{'database': 'address_line_1', 'form': 'address_line_1'}, {'database': 'address_line_2', 'form': 'address_line_2'}, {'database': 'address_line_3', 'form': 'address_line_3'}, {'database': 'address_town_or_city', 'form': 'address_town_or_city'}, {'database': 'postcode', 'form': 'postcode'}, {'database': 'UPRN', 'form': 'UPRN'}], 'ownership': [{'database': 'lease_or_free', 'form': 'lease_or_free'}, {'database': 'years_left', 'form': 'years_left'}, {'database': 'rent_value', 'form': 'rent_value'}, {'database': 'ground_rent_increase_bool', 'form': 'ground_rent_increase_bool'}, {'database': 'ground_rent_increase_date', 'form': 'ground_rent_increase_date'}, {'database': 'ground_rent_increase_frequency', 'form': 'ground_rent_increase_frequency'}, {'database': 'rent_increase_type', 'form': 'rent_increase_type'}, {'database': 'rent_increase_type_details', 'form': 'rent_increase_type_details'}], 'service_charges': [{'database': 'service_charge_bool', 'form': 'service_charge_bool'}, {'database': 'last_service_charge', 'form': 'last_service_charge'}, {'database': 'service_charge_budget_bool', 'form': 'service_charge_budget_bool'}, {'database': 'service_charge_bill_docu', 'form': 'service_charge_bill_docu'}, {'database': 'service_charge_payments_due', 'form': 'service_charge_payments_due'}, {'database': 'service_charge_pay_reciever', 'form': 'service_charge_pay_reciever'}, {'database': 'service_charge_organisation', 'form': 'service_charge_organisation'}, {'database': 'service_charge_Building_name', 'form': 'service_charge_Building_name'}, {'database': 'service_charge_street_no', 'form': 'service_charge_street_no'}, {'database': 'service_charge_street_name', 'form': 'service_charge_street_name'}, {'database': 'service_charge_town_or_city', 'form': 'service_charge_town_or_city'}, {'database': 'service_charge_postcode', 'form': 'service_charge_postcode'}], 'new_builds_and_conversions': [{'database': 'first_to_occupy', 'form': 'first_to_occupy'}, {'database': 'warranties_docu', 'form': 'warranties_docu'}], 'timing': [{'database': 'property_dependant', 'form': 'property_dependant'}, {'database': 'property_dependant_details', 'form': 'property_dependant_details'}, {'database': 'school_term', 'form': 'school_term'}, {'database': 'school_term_date', 'form': 'school_term_date'}, {'database': 'upcoming_holiday', 'form': 'upcoming_holiday'}, {'database': 'upcoming_holiday_date', 'form': 'upcoming_holiday_date'}, {'database': 'job_move', 'form': 'job_move'}, {'database': 'job_move_date', 'form': 'job_move_date'}, {'database': 'redundancy', 'form': 'redundancy'}, {'database': 'redundancy_date', 'form': 'redundancy_date'}, {'database': 'medical', 'form': 'medical'}, {'database': 'medical_date', 'form': 'medical_date'}, {'database': 'notice_to_tenant', 'form': 'notice_to_tenant'}, {'database': 'notice_to_tenant_date', 'form': 'notice_to_tenant_date'}, {'database': 'retirement', 'form': 'retirement'}, {'database': 'retirement_date', 'form': 'retirement_date'}, {'database': 'build_complete', 'form': 'build_complete'}, {'database': 'build_complete_date', 'form': 'build_complete_date'}, {'database': 'other_move_factor', 'form': 'other_move_factor'}, {'database': 'other_move_factor_date', 'form': 'other_move_factor_date'}, {'database': 'other_move_factor_details', 'form': 'other_move_factor_details'}], 'property_alteration': [{'database': 'works_and_alterations_count', 'form': 'works_and_alterations_count', 'table': '`form_data`.`TA6_Part_1_works_and_alterations`', 'rows': [{'database': 'building_works_and_alterations', 'form': 'building_works_and_alterations'}, {'database': 'property_alterations_work_details', 'form': 'property_alterations_work_details'}, {'database': 'alterations_work_start', 'form': 'alterations_work_start'}, {'database': 'alterations_work_end', 'form': 'alterations_work_end'}, {'database': 'property_works_completed_bool', 'form': 'property_works_completed_bool'}, {'database': 'completion_of_work_details', 'form': 'completion_of_work_details'}]}], 'liabilities': [{'database': 'planning_breach', 'form': 'planning_breach'}, {'database': 'planning_breach_details', 'form': 'planning_breach_details'}, {'database': 'bulding_reg_breach', 'form': 'bulding_reg_breach'}, {'database': 'bulding_reg_breach_details', 'form': 'bulding_reg_breach_details'}, {'database': 'unfinished_work', 'form': 'unfinished_work'}, {'database': 'unfinished_work_details', 'form': 'unfinished_work_details'}, {'database': 'consent_lack', 'form': 'consent_lack'}, {'database': 'consent_lack_details', 'form': 'consent_lack_details'}], 'solar_panels': [{'database': 'solar_panels_bool', 'form': 'solar_panels_bool'}, {'database': 'solar_installation_year', 'form': 'solar_installation_year'}, {'database': 'solar_panels_ownership_bool', 'form': 'solar_panels_ownership_bool'}, {'database': 'solar_panels_long_lease_ownership_bool', 'form': 'solar_panels_long_lease_ownership_bool'}, {'database': 'solar_electrical_tarrif_docu', 'form': 'solar_electrical_tarrif_docu'}], 'protected_buildings': [{'database': 'protected_buildings_bool', 'form': 'protected_buildings_bool'}, {'database': 'protected_buildings_docu', 'form': 'protected_buildings_docu'}, {'database': 'conservation_area_bool', 'form': 'conservation_area_bool'}, {'database': 'conservation_area_docu', 'form': 'conservation_area_docu'}], 'protected_trees': [{'database': 'TPO_bool', 'form': 'TPO_bool'}, {'database': 'order_terms_complied_with', 'form': 'order_terms_complied_with'}, {'database': 'TPO_docu', 'form': 'TPO_docu'}], 'consent': [{'database': 'all_required_consents', 'form': 'all_required_consents'}, {'database': 'all_required_consents_details', 'form': 'all_required_consents_details'}], 'charges': [{'database': 'charges_bool', 'form': 'charges_bool'}, {'database': 'charges_details', 'form': 'charges_details'}], 'access_roads': [{'database': 'maintain_road_bool', 'form': 'maintain_road_bool'}, {'database': 'maintain_road_payement_details', 'form': 'maintain_road_payement_details'}, {'database': 'private_road', 'form': 'private_road'}, {'database': 'public_expense_road', 'form': 'public_expense_road'}], 'services': [{'database': 'mains_drainage', 'form': 'mains_drainage'}, {'database': 'electricity', 'form': 'electricity'}, {'database': 'water_supply', 'form': 'water_supply'}, {'database': 'gas', 'form': 'gas'}, {'database': 'broadband', 'form': 'broadband'}, {'database': 'sewage_plant', 'form': 'sewage_plant'}, {'database': 'telephone_landlines', 'form': 'telephone_landlines'}, {'database': 'solar_panels', 'form': 'solar_panels'}, {'database': 'heat_pumps', 'form': 'heat_pumps'}, {'database': 'other_provisioned_services', 'form': 'other_provisioned_services'}, {'database': 'other_provisioned_services_details', 'form': 'other_provisioned_services_details'}], 'shared_facilities': [{'database': 'shared_facilities_bool', 'form': 'shared_facilities_bool'}, {'database': 'shared_facilities_text_details', 'form': 'shared_facilities_text_details'}], 'parking': [{'database': 'parking_arrangement_details', 'form': 'parking_arrangement_details'}, {'database': 'controlled_parking', 'form': 'controlled_parking'}], 'occupiers': [{'database': 'live_at_prop_bool', 'form': 'live_at_prop_bool'}, {'database': 'over_17_bool', 'form': 'over_17_bool'}, {'database': 'over_17_count', 'form': 'over_17_count', 'table': '`form_data`.`TA6_Part_1_over_17`', 'rows': [{'database': 'first_name_17', 'form': 'first_name_17'}, {'database': 'middle_name_17', 'form': 'middle_name_17'}, {'database': 'surname_17', 'form': 'surname_17'}]}, {'database': 'lodgers_bool', 'form': 'lodgers_bool'}, {'database': 'agree_to_leave_bool', 'form': 'agree_to_leave_bool'}, {'database': 'occupiers_contract_sign_bool', 'form': 'occupiers_contract_sign_bool'}, {'database': 'vacant_possession_bool', 'form': 'vacant_possession_bool'}, {'database': 'vacant_possession_proof_docu', 'form': 'vacant_possession_proof_docu'}], 'flooding': [{'database': 'flooding_bool', 'form': 'flooding_bool'}, {'database': 'flood_events_count', 'form': 'flood_events_count', 'table': '`form_data`.`TA6_Part_1_flood_events`', 'rows': [{'database': 'flood_type', 'form': 'flood_type'}, {'database': 'other_flood_type_description', 'form': 'other_flood_type_description'}, {'database': 'flood_event_date', 'form': 'flood_event_date'}, {'database': 'flood_area_details', 'form': 'flood_area_details'}]}, {'database': 'flood_risk_report_bool', 'form': 'flood_risk_report_bool'}, {'database': 'flood_risk_report_docu', 'form': 'flood_risk_report_docu'}], 'right_to_enjoy': [{'database': 'nearby_development_bool', 'form': 'nearby_development_bool'}, {'database': 'nearby_development', 'form': 'nearby_development'}], 'disputes': [{'database': 'complaints_bool', 'form': 'complaints_bool'}, {'database': 'complaints_details', 'form': 'complaints_details'}, {'database': 'disputes_bool', 'form': 'disputes_bool'}, {'database': 'disputes_details', 'form': 'disputes_details'}], 'other_info': [{'database': 'knotweed_bool', 'form': 'knotweed_bool'}, {'database': 'knotweed', 'form': 'knotweed'}, {'database': 'mining_bool', 'form': 'mining_bool'}, {'database': 'mining', 'form': 'mining'}, {'database': 'influence_decision_bool', 'form': 'influence_decision_bool'}, {'database': 'influence_decision', 'form': 'influence_decision'}, {'database': 'neighbours_access_bool', 'form': 'neighbours_access_bool'}, {'database': 'neighbours_access', 'form': 'neighbours_access'}, {'database': 'anything_else_bool', 'form': 'anything_else_bool'}, {'database': 'anything_else', 'form': 'anything_else'}]}

#pairings = {'personal_details': {'data_providers_count': {'database': 'data_providers_count', 'table': '`form_data`.`TA6_Part_1_data_providers`', 'rows': {'data_provider_first_name': {'database': 'data_provider_first_name'}, 'data_provider_middle_name': {'database': 'data_provider_middle_name'}, 'data_provider_surname': {'database': 'data_provider_surname'}, 'data_provider_type': {'database': 'data_provider_type'}, 'data_provider_type_details': {'database': 'data_provider_type_details'}}}}, 'basic_data': {'postcode': {'database': 'postcode'}, 'address_line_1': {'database': 'address_line_1'}, 'address_line_2': {'database': 'address_line_2'}, 'address_town_or_city': {'database': 'address_town_or_city'}, 'UPRN': {'database': 'UPRN'}}, 'ownership': {'lease_or_free': {'database': 'lease_or_free'}, 'years_left': {'database': 'years_left'}, 'rent_value': {'database': 'rent_value'}, 'ground_rent_increase_bool': {'database': 'ground_rent_increase_bool'}, 'ground_rent_increase_date': {'database': 'ground_rent_increase_date'}, 'ground_rent_increase_frequency': {'database': 'ground_rent_increase_frequency'}, 'rent_increase_type': {'database': 'rent_increase_type'}, 'rent_increase_type_details': {'database': 'rent_increase_type_details'}}, 'service_charges': {'service_charge_bool': {'database': 'service_charge_bool'}, 'last_service_charge': {'database': 'last_service_charge'}, 'service_charge_budget_bool': {'database': 'service_charge_budget_bool'}, 'service_charge_bill_docu': {'database': 'service_charge_bill_docu'}, 'service_charge_payments_due': {'database': 'service_charge_payments_due'}, 'service_charge_pay_reciever': {'database': 'service_charge_pay_reciever'}, 'service_charge_organisation': {'database': 'service_charge_organisation'}, 'service_charge_Building_name': {'database': 'service_charge_Building_name'}, 'service_charge_street_no': {'database': 'service_charge_street_no'}, 'service_charge_street_name': {'database': 'service_charge_street_name'}, 'service_charge_town_or_city': {'database': 'service_charge_town_or_city'}, 'service_charge_postcode': {'database': 'service_charge_postcode'}}, 'new_builds_and_conversions': {'first_to_occupy': {'database': 'first_to_occupy'}, 'warranties_docu': {'database': 'warranties_docu'}}, 'timing': {'property_dependant': {'database': 'property_dependant'}, 'property_dependant_details': {'database': 'property_dependant_details'}, 'school_term': {'database': 'school_term'}, 'school_term_date': {'database': 'school_term_date'}, 'upcoming_holiday': {'database': 'upcoming_holiday'}, 'upcoming_holiday_date': {'database': 'upcoming_holiday_date'}, 'job_move': {'database': 'job_move'}, 'job_move_date': {'database': 'job_move_date'}, 'redundancy': {'database': 'redundancy'}, 'redundancy_date': {'database': 'redundancy_date'}, 'medical': {'database': 'medical'}, 'medical_date': {'database': 'medical_date'}, 'notice_to_tenant': {'database': 'notice_to_tenant'}, 'notice_to_tenant_date': {'database': 'notice_to_tenant_date'}, 'retirement': {'database': 'retirement'}, 'retirement_date': {'database': 'retirement_date'}, 'build_complete': {'database': 'build_complete'}, 'build_complete_date': {'database': 'build_complete_date'}, 'other_move_factor': {'database': 'other_move_factor'}, 'other_move_factor_date': {'database': 'other_move_factor_date'}, 'other_move_factor_details': {'database': 'other_move_factor_details'}}, 'property_alteration': {'works_and_alterations_count': {'database': 'works_and_alterations_count', 'table': '`form_data`.`TA6_Part_1_works_and_alterations`', 'rows': {'building_works_and_alterations': {'database': 'building_works_and_alterations'}, 'property_alterations_work_details': {'database': 'property_alterations_work_details'}, 'alterations_work_start': {'database': 'alterations_work_start'}, 'alterations_work_end': {'database': 'alterations_work_end'}, 'property_works_completed_bool': {'database': 'property_works_completed_bool'}, 'completion_of_work_details': {'database': 'completion_of_work_details'}}}}, 'liabilities': {'planning_breach': {'database': 'planning_breach'}, 'planning_breach_details': {'database': 'planning_breach_details'}, 'bulding_reg_breach': {'database': 'bulding_reg_breach'}, 'bulding_reg_breach_details': {'database': 'bulding_reg_breach_details'}, 'unfinished_work': {'database': 'unfinished_work'}, 'unfinished_work_details': {'database': 'unfinished_work_details'}, 'consent_lack': {'database': 'consent_lack'}, 'consent_lack_details': {'database': 'consent_lack_details'}}, 'solar_panels': {'solar_panels_bool': {'database': 'solar_panels_bool'}, 'solar_installation_year': {'database': 'solar_installation_year'}, 'solar_panels_ownership_bool': {'database': 'solar_panels_ownership_bool'}, 'solar_panels_long_lease_ownership_bool': {'database': 'solar_panels_long_lease_ownership_bool'}, 'solar_electrical_tarrif_docu': {'database': 'solar_electrical_tarrif_docu'}}, 'protected_buildings': {'protected_buildings_bool': {'database': 'protected_buildings_bool'}, 'protected_buildings_docu': {'database': 'protected_buildings_docu'}, 'conservation_area_bool': {'database': 'conservation_area_bool'}, 'conservation_area_docu': {'database': 'conservation_area_docu'}}, 'protected_trees': {'TPO_bool': {'database': 'TPO_bool'}, 'order_terms_complied_with': {'database': 'order_terms_complied_with'}, 'TPO_docu': {'database': 'TPO_docu'}}, 'consent': {'all_required_consents': {'database': 'all_required_consents'}, 'all_required_consents_details': {'database': 'all_required_consents_details'}}, 'charges': {'charges_bool': {'database': 'charges_bool'}, 'charges_details': {'database': 'charges_details'}}, 'access_roads': {'maintain_road_bool': {'database': 'maintain_road_bool'}, 'maintain_road_payement_details': {'database': 'maintain_road_payement_details'}, 'private_road': {'database': 'private_road'}, 'public_expense_road': {'database': 'public_expense_road'}}, 'services': {'mains_drainage': {'database': 'mains_drainage'}, 'electricity': {'database': 'electricity'}, 'water_supply': {'database': 'water_supply'}, 'gas': {'database': 'gas'}, 'broadband': {'database': 'broadband'}, 'sewage_plant': {'database': 'sewage_plant'}, 'telephone_landlines': {'database': 'telephone_landlines'}, 'solar_panels': {'database': 'solar_panels'}, 'heat_pumps': {'database': 'heat_pumps'}, 'other_provisioned_services': {'database': 'other_provisioned_services'}, 'other_provisioned_services_details': {'database': 'other_provisioned_services_details'}}, 'shared_facilities': {'shared_facilities_bool': {'database': 'shared_facilities_bool'}, 'shared_facilities_text_details': {'database': 'shared_facilities_text_details'}}, 'parking': {'parking_arrangement_details': {'database': 'parking_arrangement_details'}, 'controlled_parking': {'database': 'controlled_parking'}}, 'occupiers': {'live_at_prop_bool': {'database': 'live_at_prop_bool'}, 'over_17_bool': {'database': 'over_17_bool'}, 'over_17_count': {'database': 'over_17_count', 'table': '`form_data`.`TA6_Part_1_over_17`', 'rows': {'first_name_17': {'database': 'first_name_17'}, 'middle_name_17': {'database': 'middle_name_17'}, 'surname_17': {'database': 'surname_17'}}}, 'lodgers_bool': {'database': 'lodgers_bool'}, 'agree_to_leave_bool': {'database': 'agree_to_leave_bool'}, 'occupiers_contract_sign_bool': {'database': 'occupiers_contract_sign_bool'}, 'vacant_possession_bool': {'database': 'vacant_possession_bool'}, 'vacant_possession_proof_docu': {'database': 'vacant_possession_proof_docu'}}, 'flooding': {'flooding_bool': {'database': 'flooding_bool'}, 'flood_events_count': {'database': 'flood_events_count', 'table': '`form_data`.`TA6_Part_1_flood_events`', 'rows': {'flood_type': {'database': 'flood_type'}, 'other_flood_type_description': {'database': 'other_flood_type_description'}, 'flood_event_date': {'database': 'flood_event_date'}, 'flood_area_details': {'database': 'flood_area_details'}}}, 'flood_risk_report_bool': {'database': 'flood_risk_report_bool'}, 'flood_risk_report_docu': {'database': 'flood_risk_report_docu'}}, 'right_to_enjoy': {'nearby_development_bool': {'database': 'nearby_development_bool'}, 'nearby_development': {'database': 'nearby_development'}}, 'disputes': {'complaints_bool': {'database': 'complaints_bool'}, 'complaints_details': {'database': 'complaints_details'}, 'disputes_bool': {'database': 'disputes_bool'}, 'disputes_details': {'database': 'disputes_details'}}, 'other_info': {'knotweed_bool': {'database': 'knotweed_bool'}, 'knotweed': {'database': 'knotweed'}, 'mining_bool': {'database': 'mining_bool'}, 'mining': {'database': 'mining'}, 'influence_decision_bool': {'database': 'influence_decision_bool'}, 'influence_decision': {'database': 'influence_decision'}, 'neighbours_access_bool': {'database': 'neighbours_access_bool'}, 'neighbours_access': {'database': 'neighbours_access'}, 'anything_else_bool': {'database': 'anything_else_bool'}, 'anything_else': {'database': 'anything_else'}}}

#damage claims incidence vulrability
"""object_links_orig = {
	'postal_address':{
		'links':{
			'postcode':'postcode',
			'first_line':'address_line_1',
			'second__line':'address_line_2',
			'third_line':'address_town_or_city',
			'fourth_line':None
		},
		'local_ident':'disclosure_address',
		'meaning': 'The postal address of the property is {}, {}, {}, {}',
		'section':'basic_data',
		'position':'first'
	}
}"""

object_links = {
	'disclosure_address':{
		'links':{
			'postcode':'postcode',
			'first_line':'address_line_1',
			'second__line':'address_line_2',
			'third_line':'address_town_or_city',
			'fourth_line':None
		},
		'object':'postal_address',
		'meaning': 'The postal address of the property has been given as: {first_line}, {second__line}, {third_line}, {postcode}',
		'section':'basic_data',
		'position':'first'
	}
}
""",
	'service_charge_payment_address':{
		'links':{
			'postcode':'service_charge_postcode',
			'first_line':'service_charge_Building_name',
			'second__line':'service_charge_street_no',
			'third_line':'service_charge_street_name',
			'fourth_line':'service_charge_town_or_city'			
		},
		'object':'postal_address',
		'meaning':'the postal address of the recipient of the service charges for the preoperty is {first_line}, {second__line}, {third_line}, {fourth_line}, {postcode}'
	}"""
bjects = {
	'address': {
		'postcode':''
		}
}
aggregate_sets = {
	'address':{''
	}
}

TA6_Part_1 = {'template':template, 'object_links':object_links, 'pairings':pairings,'sub_tables':sub_tables, 'query_select':query_select, 'query_columns':query_columns, 'meanings':meanings, 'comp_risk_fraud':comp_risk_fraud, 'pro_meanings':pro_meanings}


