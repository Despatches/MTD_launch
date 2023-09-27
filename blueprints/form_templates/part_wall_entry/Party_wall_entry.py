import copy
from launch.blueprints.form_templates import template_objects

template={
	"Form" : "New Party Wall Entry", 
	'form_identifier':'party_wall_entry',
	"Sections" : [
			{
				"section_name":'Address of Party Wall Issuer',
				'section_identifier':'address_sending_notice',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					template_objects.address_set(
						{
							'question_title':'Provide the address of the property proposing works covered by the party wall notice',
							'identifier':'address_sending_notice',
							'ident_prefix':'psn_',
						},
						postcode_address_town_or_city={'mandatory':'false'},
					),				
				]
			},
			{
				"section_name":'Address of Party Wall Reciever',
				'section_identifier':'address_recieving_notice',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					template_objects.address_set(
						{
							'question_title':'Provide the address of the property the party wall notice has been served upon',
							'identifier':'address_recieving_notice',
							'ident_prefix':'prn_',
						},
						postcode_address_town_or_city={'mandatory':'false'}
					)				
				]
			},
			{
				"section_name":'Party Wall Details',
				'section_identifier':'party_wall_details',
				#'question_set_data':{'set_numbering':"3.2"},
				"main_questions":[
					{
						'question_title':'What is the type of the party wall notice?',
						'input_type':'radio',
						'identifier':'party_notice_type',
						'radio_options':[
							{'radio_text':'Party Excavation Notice', 'radio_value':'excavation'},
							{'radio_text':'Party Wall Notice', 'radio_value':'wall'},
							{'radio_text':'Party Fence Wall Notice', 'radio_value':'fence'},
						]
					},
					{
						'question_title':'was a Party Wall Surveyor enlisted to aid in serving this notice?',
						'input_type':'bool',
						'identifier':'party_wall_surveyor_bool',
						'sub_questions':[
							{
								'question_title':'What was the name of the surveyor who aided in serving the notice?',
								'question_set':'true',
								'identifier':'surveyor_name',
								'ident_prefix' : 'aiding_surveyor_',
								'display_reliance':[{'identifier':'parent', 'value':['1']}],
								'sub_questions':[
									{
										'question_title':'First Name',
										'input_type':'text',
										'identifier':'first_name'
									},
									{
										'question_title':'Surname',
										'input_type':'text',
										'identifier':'surname'
									},	
									{
										'question_title':'Other Names',
										'input_type':'text',
										'identifier':'other_names'
									},
									{
										'question_title':'Is/Was the surveyor acting as the representative of a particular company or agency?',
										'input_type':'bool',
										'identifier':'company_representative_bool',
										'sub_questions':[
											{
												'question_title':'What is the name of the Company or Agency the surveyor was represeting in serving the notice?',
												'input_type':'text',
												'identifier':'represented_agency',
												'display_reliance':[{'identifier':'parent', 'value':['1']}]
											}
										]
									}																
								]
							}
						]
					},
					{
						'identifier':'date_of_service',
						'question_title':'On what date was the notice issued',
						'input_type':'date'
					},
					{
						'identifier':'response_bool',
						'question_title':'Has a response to the notice been recieved yet?',
						'input_type':'bool',
						'sub_questions':[
							{
								'question_set':'true',
								'identifier':'notice_response_data',
								'display_reliance':[{'identifier':'parent', 'value':['1']}],
								'sub_questions':[							
									{
										'identifier':'response_type',
										'question_title':'What was the response to the notice that was recieved?',
										'input_type':'radio',
										'radio_options':[
															{'radio_text':'Works Allowed', 'radio_value':'allowed'},
															{'radio_text':'Works Denied', 'radio_value':'denied'}
														],
									},
									{
										'identifier':'response_date',
										'question_title':'On what date was a response recieved?',
										'input_type':'date'
									}
								]
							},
						]
					},							
				]
			},			
		]
	}
query_select = {'psn_postcode' : {'db_position': 0, 'input_type': 'postcode'} , 

'psn_address_line_1' : {'db_position': 1, 'input_type': 'text'} , 

'psn_address_line_2' : {'db_position': 2, 'input_type': 'text'} , 

'psn_postcode_address_town_or_city' : {'db_position': 3, 'input_type': 'text'} , 

'psn_UPRN' : {'db_position': 4, 'input_type': 'UPRN'} , 

'prn_postcode' : {'db_position': 5, 'input_type': 'postcode'} , 

'prn_address_line_1' : {'db_position': 6, 'input_type': 'text'} , 

'prn_address_line_2' : {'db_position': 7, 'input_type': 'text'} , 

'prn_postcode_address_town_or_city' : {'db_position': 8, 'input_type': 'text'} , 

'prn_UPRN' : {'db_position': 9, 'input_type': 'UPRN'} , 

'party_notice_type' : {'db_position': 10, 'input_type': 'radio'} , 

'party_wall_surveyor_bool' : {'db_position': 11, 'input_type': 'bool'} , 

'aiding_surveyor_first_name' : {'db_position': 12, 'input_type': 'text'} , 

'aiding_surveyor_surname' : {'db_position': 13, 'input_type': 'text'} , 

'aiding_surveyor_other_names' : {'db_position': 14, 'input_type': 'text'} , 

'aiding_surveyor_company_representative_bool' : {'db_position': 15, 'input_type': 'bool'} , 

'aiding_surveyor_represented_agency' : {'db_position': 16, 'input_type': 'text'} , 

'date_of_service' : {'db_position': 17, 'input_type': 'date'} , 

'response_bool' : {'db_position': 18, 'input_type': 'bool'} , 

'response_type' : {'db_position': 19, 'input_type': 'radio'} , 

'response_date' : {'db_position': 20, 'input_type': 'date'}
}

query_columns = 'psn_postcode,psn_address_line_1,psn_address_line_2,psn_postcode_address_town_or_city,psn_UPRN,prn_postcode,prn_address_line_1,prn_address_line_2,prn_postcode_address_town_or_city,prn_UPRN,party_notice_type,party_wall_surveyor_bool,aiding_surveyor_first_name,aiding_surveyor_surname,aiding_surveyor_other_names,aiding_surveyor_company_representative_bool,aiding_surveyor_represented_agency,date_of_service,response_bool,response_type,response_date'

pairings = {'address_sending_notice': [{'database': 'psn_postcode', 'form': 'psn_postcode'}, {'database': 'psn_address_line_1', 'form': 'psn_address_line_1'}, {'database': 'psn_address_line_2', 'form': 'psn_address_line_2'}, {'database': 'psn_postcode_address_town_or_city', 'form': 'psn_postcode_address_town_or_city'}, {'database': 'psn_UPRN', 'form': 'psn_UPRN'}], 'address_recieving_notice': [{'database': 'prn_postcode', 'form': 'prn_postcode'}, {'database': 'prn_address_line_1', 'form': 'prn_address_line_1'}, {'database': 'prn_address_line_2', 'form': 'prn_address_line_2'}, {'database': 'prn_postcode_address_town_or_city', 'form': 'prn_postcode_address_town_or_city'}, {'database': 'prn_UPRN', 'form': 'prn_UPRN'}], 'party_wall_details': [{'database': 'party_notice_type', 'form': 'party_notice_type'}, {'database': 'party_wall_surveyor_bool', 'form': 'party_wall_surveyor_bool'}, {'database': 'aiding_surveyor_first_name', 'form': 'aiding_surveyor_first_name'}, {'database': 'aiding_surveyor_surname', 'form': 'aiding_surveyor_surname'}, {'database': 'aiding_surveyor_other_names', 'form': 'aiding_surveyor_other_names'}, {'database': 'aiding_surveyor_company_representative_bool', 'form': 'aiding_surveyor_company_representative_bool'}, {'database': 'aiding_surveyor_represented_agency', 'form': 'aiding_surveyor_represented_agency'}, {'database': 'date_of_service', 'form': 'date_of_service'}, {'database': 'response_bool', 'form': 'response_bool'}, {'database': 'response_type', 'form': 'response_type'}, {'database': 'response_date', 'form': 'response_date'}]}

party_wall_entry = {'template':template, 'pairings':pairings, 'query_select':query_select, 'query_columns':query_columns}





