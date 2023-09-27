from flask_googlemaps import GoogleMaps,Map
from launch import db
from flask_login import login_user , current_user
from launch.models.models import User, market_particulars, answer 
from launch.functions.data_base_procedures import add_to_selections_with_parents, counter,last_input_to_select_set, find_propagations,delete_last_from_queue, sort_answers_and_add,add_to_selections_without_parents,get_selection_keys, check_selection_set,delete_last_from_object_queue, sort_answers_and_add_objects, add_to_selections_without_parents_objects,add_to_selections_with_parents_objects
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
import mysql.connector

static_q = Blueprint('static_q' , __name__)

@static_q("/oilandtanks")
def add_tank_micro_disclosure()
	return render_template('micro_disclosure_oiltanks.html')


@static_q("/oilandtanks")
def recieve_data()
	