"""

		total_objects= mp_objects[0]
		object_list = mp_objects [1]


		single_object = None

		if total_objects == 1:
			for obj in object_list:
				if not obj[0] == 1:
					continue
				else:
					single_object = obj[1][0]

			setfind.close()"""
#		return render_template("mp_views_and_profiles/mp_profile.html" ,leasehold_data = object_list[2][1],sudo_name = mp.sudo_name,
#									freehold_share_data=object_list[1][1] ,creation_date = mp.creation, 
#									cns_data=object_list[0][1],cns_headings=cns_headings, mid=mp.id, freehold_headings= freehold_headings, 
#									freehold_data=object_list[3][1],particular_id=particular_id,selec_set_ID=selec_set_ID, 
#									single_object=single_object ,location_data=location_data,holding_ID=holding_ID,
#									reference_name=reference_name, leasehold_headings=leasehold_headings)#,comp_score=comp_score,fraud_score=fraud_score,risk_score=risk_score)
# find fraud, competancy and other data
		#query = "select selection_routines.market_particulars_selections.selection_ans, questions_answers.answer_data.answer_meaning, questions_answers.answer_data.competancy_imp, questions_answers.answer_data.fraud_imp, questions_answers.answer_data.inherant_risk_value from selection_routines.market_particulars_selections left join market_particulars_selections on market_particulars_selections.selection_ans = questions_answers.answer_data.full_code where `answer_data`.`competancy_imp` = True or answer_data.`fraud_imp` = True or answer_data.inherant_risk_value > 0.0000 and market_particulars_selections.parent_set = %s;"
		#params= (selec_set_ID,)
		#setfind.execute(query,params)
		#ans_data= setfind.fetchall()
		#comp_score =0
		#fraud_score = 0
		#risk_score = 0.0000
		#for ans in ans_data:
		#	if ans[2] == 1:
		#		comp_score = comp_score+1
		#	if ans[3] == 1:
	#			fraud_score = fraud_score+1
	#		if ans[4] > 0.0000:
	#			risk_score = risk_score+ ans[4]
			# there are currently an above average number of data points that could be indicitive of frauldulent activity 

#		setfind.close()
#		object_breakdown =(['Companies and Shares','Freehold Shares','Leaseholds','Freeholds'],[object_list[0][0],object_list[1][0],object_list[2][0],object_list[3][0]])
#		return render_template("mp_views_and_profiles/mp_profile.html" ,leasehold_data = object_list[2][1],sudo_name = mp.sudo_name,
#								freehold_share_data=object_list[1][1] ,creation_date = mp.creation, 
#								cns_data=object_list[0][1],cns_headings=cns_headings, mid=mp.id, freehold_headings= freehold_headings,
#								 freehold_data=object_list[3][1],particular_id=particular_id,selec_set_ID=selec_set_ID, 
#								 single_object=single_object,object_breakdown=object_breakdown, leasehold_headings=leasehold_headings)#,comp_score=comp_score,fraud_score=fraud_score,risk_score=risk_score)

# add a new company or company share as a market particular component

# submit form to create new market_particulars



#	query = "select answer_meaning, competancy_imp, fraud_imp, unique_selection_ID,selection_ans\
#			from questions_answers.answers \
#			left join selection_routines.market_particulars_selections \
#			on market_particulars_selections.selection_ans = answers.full_code \
#			where parent_set = %s;"


#	params = (selec_set_ID,)
#	synopsis.execute(query,params)
#	meanings = synopsis.fetchall()
#	result = []
#	j = "Insufficient information is held to determine;"
#	a=""
#	n="No information;"
#	b=[]
#	for meaning in meanings:
#		if f"{meaning[0]}" == "":
#			continue
#		m = f"{meaning[0]}"
#		if m ==".":
#			m= m[0:-1]
#		if ';' in m:
#			a= a+m[46:]+','

#		elif "No information" in m:
#			m = m[14:]
#			mc=[m,meaning[1]]
#			b.append(mc)
#		else:
#			result.append(meaning)
#	no_info = [n,b]
	#result = [result,j+a,no_info]
#	jsonresult=ld =json.dumps(result)