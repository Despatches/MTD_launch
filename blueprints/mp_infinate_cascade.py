from flask import Blueprint,render_template, redirect, url_for, request, flash, session,json,jsonify
#from launch.blueprints.market_partics import mp
from flask_login import login_user , current_user, login_required

#@mp.route("/basic_pre_select/<particular_id>/<selec_set_ID>/")
@login_required
def mp_basic(particular_id,selec_set_ID):
	selection = db.cursor()
	query = "SELECT selection_routines.mp_selection_set_queue.Q_ID,\
			selection_routines.mp_selection_set_queue.propagating_unique_selec_ID,\
			questions_answers.answers.full_code,\
			questions_answers.answers.answer,\
			questions_answers.answers.auxilliary_data, \
			questions_answers.questions.question_meaning \
			from selection_routines.mp_selection_set_queue \
			join questions_answers.answers \
			on selection_routines.mp_selection_set_queue.Q_ID= questions_answers.answers.Q_ID\
			join questions_answers.questions \
			on selection_routines.mp_selection_set_queue.Q_ID = questions_answers.questions.Q_ID \
			where selection_routines.mp_selection_set_queue.prop_order = \
			(SELECT max(selection_routines.mp_selection_set_queue.prop_order) \
			from selection_routines.mp_selection_set_queue where mp_selection_set_ID = %s) \
			AND mp_selection_set_ID = %s \
			AND selection_routines.mp_selection_set_queue.Q_ID \
			NOT IN (select questions_answers.auxilliary_delimiters_of_questions.delimited_question\
				from questions_answers.`auxilliary_delimiters_of_questions`\
				inner join selection_routines.`market_particulars_selections` \
				on questions_answers.`auxilliary_delimiters_of_questions`.question_answer = selection_routines.`market_particulars_selections`.selection_ans \
				where selection_routines.market_particulars_selections.parent_set = %s)\
			AND questions_answers.answers.full_code \
			NOT IN(select `questions_answers`.`auxilliary_delimiters_of_answers`.`delimited_answer`\
				from `questions_answers`.`auxilliary_delimiters_of_answers`\
				inner join selection_routines.`market_particulars_selections`\
				on `questions_answers`.`auxilliary_delimiters_of_answers`.`question_answer` = selection_routines.`market_particulars_selections`.selection_ans \
				where selection_routines.market_particulars_selections.parent_set = %s);"
	
	params = (selec_set_ID,selec_set_ID,selec_set_ID,selec_set_ID)

	selection.execute(query,params)

	answers =selection.fetchall()
 
	check = len(answers)
	if not check > 0:
		selection.close()
		return redirect(url_for('mp.selectedmp',particular_id=particular_id))

	if check == 1:
		single_ans=answer([answers[0][3]],[answers[0][2]],[answers[0][4]],answers[0][0])
		if single_ans.auxilliary_data == 'no_extra':
			delete_last_from_queue(selec_set_ID)
			if answers[0][1] == None:
				add_to_selections_without_parents(single_ans,selec_set_ID)
			else:
				add_to_selections_with_parents(single_ans,selec_set_ID,single_ans[1])
			selection.close()
			return redirect(url_for('mp.mp_basic',particular_id=particular_id,selec_set_ID=selec_set_ID))

	q_data = answers[0]
	Q_ID = q_data[0]
	selection.close()
	no_extra = 0
	no_extra_a=[]
	text_extra=[]
	extra_text_codes=[]
	create_entries=[]
	create_entries_code=[]

	for row in answers:
		if row[4] == "extra":
			if not row[2] in extra_text_codes:
				text_extra.append(row)
				extra_text_codes.append(row[2])
		elif row[4] =="no_extra":
			if row[3] == "2":
				skip=row
			else:
				no_extra = no_extra + 1
				no_extra_a.append(row)
		elif row[4] == "create_entries":
			create_entries.append(row)

#store answer id's 
	session['extra_text_codes']= extra_text_codes
	session['create_entries_codes'] = create_entries_code
	session['no_extra'] = no_extra

#store question data in session
	question_meaning = q_data[5]
	parent_selection_ID = q_data[1]
	q_d=[Q_ID,question_meaning,parent_selection_ID]
	session['q_d']=q_d
	
	if not 'skip' in locals():
		skip = None	
	selection.close()	
	return render_template("answer_module/answers_module.html", answer = no_extra_a, text_answer=text_extra, 
															Question=q_d, skip=skip, particular_id=particular_id,
															selec_set_ID=selec_set_ID, no_extra=no_extra,
															extra_text_codes=extra_text_codes, selections="none",
															 create_entries=create_entries)


# submitting form from the market particulars selections, selections form

#@mp.route("/basic_pre_select/<particular_id>/<selec_set_ID>/",methods=['POST'])
@login_required
def collect_answers(particular_id,selec_set_ID):
	particular_id=particular_id
	answers =[]
	if not session['no_extra'] == 0:
		form_answer = request.form.get("selections")
		if form_answer == None:
			flash("Please make a selection or skip","non_text")
			return redirect(url_for('mp.mp_basic',particular_id=particular_id,selec_set_ID=selec_set_ID,
									 			selections=form_answer))
		key = ("no_extra",form_answer)
		answers.append(key)

	form_answer = None
	q_data = request.form.get("question")
	process = get_selection_keys(session['extra_text_codes'],answers,"extra",particular_id,selec_set_ID,form_answer)
	if process == 1:
		flash("Please enter an answer or skip","text_error")
		return redirect(url_for('mp.mp_basic',particular_id=particular_id,selec_set_ID=selec_set_ID, selections=form_answer))
	answers = get_selection_keys(session['create_entries_codes'],process,"entries",particular_id,selec_set_ID,form_answer)
	if answers == 1:
		flash("Please enter an answer or skip","text_error")
		return redirect(url_for('mp.mp_basic',particular_id=particular_id,selec_set_ID=selec_set_ID, selections=form_answer))

	parent_selec_ID = session['q_d'][2]
	delete_last_from_queue(selec_set_ID)
	answer_count = len(answers)
	if answer_count >= 2:
		
		answer = "FOLDER.folder"
#selec_set_ID placed in quotes to not cause error in mysql

		if parent_selec_ID == None or 0:
			add_to_selections_without_parents(answer,selec_set_ID)
		else:
			add_to_selections_with_parents(answer,selec_set_ID,parent_selec_ID)
		parent_selec_ID=last_input_to_select_set(selec_set_ID)
		for answer in answers:
			sort_answers_and_add(answer,selec_set_ID,parent_selec_ID)

	else:
		for answer in answers:
			sort_answers_and_add(answer,selec_set_ID,parent_selec_ID)

	return redirect(url_for("mp.mp_basic",particular_id=particular_id,selec_set_ID=selec_set_ID)) 

##@mp.route("/findmp_set/<particular_id>")
#def check_set(particular_id):
#	selec_set_ID = session['current_mp_set'][1]
#	selec_set_ID=check_selection_set(particular_id,current_user.id)
#	return redirect(url_for('mp.mp_basic',particular_id=particular_id, selec_set_ID=selec_set_ID))

#@mp.route("/<particular_id>/<holding_ID>/<selec_set_ID>/overview")
@login_required
def mp_object_props(particular_id,selec_set_ID,holding_ID):
	selection = db.cursor(buffered=True)
	object_selection_set = "selections_for_unassigned_freehold" #"selections_for_mp_freehold"
	object_selection_set_queue= "mp_unassigned_freehold_selection_set_queue" #"create table mp_freehold_selection_set_queue"
	object_ID_type = "holding_ID"

	query = "SELECT selection_routines.mp_unassigned_freehold_selection_set_queue.Q_ID,\
			selection_routines.mp_unassigned_freehold_selection_set_queue.propagating_unique_selec_ID, questions_answers.answers.full_code, questions_answers.answers.answer, questions_answers.answers.auxilliary_data, questions_answers.questions.question_meaning\
			from selection_routines.mp_unassigned_freehold_selection_set_queue \
			join questions_answers.answers \
			on selection_routines.mp_unassigned_freehold_selection_set_queue.Q_ID = questions_answers.answers.Q_ID \
			join questions_answers.questions \
			on selection_routines.mp_unassigned_freehold_selection_set_queue.Q_ID = questions_answers.questions.Q_ID \
			where holding_ID = %s and selection_routines.mp_unassigned_freehold_selection_set_queue.prop_order = (select max(selection_routines.mp_unassigned_freehold_selection_set_queue.prop_order) \
			from selection_routines.mp_unassigned_freehold_selection_set_queue where mp_selection_set_ID = %s) \
			and mp_selection_set_ID = %s and \
			selection_routines.mp_unassigned_freehold_selection_set_queue.Q_ID \
			NOT IN ( select questions_answers.`auxilliary_delimiters_of_questions`.delimited_question from questions_answers.`auxilliary_delimiters_of_questions` inner join selection_routines.`market_particulars_selections` \
			on questions_answers.`auxilliary_delimiters_of_questions`.question_answer = selection_routines.`market_particulars_selections`.selection_ans \
			inner join selection_routines.`selections_for_unassigned_freehold` \
			on questions_answers.`auxilliary_delimiters_of_questions`.question_answer = selection_routines.`selections_for_unassigned_freehold`.selection_ans \
			where selection_routines.market_particulars_selections.parent_set = %s \
			and selection_routines.`selections_for_unassigned_freehold`.holding_ID = %s) \
			and questions_answers.answers.full_code NOT IN (select `questions_answers`.`auxilliary_delimiters_of_answers`.`delimited_answer` \
			from `questions_answers`.`auxilliary_delimiters_of_answers` inner join selection_routines.`market_particulars_selections` \
			on `questions_answers`.`auxilliary_delimiters_of_answers`.`question_answer` = selection_routines.`market_particulars_selections`.selection_ans \
			inner join selection_routines.`selections_for_unassigned_freehold` on questions_answers.auxilliary_delimiters_of_answers.question_answer =selection_routines.`selections_for_unassigned_freehold`.selection_ans \
			where selection_routines.market_particulars_selections.parent_set = %s \
			and selection_routines.`selections_for_unassigned_freehold`.holding_ID = %s);"

	params =(holding_ID,selec_set_ID,selec_set_ID,selec_set_ID,holding_ID,selec_set_ID,holding_ID)
	selection.execute(query,params)

	check =selection.fetchone()
	if check == None:
		return redirect(url_for('mp.freehold_profile',holding_ID=holding_ID, selec_set_ID=selec_set_ID))

	count = selection.rowcount
	if count == 1:
		if check[4] == 'no_extra':
			delete_last_from_object_queue (selec_set_ID,object_selection_set_queue, object_ID_type ,holding_ID)
			if check[1] == None:
				add_to_selections_without_parents_objects(check[2],selec_set_ID,object_selection_set)
			else:
				add_to_selections_with_parents_objects(check[2],selec_set_ID,check[1],object_selection_set,object_ID_type)
			return redirect(url_for('mp.mp_basic',particular_id=particular_id,selec_set_ID=selec_set_ID))

	answers = selection.fetchall()

	q_data = answers[0]
	Q_ID = q_data[0]
	selection.close()
	no_extra = 0
	no_extra_a=[]
	text_extra=[]
	extra_text_codes=[]
	create_entries=[]
	create_entries_code=[]

	for row in answers:
		if row[4] == "extra":
			if not row[2] in extra_text_codes:
				text_extra.append(row)
				extra_text_codes.append(row[2])
		elif row[4] =="no_extra":
			if row[3] == "2":
				skip=row
			else:
				no_extra = no_extra + 1
				no_extra_a.append(row)
		elif row[4] == "create_entries":
			create_entries.append(row)

#store answer id's 
	session['extra_text_codes']= extra_text_codes
	session['create_entries_codes'] = create_entries_code
	session['no_extra'] = no_extra

#store question data in session
	question_meaning = q_data[5]
	parent_selection_ID = q_data[1]
	q_d=[Q_ID,question_meaning,parent_selection_ID]
	session['q_d']=q_d
	
	if not 'skip' in locals():
		skip = None		
	return render_template("answers_module.html", header = ("work","please","sob"), answer = no_extra_a, text_answer=text_extra, Question=q_d, skip=skip, particular_id=particular_id,selec_set_ID=selec_set_ID, no_extra=no_extra,extra_text_codes=extra_text_codes, selections="none", create_entries=create_entries, type="objects",holding_ID=holding_ID )

#@mp.route("/<particular_id>/<holding_ID>/<selec_set_ID>/overview",methods=['POST'])
@login_required
def collect_answers_objects(particular_id,selec_set_ID,holding_ID):
	object_selection_set = 'selections_for_unassigned_freehold' 
	object_selection_set_queue= "mp_unassigned_freehold_selection_set_queue"
	object_ID_type = "holding_ID"

	answers =[]
	if not session['no_extra'] == 0:
		form_answer = request.form.get("selections")
		if form_answer == None:
			flash("Please make a selection or skip","non_text")
			return redirect(url_for('mp.mp_object_props',particular_id=particular_id,selec_set_ID=selec_set_ID, selections=form_answer, holding_ID = holding_ID,type="objects"))
		
		key = ("no_extra",form_answer)
		answers.append(key)

	form_answer = None
	q_data = request.form.get("question")
	process = get_selection_keys(session['extra_text_codes'],answers,"extra",particular_id,selec_set_ID,form_answer)
	if process == 1:
		flash("Please enter an answer or skip","text_error")
		return redirect(url_for('mp.mp_object_props',particular_id=particular_id,selec_set_ID=selec_set_ID, 
									holding_ID = holding_ID ,selections=form_answer))

	answers = get_selection_keys(session['create_entries_codes'],process,"entries",particular_id,selec_set_ID,form_answer)

	if answers == 1:
		flash("Please enter an answer or skip","text_error")
		return redirect(url_for('mp.mp_object_props',particular_id=particular_id,selec_set_ID=selec_set_ID,
													holding_ID = holding_ID, selections=form_answer))

	parent_selec_ID = session['q_d'][2]
	delete_last_from_object_queue(selec_set_ID,object_selection_set_queue, object_ID_type ,holding_ID)
	answer_count = len(answers)
	if answer_count >= 2:
		
		answer = "FOLDER.folder"
#selec_set_ID placed in quotes to not cause error in mysql

		if parent_selec_ID == None or 0:
			add_to_selections_without_parents_objects(answer,selec_set_ID,object_selection_set)
		else:
			add_to_selections_with_parents_objects(answer,selec_set_ID,parent_selec_ID,object_selection_set,object_ID_type)
		parent_selec_ID=last_input_to_select_set(selec_set_ID)
		for answer in answers:
			sort_answers_and_add_objects(answer,selec_set_ID,parent_selec_ID,object_selection_set,object_selection_set_queue,object_ID_type,holding_ID)

	else:
		for answer in answers:
			sort_answers_and_add_objects(answer,selec_set_ID,parent_selec_ID,object_selection_set,object_selection_set_queue,object_ID_type,holding_ID)

	update_last_data_entry_mp(selec_set_ID)
	return redirect(url_for("mp.mp_object_props",particular_id=particular_id,selec_set_ID=selec_set_ID,
													holding_ID = holding_ID)) 

#@mp.route("/change_selection/<particular_id>/<selec_set_ID>/<unique_selection_ID>/<selec_ans>")
@login_required
def mp_basic_props_reselect(particular_id,selec_set_ID,unique_selection_ID,selec_ans):
	selection = db.cursor(buffered=True)
	
	query ="SELECT questions_answers.answers.`Q_ID`,\
			questions_answers.answers.`full_code`,\
			questions_answers.answers.`answer`,\
			questions_answers.answers.`auxilliary_data`, \
			questions_answers.questions.`question_meaning` \
			FROM questions_answers.questions\
			JOIN questions_answers.answers\
			ON questions_answers.questions.`Q_ID` = questions_answers.answers.`Q_ID`\
			where questions_answers.answers.`Q_ID` = (select Q_ID from questions_answers.answers where full_code = %s limit 1) \
			AND questions_answers.answers.full_code \
			NOT IN(select `questions_answers`.`auxilliary_delimiters_of_answers`.`delimited_answer`\
				from `questions_answers`.`auxilliary_delimiters_of_answers`\
				inner join selection_routines.`market_particulars_selections`\
				on `questions_answers`.`auxilliary_delimiters_of_answers`.`question_answer` = selection_routines.`market_particulars_selections`.selection_ans \
				where selection_routines.market_particulars_selections.parent_set = %s)\
			And full_code != %s;"
	
	params = (selec_ans,selec_set_ID,selec_ans)

	selection.execute(query,params)

	check =selection.fetchone()
	if check == None:
		flash("reselection currently unavailable")
		return redirect(url_for('mp.synopsis',particular_id=particular_id))

	count = selection.rowcount
	if count == 1:
		if check[0] == selec_ans:
			flash ("no alternative option")
			return redirect(url_for('mp.synopsis',particular_id=particular_id))
		#else.   ### add way to asc if single selection is acceptable

	answers = selection.fetchall()

	q_data = answers[0]
	Q_ID = q_data[0]
	selection.close()
	no_extra = 0
	no_extra_a=[]
	for row in answers:
		if row[3] =="no_extra":
			if row[2] == "2":
				skip=row
			else:
				no_extra = no_extra + 1
				no_extra_a.append(row)	

	session['no_extra'] = no_extra

#store question data in session
	question_meaning = q_data[4]
	q_d=[Q_ID,question_meaning]
	session['q_d']=q_d
	
	if not 'skip' in locals():
		skip = None

	return render_template("answer_module/change_selection_answer_module.html" ,unique_selection_ID=unique_selection_ID,
							particular_id=particular_id,selec_set_ID=selec_set_ID,selec_ans=selec_ans,no_extra=no_extra, skip=skip,
							answer=no_extra_a,selection_type = "change")
###needs work 


	return redirect(url_for('mp.mp_basic',particular_id=particular_id, selec_set_ID=selec_set_ID))


# Synopsis provides the currently active report for the open market particulars

#@mp.route("/synopsis/<particular_id>")
@login_required
def synopsis(particular_id):

	query = "SELECT `market_particulars_selections_set_ID`, `selections_owner`, `selection_ID_counter`, `creation_moment`,`time_of_last_data_entry` FROM selection_routines.market_particulars_selection_set where `market_particulars_ID` = %s\
			 ORDER BY market_particulars_selections_set_ID DESC;"

	synopsis = db.cursor()

	class selection_set:
		def __init__(self,row):
			self.set_ID = row[0]
			self.owner = row[1]
			self.selec_counter = row[2]
			self.creation_moment = row[3]
			self.last_entry = row[4]
			return None

	params = (particular_id,)

	params = (particular_id,)
	synopsis.execute(query,params)
	sets=synopsis.fetchall()
#	selec_set_ID=sets[0][0]
	selection_sets=[]

	for s in sets:
		selecs = selection_set(s)
		selection_sets.append(json.dumps(selecs.__dict__))
	number_of_selec_sets = len(selection_sets)
	selection_sets = json.dumps(selection_sets)
	urlr = request.url_root

	return render_template("synopsis.html" ,particular_id=particular_id, urlr=urlr, number_of_selec_sets=number_of_selec_sets,selection_sets=selection_sets)

	selection_sets = json.dumps(selection_sets)
	urlr = request.url_root


