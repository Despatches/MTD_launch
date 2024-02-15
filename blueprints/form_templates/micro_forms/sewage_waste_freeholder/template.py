template = {
    # Completed by LANDLORD or Agent.
    "Form": "Freeholder_sewage and Waste",
    "form_identifier": "sewage_waste_freeholder",
    "Sections": [
        {
            "section_name": "Personal Details",
            "section_identifier": "personal_details",
            #'question_set_data':{'set_numbering':"3.2"},
            "main_questions": [
                {
                    "question_numbering": "1",
                    "question_title": "Provide the following personal details for each individual providing preliminary information",
                    "identifier": "data_providers",
                    "multi_row_guidance": "for each person who enters data complete this section out separately",
                    "input_type": "multi_row",
                    "sub_questions": [
                        {
                            "question_numbering": "1.1",
                            "question_title": "First Name",
                            "input_type": "text",
                            "identifier": "data_provider_first_name",
                            "required": "true",
                        },
                        {
                            "question_numbering": "1.2",
                            "question_title": "Middle Name(s)",
                            "input_type": "text",
                            "identifier": "data_provider_middle_name",
                        },
                        {
                            "question_numbering": "1.2",
                            "question_title": "surname",
                            "sub_q_other_text": "",
                            "input_type": "text",
                            "identifier": "data_provider_surname",
                            "required": "true",
                        },
                        {
                            "question_numbering": "1.3",
                            "question_title": "Please provide details of the capacity in which you are providing preliminary information for the sale",
                            "sub_q_other_text": "",
                            "input_type": "radio",
                            "identifier": "data_provider_type",
                            "required": "true",
                            "table_title": "Data Provider Type",
                            "radio_options": [
                                {"radio_text": "Seller", "radio_value": "seller"},
                                {
                                    "radio_text": "Seller’s personal representative",
                                    "radio_value": "seller_rep",
                                },
                                {"radio_text": "Other", "radio_value": "Other"},
                            ],
                            "sub_questions": [
                                {
                                    "question_numbering": "",
                                    "question_title": "please specify your relationship to the property being sold, below:For example, seller’s family member, seller’s friend, estate agent, mortgagee in possession.",
                                    "sub_q_other_text": "",
                                    "table_title": "Data Provider Details",
                                    "identifier": "data_provider_type_details",
                                    "input_type": "detail_text",
                                    "display_reliance": [
                                        {"identifier": "parent", "value": ["Other"]},
                                    ],
                                },
                            ],
                        },
                    ],
                }
            ],
        },
        {
            "section_name": "Basic Property Details",
            "section_identifier": "basic_data",
            #'question_set_data':{'set_numbering':"3.2"},
            "main_questions": [
                {
                    "question_numbering": "1",
                    "question_title": "Enter the full address",
                    "sub_q_other_text": "",
                    "question_set": "true",
                    "identifier": "property_address",
                    "sub_questions": [
                        {
                            "question_numbering": "1",
                            "question_title": "Postcode",
                            "sub_q_other_text": "",
                            "identifier": "postcode",
                            "input_type": "postcode",
                        },
                        {
                            "question_numbering": "1",
                            "question_title": "Address Line 1",
                            "sub_q_other_text": "",
                            "identifier": "address_line_1",
                            "input_type": "text",
                        },
                        {
                            "question_numbering": "1",
                            "question_title": "Address Line 2",
                            "sub_q_other_text": "",
                            "identifier": "address_line_2",
                            "input_type": "text",
                        },
                        {
                            "question_numbering": "1",
                            "question_title": "Town or City",
                            "sub_q_other_text": "",
                            "identifier": "address_town_or_city",
                            "input_type": "text",
                        },
                        {
                            "question_numbering": "1",
                            "question_title": "UPRN",
                            "sub_q_other_text": "",
                            "identifier": "UPRN",
                            "input_type": "text",
                        },
                    ],
                }
            ],
        },
        {
            "section_name": "Sewage Connections",
            "section_identifier": "sewage_connections",
            #'question_set_data':{'set_numbering':"3.2"},
            "main_questions": [
                {
                    "question_title": "Is the property connected to mains sewage?",
                    "sub_q_other_text": "",
                    "input_type": "bool",
                    "identifier": "mains_sewage_connection_bool",
                },
                # IF "NO" (not connected to mains sewage)
            ],
            "section_name": "Sewage Pipes Installation",
            "section_identifier": "sewage_pipes_installation",
            #'question_set_data':{'set_numbering':"3.2"},
            "main_questions": [
                {
                    "question_title": "When were the sewage pipes that exclusively serve this property installed?",
                    "sub_q_other_text": "",
                    "input_type": "date",
                    "identifier": "sewage_pipes_excl_serving_this_property_install_date",
                },
                {
                    "question_title": "When were the sewage pipes on this property that carry media from other properties installed?",
                    "multi_row_guidance": "Note; ",
                    # Re-arrange to a Poll :
                    # Date : Date
                    # Date un-known > sub Question
                    #   "sub_q_other_text": "When was the property constructed?
                    #   "sub_q_other_text": "Is this property design contemporary with the adjacent neighbouring properties?"
                    "sub_q_other_text": "",
                    "input_type": "date",
                    "identifier": "shared_sewage_pipes_installation_date",
                },
            ],
            "section_name": "Sewage Pipes Locations",
            "section_identifier": "sewage_pipes_locations",
            #'question_set_data':{'set_numbering':"3.2"},
            "main_questions": [
                {
                    "question_title": "Do you have any record that specifies where the existing waste pipes are located?",
                    "input_type": "bool",
                    "identifier": "location_pipes_cross_boundaries_bool",
                },
                # IF "NO" (no idea where sewage pipes located)
                # Attach a plan identifying the locations where sewage from this property connect and flow through the sewage pipes on this freehold?
            ],
            "section_name": "Sewage Boundary Intersections",
            "section_identifier": "sewage_boundary_intersections",
            #'question_set_data':{'set_numbering':"3.2"},
            "main_questions": [
                {
                    "question_title": "Do any of the drains entering or leaving the property do so by crossing the boundary from an adjacent property?",
                    "multi_row_guidance": "Note; Disclude the street / road or public land.",
                    "sub_q_other_text": "",
                    "input_type": "bool",
                    "identifier": "sewage_pipes_crossing_adjacent_property_boundary_bool",
                },
                {
                    "question_title": "Do you have any record of where on the propertys boundaries these pipes enter and exit the property?",
                    "input_type": "bool",
                    "identifier": "known_location_pipes_cross_boundaries_bool",
                },
                {
                    "question_title": "Do any of the drains entering or leaving the property do so by crossing the boundary from an adjacent property? ",
                    "sub_q_other_text": "",
                    "input_type": "bool",
                    "identifier": "drains_via_adjacent_property_bool",
                },
                {
                    "question_title": "Attach a plan identifying the locations on the boundary where the sewage pipes cross the boundary or boundaries.",
                    "sub_q_other_text": "",
                    "identifier": "plan_of_location_pipes_cross_boundaries_docu",
                    "input_type": "docu",
                    "styling": {
                        "stock_options": {
                            "options": [
                                "annually",
                                "bi-annually",
                                "quarterly",
                                "every 5 years",
                                "every 10 years",
                            ]
                        }
                    },
                },
                #
                {
                    "question_title": "Attach a plan identifying the locations on the boundary where the sewage pipes cross the boundary or boundaries.",
                    "multi_row_guidance": "Note; In the absence of a drainage plan mark upon a Title plan or scaled plan.",
                    "sub_q_other_text": "",
                    "input_type": "docu",
                    "identifier": "plan_of_shared_sewage_pipes_plan_docu",
                },
            ],
            "section_name": "Sewage Conduit Capacity",
            "section_identifier": "sewage_conduit_capacity",
            #'question_set_data':{'set_numbering':"3.2"},
            "main_questions": [
                {
                    "question_title": "Confirm the total number of properties presently served by the shared sewage pipe:",
                    "multi_row_guidance": "Note; Include in the total all anexes and multiple dwellings located upon a single tite",
                    "sub_q_other_text": "",
                    "input_type": "number",
                    "identifier": "number_properties_served_by_shared_sewage_pipe",
                },
                {
                    "question_title": "Has the number of properties served by this sewerage pipe been increased since the present infrastructure specification was installed?",
                    "sub_q_other_text": "",
                    "input_type": "bool",
                    "identifier": "number_properties_served_by_sewage_increased_bool",
                },
                {
                    "question_title": "By how many properties has the increased burden on this sewerage pipe been increased since the present infrastructure specification was installed?",
                    "multi_row_guidance": "Note; Include division of properties to multiple dwellings.",
                    "sub_q_other_text": "",
                    "input_type": "number",
                    "identifier": "increased_number_properties_served_by_sewage_post_install",
                    "display_reliance": [
                        {
                            "identifier": "number_properties_served_by_sewage_increased_bool",
                            "value": ["1"],
                        }
                    ],
                },
                {
                    "question_title": "Confirm the total number of permanent residents currently served by the pipe:",
                    "multi_row_guidance": "Note; Where the pipe serves a community confirm if this Number total is estimated",
                    "sub_q_other_text": "",
                    "input_type": "number",
                    "identifier": "number_permanent_residents_served_by_sewage_pipe",
                },
                {
                    "question_title": "What is the current rated occupier capacity (number of persons or average households) of this pipe?",
                    "multi_row_guidance": "Note; Disclude the street / road or public land.",
                    "sub_q_other_text": "",
                    "input_type": "number",
                    "identifier": "rated_capacity_of_sewage_pipe",
                },
            ],
        },
    ],
}
