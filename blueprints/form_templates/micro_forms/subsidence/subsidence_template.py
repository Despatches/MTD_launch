template = {
'form_identifier':'subsidence',
"Form":'Subsidence',
'Sections':[
		{
			'section_name':'Subsidence and remedial works',
			'section_identifier':'susidence_and_remedial',
			'main_questions':[
				{
					'question_title':'Has any component of this property ever suffered from subsidence?',
					#Has any property contained in this title ever suffered from subsidence?
					'input_type':'bool_extra',
					'identifier':'ever_susidence',
					'radio_options':[{'radio_value':'not_known','radio_text':'Not Known'}],
					'sub_questions':[
						{
							'question_set':'true',
							'identifier':'subsidence_suffered',
							'display_reliance':[{'identifier':'parent','value':['1']}],
							'sub_questions':[
								{
									'question_title':'What areas of the property were effected by the subsidence?',
									'input_type':'detail_text',
									'identifier':'subsidence_areas_detail',
								},
								{
									"question_title": "Has any work been undertaken to remedy the subsidence?",
									"identifier":"remedy_subsidence", 
									"input_type":"bool",
									'sub_questions':[
										{
											'question_title':'Provide details on any of subsidence remedies undertaken.',
											'object_type':'Subsidence Remedy',
											'identifier':'undertaken_remedies',
											'input_type':'multi_row',
											'display_reliance':[{'identifier':'parent','value':['1']}],
											'sub_questions':[								
												{
													'question_title':'Were the works to remedy subsidence undertaken by an accredited contractor?',
													'other_question_text':[], #list of peoples that would be considered accredited contractors for this purpose
													'input_type':'bool',
													'identifier':'accredited_contractor_remedy',
												},
												{
													'question_title':'Was the subsidence remedy covered by an insurance policy?',
													'input_type':'bool',
													'identifier':'prior_subsidence_insured_remedy',
													'sub_questions':[
														{
															'question_title':'Confirm details of the prior subsidence repair including: date, values, extent of damage/repair.',
															'identifier':'prior_remedy_detail',
															'input_type':'detail_text',
															'display_reliance':[{'identifier':'parent','value':['1']}],
														},
														{
															'question_title':'Was the subsidence remedy schedule of works covered by any insurance backed warranty or guarantee?',
															'identifier':'warranty_guarantee',
															'input_type':'bool',
															'display_reliance':[{'identifier':'parent','value':['1']}],
														}
													]
												},
											]
										},
									]
								},
							]
						},

					]
				},
			]
		},
		{
			'section_name':'Building Movement',
			'section_identifier':'building_movement',
			'main_questions':[
				{
					'question_title':'Have there been any signs of building movement,subsequent to any subsidence remedies if any were undertaken,: such as cracks in walls or ceilings?',
					'input_type':'multi_row',
					'identifier':'building_movement_indicators',
					'sub_questions':[
					# This is a bool question ;  either "provide detils where any ... have been concealed ... "  or change answer to bool
						{
							'question_title':'Have any sign of building movement (such as cracks to ceilings or walls) been covered by redecoration during your ownership?',
							'identifier':'building_movement_consealed',
							'input_type':'text',
						},
						{
							'question_title':'Has any Underwriter ever imposed additional premiums or exclusions to any buildings insurance policy in relation to subsidence risks?',
							'identifier':'insurance_special_terms',
							'input_type':'bool',
						},
						{
							'question_title':'Has the prior subsidence damage been declare to underwriters when obtaining buildings insurance protection?',
							'display_reliance':[{'identifier':'insurance_special_terms','value':['0']}],
							'identifier':'subsidence_insurance_declaration',
							'input_type':'text',
						},
					]
				}
			]
		}
	]
}