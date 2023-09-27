
#from flask_googlemaps import Map
from launch import db
from flask_login import login_user , current_user, login_required
from launch.models.models import User, market_particulars
from launch.functions.data_base_procedures import add_to_selections_with_parents, counter,last_input_to_select_set, find_propagations,delete_last_from_queue, sort_answers_and_add,add_to_selections_without_parents,get_selection_keys, check_selection_set,delete_last_from_object_queue, sort_answers_and_add_objects, add_to_selections_without_parents_objects,add_to_selections_with_parents_objects,collect_object_selections,update_last_data_entry_mp
from launch.functions.access_record_procedures import update_last_user_access
from flask import Blueprint, render_template, redirect, url_for, request, flash, session,jsonify
import mysql.connector
import string
import random
import datetime

spatial = Blueprint('spatial' , __name__)

@spatial.route("/get_post_code_data",methods= ['POST'])
def post_code_data():
	get_data=db.cursor()
	postcode=request.form.get('postcode')
	query=f"SELECT `latitude`,`longitude` from spatial_db.postcodelatlng where `postcode` = '{postcode}';"
	get_data.execute(query)
	latlong = get_data.fetchall()
	get_data.close()
	data = {'latitude':latlong[0][0],'longitude':latlong[0][1]}
	return jsonify(data)

	return None
#<script>
#$( document ).ready(function() {
#      $("#show_map").click(function(event){
#        alert("working")
#
#        .done(function(data) {
#          alert(data.latitude);
#      });
#      });
#});
#</script>
#$("#ajax_pc").on('submit',function(e){
#    e.preventDefault();
#   e.stopPropagation();

#    $.ajax({
#    data : {postcode:$('#postcode_input').val()},
#    type : 'POST',
#    url : "/get_post_code_data",
 #   success: function(data){
#    }
#    })
#});


  #      success: function(data){
   #        console.log(data);
    #    },
     #   error: function(error) {
      #     console.log(error);
      #  }  


