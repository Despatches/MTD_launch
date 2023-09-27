template={
	"Form" : "TA6 Part 1",'process':'single_selection', 'form_identifier':'TA6_Part_1',"Sections" : [
		{
			"section_name":'Personal Details',
			'section_identifier':'personal_details',
			#'question_set_data':{'set_numbering':"3.2"},
			"main_questions":[
				{
					'question_title':'Offer Value',
					'input_type':'currency',
					'identifier':'offer_value'
				},
				{
					'question_title':'when will the property transact?',
					'input_type':'date',
					'identifier':'transaction_date'
				}
			]
		}
	]
}