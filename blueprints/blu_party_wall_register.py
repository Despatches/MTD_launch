from launch import db
from flask_login import login_user, current_user, login_required
from launch.blueprints.form_templates.json_form_templates import template_sort
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
)
from launch.functions.access_record_procedures import update_last_user_access
from launch.blueprints.form_templates import template_data_transitions
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session,
    jsonify,
    json,
)
from launch.blueprints.form_templates.part_wall_entry.Party_wall_entry import (
    party_wall_entry,
)
import mysql.connector
import string
import random
import datetime

party_Wall_register = Blueprint("party_Wall_register", __name__)


@party_Wall_register.route("/lodge_party_wall_new_entry")
def lodge_party_wall_new_entry():
    template = party_wall_entry["template"]
    # return basic_template_render(template, 'single', '/pw_register_submission')


@party_Wall_register.route("/search_register")
def search_register():
    return render_template("party_wall_register/search_register.html")


# launch/templates/party_wall_register/search_register.html
def generic_input(pairs, table):
    cursor = db.cursor()

    u_num = 0
    rows = ""
    values = ""

    for p in pairs:
        u_num += 1
        if u_num == 1:
            rows = f"{p['row']} "
            values = f"{p['value']} "
        else:
            rows = f"{rows} ,{p['row']}"
            values = f"{values} ,{p['value']}"

    query = f"INSERT into {table}\
				({rows})\
				VALUES({values})"

    cursor.execute(query)

    db.commit()

    cursor.close()


@party_Wall_register.route("/pw_register_submission", methods=["POST"])
def pw_register_submission():
    # form = get_form_id()
    inputs = json.loads(request.form.get("inputs"))
    print(inputs)
    template_set = party_wall_entry
    pairings = template_set["pairings"]
    full_input_set = {"pairs": [], "details": [], "docu": []}
    for key in inputs:
        equals = pairings[key]
        final_inputs = template_data_transitions.form_equals_evaluation(
            equals, inputs[key], None
        )
        print(final_inputs)
        for key in final_inputs:
            full_input_set[key] += final_inputs[key]
    print(full_input_set["pairs"])
    # opportunity to add irregular data to register e.g user provisioning entry
    full_input_set["pairs"].append({"row": "user_initiator", "value": current_user.id})
    print(full_input_set["pairs"])
    generic_input(
        full_input_set["pairs"], "`party_wall_register`.party_wall_entry_data"
    )
    return "success"


@party_Wall_register.route("/search_pw_register", methods=["POST"])
def search_pw_register():
    address = json.loads(request.form.get("address"))
    postcode = address["postcode"]
    base_query = """SELECT {}
	 			FROM `party_wall_register`.party_wall_entry_data """
    if request.form.get("filtered") == "1":
        filters = json.loads(request.form.get("filters"))
        if filters["address_type"] == "both":
            base_query += "WHERE (psn_postcode = '{postcode}' OR prn_postcode = '{postcode}')".format(
                postcode=postcode
            )
        elif filters["address_type"] == "psn":
            base_query += "WHERE psn_postcode = {}".format(f"'{postcode}'")
        elif filters["address_type"] == "prn":
            base_query += "WHERE prn_postcode = {}".format(f"'{postcode}'")

        if filters["notice_type"] != "all":
            if len(filters["notice_type"]) == 1:
                notice_query = "AND party_notice_type ='{}'".format(
                    filters["notice_type"][0]
                )
                base_query += notice_query
            else:
                notice_query = "AND party_notice_type IN ('{}'".format(
                    filters["notice_type"][0]
                )
                for f in filters["notice_type"][1:]:
                    notice_query += f",'{f}'"
                notice_query += ")"
                base_query += notice_query

    # if filters['status_type'] != 'all'
    else:
        base_query += (
            "WHERE (psn_postcode = '{postcode}' OR prn_postcode = '{postcode}')".format(
                postcode=postcode
            )
        )
        if address["line_1"] != "":
            base_query += (
                "AND (psn_address_line_1 = '{}' OR prn_address_line_1 = '{}')".format(
                    address["line_1"], address["line_1"]
                )
            )
        if address["line_2"] != "":
            base_query += (
                "AND (psn_address_line_2 = '{}' OR prn_address_line_2 = '{}')".format(
                    address["line_2"], address["line_2"]
                )
            )
        if address["town_or_city"] != "":
            base_query += "AND (psn_postcode_address_town_or_city = '{}' OR prn_postcode_address_town_or_city = '{}')".format(
                address["town_or_city"], address["town_or_city"]
            )

    cursor = db.cursor()
    collect_set = [
        "form_id",
        "psn_postcode",
        "psn_address_line_1",
        "psn_address_line_2",
        "psn_postcode_address_town_or_city",
        "psn_UPRN",
        "prn_postcode",
        "prn_address_line_1",
        "prn_address_line_2",
        "prn_postcode_address_town_or_city",
        "prn_UPRN",
        "party_notice_type",
        "date_of_service",
    ]
    collect_string = "{}".format(collect_set[0])
    for c in collect_set[1:]:
        collect_string += f",{c}"
    query = base_query.format(collect_string)

    print(query)
    cursor.execute(query)

    results = cursor.fetchall()
    cursor.close()
    if len(results) < 1:
        return "none"
    else:
        entries = []
        for r in results:
            new_object = {}
            object_length = len(collect_set)
            n = 0
            while n < object_length:
                new_object[collect_set[n]] = r[n]
                n += 1
            entries.append(new_object)
        return json.dumps(entries)


@party_Wall_register.route("/record_search/<notice>")
@login_required
def search_pw_records(notice):
    form_name = party_wall_entry["template"]["form_identifier"]
    notice = template_data_transitions.form_results_collection(
        template_data_transitions.collect_form_data(
            party_wall_entry["query_columns"],
            notice,
            "`party_wall_register`.party_wall_entry_data",
        ),
        party_wall_entry["query_select"],
        notice,
        form_name,
    )

    return render_template(
        "party_wall_register/view_notice.html",
        notice=notice,
        json_notice=json.dumps(notice.__dict__),
    )


@party_Wall_register.route("/user_pw_records")
@login_required
def user_relevant_lodgements():
    return 0
