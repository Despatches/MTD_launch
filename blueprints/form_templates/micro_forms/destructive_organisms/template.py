template = {
'form_identifier':'destructive_organism_and_parasite',
'Sections':[
		{
			'Section_name':'Infestations and Building Fabric',
			'section_identifier':'infestation',
			'main_questions':[
				{
					'question_title':'Has this property ever suffered from an infestation of any species of insect, mammal, or bio-organism?',
					'input_type':'bool_extra',
					'identifier':'ever_suffered_infestation'
					'radio_options':{'radio_value':'not_known','radio_text':'Not Known'},
					'sub_questions':[
						{
							'question_title':'what was the nature / mode of the infestation?',
							'other question text': ['confirm ; what type of infestation, the building fabric effected, the scale and severity. '],
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
							'question_title':'Has the property ever been treated to prevent the infestation of any bug or animal?',
							'input_type':'multi_row',
							'identifier':'other_treatments',
							'sub_questions':[
								{
									'question_title':'What was the nature of the pest repellant measure undertaken?',
									'identifier':'pest_repel_nature',
									'input_type':'text',
								},
								{
									'question_title':'Was any warranty provided with the infestation resolution measure',
									'identifier':'repel_warranty',
									
								}
							]
						}
						{
							'question_title':'Was any fabric forming part of the property damaged and replaced as a result of the infestation?',
							'input_type':'bool',
							'identifier':'replaced_building_fabiric',
							'display_reliance':{'identifier':'parent','display_value':['1']},
						},
						{
							'question_title':'Were all appropriate building and or conservation consents obtained with regard to these works?',
							'input_type':'bool', 
							'display_reliance': [{'identifier':'replaced_building_fabric','value':['1']}],
							'identifier':'appropriate_consents',
							'display_reliance':{'identifier':'parent','display_value':['1']},
						},
						{
							'question_title':'Was any adjacent property affected by the infestation at this time?',
							'input_type':'bool',
							'identifier':'other_property_affected',
							'display_reliance':{'identifier':'parent','display_value':['1']},
						},
						{
							'question_title':'Ia a copy of the infestation remedy and related warranty documents avilable',
							'input_type':'bool',
							'identifier':'remedy_warranty_docu',
							'display_reliance':{'identifier':'parent','display_value':['1']},
						},
						{
							'question_title':'Upload the relevant documentation relating to the infestation remedy and any associated warranty.',
							'input_type':'docu',
							'display_reliance': [{'identifier':'remedy_warranty_docu','value':['1']}],
							'identifier':'remedy_warranty_docu',
							'display_reliance':{'identifier':'parent','display_value':['1']},
						},
					]
				},
			]
		}
	]
}