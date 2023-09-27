from launch import currency

template={
'form_identifier':'attic_development',
'Form':'Loft Evaluation',
'Sections':[
		{
			'section_name':'Loft Conversion Prospect',
			'section_identifier':'loft_prospect',
			'main_questions':[
				{
					'question_title':'Does the property contain a loft, attic or any eves areas?',
					'input_type':'bool',
					'identifier':'contain_attic',
				},
				{
					'question_title':'do any of the loft, attic or any eves areas not presenty form part of the habitable area?',
					'input_type':'bool',
					'identifier':'attic_not_habitable',
					'display_reliance':[{'identifier':'contain_attic','value':['1']}],
					'sub_questions':[
						{
							'question_title':'Has a design for conversion utilising loft or eaves space or the creation of a roof adaptation been prepared?',
							'input_type':'bool_extra',
							'identifier':'util',
							'display_reliance':[{'identifier':'parent','value':['1']}],
							'radio_options':[{'radio_value':'not_known','radio_text':'Not Known'}],
							'sub_questions':[
								{
									'question_title':'Is there any future consideration or intent to create a habitable space utilising a loft or eaves space?',
									'input_type':'bool',
									'display_reliance':[{'identifier':'parent','value':['0']}],
									'identifier':'loft_creation_intent',
								},
							]
						}
					]
				}
			]
		},
		{
			'section_name':'Loft Conversion Existing',
			'section_identifier':'loft_conversion_existing',
			'display_reliance':[{'identifier':'contain_attic','value':['1']}],
			'main_questions':[
				{
					'question_title':'Has any work previously been undertaken to create habitable space within a loft,  eaves or other previously non habitable area?',
					'input_type':'bool',
					'identifier':'previous_loft_enlargement',
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
							'input_type':'bool',												
						},
						{
							'question_title':'Was planning approval attained for the conversion works?',
							'identifier':'gas_ventilation_cavity',
							'input_type':'bool',
							'sub_questions':[
								{
									'question_title':'Was the conversion of the loft completed within 4 years of planning permission beig attained?',
									'identifier':'loft_completion_years',
									'input_type':'checkbox',
									'display_reliance':[{'identifier':'parent','value':['1']}]
								},
							]
						},
						
						{
							'question_title':'Does the loft have any protective waterproofing membrane or treatment?',
							'identifier':'waterproofing',
							'input_type':'bool',
						},
						#{
						#	'question_title':'Was the are inspected by a professional to identify any signs of invasive species ',
						#	'identifier':'water_risk_assessment',
						#	'input_type':'checkbox',								
						#},
					],
				},
			]
		},
		{
			'section_name':'Loft Conversion Viability',
			'section_identifier':'loft_conversion_viability',
			'main_questions':[
				{
					'question_title':'Has any formal opinion been provided by a professional to determine whether a loft conversion or enlargement would be possible and viable in relation to the existing property value?',
					'input_type':'bool',
					'identifier':'loft_viability',
					'display_reliance':[{'identifier':'loft_creation_intent','value':['0']}],
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
							'input_type':'area',
							'measurement':'meters',
						},
						{
							'question_title':'What is the quoted cost to undertake the conversion works (including planning and professional fees)? ',
							'identifier':'prospective_conversion_cost',
							'input_type':'currency',
							'currency':currency
						},
						{
							'question_title':'Was any advice provided to indicate the likely improvement value that could be expected from a prospective conversion of a loft and or eave space?',
							'identifier':'improved_value',
							'input_type':'currency',
							'currency':currency
						},
						{
							'question_title':'What potential value uplift has a professional specified could result from the prospective loft or eaves conversion proposal?',
							'input_type':'bool',
							'identifier':'potential_value_uplift',
							'display_reliance':[{'identifier':'improved_value','value':['1']}],
							'input_type':'currency',
							'currency':currency
						},
					# Open New form IF True (1)
					]
				} 
			]
		}
	]
}
