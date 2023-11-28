def set_editor(kwargs, ob_set):
    if len(kwargs) > 0:
        for k in kwargs:
            for ad in ob_set:
                if k == ad["identifier"]:
                    for elem in kwargs[k]:
                        ad[elem] = kwargs[k][elem]

    return ob_set


def ini_object_prep(set_type, ini_object, new_set):
    ini_object["sub_questions"] = new_set
    if "ident_prefix" not in ini_object:
        ini_object["ident_prefix"] = "{}_".format(ini_object["identifier"])

    set_data = {
        "type": set_type,
        "identifier": "{}{}".format(ini_object["ident_prefix"], set_type),
    }

    ini_object["question_set"] = set_data

    return ini_object


def address_set(ini_object, **kwargs):
    address_set = [
        {
            "identifier": "address_line_1",
            "input_type": "text",
            "question_title": "Address line 1",
            "mandatory": "true",
            "element": "line_1",
        },
        {
            "identifier": "address_line_2",
            "input_type": "text",
            "question_title": "Address line 2",
            "element": "line_2",
        },
        {
            "identifier": "address_line_3",
            "input_type": "text",
            "question_title": "Address line 3",
            "element": "line_3",
        },
        {
            "identifier": "postcode_address_town_or_city",
            "input_type": "text",
            "question_title": "Town or City",
            "mandatory": "true",
            "element": "post_town",
        },
        {
            "identifier": "postcode",
            "input_type": "postcode",
            "question_title": "Postcode",
            "mandatory": "true",
            "element": "postcode",
        },
        {
            "identifier": "UPRN",
            "input_type": "UPRN",
            "question_title": "UPRN",
            "input_type": "text",
            "element": "UPRN",
        },
    ]

    ini_object = ini_object_prep("address", ini_object, set_editor(kwargs, address_set))
    return ini_object


"""address_set(
	{
		'question_title':'Provide the address of the property proposing works covered by the party wall notice',
		'identifier':'address_sending_notice',
		'ident_prefix':'psn_',
	},
	postcode_address_town_or_city={'mandatory':'false'}
)"""


def full_name(ini_object, **kwargs):
    name_set = [
        {
            "identifier": "first_name",
            "input_type": "text",
            "element": "first_name",
            "question_title": "First Name",
        },
        {
            "identifier": "middle_names",
            "input_type": "text",
            "element": "middle_names",
            "question_title": "Middle Names",
        },
        {
            "identifier": "surname",
            "input_type": "text",
            "element": "surname",
            "question_title": "Surname",
        },
    ]

    ini_object = ini_object_prep("full_name", ini_object, set_editor(kwargs, name_set))
    return ini_object


def contacts(ini_object, **kwargs):
    contacts = [
        {
            "identifier": "email",
            "input_type": "email",
            "element": "email",
            "question_title": "Email",
        },
        {
            "identifier": "phone_number",
            "input_type": "phone_number",
            "element": "phone_number",
            "question_title": "Contact Number",
        },
    ]

    ini_object = ini_object_prep("contacts", ini_object, set_editor(kwargs, contacts))

    return ini_object
