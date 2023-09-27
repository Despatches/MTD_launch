from launch.blueprints.form_templates import template_objects

template = {
	"Form" : 'New Market Particular',
	'form_identifier':'new_market_particular',
	'Sections' : [
		{
			'section_name' : 'Basic Data',
			'section_identifier':'basic_mp_data',
			'main_questions':[
				{
					'identifier':'particular_name',
					'place_holder':'New MP Ref.Name',
					'input_type':'text',
					'question_title':'Name'
				},
				{
					'input_type':'radio',
					'radio_options':[
						{
							'radio_text':'Domestic Residential Conveyance',
							'radio_value':'dom_resi_convey'
						},
						{
							'radio_text':'Simple Commercial Conveyance',
							'radio_value':'simp_com_convey'
						},
						{
							'radio_text':'Large or MnA Transaction',
							'radio_value':'large_mna'
						},						
					],
					'identifier':'basic_convey_type',
					'question_title':'Basic property Conveyance Type'
				},
				{
					'input_type':'multi_row',
					'identifier':'vendor_names',
					'sub_questions':[
						template_objects.full_name(
							{
								'identifier':'vendor_name',
								'ident_prefix':'vendor_',
								'question_title':'vendor names'

							}
						)
					]
				}
			]
		}
	]
}