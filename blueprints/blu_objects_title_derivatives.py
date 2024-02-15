# from flask_googlemaps import GoogleMaps
# from flask_googlemaps import Map
from launch import db
from flask_login import login_user, current_user
from launch.models.models import User, market_particulars
from launch.functions.data_base_procedures import (
    add_to_selections_with_parents,
    counter,
    last_input_to_select_set,
    find_propagations,
    delete_last_from_queue,
    sort_answers_and_add,
    add_to_selections_without_parents,
    get_selection_keys,
    check_selection_set,
    delete_last_from_object_queue,
    sort_answers_and_add_objects,
    add_to_selections_without_parents_objects,
    add_to_selections_with_parents_objects,
    collect_object_selections,
    update_last_data_entry_mp,
    fetch_market_particular_components,
)
from launch.functions.access_record_procedures import update_last_user_access
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session,
    json,
)
import mysql.connector
import string
import random
import datetime

title_derivatives = Blueprint("title_derivatives", __name__)


@title_derivatives.route("/new_leasehold/<particular_id>")
def new_leasehold(particular_id):
    return render_template(
        "create_mp_objects/new_leasehold.html", particular_id=particular_id
    )


@title_derivatives.route("/new_leasehold/<particular_id>", methods=["POST"])
def new_leasehold_proceed(particular_id):
    mp = market_particulars(particular_id)
    cursor = db.cursor()
    Address = request.form.get("Address")
    reference_name = request.form.get("reference_name")
    freehold_ID = request.form.get("freehold_ID")
    X_location_point = request.form.get("lat")
    y_location_point = request.form.get("lng")

    query = "INSERT INTO `selection_routines`.`unassigned_leasehold`\
		(\
			`market_particulars`,\
			creating_user,\
			`reference_name`,\
			`freehold_ID`,\
			date_first_specified,\
			X_location_point,\
			Y_location_point\
		)\
		VALUES\
		(\
			%s,\
			%s,\
			%s,\
			%s,\
			curtime(),\
			%s,\
			%s\
		);"

    params = (
        particular_id,
        current_user.id,
        reference_name,
        freehold_ID,
        X_location_point,
        y_location_point,
    )
    cursor.execute(query, params)

    db.commit()

    cursor.close()
    return redirect(url_for("mp.selectedmp", particular_id=particular_id))


@title_derivatives.route("/new_cns/<particular_id>")
def new_cns(particular_id):
    return render_template(
        "create_mp_objects/new_cns.html", particular_id=particular_id
    )


@title_derivatives.route("/new_cns/<particular_id>")
def new_cns_proceed(particular_id):
    mp = market_particulars(particular_id)
    reference_name = request.form.get("reference_name")
    Title_ID = request.form.get("Title_ID")
    if reference_name == None or len(reference_name) < 4:
        pass
    add_title = db.cursor()
    query = "call selection_routines.add_unassigned_freehold_to_mp(%s,%s,%s,%s)"
    params = (mp.id, current_user.id, reference_name, Title_ID)
    add_title.execute(query, params)
    db.commit()
    add_title.close()

    mp.close()
    return redirect(url_for("mp.selectedmp", particular_id=particular_id))


# add a new freehold


@title_derivatives.route("/newfh/<particular_id>", methods=["GET"])
def newfreehold(particular_id):
    return render_template(
        "create_mp_objects/new_mp_freehold.html", particular_id=particular_id
    )


# submit form to add a new freehold to market particulars


@title_derivatives.route("/newfh/<particular_id>", methods=["POST", "GET"])
def newfreehold_proceed(particular_id):
    mp = market_particulars(particular_id)
    reference_name = request.form.get("reference_name")
    Title_ID = request.form.get("Title_ID")
    if reference_name == None or len(reference_name) < 4:
        pass
    add_title = db.cursor()
    query = "call selection_routines.add_unassigned_freehold_to_mp(%s,%s,%s,%s)"
    params = (mp.id, current_user.id, reference_name, Title_ID)
    add_title.execute(query, params)
    db.commit()
    add_title.close()

    mp.close()
    return redirect(url_for("mp.selectedmp", particular_id=particular_id))


# add a new freehold share to market particulars


@title_derivatives.route("/newfhshare/<particular_id>", methods=["GET"])
def newfreeholdshare(particular_id):
    return render_template(
        "create_mp_objects/new_mp_freehold_share.html", particular_id=particular_id
    )


@title_derivatives.route("/newfh/<particular_id>", methods=["POST", "GET"])
def newfreeholdshare_proceed(particular_id):
    mp = particular_id
    reference_name = request.form.get("reference_name")
    Title_ID = request.form.get("Title_ID")
    add_title = db.cursor()


# complete form to add new market particulars

# @mp.route("/newfhshare/<particular_id>",methods=['GET'] )
# def newfreeholdshare_proceed(particular_id):

# create a new market particulars web page render
