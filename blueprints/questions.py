
from launch import db
from flask_login import login_user , current_user
from launch.models.models import User, market_particulars, answer 
from launch.functions.data_base_procedures import add_to_selections_with_parents, counter,last_input_to_select_set, find_propagations,delete_last_from_queue, sort_answers_and_add,add_to_selections_without_parents,get_selection_keys, check_selection_set,delete_last_from_object_queue, sort_answers_and_add_objects, add_to_selections_without_parents_objects,add_to_selections_with_parents_objects,collect_object_selections,update_last_data_entry_mp
from launch.functions.access_record_procedures import update_last_user_access
from flask import Blueprint, render_template, redirect, url_for, request, flash, session,jsonify
import mysql.connector
import string
import random
import datetime

questions = Blueprint('questions' , __name__)

def find_answers(Q_ID):
	q_d = db.cursor()
	query = "SELECT * from `questions_answers`.`answers` where Q_ID = %s"
	params =(Q_ID,)
	q_d.execute(query,params)
	answers = q_d.fetchall()
	return (answers)

@questions.route("/question_layout")
def find_data():
	q_d = db.cursor()
	query = "SELECT * from `questions_answers`.`questions`"
	q_d.execute(query)
	base_questions = q_d.fetchall()
	qp=[]
	for q in base_questions:
		answers= find_answers(q[1])
		if answers == None:
			q_a_set =(q,None)
		else:
			q_a_set =(q,answers)
		qp.append(q_a_set)
	base_questions = qp
	return render_template("question_layout.html",base_questions=base_questions)

#@questions.route("/_get_answers/Q_ID")
#def find_answers(Q_ID):
#	q_d = db.cursor()
#	query = "SELECT * from `questions_answers`.`answer` where Q_ID = '%s'"
#	params =(Q_ID,)
#	q_d.execute(query,params)
#	answers = q_d.fetchall()
#	return jsonify(answers)
#
#def find_props(full_code):
#	q_d = db.cursor()
#	query = "SELECT * from `questions_answers`.`questions` where base_q = TRUE"
