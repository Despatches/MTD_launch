template={
'form_identifier':'attic',
'form_name':'Loft Evaluation',
'Sections':[
	{
		'Section_name':'loft_conversion_prospect',
		'section_identifier':'loft_prospect',
		'main_questions':[
			{	
				'question_title':'Does the property contain a loft, attic or any eves areas not presenty forming part of the habitable area?',
				'input_type':'bool',
				'identifier':'contain_attic',
			},
			{
				'question_title':'Has a design for conversion utilising loft or eaves space or the creation of a roof adaptation been prepared?',
				'input_type':'bool_extra',
				'identifier':'util',
				'radio_options':[{'radio_value':'not_known','radio_text':'Not Known'}],
				'sub_questions':[
					{
						'question_title':'Is there any future consideration or intent to create a habitable space utilising a loft or eaves space?',
						'input_type':'bool',
						'display_reliance':[{'identifier':'parent','display_value':['0']}],
						'identifier':'loft_creation_intent',
					},
					{
						'question_title':'Has any work previously been undertaken to create a new loft or enlargement of an existing subterranian space?',
						'input_type':'bool',
						'identifier':'previous_loft_enlargement',
						'display_reliance':[{'identifier':'parent','display_value':['1']}],
					},
					{
						'question_title':'Specify the enlargement or conversion works that have been undertaken either during your ownership or during the last 6 years:',
						'other_question_text':['select relevant aspects'],
						'question_set':'true',
						'identifier':'other_treatments',
						'sub_questions':[
							{
								'question_title':'Did the loft enlargement or conversion works include any provision to assess and fortify any structural elements or foundations?',
								'identifier':'loft_foundation_provision',
								'input_type':'checkbox',
							},
							{
								'question_title':'Were any measures taken to create or preserve cavity space to remove gas?',
								'identifier':'gas_ventilation_cavity',
								'input_type':'checkbox',	
							},
							{
								'question_title':'Has any protective membrane been installed at the property to exclude gas?',
								'identifier':'protective_membrane',
								'input_type':'checkbox',
							},
							{
								'question_title':'Does the loft have any protective waterproofing membrane or treatment?',
								'identifier':'waterproofing',
								'input_type':'checkbox',
							},
							{
								'question_title':'Has any structural waterproofing risk assessment been undertaken?',
								'identifier':'water_risk_assessment',
								'input_type':'checkbox',								
							},
						],
					},
					{
						'question_title':'Has any formal opinion been provided by a professional to determine whether a loft conversion or enlargement would be possible and viable in relation to the existing property value?',
						'input_type':'bool',
						'identifier':'loft_viability',
						'display_reliance':[{'identifier':'loft_creation_intent', 'display_value':['0']}],
					},
					{
						'question_title':'Confirm the scope and impact of the proposed conversion:',
						'other_question_text':['select relevant aspects'],
						'question_set':'true',
						'identifier':'conversion_benefits',
						'sub_questions':[
							{
								'question_title':'How many additional square metres of habitable floor space could the prospective conversion create within the property?',
								'identifier':'prospective_habitable_area',
								'input_type':'checkbox',
							},
							{
								'question_title':'What was the quoted cost to undertake the conversion works (including planning and professional fees)? ',
								'identifier':'prospective_conversion_cost',
								'input_type':'checkbox',
							},
							{
								'question_title':'Was any advice provided to indicate the likely improvement value that could be expected from a prospective conversion of a loft and or eave space?',
								'identifier':'improved_value',
								'input_type':'checkbox',
							},
							{
								'question_title':'What potential value uplift did the professional specify would result from the prospective loft or eaves conversion proposal?',
								'input_type':'bool',
								'identifier':'potential_value_uplift',
								'display_reliance':[{'identifier':'improved_value','display_value':['checkbox']}],
							},

							{
								'question_title':'Has any work previously been undertaken to create new habitable areas within a loft or eaves?',
								'input_type':'detail_text',
								'identifier':'vaiable_loft_proposition',
								'display_reliance':[{'identifier':'improved_value','display_value':['1']}],
							},
						# Open New form IF True (1)
						]
					} 
				]
			}
		]
	}
]}