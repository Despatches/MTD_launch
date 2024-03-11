# from flask_googlemaps import GoogleMaps
# from flask_googlemaps import Map
from launch import db
from flask_login import login_user, current_user, login_required
from launch.Objects.selections import market_particular_selection
from launch.models.models import User, market_particulars, freehold, templates
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
    jsonify,
)
import mysql.connector
from launch.blueprints.form_templates.templates import templates
import string
import random
import datetime
from werkzeug.utils import secure_filename
import base64


mp = Blueprint("mp", __name__)


# display a list of all market particulars user is attatched to
@mp.route("/newmp/<user_type>")
@login_required
def newmp(user_type):
    return render_template("new_mp_form.html", user_type=user_type)


@mp.route("/newmp", methods=["POST"])
@login_required
def mp_proceed():
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

    def allowed_file(filename):
        return (
            "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )

    sudo_name = request.form.get("sudo_name")
    market_type = request.form.get("market_type")
    if sudo_name == None or len(sudo_name) <= 1:
        flash("provide a name to identify the market particulars")
        return redirect(url_for("mp.newmp", user_type=user_type))

    create_mp = db.cursor()
    cid = current_user.id
    mp_creator = cid

    cover_image = "none"
    filename = "none"
    if "cover_image" not in request.files:
        cover_image = "none"
    elif request.files["cover_image"].filename == "":
        cover_image = "none"
    else:
        cover_image = request.files["cover_image"]
        if cover_image and allowed_file(cover_image.filename):
            filename = secure_filename(cover_image.filename)
            if len(filename) > 30:
                filename = filename[0:30]

    if current_user.agent == True:
        query = "call particulars_and_objects.agent_new_mp (%s,%s,%s, %s, %s);"
    else:
        query = "call particulars_and_objects.new_market_particulars_by_vendor(%s,%s,%s, %s, %s);"

    # if user_type=="vendor":
    # query = 'call particulars_and_objects.new_market_particulars(%s,%s,%s);'

    # elif user_type=="agent":
    # query = "call particulars_and_objects.agent_new_mp (%s,%s,%s);"

    if cover_image != "none":
        cover_image = base64.b64encode(cover_image.stream.read())
    if not market_type == "fully_custom":
        prc_last_id = "select last_insert_id();"
        params = (cid, cid, sudo_name, cover_image, filename)
        create_mp.execute(query, params)
        db.commit()
        create_mp.execute(prc_last_id)
        last_insert = create_mp.fetchall()
        new_mp_id = last_insert[0][0]
        create_mp.close()

        return redirect(url_for("mp.selectedmp", particular_id=new_mp_id))
        # return redirect(url_for('mp.mp_basic',particular_id = new_mp_id, selec_set_ID=selec_set))
    else:
        return redirect(url_for("mp.selectedmp", particular_id=new_mp_id))
        # return redirect(url_for('mp.mp_basic', particular_id =new_mp_id, selec_set_ID=selec_set))


# see revisons to market particulars over time


def db_null_bool_eval(bool_data):
    if bool_data != 1:
        bool_date = False
    else:
        bool_data = True
    return bool_data


class market_particulars_set:
    def __init__(self, db_row):
        self.id = db_row[0]
        self.name = db_row[1]
        self.creation_date = db_row[2]
        self.confirmed_on_the_market = db_null_bool_eval(db_row[3])
        self.active_offers = db_null_bool_eval(db_row[4])
        self.last_user_to_change = db_row[5]
        self.last_data_change = db_row[6]
        self.most_recent_access = db_row[7]
        if (
            not self.last_user_to_change == None
            or self.last_user_to_change == current_user.id
        ):
            if datetime.datetime(self.last_data_change) > datetime.datetime(
                self.most_recent_access
            ):
                self.updates = True
            else:
                self.updates = False
        else:
            self.updates = False


def fetch_mps():
    get_mps = db.cursor()
    query = "SELECT market_particulars_ID,sudo_name, creation, confirmed_on_the_market,active_offers,last_user_to_change,last_data_change,`market_particulars_access_log`.`most_recent_access`\
        FROM `particulars_and_objects`.`market_particulars`\
        LEFT JOIN `particulars_and_objects`.`market_particulars_access_log`\
        on `market_particulars`.market_particulars_ID = `market_particulars_access_log`.`market_particulars`\
        AND particulars_and_objects.`market_particulars`.vendor_ID = `market_particulars_access_log`.`user`\
        LEFT JOIN user_data.agency_assigned_to_market_partics\
        on user_data.agency_assigned_to_market_partics.market_particulars = particulars_and_objects.market_particulars.`market_particulars_ID`\
        WHERE user_data.agency_assigned_to_market_partics.`agency` = %s;"

    params = (current_user.agency,)
    get_mps.execute(query, params)
    data = get_mps.fetchall()
    row_count = len(data)
    if not row_count == 0:
        d = []

        for mp in data:
            mp = market_particulars_set(mp)
            d.append(mp)
        data = d
    else:
        data = "none"
    get_mps.close()
    return {"data": data, "row_count": row_count}


@mp.route("/market_partics/agency")
@login_required
def display_mp():
    if current_user.agency != False:
        mps = fetch_mps()
    else:
        return redirect("/market_partics/vendor")

    headings = (
        "ID",
        "name",
        "Genesis Date",
        "Market Conformation",
        "active offers",
        "unread updates",
    )
    return render_template(
        "display_mp_agent.html",
        headings=headings,
        data=mps["data"],
        row_count=mps["row_count"],
        agent=current_user.agent,
    )


@mp.route("/market_partics/vendor")
@login_required
def display_mp_vendor():
    get_mps = db.cursor()
    query = "SELECT market_particulars_ID,sudo_name, creation, confirmed_on_the_market,active_offers,last_user_to_change,last_data_change,`market_particulars_access_log`.`most_recent_access`, cover_img, cover_name\
        FROM `particulars_and_objects`.`market_particulars`\
        LEFT JOIN `particulars_and_objects`.`market_particulars_access_log`\
        on `market_particulars`.market_particulars_ID = `market_particulars_access_log`.`market_particulars`\
        AND particulars_and_objects.`market_particulars`.vendor_ID = `market_particulars_access_log`.`user`\
        LEFT JOIN user_data.agency_assigned_to_market_partics\
        on user_data.agency_assigned_to_market_partics.market_particulars = particulars_and_objects.market_particulars.`market_particulars_ID`\
        WHERE `particulars_and_objects`.`market_particulars`.`vendor_ID` = %s;"

    params = (current_user.id,)
    get_mps.execute(query, params)
    data = get_mps.fetchall()
    row_count = len(data)
    if not row_count == 0:
        d = []

        for mp in data:
            mp = market_particulars_set(mp)
            d.append(mp)
        data = d
    else:
        data = "none"
    get_mps.close()
    headings = (
        "ID",
        "name",
        "Genesis Date",
        "Market Conformation",
        "active offers",
        "unread updates",
    )
    return render_template(
        "display_mp_agent.html",
        headings=headings,
        data=data,
        row_count=row_count,
        agent=current_user.agent,
    )


# display basic data about objects contained within a market particuars requires dashboard layout


@mp.route("/market_partics/<particular_id>", methods=["GET"])
@login_required
def selectedmp(particular_id):
    freehold_headings = ("name", "ID", "Date First Specified")
    freehold_share_headings = "reference_name"
    c_n_s_headings = ("reference_name`", "registered at companies house")
    leasehold_headings = ("Reference Name", "Freehold Type", "Freehold ID")
    headings = {
        "freehold": freehold_headings,
        "freehold_share": freehold_share_headings,
        "c_n_s": c_n_s_headings,
        "leasehold": leasehold_headings,
    }

    setfind = db.cursor()
    mp = market_particulars(particular_id)

    if int(current_user.id) == (int(mp.user_creator) or int(mp.vendor)):
        # mp_objects = fetch_market_particular_components(particular_id)
        # mp.form_status()
        mp.fetch_market_particular_components()
        mp.TA6_and_subs()
        mp.stamp_evaluation()
        mp.auto_objects()
        if not mp.TA6 == None:
            TA6_data = json.dumps(
                {
                    "data": mp.TA6.data,
                    "sub_forms": mp.TA6.sub_forms,
                    "form": mp.TA6.form,
                }
            )
        else:
            TA6_data = None
        for stamp in mp.stamps.stamps:
            mp.stamps.stamps[stamp] = mp.stamps.stamps[stamp].__dict__

        return render_template(
            "mp_views_and_profiles/mp_profile.html",
            sudo_name=mp.sudo_name,
            creation_date=mp.creation,
            mid=mp.id,
            particular_id=particular_id,
            mp=mp,
            headings=headings,
            TA6_data=TA6_data,
        )
    else:
        return redirect(url_for("blu_main.profile", userid=current_user.id))


# selection page to select data for the market particulars selections table


@mp.route("/findmp_set/<particular_id>")
@login_required
def check_set(particular_id):
    selec_set_ID = session["current_mp_set"][1]
    selec_set_ID = check_selection_set(particular_id, current_user.id)
    return render_template("answer_module/client_based_answer_module.html")


@mp.route("/mp/data/<particular_id>/<selec_set_ID>")
@login_required
def current_mp_data(particular_id, selec_set_ID):
    go = db.cursor()

    # query ="select * from selection_routines.market_particulars_selections where selec_set_ID=%s and `parent_unique_selection_ID`= null;"
    # params = (selec_set_ID,)

    # query = "insert into `selection_routines`.`mp_selection_set_queue`(mp_selection_set_ID,Q_ID,prop_order,propagating_unique_selec_ID) Values(%s,'TFU100',1,0)"
    # params = (selec_set_ID,)
    # go.execute(query,params)
    # db.commit()
    go.close()


#   return render_template("synopsis.html" ,particular_id=particular_id, urlr=urlr, number_of_selec_sets=number_of_selec_sets,selection_sets=selection_sets)


# overview profile of a freehold within a market particulars


@mp.route("/freehold/<holding_ID>/<selec_set_ID>/overview")
@login_required
def freehold_profile(holding_ID, selec_set_ID):
    freehold_collect = db.cursor()
    params = (holding_ID,)
    query = "SELECT \
                `holding_ID`,\
                `market_particulars`,\
                `creating_user`,\
                `reference_name`,\
                `provisioned_ID`,\
                `date_first_specified`,\
                `X_location_point`,\
                `Y_location_point`\
             from `selection_routines`.`unassigned_freehold` where holding_ID=%s"
    freehold_collect.execute(query, params)
    unassigned_freehold_data = freehold_collect.fetchall()
    freehold_data = freehold(unassigned_freehold_data[0])
    #   ld = [unassigned_freehold_data[6], unassigned_freehold_data[7]]
    #   ld =json.dumps(ld)
    table_name = "`selection_routines`.`selections_for_unassigned_freehold`"
    freehold_selections = collect_object_selections(
        table_name, holding_ID, selec_set_ID
    )

    freehold_collect.close()
    return render_template(
        "/create_mp_objects/unassigned_freehold.html",
        selec_set_ID=selec_set_ID,
        particular_id=session["current_mp_set"][0],
        freehold_data=freehold_data,
    )


#   return render_template("/create_mp_objects/unassigned_freehold.html",
#                           location_data=ld,selec_set_ID=selec_set_ID,holding_ID=holding_ID,
#                           particular_id=session['current_mp_set'][0], reference_name=reference_name)


@mp.route("/leasehold/<holding_ID>/<selec_set_ID>/overview")
def leasehold_profile(holding_ID, selec_set_ID):
    leasehold_collect = db.cursor()
    params = (holding_ID,)
    query = (
        "select * from `selection_routines`.`unassigned_leasehold` where holding_ID=%s"
    )
    leasehold_collect.execute(query, params)
    unassigned_freehold_data = freehold_collect.fetchone()
    reference_name = unassigned_freehold_data[3]
    ld = [unassigned_freehold_data[6], unassigned_freehold_data[7]]
    ld = json.dumps(ld)

    table_name = "`selection_routines`.`selections_for_unassigned_freehold`"
    freehold_selections = collect_object_selections(
        table_name, holding_ID, selec_set_ID
    )

    freehold_collect.close()
    return render_template(
        "/create_mp_objects/unassigned_freehold.html",
        location_data=ld,
        selec_set_ID=selec_set_ID,
        holding_ID=holding_ID,
        particular_id=session["current_mp_set"][0],
        reference_name=reference_name,
    )


# selections for subsidery objects within a market particulars

# collection of form selections regarding subsidery objects within market particulars

# from to change selections for market particulars

# colect from form change selections for standard amrket particulars selections


@mp.route(
    "/change_selection/<particular_id>/<selec_set_ID><unique_selection_ID>/",
    methods=["POST"],
)
@login_required
def change_selection(particular_id, selec_set_ID, unique_selection_ID):
    particular_id = particular_id
    change_selec = db.cursor()
    answers = []
    if session["no_extra"] != 0:
        form_answer = request.form.get("selections")
        if form_answer == None:
            flash("Please make a selection or skip", "non_text")
            return redirect(
                url_for(
                    "mp.mp_basic_props",
                    particular_id=particular_id,
                    selec_set_ID=selec_set_ID,
                    selections=form_answer,
                )
            )

    query = "update selection_routines.market_particulars_selections set selection_ans = %s \
            where parent_set = %s and unique_selection_ID = %s"

    params = (form_answer, selec_set_ID, unique_selection_ID)
    change_selec.execute(query, params)
    db.commit()

    # update_last_data_entry_mp(selec_set_ID,current_user.id)
    return redirect(url_for("synopsis", particular_id=particular_id))


@mp.route("/newfhshare/pro/<particular_id>", methods=["POST"])
@login_required
def newfreehold_share_proceed(particular_id):
    mp = market_particulars(particular_id)
    reference_name = request.form.get("reference_name")
    Title_ID = request.form.get("Title_ID")
    share_percentage = request.form.get("share percentage")
    if reference_name == None or len(reference_name) <= 1:
        flash("provide a name to identify the the new freehold_share")
    if share_percentage == None or len(share_percentage) < 1:
        flash(
            "provide a percentage to indicate how much of freehold this freehold share conveys(this can be changed at a later stage)"
        )
    elif share_percentage == "100":
        flash(
            "this object will be created as a full freehold instead of a freehold share if the share value remains at %100",
            "full_freehold",
        )
        return redirect(url_for("mp.newfreeholdshare", particular_id=particular_id))

    add_title = db.cursor()
    query = "CALL selection_routines.add_unassigned_freehold_to_mp(%s,%s,%s,%s)"
    params = (mp.id, current_user.id, reference_name, Title_ID)
    add_title.execute(query, params)
    db.commit()
    add_title.close()
    return redirect(url_for("mp.selectedmp", particular_id=particular_id))


@mp.route("/View_code")
@login_required
def redeem_view_code():
    return render_template("redeem_view_code.html")


@mp.route("/redeem_code", methods=["POST"])
def redeem_view_code_proceed():
    view_code = request.form.get("view_code")
    vc = db.cursor()
    params = (f"{view_code}",)
    query = "SELECT EXISTS(SELECT access_code FROM mp_disclosure_access.mp_access_requests WHERE access_code = %s) as truth;"
    vc.execute(query, params)
    code_exists = vc.fetchone()
    if not code_exists[0] == 1:
        vc.close()
        flash(
            "provisioned view code is invlid, please try check for errors and try again or request a new access code"
        )
        return redirect(url_for("mp.redeem_view_code"))

    params = (f"{view_code}", current_user.id)
    query = "call mp_disclosure_access.become_prospective_buyer(%s,%s)"
    vc.execute(query, params)
    db.commit()
    query = "select @Vmarket_prticulars"
    vc.execute(query)
    view_mp = vc.fetchone()
    vc.close()
    return redirect(url_for("mp.selectedmp", particular_id=view_mp[0]))


@mp.route("/prospects")
@login_required
def prospect_properties():
    prospects = db.cursor()
    query = "SELECT market_particulars_ID,sudo_name, confirmed_on_the_market \
    from particulars_and_objects.market_particulars\
    join mp_disclosure_access.prospective_buyer on particulars_and_objects.market_particulars.market_particulars_ID = mp_disclosure_access.prospective_buyer.market_particulars\
    where mp_disclosure_access.prospective_buyer.user_ID = %s"

    params = (current_user.id,)

    prospects.execute(query, params)

    prospect_props = prospects.fetchall()

    return render_template("prospect_properties.html", props=prospect_props)


def create_rand_string(string_length):
    code = string.ascii_letters
    code2 = string.digits
    codes = (code, code2)
    rand = ""
    counter = 0
    while counter != string_length:
        a = character_type(codes)
        rand = f"{rand}" + (random.choice(a))
        counter += 1
    return rand


@mp.route("/view_code_create/<particular_id>")
@login_required
def create_view_code(particular_id):
    def character_type(codes):
        choice = random.choice(codes)
        return choice

    exists = 1
    count = 0

    while exists == 1:
        count += 1
        if count == 5:
            flash("error producing view code request again or try again later")
            return f"{exists}"
            return redirect(url_for("mp.selectedmp", particular_id=particular_id))
        view_code = create_rand_string(10)

        check_code = db.cursor()

        params = (f"{view_code}",)

        query = "SELECT exists(SELECT access_code FROM mp_disclosure_access.mp_access_requests WHERE access_code = %s) as truth;"
        check_code.execute(query, params)
        e = check_code.fetchone()
        exists = e[0]

    return render_template(
        "new_view_code.html", view_code=view_code, particular_id=particular_id
    )


@mp.route("/validate_view_code/<particular_id>/<view_code>")
@login_required
def validate_view_code(particular_id, view_code):
    vcv = db.cursor()
    params = (particular_id, f"{view_code}", current_user.id)
    query = "INSERT INTO `mp_disclosure_access`.mp_access_requests(market_particulars,access_code,issue_timestamp,issueing_user)\
            values(%s,%s,curtime(),%s);"
    vcv.execute(query, params)
    db.commit()
    vcv.close()
    return redirect(url_for("mp.selectedmp", particular_id=particular_id))


@mp.route("/prospecting/<particular_id>")
@login_required
def load_prospect_prop(particular_id):
    mp_objects = fetch_market_particular_components(particular_id)
    total_objects = mp_objects[0]
    object_list = mp_objects[1]
    location_data = "no_map"

    return render_template(
        "mp_views_and_profiles/prospective_buyer_view.html",
        particular_id=particular_id,
        freehold_share_data=object_list[1][1],
        leasehold_data=object_list[2][1],
        cns_data=object_list[0][1],
        freehold_data=object_list[3][1],
        location_data=location_data,
        single_object=None,
    )


@mp.route("/surveyoffreehold")
def freehold_survey():
    return render_template("survey_options.html")


@mp.route("/<particular_id>/new_offer")
def new_mp_offer(particular_id):
    def barter_components():
        return 0

    return render_template("new_mp_offer.html")


@mp.route("/<form_code>/issue_code")
def form_issue_code(form_code):
    issue_code = create_rand_string()
    query = "INSERT INTO `form_data`.`form_issue_code` (form_id,view_code, creation_date_time) VALUES (%s,%s,now())"
    cursor = db.cursor()

    params = (form_code, issue_code)
    cursor.execute(query, params)

    cursor.close()
    return render_template("new_mp_offer.html", issue_code=issue_code)


# @mp.route("/disclosure_package")
# def disclosure_package(particular_id):


#   mp.route("/market_partics")
#   def create_mp(,methods=['POST']):
#       create_mp = db.cusor(prepared=True)
#       cid = current_user.id
#       mp_creator = cid
#       sudo_name = request.form.get('name')
#       vendor = cid if request.form.get = ('user_vendor')
#       if not vendor == cid:
#
#       else:
#           procedure_new_mp = "call particulars_and_objects.new_market_particulars(%s,%s,%s)"
#           params = (cid,cid,sudo_name)
#           create_mp.execute(procedure_new_mp,params)
#           create_mp.close()
#           return 0
