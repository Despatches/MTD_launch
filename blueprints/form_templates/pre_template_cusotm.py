@TA6_forms.route("/TA6_part_1")
def new_TA6_part_1():
	cursor = db.cursor()

	query = "INSERT into `TA6`.TA6_part_1_records(\
				ceation_moment,\
				user_initiator)\
			VALUES(\
				curtime(),\
				%s);"

	params = (current_user.id,)

	cursor.execute(query, params)

	query ="SELECT unique_form_ID from `TA6`.`TA6_part_1_records` where unique_form_ID = (SELECT max(unique_form_ID) from `TA6`.`TA6_part_1_records` where user_initiator = %s)"

	cursor.execute(query, params)

	u_form = cursor.fetchall()

	form_id = u_form[0][0]

	person_number= 0

	db.commit()

	cursor.close()

	return render_template("TA6.html", form_id = form_id, person_number=person_number)

@TA6_forms.route("/TA6_part_1_add_people", methods=["POST"])
def TA6_name_collect():
	cursor= db.cursor()
	inds = request.form.get("individuals")
	form = request.form.get("form_ID")
	person_number = request.form.get("person_number")

	inds = json.loads(inds)
	ind_count = 0
	insert_values = ""
	for i in inds:
		ind_count += 1
		if ind_count == 1:
			if i['other_Details'] == False:
				row = f"('{i['first_name']}','{i['surname']}','{i['middle_name']}','{i['seller_type']}','!!no_dets!!',{i['person_number']},{form})"
			else:
				row = f"('{i['first_name']}','{i['surname']}','{i['middle_name']}','{i['seller_type']}','{i['other_Details']}',{i['person_number']},{form})"
		else:
			if i['other_Details'] == False:
				row = f",('{i['first_name']}','{i['surname']}','{i['middle_name']}','{i['seller_type']}','!!no_dets!!',{i['person_number']},{form})"
			else:
				row = f",('{i['first_name']}','{i['surname']}','{i['middle_name']}','{i['seller_type']}','{i['other_Details']}',{i['person_number']},{form})"

		insert_values = f"{insert_values}{row}"


	query = f"INSERT into `TA6`.`TA6_part_1_people`(\
					first_name,\
					surname,\
					middle_name,\
					storage_reason,\
					other_specification,\
					person_number,\
					form\
				)\
				VALUES {insert_values};"

	cursor.execute(query)
	db.commit();

	cursor.close()
	return "success"

@TA6_forms.route("/TA6_part_1_add_address", methods=["POST"])
def TA6_address_collect():

	cursor = db.cursor()
	a = request.form.get("address")
	f = request.form.get("form_ID")
	form = int(f)

	address = json.loads(a)

	query = "UPDATE `TA6`.`TA6_part_1_records`\
			SET\
				postcode = %s,\
				address_line_1 = %s,\
				address_line_2 = %s,\
				address_town_or_city = %s,\
				UPRN = %s\
			where unique_form_ID = %s"

	if address['address_line_2'] == False:
		address_line_2 = "!!no_dets!!"
	else: 
		address_line_2 = address['address_line_2']

	if address['UPRN'] == False:
		UPRN = "!!no_dets!!"
	else: 
		UPRN = address['UPRN']	

	params = (address['postcode'], address['address_line_1'],
			 address_line_2, address['address_town_or_city'], UPRN, int(form))

	cursor.execute(query, params)

	db.commit()
	cursor.close()

	return "success" 

#´TA6_forms.route("/TA6_part_1_ownership", methods=["POST"])
#def TA6_ownership_collect():
#	cursor = db.cursor()
#	owner = request.form.get("ownership")
#	form = request.form.get("form_ID")
#
#	ownership = json.loads(owner)
#
#	if ownership['tenure'] == "freehold":
#
#		query = "UPDATE `TA6`.`TA6_part_1_records`\
#				SET\
#					Q_3p1 = 1\
#				where unique_form_ID = %s"

	#elif ownership['tenure'] == "leasehold":

@TA6_forms.route("/TA6_part_1_ownership", methods=["POST"])
def TA6_part_1_ownership():
	form = get_form_id()
	data = request.form.get("inputs")
	data = json.loads(data)
	details=[]
	
	ownership = [
		{"database":"Q_3p1","form":"lease_or_free"}
	]

	owner_pair = form_equals_evaluation(ownership,data)

	#if owner_pair[0]["value"] == "Leas"

	leasehold = [
		{"database":"3p2p1","form":"years_left"},
		{"database":"3p2p3","form":"rent_value"},
		{"database":"3p2p4","form":"ground_rent_increase_bool"},
		{"database":"3p2p4p1","form":"ground_rent_increase_date"},
		{"database":"3p2p5","form":"rent_increase_type"},
		{"database":"3p2p4p2","form":"ground_rent_increase_frequency_text"},
		{"database":"3p2p5p1_details","form":"rent_increase_type_details"}
	]

	table = "`TA6`.`TA6_part_1_leaseholds`"

	leasehold_pairs = form_equals_evaluation(leasehold, data)
		
	leasehold_pairs["pairs"].append({"row":"unique_form_ID", 'value':form})

	generic_input(leasehold_pairs['pairs'], table)

	if len(owner_pair['pairs']) > 0:
		update_statement(owner_pair['pairs'],form,'`TA6`.`TA6_part_1_records`' )
		
	if len(details) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")

	db.commit()

	return "success"

@TA6_forms.route("/TA6_part_1_service_charges", methods=["POST"])
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
			{"database":"service_charges_postcode","form":"service_charge_postcode"},
			{"database":"3p3","form":"landlord_extension_bool"},
			{"database":"3p3p1_details","form":"lease_extension_application"}
		]

	data = form_equals_evaluation(equals, charges)

	pairs += data['pairs']
	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_leaseholds`")

	if len(details) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")

	db.commit();
	return "success"

@TA6_forms.route("/TA6_part_1_new_builds_converts", methods=["POST"])
def TA6_part_1_new_builds_converts():
	form =get_form_id()
	new_build = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	new_build = json.loads(new_build)

	equals = [
			{"database":"4p1","form":"first_to_occupy"},
			{"database":"warranties_and_guarantees_docu","form":"warranties_docu"}
		]

	data = form_equals_evaluation(equals,new_build)

	pairs += data['pairs']

	#if new_build["first_to_occupy"] != False:
		#pairs.append({"row":"3p2p10", 'value':new_build['first_to_occupy']})
	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")

	return 'success'

@TA6_forms.route("/TA6_part_1_timing", methods=["POST"])
def TA6_part_1_timing():
	form = get_form_id()
	timing = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	timing = json.loads(timing)

	equals = [
			{"database":"5p1","form":"property_dependant"},
			{"database":"5p1p1_details","form":"property_dependant_details_text"},
			{"database":"5p2p1p1","form":"school_term"},
			{"database":"5p2p1p2","form":"school_term_date"},
			{"database":"5p2p2p1","form":"upcoming_holiday"},
			{"database":"5p2p2p2","form":"upcoming_holiday_date"},
			{"database":"5p2p3p1","form":"job_move"},
			{"database":"5p2p3p2","form":"job_move_date"},
			{"database":"5p2p4p1","form":"redundancy"},
			{"database":"5p2p4p2","form":"redundancy_date"},
			{"database":"5p2p5p1","form":"medical"},
			{"database":"5p2p5p2","form":"medical_date"},
			{"database":"5p2p6p1","form":"notice_to_tenant"},
			{"database":"5p2p6p2","form":"notice_to_tenant_date"},
			{"database":"5p2p7p1","form":"retirement"},
			{"database":"5p2p7p2","form":"retirement_date"},
			{"database":"5p2p8p1","form":"build_complete"},
			{"database":"5p2p8p2","form":"build_complete_date"},
			{"database":"5p2p9p1","form":"other_move_factor"},
			{"database":"5p2p9p2","form":"other_move_factor_date"},
			{"database":"5p2p9p3_details","form":"other_move_factor_details"}																		
		]

	data = form_equals_evaluation(equals,timing)

	pairs += data['pairs']

	#if new_build["first_to_occupy"] != False:
		#pairs.append({"row":"3p2p10", 'value':new_build['first_to_occupy']})
	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")

	return 'success'

@TA6_forms.route("/TA6_part_1_liabilities", methods=["POST"])
def TA6_part_1_liabilities():
	form = get_form_id()
	liabilities = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	liabilities = json.loads(liabilities)

	equals = [
		{"database":"7p1p1","form":"planning_breach"},
		{"database":"7p1p1p2_details","form":"planning_breach_details"},
		{"database":"7p1p2","form":"bulding_reg_breach"},
		{"database":"7p1p2p2_details","form":"bulding_reg_breach_details"},	
		{"database":"7p1p3","form":"unfinished_work"},
		{"database":"7p1p3p2_details","form":"unfinished_work_details"},
		{"database":"7p1p4","form":"consent_lack"},
		{"database":"7p1p4p2_details","form":"consent_lack_details"}						
	]

	data = form_equals_evaluation(equals,liabilities)

	pairs += data['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")

	return 'success'
@TA6_forms.route("/TA6_part_1_solar_panels", methods=["POST"])
def TA6_part_1_solar_panels():	
	form = get_form_id()
	solar_panels = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	solar_panels = json.loads(solar_panels)
	
	equals = [
		{"database":"8p1","form":"solar_panels_bool"},
		{"database":"8p1p1","form":"solar_installation_year"},
		{"database":"8p1p2","form":"solar_panels_ownership_bool"},
		{"database":"8p1p3","form":"solar_panels_long_lease_ownership_bool"},		
		{"database":"8p1p3p1_docu","form":"solar_electrical_tarrif_docu"}
	]

	data = form_equals_evaluation(equals,solar_panels)

	pairs += data['pairs']


	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")
	return 'success'

@TA6_forms.route("/TA6_part_1_protected_buildings", methods=["POST"])
def TA6_part_1_protected_buildings():	
	form = get_form_id()
	protected_buildings = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	protected_buildings = json.loads(protected_buildings)
	
	equals = [
		{"database":"9p1","form":"protected_buildings_bool"},
		{"database":"9p1p1_docu","form":"protected_buildings_docu"},
		{"database":"9p2","form":"conservation_area_bool"},
		{"database":"9p2p1_docu","form":"conservation_area_details"}		
	]

	data = form_equals_evaluation(equals,protected_buildings)

	pairs += data['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")
	return 'success'

@TA6_forms.route("/TA6_part_1_protected_trees", methods=["POST"])
def TA6_part_1_protected_trees():	
	form = get_form_id()
	protected_trees = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	protected_trees = json.loads(protected_trees)
	
	equals = [
		{"database":"10p1","form":"TPO_bool"},
		{"database":"10p1p1","form":"order_terms_complied_with"},
		{"database":"10p1p2_docu","form":"tpo_docu"}
	]

	data = form_equals_evaluation(equals, protected_trees)

	pairs += data['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")
	return 'success'

@TA6_forms.route("/TA6_part_1_consents", methods=["POST"])
def TA6_part_1_consents():	
	form = get_form_id()
	consents = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	consents = json.loads(consents)
	
	equals = [
		{"database":"11p1", "form":"all_required_consents"},
		{"database":"11p1p1_details", "form":"all_required_consents_details"}
	]

	data = form_equals_evaluation(equals, consents)

	pairs += data['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")
	return 'success'

@TA6_forms.route("/TA6_part_1_charges", methods=["POST"])
def TA6_part_1_charges():	
	form = get_form_id()
	charges = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	charges = json.loads(charges)
	
	equals = [
		{"database":"12p1", "form":"charges_bool"},
		{"database":"12p1p1_details", "form":"charges_details"}
	]

	data = form_equals_evaluation(equals, charges)

	pairs += data['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")
	return 'success'


@TA6_forms.route("/TA6_part_1_access_roads", methods=["POST"])
def TA6_part_1_access_roads():	
	form = get_form_id()
	access_roads = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	access_roads = json.loads(access_roads)
	
	equals = [
		{"database":"12p1", "form":"charges_bool"},
		{"database":"12p1p1_details", "form":"charges_details"}
	]

	data = form_equals_evaluation(equals, access_roads)

	pairs += data['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")
	return 'success'

@TA6_forms.route("/TA6_part_1_services", methods=["POST"])
def TA6_part_1_services():	
	form = get_form_id()
	services = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	services = json.loads(services)
	
	equals = [
		{"database":"14p1p1", "form":"mains_drainage"},
		{"database":"14p1p2", "form":"electricity"},
		{"database":"14p1p3", "form":"broadband"},
		{"database":"14p1p4", "form":"telephone_landlines"},
		{"database":"14p1p5", "form":"heat_pumps"},
		{"database":"14p1p6", "form":"water_supply"},
		{"database":"14p1p7", "form":"gas"},
		{"database":"14p1p8", "form":"sewage_plant"},
		{"database":"14p1p9", "form":"solar_panels"},
		{"database":"14p1p10", "form":"other_provisioned_services"},
		{"database":"14p1p10", "form":"other_provisioned_services_details"},
	]

	data = form_equals_evaluation(equals, services)

	pairs += data['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")
	return 'success'

@TA6_forms.route("/TA6_part_1_shared_facilities", methods=["POST"])
def TA6_part_1_shared_facilities():	
	form = get_form_id()
	shared_facilities = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	shared_facilities = json.loads(shared_facilities)
	
	equals = [
		{"database":"15p1", "form":"shared_facilities_bool"},
		{"database":"15p1p1_details", "form":"shared_facilities_text_details"},

	]

	data = form_equals_evaluation(equals, shared_facilities)

	pairs += data['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")
	return 'success'

@TA6_forms.route("/TA6_part_1_parking", methods=["POST"])
def TA6_part_1_parking():
	form = get_form_id()
	parking = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	parking = json.loads(parking)
	
	equals = [
		{"database":"16p1_details", "form":"parking_arrangement_details"},
		{"database":"16p2", "form":"controlled_parking"},
	]

	data = form_equals_evaluation(equals, parking)

	pairs += data['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")
	return 'success'

@TA6_forms.route("/TA6_part_1_occupiers", methods=["POST"])
def TA6_part_1_occupiers():
	form = get_form_id()
	occupiers = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	occupiers = json.loads(occupiers)

	equals = [
		{"database":"17p2", "form":"over_17_bool"},
		{"database":"`TA6`.`TA6_part_1_people`", "form":"over_17_table", 
		'rows' :[{'row':'first_name',"form":'first_name_17', 'default':"''", 'data':[]},
				{'row':'middle_name',"form":'middle_name_17', 'default':"''", 'data':[]},
				{'row':'surname',"form":'surname_17', 'default':'', 'data':[]},
				{'row':'storage_reason',"form":'person_type','default':"'property_dweller'", 'data':[] }]
		},
		{"database":"17p1", "form":"live_at_prop_bool"},
		{"database":"17p2p2", "form":"lodgers_bool"},
		{"database":"17p3p1", "form":"agree_to_leave_bool"},
		{"database":"17p3", "form":"vacant_possession_bool"},
		{"database":"17p3p2", "form":"occupiers_contract_sign_bool"},
		{"database":"17p4_docu", "form":"vacant_possession_proof_docu"}
	]

	occupiers = form_equals_evaluation(equals, occupiers)

	pairs += occupiers['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")
	return 'success'	

@TA6_forms.route("/TA6_part_1_flooding", methods=["POST"])
def TA6_part_1_flooding():
	form = get_form_id()
	occupiers = request.form.get("inputs")
	pairs=[]
	details=[]
	docu = []
	occupiers = json.loads(occupiers)

	equals = [
		{"database":"17p2", "form":"over_17_bool"},
		{"database":"`TA6`.`TA6_part_1_people`", "form":"over_17_table", 
		'rows' :[{'row':'first_name',"form":'first_name_17', 'default':"''", 'data':[]},
				{'row':'middle_name',"form":'middle_name_17', 'default':"''", 'data':[]},
				{'row':'surname',"form":'surname_17', 'default':'', 'data':[]},
				{'row':'storage_reason',"form":'person_type','default':"'property_dweller'", 'data':[] }]
		},
		{"database":"17p1", "form":"live_at_prop_bool"},
		{"database":"17p2p2", "form":"lodgers_bool"},
		{"database":"17p3p1", "form":"agree_to_leave_bool"},
		{"database":"17p3", "form":"vacant_possession_bool"},
		{"database":"17p3p2", "form":"occupiers_contract_sign_bool"},
		{"database":"17p4_docu", "form":"vacant_possession_proof_docu"}
	]

	occupiers = form_equals_evaluation(equals, occupiers)

	pairs += occupiers['pairs']

	if len(pairs) > 0:
		update_statement(pairs, form, "`TA6`.`TA6_part_1_records`")
	if len(pairs) > 0:
		details.append({"row":"unique_form_ID", 'value':form})
		generic_input(details, "`TA6`.`extra_unformatted_text_TA6_part_1`")


@TA6_forms.route("/TA6_part_1/<p_type>/<particular_id>")
@login_required
def TA6_part_1(p_type, particular_id, **kwargs):

	if 'form' in kwargs:
		form = kwargs['form'][0]
		form_age = kwargs['form'][1]

	else:
		results = form_particular_creation('TA6_part_1', p_type, particular_id)
		form = results[0]
		form_age = results[1]
	
	#template_set = template[form_set]
	template_set = templates['TA6_part_1']
	template = template_set['template']

	"""if results[1] == 'old_form':
		form_results = form_results_collection(collect_form_data(TA6_part_1_query_columns,form), ta6_part_1_query_select, form, template['Form'])
		"""

	returns = template_sort(template)
	
	template = returns['template']
	flow_controls = returns['flow_controls']

	js_template = json.dumps(template)

	questions = returns['questions']

	sections = returns['sections']
	flow_controls = json.dumps(flow_controls)

	questions = json.dumps(questions)

	sections = json.dumps(sections)

	if form_age == 'old_form':
		form_results = form_results_collection(collect_form_data(template_set['query_columns'],form), template_set['query_select'], form, template['form_identifier'])
		form_results.fetch_detail_data()
		form_results.collect_multi_row_data(template_set['sub_tables'])
		result_send = json.dumps(form_results.data)
		sub_tables_send = json.dumps(form_results.sub_tables)
		return render_template("Json_form_templating/Json_form_templating.html", template = template, flow_controls = flow_controls, js_template=js_template, questions=questions ,form_id = form, sections=sections, results = result_send, sub_table_data = sub_tables_send, section_marker=form_results.section_marker)
	else:
		sub_tables_send = 'none'

	return render_template("Json_form_templating/Json_form_templating.html", template = template, flow_controls = flow_controls, js_template=js_template, questions=questions ,form_id = form, sections=sections, results = result_send, sub_table_data = sub_tables_send)

	return 'success'