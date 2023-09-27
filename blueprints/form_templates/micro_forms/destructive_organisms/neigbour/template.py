template = {
'form_identifier':'dneighbour_infestation_destructive_organism_and_parasite',
'Sections':[
			{
			'Section_name':'Neighbouring Infestations',
			'section_identifier':'neighbouring_infestation',
			'main_questions':[
				{	'question_title':'Are you aware of any infestation, destructive orgnism or parasite affecting an adjacent neighbouring property?',
					'input_type':'bool',
					'identifier':'adjacent_ever_infestation'
				}
				{	'question_title':'How many adjacent neighbour properties have been affectd by infestations?',
					'input_type':'value',
					'display_reliance':{'identifier':'neighbouring_infestation','display_value':['1']},
					'identifier':'adjacent_ever_infestation'
				}

				{
					'question_title':'If you are aware of an adjacent neighbour property ever suffereing infestation within the last 6 years confirm the following:',
					'input_type':'bool_extra',
					'display_reliance':{'identifier':'neighbouring_infestation','display_value':['1']},
					'identifier':'ever_suffered_infestation'
					'radio_options':{'radio_value':'not_known','radio_text':'Not Known'},
					'sub_questions':[
						{
							'question_title':'What was the nature or mode of the infestation in the negihbouring property?',
							'input_type':'detail_text',
							'display_reliance':{'identifier':'parent','display_value':['1']},
							'identifier':'infestation_details'
						},
						{
							'question_title':'Was the property subsequently treated in order to combat the infestation?',
							'input_type':'bool',
							'identifier':'was_property_sub_treated',
							'display_reliance':{'identifier':'parent','display_value':['1']},
						},
						{
							'question_title':'Did any similar infestation manifest within this property within the same period or subsequent 24 months?',
							'input_type':'multi_row',
							'identifier':'similar_infestation',
							'sub_questions':[
								{
									'question_title':'Did any infestation control or treatment professional attribute any spread risk from the neighbouring property?',
									'identifier':'spread_risk',
									'input_type':'bool',
								},
								{
									'question_title':'Other than treatment was any measure required or implimented to prevent the neghbouring infestation spreading to other properties?',
									'identifier':'spread_prevent_measures',
									'input_type':'bool',
									
								}
							]
						}
						
					]
				},
			]
		}