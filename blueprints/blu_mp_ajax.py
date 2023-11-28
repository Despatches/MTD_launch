#from flask_googlemaps import GoogleMaps
#from flask_googlemaps import Map
from launch import db
from flask_login import login_user , current_user
from launch.models.models import User, market_particulars, answer, answer_mp_data
from launch.Objects.selections import market_particular_selection
from launch.functions.data_base_procedures import (add_to_selections_with_parents, 
												counter,last_input_to_select_set, find_propagations,
												delete_last_from_queue, sort_answers_and_add,add_to_selections_without_parents,
												get_selection_keys, check_selection_set,delete_last_from_object_queue, 
												sort_answers_and_add_objects, add_to_selections_without_parents_objects,
												add_to_selections_with_parents_objects,collect_object_selections,
												update_last_data_entry_mp, fetch_market_particular_components)
from launch.functions.access_record_procedures import update_last_user_access
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, json, jsonify
import mysql.connector
import string
import random
import datetime

mp_ajax = Blueprint('mp_ajax' , __name__)

def collect_next_selections_mp(selec_set_ID):
	selection = db.cursor()
	query = "SELECT \
						\
							ans_list.Q_ID,\
							ans_list.propagating_unique_selec_ID,\
							ans_list.full_code,\
							ans_list.answer,\
							ans_list.auxilliary_data, \
							ans_list.answer_text, \
							ans_list.question_meaning,\
                            glossary.main_glossary.glossary_term\
			FROM(\
            SELECT \
						\
							selection_routines.mp_selection_set_queue.Q_ID,\
							selection_routines.mp_selection_set_queue.propagating_unique_selec_ID,\
							questions_answers.answers.full_code,\
							questions_answers.answers.answer,\
							questions_answers.answers.auxilliary_data, \
							questions_answers.answers.answer_text, \
							questions_answers.questions.question_meaning \
							FROM selection_routines.mp_selection_set_queue \
							JOIN questions_answers.answers \
							ON selection_routines.mp_selection_set_queue.Q_ID= questions_answers.answers.Q_ID\
							\
							join questions_answers.questions \
							on selection_routines.mp_selection_set_queue.Q_ID = questions_answers.questions.Q_ID \
							\
							where selection_routines.mp_selection_set_queue.prop_order = (\
								SELECT max(selection_routines.mp_selection_set_queue.prop_order\
							) \
							from selection_routines.mp_selection_set_queue where mp_selection_set_ID = %s)\
							\
							AND mp_selection_set_ID = %s \
							\
							AND selection_routines.mp_selection_set_queue.Q_ID NOT IN (\
								select questions_answers.auxilliary_delimiters_of_questions.delimited_question\
								from questions_answers.`auxilliary_delimiters_of_questions`\
								inner join selection_routines.`market_particulars_selections` \
								on questions_answers.`auxilliary_delimiters_of_questions`.question_answer = selection_routines.`market_particulars_selections`.selection_ans \
								where selection_routines.market_particulars_selections.parent_set =%s\
							)\
							\
							AND questions_answers.answers.full_code NOT IN(\
							select `questions_answers`.`auxilliary_delimiters_of_answers`.`delimited_answer`\
								from `questions_answers`.`auxilliary_delimiters_of_answers`\
								inner join selection_routines.`market_particulars_selections`\
								on `questions_answers`.`auxilliary_delimiters_of_answers`.`question_answer` = selection_routines.`market_particulars_selections`.selection_ans \
								where selection_routines.market_particulars_selections.parent_set = %s\
							)\
						) as ans_list\
			left join glossary.main_glossary\
			on glossary.main_glossary.glossary_identifier = ans_list.answer "
	
	params = (selec_set_ID,selec_set_ID,selec_set_ID,selec_set_ID)

	selection.execute(query,params)

	ans = selection.fetchall()

	selection.close()

	answers = []
	if len(ans) > 0:
		question = {"Q_ID" : ans[0][0], "question_meaning" : ans[0][6], "propagator" : ans[0][1]}
		for a in ans:
			a = answer_mp_data(a)
			a = json.dumps(a.__dict__)
			answers.append(a)
		return [answers, question]

	else:
	 return None

@mp_ajax.route("/find_user_access",methods=["POST"])
def find_user_access():
	particular_id=request.form.get("mp_id")
	find_buyers = db.cursor()

	query = "SELECT * from mp_disclosure_access.prospective_buyer\
			 where `market_particulars` = %s"
	params=(particular_id,)
	find_buyers.execute(query,params)
	potential_buyers = find_buyers.fetchall()
	no_of_potential_buyers = len(potential_buyers)
	find_buyers.close()
	return {"potential_buyers":no_of_potential_buyers}

@mp_ajax.route("/get_mp_next_question",methods=["POST"])
def get_mp_question():
	cursor = db.cursor()

	selec_set=request.form.get("selec_set")

	query = "SELECT COUNT(*) FROM selection_routines.mp_selection_set_queue\
			where mp_selection_set_ID = %s;"
	params = (selec_set,)

	cursor.execute(query, params)

	q = cursor.fetchone()
	queue_count = q[0]

	cursor.close()

	while queue_count > 0:
		q_a = collect_next_selections_mp(selec_set)
		if q_a == None:
			delete_last_from_queue(selec_set)
			queue_count -= queue_count
			continue
		else:
			answers = q_a[0]
			question = json.dumps(q_a[1])
			return jsonify({"answer_list" : answers, "question" : question})

	return jsonify({"answer_list" :"queue_empty"})

@mp_ajax.route("/collect_mp_answers",methods=["POST"])
def collect_mp_answers():
#	cursor = db.cursor()

	answers = request.form.get("selections")
	answers = json.loads(answers)
	propagator = request.form.get("propagator")
	selec_set_ID = request.form.get("selec_set")
	selec_set_ID = int(selec_set_ID)

	delete_last_from_queue(selec_set_ID)

# no_propagator when "0"
	if propagator == "0":
		for ans in answers:
			find_propagations(ans['full_code'], selec_set_ID)
			if ans['type'] == "no_extra" or ans['type'] == "extra":
				add_to_selections_without_parents(ans, selec_set_ID)
		return "1"
	else:
		for ans in answers:
			find_propagations(ans['full_code'], selec_set_ID)
			if ans['type'] == "no_extra":
				add_to_selections_with_parents(ans ,selec_set_ID, propagator)
	return f"{propagator}"

@mp_ajax.route("/df_grid")
def df_grid():
	return render_template("df_grid.html")

@mp_ajax.route("/get_mp_selection/revisions",methods= ['POST'])
def mp_selection_revisions():
	selec_set = request.form.get("selec_set")
	query = "SELECT \
						`selection_routines`.`market_particulars_selections`.`parent_set`,\
					    `selection_routines`.`market_particulars_selections`.`unique_selection_ID`,\
					    `selection_routines`.`market_particulars_selections`.`parent_unique_selection_ID`,\
					    `selection_routines`.`market_particulars_selections`.`selection_ans`,\
					    `selection_routines`.`market_particulars_selections`.`lft`,\
					    `selection_routines`.`market_particulars_selections`.`rgt`,\
					    `selection_routines`.`market_particulars_selections`.`selection`,\
					    `selection_routines`.`market_particulars_selections`.`user_validated`,\
					    `questions_answers`.`answers`.`answer`,\
					    `questions_answers`.`answers`.`answer_active`,\
					    `questions_answers`.`answers`.`auxilliary_data`,\
					    `questions_answers`.`answers`.`answer_meaning`,\
					    `questions_answers`.`answers`.`competancy_imp`,\
					    `questions_answers`.`answers`.`fraud_imp`,\
					    `questions_answers`.`answers`.`inherant_risk_value`,\
					    `questions_answers`.`answers`.`answer_implications`,\
					    `questions_answers`.`answers`.`last_updated`,\
					    `selection_routines`.`mp_ancilliary_selection_data`.`ancilliary_data`,\
					    `selection_routines`.`mp_ancilliary_selection_data`.`ancilliary_data_type`,\
					    `selection_routines`.`mp_ancilliary_selection_data`.`previous_record`\
			FROM `selection_routines`.`market_particulars_selections`\
			LEFT JOIN`questions_answers`.`answers`\
			ON `questions_answers`.`answers`.`full_code` =  `market_particulars_selections`.`selection_ans`\
			LEFT JOIN `selection_routines`.`mp_ancilliary_selection_data`\
			ON `selection_routines`.`mp_ancilliary_selection_data`.selection_ID = `selection_routines`.`market_particulars_selections`.`unique_selection_ID`\
			AND `selection_routines`.`mp_ancilliary_selection_data`.selection_set_ID = `selection_routines`.`market_particulars_selections`.`parent_set`\
			where parent_set = %s;"	
	
	params = (selec_set,)
	get_selections = db.cursor()
	get_selections.execute(query,params)
	selecs = get_selections.fetchall()
	if len(selecs) != 0:
		selections = []
		for s in selecs:
			selec_data=market_particular_selection(s)
			data_json =json.dumps(selec_data.__dict__)
			selections.append(data_json)
		get_selections.close()	
		return jsonify({'selec_set':selections})

	else:
		get_selections.close()
		return "no_selections"

@mp_ajax.route("/add_work_task_or_note",methods= ['POST'])
def add_work_task_or_note():
	return None

#		if ans.type == "no_extra":
#	cursor.close()
