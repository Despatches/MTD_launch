bounds_radio_options = [
	{'radio_text':'Seller', 'radio_value':'seller'},
	{'radio_text':'Neighbours', 'radio_value':'neighbours'},
	{'radio_text':'Shared', 'radio_value':'shared'},
	{'radio_text':'Not known', 'radio_value':'not_known'}
]

not_known = [{'radio_value':'not_known', 'radio_text':'Not Known'}]

template={
	"Form" : "TA6", 'form_identifier':'TA6',"Sections" : [
		{
			"section_name":'Boundaries',
			'section_identifier':'personal_details',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					"question_title":'Is the property boundary roughly regular e.g rectangular or square',
					'input_type':'bool',
					'identifier':'boundary_regular_bool'
				},
				{
					"question_title":'Looking towards the property from the road, who owns or accepts responsibility to maintain or repair the boundary features:',
					'question_set':'true',
					"identifier":"boundary_ownership", 
					'multi_row_guidance':'for each person who enters data fill this section out seperatly',
					'display_reliance':[{'identifier':'boundary_regular_bool', 'value':['1']}],
					'sub_questions':[
						{
							'question_title':'(a) on the left?',
							'identifier':'left_bound',
							'input_type':'radio',
							'radio_options': bounds_radio_options
						},
						{
							'question_title':'(b) on the right?',
							'identifier':'left_bound',
							'input_type':'radio',
							'radio_options': bounds_radio_options
						},
						{
							'question_title':'(c) on the rear?',
							'identifier':'left_bound',
							'input_type':'radio',
							'radio_options': bounds_radio_options
						},
						{
							'question_title':'(d) on the front?',
							'identifier':'left_bound',
							'input_type':'radio',
							'radio_options': bounds_radio_options
						}																		
					],
				},
				{
					'question_title':'If the boundaries are irregular please indicate ownership by written description or by reference to a plan:',
					'identifier':'irregular_bounds_description',
					'input_type':'detail_text',
					'display_reliance':[{'identifier':'boundary_regular_bool', 'value':['1']}]
				},
				{
					'question_title':'Is the seller aware of any boundary feature having been moved in the last 10 years or during the seller’s period of ownership if longer?',
					'identifier':'moved_bound_features',
					'input_type':'radio',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'moved_bound_features_detail',
							'display_reliance':[{'identifier':'moved_bound_features', 'value':['1']}]
						}
					]
				},				
				{
					'question_title':'During the seller’s ownership, has any adjacent land or property been purchased by the seller? If Yes, please give details:',
					'identifier':'adjacent_land_purchase',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'adjacent_land_purchase_detail',
							'display_reliance':[{'identifier':'adjacent_land_purchase', 'value':['1']}]
						}
					]
				},
				{
					'question_title':'Does any part of the property or any building on the property overhang, or project under, the boundary of the neighbouring property or road, for example cellars under the pavement, overhanging eaves or covered walkways',
					'identifier':'bound_overhang',
					'input_type':'detail_text',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'give details',
							'identifier':'bound_overhang_detail',
							'display_reliance':[{'identifier':'bound_overhang', 'value':['1']}]
						}
					]
				},
				{
					'question_title':'Has any notice been received under the Party Wall etc. Act 1996 in respect of any shared/party boundaries?',
					'identifier':'party_wall_bool',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'party_wall_detail',
							'display_reliance':[{'identifier':'party_wall_bool', 'value':['1']}]
						},
						{
							'input_type':'docu',
							'question_title':'please give detail',
							'identifier':'party_wall_docu',
							'display_reliance':[{'identifier':'party_wall_bool', 'value':['1']}]
						},						
					]
				},												
			]
		},
		{
			"section_name":'Disputes and complaints',
			'section_identifier':'disputes_and_complaints',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Have there been any disputes or complaints regarding this property or a property nearby?',
					'identifier':'dispute_or_complaint_bool',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'dispute_or_complaint_detail',
							'display_reliance':[{'identifier':'dispute_or_complaint_bool', 'value':['1']}]
						},					
					]
				},
				{
					'question_title':'Is the seller aware of anything which might lead to a dispute about the property or a property nearby?',
					'identifier':'cause_dispute_or_complaint_bool',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'cause_dispute_or_complaint_detail',
							'display_reliance':[{'identifier':'cause_dispute_or_complaint_bool', 'value':['1']}]
						},					
					]
				}				
			]
		},
		{
			"section_name":'Notices and proposals',
			'section_identifier':'notices_and_proposals',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Have any notices or correspondence been received or sent (e.g. from or to a neighbour, council or government department), or any negotiations or discussions taken place, which affect the property or a property nearby?',
					'identifier':'correspondence',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'correspondence_detail',
							'display_reliance':[{'identifier':'correspondence', 'value':['1']}]
						},					
					]
				},
				{
					'question_title':'Is the seller aware of any proposals to develop property or land nearby, or of any proposals to make alterations to buildings nearby?',
					'identifier':'develop_proposals',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'develop_proposals_detail',
							'display_reliance':[{'identifier':'develop_proposals', 'value':['1']}]
						},					
					]
				},				
			]
		},
		{
			"section_name":'Alterations, planning and building control',
			'section_identifier':'planning_and_control',
			'section_text':[
				'Note to seller: All relevant approvals and supporting paperwork referred to in section 4 of this form, such as listed building consents, planning permissions, Building Regulations consents and completion certificates should be provided. If the seller has had works carried out the seller should produce the documentation authorising this. Copies may be obtained from the relevant local authority website. Competent Persons Certificates may be obtained from the contractor or the scheme provider (e.g. FENSA or Gas Safe Register). Further information about Competent Persons Certificates can be found at: https://www.gov.uk/guidance/competent-person- scheme-current-schemes-and-how-schemes-are-authorised',
				'Note to buyer: If any alterations or improvements have been made since the property was last valued for council tax, the sale of the property may trigger a revaluation. This may mean that following completion of the sale, the property will be put into a higher council tax band. Further information about council tax valuation can be found at: http://www.gov.uk/government/organisations/valuation-office-agency'
			],
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Have any of the following changes been made to the whole or any part of the property (including the garden)?',
					'question_set':'true',
					'identifier':'changes',
					'sub_questions':[
				
						{
							'question_title':'(a) Building works (e.g. extension, loft or garage conversion, removal of internal walls). If Yes, please give details including dates of all work undertaken:',
							'identifier':'extensions_removals',
							'input_type':'bool',
							'sub_questions':[
								{
									'input_type':'detail_text',
									'question_title':'please give details including dates of all work undertaken',
									'identifier':'extensions_removals_detail',
									'display_reliance':[{'identifier':'parent', 'value':['1']}],
								},
								{
									'input_type':'bool',
									'question_title':'Were any planning permissions, Building Regulations approvals or Completion Certificates required?',
									'identifier':'extensions_removals_permissions',
									'display_reliance':[{'identifier':'extensions_removals', 'value':['1']}],
									'sub_questions':[
										{
											'input_type':'docu',
											'question_title':'please supply copies of the planning permissions, Building Regulations approvals and Completion Certificates',
											'identifier':'extensions_removals_docu',
											'display_reliance':[{'identifier':'extensions_removals_permissions', 'value':['1']}],
										},
										{
											'input_type':'detail_text',
											'question_title':'f none were required, please explain why these were not required – e.g. permitted development rights applied or the work was exempt from Building Regulations',
											'identifier':'extensions_removals_no_doc_details',
											'display_reliance':[{'identifier':'extensions_removals_permissions', 'value':['0']}],
										}								
									]
								},													
							]
						},
						{
							'question_title':'(b) Change of use (e.g. from an office to a residence)',
							'identifier':'use_change',
							'input_type':'bool',
							'sub_questions':[
								{
									'input_type':'date',
									'question_title':'When did this occur?',
									'identifier':'use_change_date',
									'display_reliance':[{'identifier':'use_change', 'value':['1']}],
								},
								{
									'input_type':'bool',
									'question_title':'Were any planning permissions, Building Regulations approvals or Completion Certificates required?',
									'identifier':'use_change_permissions',
									'display_reliance':[{'identifier':'use_change', 'value':['1']}],
									'sub_questions':[
										{
											'input_type':'docu',
											'question_title':'Please supply copies of the planning permissions, Building Regulations approvals and Completion Certificates',
											'identifier':'use_change_docu',
											'display_reliance':[{'identifier':'use_change_permissions', 'value':['1']}],
										},
										{
											'input_type':'detail_text',
											'question_title':'If none were required, please explain why these were not required – e.g. permitted development rights applied or the work was exempt from Building Regulations',
											'identifier':'use_change_no_doc_details',
											'display_reliance':[{'identifier':'use_change_permissions', 'value':['0']}]
										}								
									]
								}													
							]
						},
						{
							'question_title':'(c) Installation of replacement windows, roof windows, roof lights, glazed doors since 1 April 2002',
							'identifier':'windows_replace',
							'input_type':'bool',
							'sub_questions':[
								{
									'input_type':'date',
									'question_title':'When did this occur?',
									'identifier':'windows_replace_date',
									'display_reliance':[{'identifier':'windows_replace', 'value':['1']}]
								},
								{
									'input_type':'bool',
									'question_title':'Were any planning permissions, Building Regulations approvals or Completion Certificates required?',
									'identifier':'windows_replace_permissions',
									'display_reliance':[{'identifier':'windows_replace', 'value':['1']}],
									'sub_questions':[
										{
											'input_type':'docu',
											'question_title':'Please supply copies of the planning permissions, Building Regulations approvals and Completion Certificates',
											'identifier':'windows_replace_docu',
											'display_reliance':[{'identifier':'windows_replace_permissions', 'value':['1']}],
										},
										{
											'input_type':'detail_text',
											'question_title':'If none were required, please explain why these were not required – e.g. permitted development rights applied or the work was exempt from Building Regulations',
											'identifier':'windows_replace_no_doc_details',
											'display_reliance':[{'identifier':'windows_replace_permissions', 'value':['0']}],
										}								
									]
								}													
							]
						},
						{
							'question_title':'(d) Addition of a conservatory',
							'identifier':'conservatory',
							'input_type':'bool',
							'sub_questions':[
								{
									'input_type':'date',
									'question_title':'When did this occur?',
									'identifier':'conservatory_date',
									'display_reliance':[{'identifier':'conservatory', 'value':['1']}]
								},
								{
									'input_type':'bool',
									'question_title':'Were any planning permissions, Building Regulations approvals or Completion Certificates required?',
									'identifier':'conservatory_permissions',
									'display_reliance':[{'identifier':'conservatory', 'value':['1']}],
									'sub_questions':[
										{
											'input_type':'docu',
											'question_title':'Please supply copies of the planning permissions, Building Regulations approvals and Completion Certificates',
											'identifier':'conservatory_docu',
											'display_reliance':[{'identifier':'conservatory_permissions', 'value':['1']}]
										},
										{
											'input_type':'detail_text',
											'question_title':'If none were required, please explain why these were not required – e.g. permitted development rights applied or the work was exempt from Building Regulations',
											'identifier':'conservatory_no_doc_details',
											'display_reliance':[{'identifier':'conservatory_permissions', 'value':['0']}]
										}								
									]
								}					
							]
						},																							
					]
				},
				{
					'question_title':'Are any of the works disclosed unfinished',
					'input_type':'bool',
					'identifier':'unfinished_works',
					'display_reliance':[
						{'identifier':'windows_replace', 'value':['1']},
						{'identifier':'conservatory', 'value':['1']},
						{'identifier':'use_change', 'value':['1']},
						{'identifier':'extensions_removals', 'value':['1']}
					],
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'give details such as when (if) the work will be finished',
							'identifier':'unfinished_works_detail',
							'display_reliance':[{'identifier':'unfinished_works', 'value':['1']}]
						}
					]
				},
				{
					'question_title':'Is the seller aware of any breaches of planning permission conditions or Building Regulations consent conditions, unfinished work or work that does not have all necessary consents?',
					'input_type':'bool',
					'identifier':'regulation_breaches',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'give details',
							'identifier':'regulation_breaches_detail',
							'display_reliance':[{'identifier':'regulation_breaches', 'value':['1']}]
						}
					]
				},
				{
					'question_title':' Are there any planning or building control issues to resolve?',
					'input_type':'bool',
					'identifier':'planning_or_control_issues',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'give details',
							'identifier':'planning_or_control_issues_detail',
							'display_reliance':[{'identifier':'planning_or_control_issues', 'value':['1']}]
						}
					]					
				},
				{
					'question_title':' Have solar panels been installed?',
					'input_type':'bool',
					'identifier':'solar_panels',
					'sub_questions':[
						{
							'input_type':'date',
							'question_title':'In what year were the solar panels installed?',
							'identifier':'solar_panels_install_year',
							'display_reliance':[{'identifier':'solar_panels', 'value':['1']}]
						},
						{
							'input_type':'bool',
							'question_title':'Are the solar panels owned outright?',
							'identifier':'solar_panels_ownership',
							'display_reliance':[{'identifier':'solar_panels', 'value':['1']}]
						},
						{
							'input_type':'bool',
							'question_title':'Has a long lease of the roof/air space been granted to a solar panel provider?',
							'identifier':'solar_panels_lease',
							'display_reliance':[{'identifier':'solar_panels', 'value':['1']}],
							'sub_questions':[
								{
									'question_title':'please supply copies of the relevant documents e.g. copies of electricity bills for feed in tariffs.',
									'identifier':'solar_panels_lease_docu',
									'display_reliance':[{'identifier':'solar_panels_lease', 'value':['1']}],
									'input_type':'docu'
								}
							]
						}												
					]	
				},
				{
					'question_title':' Is the property or any part of it a listed building?',
					'input_type':'bool_extra',
					'identifier':'listed_building',
					'radio_options':[{'radio_value':'not_known', 'radio_text':'Not Known'}],
					'sub_questions':[
						{
							'input_type':'docu',
							'question_title':'provide any relevant documents',
							'identifier':'listed_building_docu',
							'display_reliance':[{'identifier':'listed_building', 'value':['1']}]
						}
					]					
				},
				{
					'question_title':' Is the property or any part of it in a conservation area?',
					'input_type':'bool_extra',
					'identifier':'conservation_area',
					'radio_options':[{'radio_value':'not_known', 'radio_text':'Not Known'}],
					'sub_questions':[
						{
							'input_type':'docu',
							'question_title':'provide any relevant documents',
							'identifier':'conservation_area_docu',
							'display_reliance':[{'identifier':'conservation_area', 'value':['1']}]
						}
					]					
				},
				{
					'question_title':' are there any trees on the property',
					'input_type':'bool',
					'identifier':'trees',
					'sub_questions':[
						{
							'question_title':' Are any of the trees on the property subject to a Tree Preservation Order?',
							'input_type':'bool_extra',
							'identifier':'TPO',
							'radio_options':[{'radio_value':'not_known', 'radio_text':'Not Known'}],
							'display_reliance':[{'identifier':'trees', 'value':['1']}],
							'sub_questions':[
								{
									'input_type':'docu',
									'question_title':'provide any relevant documents',
									'identifier':'conservation_area_docu',
									'display_reliance':[{'identifier':'TPO', 'value':['1']}]
								},
								{
									'question_title':' Have the terms of the Order been complied with?',
									'input_type':'bool_extra',
									'identifier':'TPO',
									'radio_options':[{'radio_value':'not_known', 'radio_text':'Not Known'}],
									'display_reliance':[{'identifier':'TPO', 'value':['1']}],
								}								
							]					
						},
					]					
				}																								
			]
		},
		{
			"section_name":'Guarantees and warranties',
			'section_identifier':'garantees_and_warranties',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':' Does the property benefit from any of the following guarantees or warranties?',
					'question_set':'true',
					'identifier':'garantees_warranties',
					'sub_questions':[			
						{
							'question_title':' New home warranty (e.g. NHBC or similar)',
							'input_type':'bool',
							'identifier':'new_home_warranty',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'new_home_warranty_docu',
									'display_reliance':[{'identifier':'new_home_warranty', 'value':['1']}],									
								}
							]
						},
						{
							'question_title':'Damp proofing',
							'input_type':'bool',
							'identifier':'damp_proofing',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'damp_proofing_docu',
									'display_reliance':[{'identifier':'damp_proofing', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Timber Treatment',
							'input_type':'bool',
							'identifier':'timber_treatment',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'timber_treatment_docu',
									'display_reliance':[{'identifier':'timber_treatment', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Windows, roof lights, roof windows or glazed doors',
							'input_type':'bool',
							'identifier':'window_glazing_lights',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'window_glazing_lights_docu',
									'display_reliance':[{'identifier':'window_glazing_lights', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Electrical work',
							'input_type':'bool',
							'identifier':'electrical_work',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'electrical_work_docu',
									'display_reliance':[{'identifier':'electrical_work', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Roofing',
							'input_type':'bool',
							'identifier':'roofing',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'roofing_docu',
									'display_reliance':[{'identifier':'roofing', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Central heating',
							'input_type':'bool',
							'identifier':'central_heating',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'central_heating_docu',
									'display_reliance':[{'identifier':'central_heating', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Underpinning',
							'input_type':'bool',
							'identifier':'underpinning',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'underpinning_docu',
									'display_reliance':[{'identifier':'underpinning', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Other',
							'input_type':'bool',
							'identifier':'other_warranties',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'other_warranties_docu',
									'display_reliance':[{'identifier':'parent', 'value':['1']}],								
								},
								{
									'question_title':'provide details of these other warranties and garantees.',
									'input_type':'detail_text',
									'identifier':'other_warranties_details',
									'display_reliance':[{'identifier':'parent', 'value':['1']}],								
								}								

							]
						}																																													
					]
				},
				{
					'question_title':'Have any claims been made under any of these guarantees or warranties?',
					'identifier': 'garantees_warranties_claims',
					'input_type':'bool',
					'sub_questions':[
						{
							'question_title':'give details',
							'input_type':'detail_text',
							'identifier':'garantees_warranties_claims_detail',
							'display_reliance':[{'identifier':'garantees_warranties_claims', 'value':['1']}]
						}
					]
				},
			]
		},
		{
			"section_name":'Insurance',
			'section_identifier':'insurance',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Does the seller insure the property?',
					'input_type':'bool',
					'identifier':'property_insured_bool',
					'sub_questions':[
						{
							'question_title':'why does the seller not insure the property?',
							'input_type':'detail_text',
							'identifier':'why_not_insured',
							'display_reliance':[{'identifier':'property_insured_bool', 'value':['0']}]
						}
					]
				},
				{
					'question_title':'Has any buildings insurance taken out by the seller ever been subject to any of the following',
					'question_set':'true',
					'identifier':'insurance_events',
					'sub_questions':[
						{
							'question_title':'subject to an abnormal rise in premiums?',
							'input_type':'bool',
							'identifier':'abnormal_premiums',
							'sub_questions':[
								{
									'question_title':'give details of this abnormal premium',
									'identifier':'abnormal_premiums_detail',
									'input_type':'detail_text',
									'display_reliance':[{'identifier':'parent', 'value':['1']}]
								}
							]
						},
						{
							'question_title':'subject to high excesses?',
							'input_type':'bool',
							'identifier':'high_excess',
							'sub_questions':[
								{
									'question_title':'give details of this high excess',
									'identifier':'high_excess_detail',
									'input_type':'detail_text',
									'display_reliance':[{'identifier':'parent', 'value':['1']}]
								}
							]							
						},
						{
							'question_title':'subject to unusual conditions?',
							'input_type':'bool',
							'identifier':'unusual_conditions',
							'sub_questions':[
								{
									'question_title':'give details of these unusual conditions',
									'identifier':'unusual_conditions_detail',
									'input_type':'detail_text',
									'display_reliance':[{'identifier':'parent', 'value':['1']}]
								}
							]
						},																	
					]
				},
				{
					'question_title':'Has any building insurance ever been refused in regard to the property?',
					'input_type':'bool',
					'identifier':'refused_insurance',
					'sub_questions':[
								{
									'question_title':'give details of this refusal',
									'identifier':'refused_insurance_detail',
									'input_type':'detail_text',
									'display_reliance':[{'identifier':'parent', 'value':['1']}]
								}
							]
				},
				{
					'question_title':'Has the seller made any building insurance claims with regard to the property enclosed within the sale?',
					'input_type':'bool',
					'identifier':'insurance_claims',
					'sub_questions':[
								{
									'question_title':'give details of the claims',
									'identifier':'refused_insurance_detail',
									'input_type':'detail_text',
									'display_reliance':[{'identifier':'parent', 'value':['1']}]
								}
							]
				},					
			]
		},
		{
			"section_name":'Environmental matters',
			'section_identifier':'environmental_matters',
			'section_text':[
				'Flooding',
				'Flooding may take a variety of forms: it may be seasonal or irregular or simply a one-off occurrence. The property does not need to be near a sea or river for flooding to occur. Further information about flooding can be found at: www.gov.uk/government/organisations/department-for-environment-food-rural-affairs. The flood risk check can be found at: www.gov.uk/check-flood-risk.',
				'Read the law societys updated Flood Risk Practice Note at https://www.lawsociety.org.uk/support- services/advice/practice-notes/flood-risk/'
			],
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Has any part of the property (whether buildings or surrounding garden or land) ever been flooded?',
					'input_type':'bool',
					'identifier':'flooding_bool',
					'sub_questions':[
						{
							'question_title':'when did the flooding occur',
							'input_type':'date',
							'identifier':'flooding_date',
							'display_reliance':[{'identifier':'parent', 'value':['1']}]
						},
						{
							'question_title':'identify the parts that flooded',
							'input_type':'detail_text',
							'identifier':'flooding_detail',
							'display_reliance':[{'identifier':'parent', 'value':['1']}]
						},
						{
							'question_title':'What type of flooding occurred?',
							'question_set':'true',
							'identifier':'flood_type_set',
						}												
					]
				},
			]
		},
	]
	}




{
	"Form" : "TA6", 'form_identifier':'TA6',"Sections" : [
		{
			"section_name":'Boundaries',
			'section_identifier':'personal_details',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					"question_title":'Is the property boundary roughly regular e.g rectangular or square',
					'input_type':'bool',
					'identifier':'boundary_regular_bool'
				},
				{
					"question_title":'Looking towards the property from the road, who owns or accepts responsibility to maintain or repair the boundary features:',
					'question_set':'true',
					"identifier":"data_providers", 
					'multi_row_guidance':'for each person who enters data fill this section out seperatly',
					'display_reliance':[{'identifier':'boundary_regular_bool', 'value':['1']}],
					"sub_questions":[
						{
							'question_title':'(a) on the left?',
							'identifier':'left_bound',
							'input_type':'radio',
							'radio_options': [
	{'radio_text':'Seller', 'radio_value':'seller'},
	{'radio_text':'Neighbours', 'radio_value':'neighbours'},
	{'radio_text':'Shared', 'radio_value':'shared'},
	{'radio_text':'Not known', 'radio_value':'not_known'}
]
						},
						{
							'question_title':'(b) on the right?',
							'identifier':'left_bound',
							'input_type':'radio',
							'radio_options': [
	{'radio_text':'Seller', 'radio_value':'seller'},
	{'radio_text':'Neighbours', 'radio_value':'neighbours'},
	{'radio_text':'Shared', 'radio_value':'shared'},
	{'radio_text':'Not known', 'radio_value':'not_known'}
]
						},
						{
							'question_title':'(c) on the rear?',
							'identifier':'left_bound',
							'input_type':'radio',
							'radio_options': [
	{'radio_text':'Seller', 'radio_value':'seller'},
	{'radio_text':'Neighbours', 'radio_value':'neighbours'},
	{'radio_text':'Shared', 'radio_value':'shared'},
	{'radio_text':'Not known', 'radio_value':'not_known'}
]
						},
						{
							'question_title':'(d) on the front?',
							'identifier':'left_bound',
							'input_type':'radio',
							'radio_options': [
	{'radio_text':'Seller', 'radio_value':'seller'},
	{'radio_text':'Neighbours', 'radio_value':'neighbours'},
	{'radio_text':'Shared', 'radio_value':'shared'},
	{'radio_text':'Not known', 'radio_value':'not_known'}
]
						}																		
					],
				},
				{
					'question_title':'If the boundaries are irregular please indicate ownership by written description or by reference to a plan:',
					'identifier':'irregular_bounds_description',
					'input_type':'detail_text',
					'display_reliance':[{'identifier':'boundary_regular_bool', 'value':['1']}]
				},
				{
					'question_title':'Is the seller aware of any boundary feature having been moved in the last 10 years or during the seller’s period of ownership if longer?',
					'identifier':'moved_bound_features',
					'input_type':'radio',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'moved_bound_features_detail',
							'display_reliance':[{'identifier':'moved_bound_features', 'value':['1']}]
						}
					]
				},				
				{
					'question_title':'During the seller’s ownership, has any adjacent land or property been purchased by the seller? If Yes, please give details:',
					'identifier':'adjacent_land_purchase',
					'input_type':'detail_text',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'adjacent_land_purchase_detail',
							'display_reliance':[{'identifier':'adjacent_land_purchase', 'value':['1']}]
						}
					]
				},
				{
					'question_title':'Does any part of the property or any building on the property overhang, or project under, the boundary of the neighbouring property or road, for example cellars under the pavement, overhanging eaves or covered walkways',
					'identifier':'bound_overhang',
					'input_type':'detail_text',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'give details',
							'identifier':'bound_overhang_detail',
							'display_reliance':[{'identifier':'bound_overhang', 'value':['1']}]
						}
					]
				},
				{
					'question_title':'Has any notice been received under the Party Wall etc. Act 1996 in respect of any shared/party boundaries?',
					'identifier':'party_wall_bool',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'adjacent_land_purchase_detail',
							'display_reliance':[{'identifier':'party_wall_bool', 'value':['1']}]
						},
						{
							'input_type':'docu',
							'question_title':'please give detail',
							'identifier':'adjacent_land_purchase_detail',
							'display_reliance':[{'identifier':'party_wall_bool', 'value':['1']}]
						},						
					]
				},												
			]
		},
		{
			"section_name":'Disputes and complaints',
			'section_identifier':'disputes_and_complaints',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Have there been any disputes or complaints regarding this property or a property nearby?',
					'identifier':'dispute_or_complaint_bool',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'dispute_or_complaint_detail',
							'display_reliance':[{'identifier':'dispute_or_complaint_bool', 'value':['1']}]
						},					
					]
				},
				{
					'question_title':'Is the seller aware of anything which might lead to a dispute about the property or a property nearby?',
					'identifier':'cause_dispute_or_complaint_bool',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'cause_dispute_or_complaint_detail',
							'display_reliance':[{'identifier':'cause_dispute_or_complaint_bool', 'value':['1']}]
						},					
					]
				}				
			]
		},
		{
			"section_name":'Notices and proposals',
			'section_identifier':'notices_and_proposals',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Have any notices or correspondence been received or sent (e.g. from or to a neighbour, council or government department), or any negotiations or discussions taken place, which affect the property or a property nearby?',
					'identifier':'correspondence',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'correspondence_detail',
							'display_reliance':[{'identifier':'correspondence', 'value':['1']}]
						},					
					]
				},
				{
					'question_title':'Is the seller aware of any proposals to develop property or land nearby, or of any proposals to make alterations to buildings nearby?',
					'identifier':'develop_proposals',
					'input_type':'bool',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'please give details',
							'identifier':'develop_proposals_detail',
							'display_reliance':[{'identifier':'develop_proposals', 'value':['1']}]
						},					
					]
				},				
			]
		},
		{
			"section_name":'Alterations, planning and building control',
			'section_identifier':'planning_and_control',
			'section_text':[
				'Note to seller: All relevant approvals and supporting paperwork referred to in section 4 of this form, such as listed building consents, planning permissions, Building Regulations consents and completion certificates should be provided. If the seller has had works carried out the seller should produce the documentation authorising this. Copies may be obtained from the relevant local authority website. Competent Persons Certificates may be obtained from the contractor or the scheme provider (e.g. FENSA or Gas Safe Register). Further information about Competent Persons Certificates can be found at: https://www.gov.uk/guidance/competent-person- scheme-current-schemes-and-how-schemes-are-authorised',
				'Note to buyer: If any alterations or improvements have been made since the property was last valued for council tax, the sale of the property may trigger a revaluation. This may mean that following completion of the sale, the property will be put into a higher council tax band. Further information about council tax valuation can be found at: http://www.gov.uk/government/organisations/valuation-office-agency'
			],
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Have any of the following changes been made to the whole or any part of the property (including the garden)?',
					'question_set':'true',
					'identifier':'changes',
					'sub_questions':[
				
						{
							'question_title':'(a) Building works (e.g. extension, loft or garage conversion, removal of internal walls). If Yes, please give details including dates of all work undertaken:',
							'identifier':'extensions_removals',
							'input_type':'bool',
							'sub_questions':[
								{
									'input_type':'detail_text',
									'question_title':'please give details including dates of all work undertaken',
									'identifier':'extensions_removals_detail',
									'display_reliance':[{'identifier':'parent', 'value':['1']}],
								},
								{
									'input_type':'bool',
									'question_title':'Were any planning permissions, Building Regulations approvals or Completion Certificates required?',
									'identifier':'extensions_removals_permissions',
									'display_reliance':[{'identifier':'extensions_removals', 'value':['1']}],
									'sub_questions':[
										{
											'input_type':'docu',
											'question_title':'please supply copies of the planning permissions, Building Regulations approvals and Completion Certificates',
											'identifier':'extensions_removals_docu',
											'display_reliance':[{'identifier':'extensions_removals_permissions', 'value':['1']}],
										},
										{
											'input_type':'detail_text',
											'question_title':'f none were required, please explain why these were not required – e.g. permitted development rights applied or the work was exempt from Building Regulations',
											'identifier':'extensions_removals_no_doc_details',
											'display_reliance':[{'identifier':'extensions_removals_permissions', 'value':['0']}],
										}								
									]
								},													
							]
						},
						{
							'question_title':'(b) Change of use (e.g. from an office to a residence)',
							'identifier':'use_change',
							'input_type':'bool',
							'sub_questions':[
								{
									'input_type':'date',
									'question_title':'When did this occur?',
									'identifier':'use_change_date',
									'display_reliance':[{'identifier':'use_change', 'value':['1']}],
								},
								{
									'input_type':'bool',
									'question_title':'Were any planning permissions, Building Regulations approvals or Completion Certificates required?',
									'identifier':'use_change_permissions',
									'display_reliance':[{'identifier':'use_change', 'value':['1']}],
									'sub_questions':[
										{
											'input_type':'docu',
											'question_title':'Please supply copies of the planning permissions, Building Regulations approvals and Completion Certificates',
											'identifier':'use_change_docu',
											'display_reliance':[{'identifier':'use_change_permissions', 'value':['1']}],
										},
										{
											'input_type':'detail_text',
											'question_title':'If none were required, please explain why these were not required – e.g. permitted development rights applied or the work was exempt from Building Regulations',
											'identifier':'use_change_no_doc_details',
											'display_reliance':[{'identifier':'use_change_permissions', 'value':['0']}]
										}								
									]
								}													
							]
						},
						{
							'question_title':'(c) Installation of replacement windows, roof windows, roof lights, glazed doors since 1 April 2002',
							'identifier':'windows_replace',
							'input_type':'bool',
							'sub_questions':[
								{
									'input_type':'date',
									'question_title':'When did this occur?',
									'identifier':'windows_replace_date',
									'display_reliance':[{'identifier':'windows_replace', 'value':['1']}]
								},
								{
									'input_type':'bool',
									'question_title':'Were any planning permissions, Building Regulations approvals or Completion Certificates required?',
									'identifier':'windows_replace_permissions',
									'display_reliance':[{'identifier':'windows_replace', 'value':['1']}],
									'sub_questions':[
										{
											'input_type':'docu',
											'question_title':'Please supply copies of the planning permissions, Building Regulations approvals and Completion Certificates',
											'identifier':'windows_replace_docu',
											'display_reliance':[{'identifier':'windows_replace_permissions', 'value':['1']}],
										},
										{
											'input_type':'detail_text',
											'question_title':'If none were required, please explain why these were not required – e.g. permitted development rights applied or the work was exempt from Building Regulations',
											'identifier':'windows_replace_no_doc_details',
											'display_reliance':[{'identifier':'windows_replace_permissions', 'value':['0']}],
										}								
									]
								}													
							]
						},
						{
							'question_title':'(d) Addition of a conservatory',
							'identifier':'conservatory',
							'input_type':'bool',
							'sub_questions':[
								{
									'input_type':'date',
									'question_title':'When did this occur?',
									'identifier':'conservatory_date',
									'display_reliance':[{'identifier':'conservatory', 'value':['1']}]
								},
								{
									'input_type':'bool',
									'question_title':'Were any planning permissions, Building Regulations approvals or Completion Certificates required?',
									'identifier':'conservatory_permissions',
									'display_reliance':[{'identifier':'conservatory', 'value':['1']}],
									'sub_questions':[
										{
											'input_type':'docu',
											'question_title':'Please supply copies of the planning permissions, Building Regulations approvals and Completion Certificates',
											'identifier':'conservatory_docu',
											'display_reliance':[{'identifier':'conservatory_permissions', 'value':['1']}]
										},
										{
											'input_type':'detail_text',
											'question_title':'If none were required, please explain why these were not required – e.g. permitted development rights applied or the work was exempt from Building Regulations',
											'identifier':'conservatory_no_doc_details',
											'display_reliance':[{'identifier':'conservatory_permissions', 'value':['0']}]
										}								
									]
								}					
							]
						},																							
					]
				},
				{
					'question_title':'Are any of the works disclosed unfinished',
					'input_type':'bool',
					'identifier':'unfinished_works',
					'display_reliance':[
						{'identifier':'windows_replace', 'value':['1']},
						{'identifier':'conservatory', 'value':['1']},
						{'identifier':'use_change', 'value':['1']},
						{'identifier':'extensions_removals', 'value':['1']}
					],
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'give details such as when (if) the work will be finished',
							'identifier':'unfinished_works_detail',
							'display_reliance':[{'identifier':'unfinished_works', 'value':['1']}]
						}
					]
				},
				{
					'question_title':'Is the seller aware of any breaches of planning permission conditions or Building Regulations consent conditions, unfinished work or work that does not have all necessary consents?',
					'input_type':'bool',
					'identifier':'regulation_breaches',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'give details',
							'identifier':'regulation_breaches_detail',
							'display_reliance':[{'identifier':'regulation_breaches', 'value':['1']}]
						}
					]
				},
				{
					'question_title':' Are there any planning or building control issues to resolve?',
					'input_type':'bool',
					'identifier':'planning_or_control_issues',
					'sub_questions':[
						{
							'input_type':'detail_text',
							'question_title':'give details',
							'identifier':'planning_or_control_issues_detail',
							'display_reliance':[{'identifier':'planning_or_control_issues', 'value':['1']}]
						}
					]					
				},
				{
					'question_title':' Have solar panels been installed?',
					'input_type':'bool',
					'identifier':'solar_panels',
					'sub_questions':[
						{
							'input_type':'date',
							'question_title':'In what year were the solar panels installed?',
							'identifier':'solar_panels_install_year',
							'display_reliance':[{'identifier':'solar_panels', 'value':['1']}]
						},
						{
							'input_type':'bool',
							'question_title':'Are the solar panels owned outright?',
							'identifier':'solar_panels_ownership',
							'display_reliance':[{'identifier':'solar_panels', 'value':['1']}]
						},
						{
							'input_type':'bool',
							'question_title':'Has a long lease of the roof/air space been granted to a solar panel provider?',
							'identifier':'solar_panels_lease',
							'display_reliance':[{'identifier':'solar_panels', 'value':['1']}],
							'sub_questions':[
								{
									'question_title':'please supply copies of the relevant documents e.g. copies of electricity bills for feed in tariffs.',
									'identifier':'solar_panels_lease_docu',
									'display_reliance':[{'identifier':'solar_panels_lease', 'value':['1']}],
									'input_type':'docu'
								}
							]
						}												
					]	
				},
				{
					'question_title':' Is the property or any part of it a listed building?',
					'input_type':'bool_extra',
					'identifier':'listed_building',
					'radio_options':[{'radio_value':'not_known', 'radio_text':'Not Known'}],
					'sub_questions':[
						{
							'input_type':'docu',
							'question_title':'provide any relevant documents',
							'identifier':'listed_building_docu',
							'display_reliance':[{'identifier':'listed_building', 'value':['1']}]
						}
					]					
				},
				{
					'question_title':' Is the property or any part of it in a conservation area?',
					'input_type':'bool_extra',
					'identifier':'conservation_area',
					'radio_options':[{'radio_value':'not_known', 'radio_text':'Not Known'}],
					'sub_questions':[
						{
							'input_type':'docu',
							'question_title':'provide any relevant documents',
							'identifier':'conservation_area_docu',
							'display_reliance':[{'identifier':'conservation_area', 'value':['1']}]
						}
					]					
				},
				{
					'question_title':' are there any trees on the property',
					'input_type':'bool',
					'identifier':'trees',
					'sub_questions':[
						{
							'question_title':' Are any of the trees on the property subject to a Tree Preservation Order?',
							'input_type':'bool_extra',
							'identifier':'TPO',
							'radio_options':[{'radio_value':'not_known', 'radio_text':'Not Known'}],
							'display_reliance':[{'identifier':'trees', 'value':['1']}],
							'sub_questions':[
								{
									'input_type':'docu',
									'question_title':'provide any relevant documents',
									'identifier':'conservation_area_docu',
									'display_reliance':[{'identifier':'TPO', 'value':['1']}]
								},
								{
									'question_title':' Have the terms of the Order been complied with?',
									'input_type':'bool_extra',
									'identifier':'TPO',
									'radio_options':[{'radio_value':'not_known', 'radio_text':'Not Known'}],
									'display_reliance':[{'identifier':'TPO', 'value':['1']}],
								}								
							]					
						},
					]					
				}																								
			]
		},
		{
			"section_name":'Guarantees and warranties',
			'section_identifier':'garantees_and_warranties',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':' Does the property benefit from any of the following guarantees or warranties?',
					'question_set':'true',
					'identifier':'garantees_warranties',
					'sub_questions':[			
						{
							'question_title':' New home warranty (e.g. NHBC or similar)',
							'input_type':'bool',
							'identifier':'new_home_warranty',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'new_home_warranty_docu',
									'display_reliance':[{'identifier':'new_home_warranty', 'value':['1']}],									
								}
							]
						},
						{
							'question_title':'Damp proofing',
							'input_type':'bool',
							'identifier':'damp_proofing',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'damp_proofing_docu',
									'display_reliance':[{'identifier':'damp_proofing', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Timber Treatment',
							'input_type':'bool',
							'identifier':'timber_treatment',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'timber_treatment_docu',
									'display_reliance':[{'identifier':'timber_treatment', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Windows, roof lights, roof windows or glazed doors',
							'input_type':'bool',
							'identifier':'window_glazing_lights',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'window_glazing_lights_docu',
									'display_reliance':[{'identifier':'window_glazing_lights', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Electrical work',
							'input_type':'bool',
							'identifier':'electrical_work',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'electrical_work_docu',
									'display_reliance':[{'identifier':'electrical_work', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Roofing',
							'input_type':'bool',
							'identifier':'roofing',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'roofing_docu',
									'display_reliance':[{'identifier':'roofing', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Central heating',
							'input_type':'bool',
							'identifier':'central_heating',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'central_heating_docu',
									'display_reliance':[{'identifier':'central_heating', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Underpinning',
							'input_type':'bool',
							'identifier':'underpinning',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'underpinning_docu',
									'display_reliance':[{'identifier':'underpinning', 'value':['1']}],								
								}

							]
						},
						{
							'question_title':'Other',
							'input_type':'bool',
							'identifier':'other_warranties',
							'sub_questions':[
								{
									'question_title':'please supply a copy.',
									'input_type':'docu',
									'identifier':'other_warranties_docu',
									'display_reliance':[{'identifier':'other_warranties', 'value':['1']}],								
								},
								{
									'question_title':'provide details of these other warranties and garantees.',
									'input_type':'detail_text',
									'identifier':'other_warranties_docu',
									'display_reliance':[{'identifier':'other_warranties', 'value':['1']}],								
								}								

							]
						}																																													
					]
				},
				{
					'question_title':'Have any claims been made under any of these guarantees or warranties?',
					'identifier': 'garantees_warranties_claims',
					'input_type':'bool',
					'sub_questions':[
						{
							'question_title':'give details',
							'input_type':'detail_text',
							'identifier':'garantees_warranties_claims_detail',
							'display_reliance':[{'identifier':'garantees_warranties_claims', 'value':['1']}]
						}
					]
				},
			]
		},
		{
			"section_name":'Insurance',
			'section_identifier':'insurance',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Does the seller insure the property?',
					'input_type':'bool',
					'identifier':'property_insured_bool',
					'sub_questions':[
						{
							'question_title':'why does the seller not insure the property?',
							'input_type':'detail_text',
							'identifier':'why_not_insured',
							'display_reliance':[{'identifier':'property_insured_bool', 'value':['0']}]
						}
					]
				},
				{
					'question_title':'Has any buildings insurance taken out by the seller ever been subject to any of the following',
					'question_set':'true',
					'identifier':'insurance_events',
					'sub_questions':[
						{
							'question_title':'subject to an abnormal rise in premiums?',
							'input_type':'bool',
							'identifier':'abnormal_premiums',
							'sub_questions':[
								{
									'question_title':'give details of this abnormal premium',
									'identifier':'abnormal_premiums_detail',
									'input_type':'detail_text',
									'display_reliance':[{'identifier':'parent', 'value':['1']}]
								}
							]
						},
						{
							'question_title':'subject to high excesses?',
							'input_type':'bool',
							'identifier':'high_excess',
							'sub_questions':[
								{
									'question_title':'give details of this high excess',
									'identifier':'high_excess_detail',
									'input_type':'detail_text',
									'display_reliance':[{'identifier':'parent', 'value':['1']}]
								}
							]							
						},
						{
							'question_title':'subject to unusual conditions?',
							'input_type':'bool',
							'identifier':'unusual_conditions',
							'sub_questions':[
								{
									'question_title':'give details of these unusual conditions',
									'identifier':'unusual_conditions_detail',
									'input_type':'detail_text',
									'display_reliance':[{'identifier':'parent', 'value':['1']}]
								}
							]
						},																	
					]
				},
				{
					'question_title':'Has any building insurance ever been refused in regard to the property?',
					'input_type':'bool',
					'identifier':'refused_insurance',
					'sub_questions':[
								{
									'question_title':'give details of this refusal',
									'identifier':'refused_insurance_detail',
									'input_type':'detail_text',
									'display_reliance':[{'identifier':'parent', 'value':['1']}]
								}
							]
				},
				{
					'question_title':'Has the seller made any building insurance claims with regard to the property enclosed within the sale?',
					'input_type':'bool',
					'identifier':'insurance_claims',
					'sub_questions':[
								{
									'question_title':'give details of the claims',
									'identifier':'refused_insurance_detail',
									'input_type':'detail_text',
									'display_reliance':[{'identifier':'parent', 'value':['1']}]
								}
							]
				},					
			]
		},
		{
			"section_name":'Environmental matters',
			'section_identifier':'environmental_matters',
			'section_text':[
				'Flooding',
				'Flooding may take a variety of forms: it may be seasonal or irregular or simply a one-off occurrence. The property does not need to be near a sea or river for flooding to occur. Further information about flooding can be found at: www.gov.uk/government/organisations/department-for-environment-food-rural-affairs. The flood risk check can be found at: www.gov.uk/check-flood-risk.',
				'Read the law societys updated Flood Risk Practice Note at https://www.lawsociety.org.uk/support- services/advice/practice-notes/flood-risk/'
			],
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Has any part of the property (whether buildings or surrounding garden or land) ever been flooded?',
					'input_type':'bool',
					'identifier':'flooding_bool',
					'sub_questions':[
						{
							'question_title':'when did the flooding occur',
							'input_type':'date',
							'identifier':'flooding_date',
							'display_reliance':[{'identifier':'parent', 'value':['1']}]
						},
						{
							'question_title':'identify the parts that flooded',
							'input_type':'detail_text',
							'identifier':'flooding_detail',
							'display_reliance':[{'identifier':'parent', 'value':['1']}]
						},
						{
							'question_title':'What type of flooding occurred?',
							'question_set':'true',
							'identifier':'flood_type_set',
							'display_reliance':[{'identifier':'parent', 'value':['1']}],
							'sub_questions':[
								{
									'question_title':'ground_water',
									'identifier':'ground_water_flooding',
									'input_type':'checkbox'
								}
							]
						},
						{
							'question_title':'Has a Flood Risk Report been prepared?',
							'input_type':'bool',
							'identifier':'flood_risk_report_bool',
							'display_reliance':[{'identifier':'parent', 'value':['1']}],
						}											
					]
				},
				{
					'question_title':'Radon',
					'identifier':'radon_set',
					'question_set':'true',
					'other_question_text':['Radon is a naturally occurring inert radioactive gas found in the ground. Some parts of England and Wales are more adversely affected by it than others. Remedial action is advised for properties with a test result above the ‘recommended action level',
						'Further information about Radon can be found at: www.gov.uk/government/organisations/public-health-england and www.publichealthwales.wales.nhs.uk.'],
					'sub_questions':[
						{
							'question_title':'Has a Radon test been carried out on the property?',
							'identifier':'radon_test_bool',
							'input_type':'bool',
							'sub_questions':[
								{
									'question_title':'please supply a copy of the report?',
									'input_type':'docu',
									'identifier':'radon_test_docu',
									'display_reliance':[{'identifier':'parent', 'value':['1']}],
								},
								{
									'question_title':'was the test result below the ‘recommended action level’?',
									'input_type':'bool',
									'identifier':'radon_action_level_bool',
									'display_reliance':[{'identifier':'parent', 'value':['1']}],
								},

							]

						},
						{
							'question_title':'Were any remedial measures undertaken on construction to reduce Radon gas levels in the property?',
							'input_type':'bool',
							'identifier':'radon_remedial_action_bool',
						},
					]
				},
				{
					'question_title':'Energy efficiency',
					'identifier':'energy_efficiency_set',
					'question_set':'true',
					'other_question_text':['An Energy Performance Certificate (EPC) is a document that gives information about a property’s energy usage',
						'Further information about EPCs can be found at: https://www.gov.uk/buy-sell-your-home/energy-performance-certificates'],
					'sub_questions':[
						{
							'question_title':'Please supply a copy of the EPC for the property.',
							'identifier':'epc_docu',
							'input_type':'docu',
						},
						{
							'question_title':'Have any installations in the property been financed under the Green Deal scheme?',
							'identifier':'green_deal_bool',
							'input_type':'bool',
							'sub_questions':[
								{
									'input_type':'detail_text',
									'question_title':'Give details of all installations in or on the property financed under the Green Deal scheme',
									'identifier':'green_deal_details',
									'display_reliance':[{'identifier':'parent', 'value':['1']}],
								},
								{
									'input_type':'docu',
									'identifier':'last_electricity_bill',
									'question_title':'Please provide a copy of your last electricity bill',
									'display_reliance':[{'identifier':'parent', 'value':['1']}],									
								}
							]
						}						
					]				
				},
				{
					'question_title':'Japanese knotweed',
					'identifier':'Japanese_knotweed_set',
					'question_set':'true',
					'other_question_text':['Japanese knotweed is an invasive non-native plant that can cause damage to property if left untreated. The plant consists of visible above ground growth and an invisible rhizome (root) below ground in the soil. It can take several years to control and manage through a management and treatment plan and rhizomes may remain alive below the soil even after treatment.'],
					'sub_questions':[
						{
							'input_type':'bool_extra',
							'question_title':'Is the property affected by Japanese knotweed?',
							'identifier':'Japanese_knotweed_bool',
							'display_reliance':[{'identifier':'parent', 'value':['yes']}],									
							'radio_options':[{'radio_value':'not_known', 'radio_text':'Not Known'}],
							'sub_questions':[
								{
									'input_type':'bool',
									'question_title':'Is there a Japanese knotweed management and treatment plan in place',
									'identifier':'knotweed_manage_plan_bool',
								},
								{
									'question_set':'true',
									'identifier':'knotweed_plan_set',
									'display_reliance':[{'identifier':'parent', 'value':['1']}],
									'sub_questions':[
										{
											'identifier':'knotweed_plan_copy',
											'input_type':'docu',
											'question_title':'Supply a copy of the Japanese knotweed management and treatment plan',
										},
										{
											'identifier':'knotweed_plan_insurance',
											'input_type':'docu',
											'question_title':'Supply a copy of any insurance cover linked to Japanese knotweed management and treatment plan',
										}
									]
								}
							]
						}
					]				
				},
			]
		},
	{
		"section_name":'Rights and informal arrangements',
		'section_identifier':'rights_and_arrangements',
		'section_text':['Rights and arrangements may relate to access or shared use. They may also include leases of less than seven years, rights to mines and minerals, manorial rights, chancel repair and similar matters. If you are uncertain about whether a right or arrangement is covered by this question, please ask your solicitor.'],
		'main_questions':[
			{
				'input_type':'multi_row',
				'identifier':'cost_contribute_services',
				'question_title':'Does ownership of the property carry a responsibility to contribute towards the cost of any jointly used services, such as maintenance of a private road, a shared driveway, a boundary or drain?',
				'sub_questions':[
					{
						'identifier':'object_of_maintenance',
						'question_title':'What is the Jointly used service which ownership of the property confers the responsibility to maintain?',
						'input_type':'radio',
						'radio_options':[
							{'radio_text':'private road', 'radio_value':'private_road'},
							{'radio_text':'shared driveway','radio_value':'shared_driveway'},
							{'radio_text':'boundary','radio_value':'boundary'},
							{'radio_text':'drain','radio_value':'drain'},
							{'radio_text':'other service' ,'radio_value': 'other_service'}							
						],
						'sub_questions':[
							{
								'identifier':'other_service_details',
								'input_type':'detail_text',
								"question_title":"Please describe the 'other' service that the property carries a responsibility to maintain",
								'display_reliance':[{'identifier':'parent', 'value':['1']}],
							},							
						]
					},
					{
						'identifier':'service_maintenance_details',
						'question_title':'Provie details of this maintenance responsibility',
						'input_type':'detail_text',
					}					
				]
			},
			{
				'input_type':'bool',
				'question_title':' Does the property benefit from any rights or arrangements over any neighbouring property (this includes any rights of way)?',
				'identifier':'rights_or_arrangements_bool',
				'sub_questions':[
					{
						'input_type':'detail_text',
						'question_title':'provide details of the right or arrangement over a neighbouring property that the property benefits from.',
						'identifier':'rights_or_arrangements_detail',
						'display_reliance':[{'identifier':'parent', 'value':['1']}],
					}
				]
			},
			{
				'input_type':'bool',
				'question_title':' Has anyone taken steps to prevent access to the property, or to complain about or demand payment for access to the property?',
				'identifier':'prevent_access_bool',
				'sub_questions':[
					{
						'input_type':'detail_text',
						'question_title':'provide details of the steps taken to prevent access or the money demanded to allow access to the property',
						'identifier':'prevent_access_detail',
						'display_reliance':[{'identifier':'parent', 'value':['1']}],
					}
				]
			},
			{
				'question_set':'true',
				'identifier':'rights_cheackbox',
				'question_title':'Does the seller know if any of the following rights benefit the property:',
				'sub_questions':[
					{
						'input_type':'checkbox',
						'question_title':'Rights of light',
						'identifier':'right_of_light',
						'sub_questions':[
							{
								'input_type':'detail_text',
								'question_title':'provide any known details of the right of light',
								'identifier':'right_of_light_details',
								'display_reliance':[{'identifier':'right_of_light','value':['checked']}]
							}
						]
					},
					{
						'input_type':'checkbox',
						'question_title':'Rights of support from adjoining properties',
						'identifier':'right_of_support',
						'sub_questions':[
							{
								'input_type':'detail_text',
								'question_title':'provide any known details of the right of support',
								'identifier':'right_of_support_details',
								'display_reliance':[{'identifier':'right_of_support','value':['checked']}]
							}
						]						
					},
					{
						'input_type':'checkbox',
						'question_title':'Customary rights (e.g. rights deriving from local traditions)',
						'identifier':'customary_rights',
						'sub_questions':[
							{
								'input_type':'detail_text',
								'question_title':'provide any known details of the customary right(s)',
								'identifier':'customary_rights_details',
								'display_reliance':[{'identifier':'customary_rights','value':['checked']}],
							}
						]												
					},										
				]
			},
			{
				'question_set':'true',
				'identifier':'rights_cheackbox',
				'question_title':'Does the seller know if any of the following arrangements affect the property:',
				'sub_questions':[
					{
						'input_type':'checkbox',
						'question_title':'Other people’s rights to mines and minerals under the land',
						'identifier':'mineral_rights',
						'sub_questions':[
							{
								'input_type':'detail_text',
								'question_title':'provide any known details of the mineral or extraction rights',
								'identifier':'mineral_rights_details',
								'display_reliance':[{'identifier':'mineral_rights','value':['checked']}]
							}
						]						
					},						
					{
						'input_type':'checkbox',
						'question_title':'Chancel repair liability',
						'identifier':'chancel_repair',
						'sub_questions':[
							{
								'input_type':'detail_text',
								'question_title':'provide any known details of the chancel repair obligation',
								'identifier':'chancel_repair_details',
								'display_reliance':[{'identifier':'chancel_repair','value':['checked']}]
							}
						]						
					},
					{
						'input_type':'checkbox',
						'question_title':'Other people’s rights to take things from the land (such as timber, hay or fish)',
						'identifier':'extract_rights',
						'sub_questions':[
							{
								'input_type':'detail_text',
								'question_title':'provide any known details of the right to certain products of the land or property',
								'identifier':'extract_rights_details',
								'display_reliance':[{'identifier':'extract_rights','value':['checked']}]
							}
						]						
					},										
				]
			},
			{
				'input_type':'bool',
				'question_title':'Are there any other rights or arrangements affecting the property? This includes any rights of way.',
				'identifier':'other_rights',
				'sub_questions':[
					{
						'input_type':'detail_text',
						'question_title':'provide any known details of the other rights affecting the property',
						'identifier':'other_rights_details',
						'display_reliance':[{'identifier':'other_rights','value':['1']}]
					}
				]						
			},
																	
		]
	},
	{
		"section_name":'Services crossing the property or neighbouring property',
		'section_identifier':'crossing_services',
		'main_questions':[
			{
				'question_title':'Do any drains, pipes or wires serving the property cross any neighbour’s property?',
				'input_type':'bool_extra',
				'radio_options':not_known,
				'identifier':'neighbour_conduits'
			},
			{
				'question_title':'Do any drains, pipes or wires leading to any neighbour’s property cross the property?',
				'input_type':'bool_extra',
				'radio_options':not_known,
				'identifier':'conduits_to_neighbour'
			},
			{
				'question_title':'Is there any agreement or arrangement about drains, pipes or wires?',
				'input_type':'bool_extra',
				'radio_options':not_known,
				'identifier':'conduit_agreements',
				'sub_questions':[
					{
						'input_type':'detail_text',
						'display_reliance':[{'identifier':'parent','value':['1']}],
						'question_title':'give details',
						'identifier':'conduit_details'
					},
					{
						'input_type':'docu',
						'display_reliance':[{'identifier':'parent','value':['1']}],
						'question_title':'provide any relevant documentation',
						'identifier':'conduit_docs'
					}					
				]
			},						
		]
	},
	{
		"section_name":'Parking',
		'section_identifier':'parking',
		'main_questions':[
			{
				'input_type':'detail_text',
				'identifier':'parking_arrangements',
				'question_title':'What are the parking arrangements at the property?'
			},
			{
				'identifier':'controlled_parking',
				'input_type':'bool_extra',
				'radio_options':not_known,
			}
		]
	},
	{
		"section_name":'Other charges',
		'section_identifier':'other_charges',
		'section_text':['If the property is leasehold, details of lease expenses such as service charges and ground rent should be set out on the separate TA7 Leasehold Information Form. If the property is freehold, there may still be charges: for example, payments to a management company or for the use of a private drainage system.'],
		'main_questions':[
			{
				'input_type':'bool',
				'identifier':'extra_charges_bool',
				'question_title':'Doesthesellerhavetopayanychargesrelatingto the property (excluding any payments such as council tax, utility charges, etc.), for example payments to a management company?',
				'sub_questions':[
					{
						'input_type':'detail_text',
						'identifier':'extra_charges_detail',
						'question_title':'provide details of the extra charges',
					}
				]
			},
			{
				'identifier':'controlled_parking',
				'input_type':'bool_extra',
				'radio_options':not_known,
			},
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
		'section_name':'Services',
		'section_identifier':'services',
		'section_text':['If the seller does not have a certificate requested below this can be obtained from the relevant Competent Persons Scheme. Further information about Competent Persons Schemes can be found at: https://www.gov.uk/guidance/competent-person-scheme-current-schemes- and-how-schemes-are-authorised'],
		"main_questions":[
			{

			}
		]
	}		
]

}







