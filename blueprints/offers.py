"""
from launch import db
from flask_login import login_user , current_user
from launch.models.models import User, market_particulars, answer 
from launch.functions.data_base_procedures import add_to_selections_with_parents, counter,last_input_to_select_set, find_propagations,delete_last_from_queue, sort_answers_and_add,add_to_selections_without_parents,get_selection_keys, check_selection_set,delete_last_from_object_queue, sort_answers_and_add_objects, add_to_selections_without_parents_objects,add_to_selections_with_parents_objects,collect_object_selections,update_last_data_entry_mp
from launch.functions.access_record_procedures import update_last_user_access
"""
from flask import Blueprint, render_template, redirect, url_for, request, flash, session,jsonify
import mysql.connector
import string
import random
import datetime

offers = Blueprint('offers' , __name__)

@offers.route("/new_offer/<mp>", methods=["POST"])
def new_offer(mp):
	return render_template("new_offer.html")