def TA6_part_1_ownership():
	form = get_form_id()
	ownership = request.form.get("ownership")
	owner_type = json.loads(ownership)
	details=[]
	if owner_type['value'] == False:
		updates = [{"row" : 'Q_3p1', "value" : 1}]
		update_statement(updates, form, '`TA6`.`TA6_part_1_records`')
	elif owner_type['value'] == "freehold":
		updates = [{"row" : 'Q_3p1', "value" : 2}]
		update_statement(updates, form, '`TA6`.`TA6_part_1_records`')
	elif owner_type['value'] == "leasehold":
		pairs = []

		updates = [{"row" : 'Q_3p1', "value" : 3}]
		update_statement(updates, form, '`TA6`.`TA6_part_1_records`')

		lease = request.form.get("leasehold")

		leasehold = json.loads(lease)

		leasehold = [
			{"database":"3p2p1","form":"years_left"},
			{"database":"3p2p3","form":"rent_value"},
			{"database":"3p2p4","form":"ground_rent_increase_bool"},
			{"database":"3p2p4p1","form":"ground_rent_increase_date"},
			{"database":"3p2p5","form":"rent_increase_type"},
			{"database":"3p2p4p2","form":"ground_rent_increase_frequency_text"},
			{"database":"3p2p5p1_details","form":"rent_increase_type_details"},
		]

	#	if leasehold['years_left'] != False:
	#		pairs.append({"row":"3p2p1", 'value':leasehold['years_left']})

	#	if leasehold["rent_value"] != False:
	#		pairs.append({"row":"3p2p3", 'value':leasehold['rent_value']})

	#	#return f"{leasehold['ground_rent_increase_bool']}"

	#	ground_rent_increase_bool = bool_java_conversion(leasehold['ground_rent_increase_bool'])
		pairs.append({"row":"3p2p4", 'value':f"'{ground_rent_increase_bool}'"})

		if leasehold["ground_rent_increase_date"] != False:
			pairs.append({"row":"3p2p4p1", 'value': leasehold['ground_rent_increase_date']})


		pairs.append({"row":"3p2p5", 'value': f"'{leasehold['rent_increase_type']}'"})

		if leasehold["ground_rent_increase_frequency_text"] != False:
			pairs.append({"row":"3p2p4p2", 'value': leasehold['ground_rent_increase_frequency_text']})

		if leasehold["rent_increase_type_details"] != False:
			pairs.append({"row":"3p2p5p1_details", 'value':1})
			details.append({"row":"3p2p5p1", 'value': "'leasehold['rent_increase_type_details']'" })

		table = "`TA6`.`TA6_part_1_leaseholds`"

		pairs.append({"row":"unique_form_ID", 'value':form})

		generic_input(pairs, table)
		
		if len(details) > 0:
			details.append({"row":"unique_form_ID", 'value':form})
			generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")

		db.commit()

	return "success"

def TA6_part_1_service_charges():
	form =get_form_id()
	service_charges = request.form.get("inputs")
	charges = json.loads(service_charges)

	pairs=[] 
	details=[]
	equals = [
			{"database":"3p2p7","form":"service_charge_bool"},
			{"database":"3p2p8","form":"last_service_charge"},
			{"database":"3p2p9","form":"service_charge_budget_bool"},
			{"database":"3p2p10","form":"service_charge_payments_due"},
			{"database":"3p2p11","form":"service_charge_pay_reciever"},
			{"database":"Service_charges_org_name","form":"service_charge_organisation"},
			{"database":"Service_charges_Building_name","form":"service_charge_Building_name"},
			{"database":"Service_charges_Building_street","form":"service_charge_street_no"},
			{"database":"Service_charges_Street_name","form":"service_charge_street_name"},
			{"database":"Service_charges_Town_City","form":"service_charge_town_or_city"},
			{"database":"service_charge_postcode","form":"service_charge_postcode"},
			{"database":"3p3","form":"landlord_extension_bool"},
			{"database":"3p3p1_details","form":"lease_extension_application"}
		]

	data = form_equals_evaluation(equals, charges)
#	service_charge_bool=bool_java_conversion(charges['service_charge_bool']['value'])

	#pairs.append({"row":"3p2p7", 'value':f"'{service_charge_bool}'"})

	#if service_charge_bool == 2:
	#	if charges["last_service_charge"] != False:
	#		pairs.append({"row":"3p2p8", 'value':charges['last_service_charge']})
		
	#	service_charge_budget_bool=bool_java_conversion(charges['service_charge_budget_bool'])
	#	pairs.append({"row":"3p2p9", 'value': f"'{service_charge_budget_bool}'"})

		#if service_charge_budget_bool == "yes":
			#service_bill_documents

	#	if charges["service_charge_payments_due"] != False:
	#		pairs.append({"row":"3p2p10", 'value':charges['service_charge_payments_due']})

	#	pairs.append({"row":"3p2p11", 'value':f"'{charges['service_charge_pay_reciever']}'"})

	#	if charges["service_charge_organisation"] != False:
	#		pairs.append({"row":"Service_charges_org_name", 'value':f"'{charges['service_charge_organisation']}'"})

	#	if charges["service_charge_Building_name"] != False:
	#		pairs.append({"row":"Service_charges_Building_name", 'value':f"'{charges['service_charge_Building_name']}'"})

#		if charges["service_charge_street_no"] != False:
#			pairs.append({"row":"Service_charges_Building_street", 'value':f"'{charges['service_charge_street_no']}'"})
#		
#		if charges["service_charge_street_name"] != False:
#			pairs.append({"row":"Service_charges_Street_name", 'value':f"'{charges['service_charge_street_name']}'"})
		
#		if charges["service_charge_town_or_city"] != False:
#			pairs.append({"row":"Service_charges_Town_City", 'value':f"'{charges['service_charge_town_or_city']}'"})

#		if charges["service_charge_postcode"] != False:
#			pairs.append({"row":"service_charge_postcode", 'value':f"'{charges['service_charge_postcode']}'"})

#		landlord_extension_bool=bool_java_conversion(charges['landlord_extension_bool'])
#		pairs.append({"row":"3p3", 'value': f"'{landlord_extension_bool}'"})

#		if landlord_extension_bool == 2:
#			if charges["lease_extension_application"] != False:
#				pairs.append({"row":"3p3p1_details", 'value': 1 })
#				details.append({"row":"question", 'value': "'3p3p1'" })

	pairs += data['pairs']
	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_leaseholds`")

	if len(details) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")

	db.commit()
	return "success"