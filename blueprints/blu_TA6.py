from launch import db
from flask_login import login_user, current_user, login_required
from launch.models.models import User, market_particulars, new_form_object, templates
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
from launch.blueprints.form_templates.standard_TA6.standard_TA6 import (
    template as standard_ta6_template,
    bounds_radio_options,
)
from launch.blueprints.form_templates.json_form_templates import (
    template_sort,
    # basic_template_render,
)
from launch.blueprints.form_templates.new_db_sql_code_writer import (
    create_new_sql_table,
    element_relevancy,
)
from launch.blueprints.form_templates.obj_form_collection import (
    collect_form_data,
    form_results_collection,
    input_type_jiggling,
    form_equals_evaluation,
    multi_line_input,
    generic_input,
    flow_control_tiers,
    bool_java_conversion,
    print_for_eqivilents,
    print_text_modifier,
    work_task as work_task_class,
    evaluate_form_mp_relation,
)
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
from launch.blueprints.form_templates import template_objects
import mysql.connector
import string, copy, random, datetime
import ast

TA6_forms = Blueprint("TA6_forms", __name__)


@TA6_forms.route("/cheat")
def cheat():
    return render_template("cheat.html")


current_year = 2022

""" class result:
def __init__(self):
        self."""
# query_parings represents the paired item stores in template file matching q_identifier


def get_form_id():
    f = request.form.get("form_ID")
    form = int(f)
    return form


def update_statement(updates, form, table):
    cursor = db.cursor()

    u_num = 0
    lines = ""
    for u in updates:
        u_num += 1
        if u_num == 1:
            line = f"{u['row']} = {u['value']}"
        else:
            line = f",{u['row']} = {u['value']}"
        lines = f"{lines} {line}"

    query = f"UPDATE {table}\
        SET\
            {lines}\
        where form_id = %s"

    params = (form,)

    cursor.execute(query, params)

    db.commit()

    cursor.close()


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


def form_collection():
    form = get_form_id()
    collect = request.form.get("inputs")
    collected_values = json.loads(service_charges)


def form_particular_creation(form_name, p_type, p_id):
    result = evaluate_form_mp_relation(form_name, p_type, p_id)
    cursor = db.cursor()

    if result[0] == None:
        query = f"INSERT into `form_data`.`{form_name}_data`(\
                    ceation_moment,\
                    user_initiator)\
                VALUES(\
                    curtime(),\
                    %s);"

        params = (current_user.id,)

        cursor.execute(query, params)

        query = f"SELECT form_id from `form_data`.`{form_name}_data` where form_id = (SELECT max(form_id) from `form_data`.`{form_name}_data` where user_initiator = %s)"

        cursor.execute(query, params)
        u_form = cursor.fetchall()
        form = u_form[0][0]

        query = f"INSERT INTO `form_data`.`{form_name}_{p_type}_relationship` (form_id, market_particulars)\
                        VALUES (%s, %s)"

        params = (form, p_id)

        cursor.execute(query, params)

        db.commit()

        cursor.close()

        return (form, "new_form")
    else:
        cursor.close()
        return (result[0], "old_form")


# @TA6_forms.route("/form_submit/<form_set>", methods=["POST"])
@TA6_forms.route("/TA6_Part_1_submit", methods=["POST"])
# def template_form_collect(form_set):
def template_form_collect():
    form = get_form_id()
    inputs = request.form.get("inputs")
    pairs = []
    details = []
    docu = []
    section = request.form.get("section")
    sec_status = request.form.get("sec_status")
    # template_set = templates[form_set]
    template_set = templates["TA6_Part_1"]

    # print(inputs)

    inputs = json.loads(inputs)

    pairings = template_set["pairings"]

    equals = pairings[section]

    final_inputs = form_equals_evaluation(equals, inputs, form)

    pairs += final_inputs["pairs"]

    if len(final_inputs["details"]) > 0:
        query = "INSERT INTO `form_data`.`TA6_Part_1_detail_text` (parent_form, text_content, text_reference) VALUES (%s,%s, %s)"
        cursor = db.cursor()
        cursor.executemany(query, final_inputs["details"])
        cursor.close()

    if len(pairs) > 0:
        """update_statement(pairs, form, "`TA6`.`TA6_Part_1_records`")"""
        if sec_status != "steady":
            pairs.append({"row": "section_marker", "value": sec_status})
        update_statement(pairs, form, "`form_data`.`TA6_Part_1_data`")
    """if len(pairs) > 0:
        details.append({"row":"form_id", 'value':form})
            generic_input(details, "`TA6`.`extra_unformatted_text_TA6_Part_1`")
        generic_input(details, "`form_data`.`TA6_Part_1_data`")"""
    return "success"


@TA6_forms.route("/form_creator")
def form_creator():
    return render_template("Json_form_templating/form_creator.html")


@TA6_forms.route("/TA6_reporting")
def TA6_report():
    return render_template("Json_form_templating/pdf_report.html")


@TA6_forms.route("/test_template_input")
def test_template_input():
    return render_template("Json_form_templating/test_template_input.html")


@TA6_forms.route("/test_template", methods=["POST", "GET"])
def test_template():
    tempy = request.form.get("template")

    tp = {}
    exec(tempy, tp)
    template = tp["template"]
    # from launch.blueprints.form_templates.market_particulars.new_market_particular import template as nmp_temp
    # template = nmp_temp
    # return basic_template_render(template)


@TA6_forms.route("/synopsis_temp")
def template_synopsis():
    return render_template("synopsis_template.html", methods=["POST"])


def bulk_form_collect(form, template_set, *args):
    template = template_set["template"]
    form_results = form_results_collection(
        collect_form_data(template_set["query_columns"], form),
        form,
        template["form_identifier"],
    )
    # form_results.append_data(TA6_Part_1_comp_risk_fraud,)
    form_results.append_data(template_set["meanings"], "meanings")
    form_results.append_data(template_set["pro_meanings"], "pro_meanings")
    form_results.add_element_relevances()
    form_results.exclude_irrelevants()
    # form_results.fraud_risk_comp(templates)

    form_results.append_data_group(template_set["comp_risk_fraud"])
    form_results.evaluate_objects(template_set["object_links"])
    form_results.work_tasks()
    form_results.fetch_detail_data()
    form_results.sub_forms_gather(True)
    gather = False
    if "gather" in args:
        gather = True
    form_results.find_documents(gather)
    form_results.collect_multi_row_data(template_set["sub_tables"])
    return form_results


@TA6_forms.route("/synopsis_temp/<form_name>/<p_type>/<particular_id>")
def collect_synopsis_data(form_name, p_type, particular_id):
    if form_name == "TA6_Par_1":
        template_set = templates[form_name]
        template = template_set["template"]
        results = form_particular_creation(form_name, p_type, particular_id)
        form = results[0]
        if results[1] == "old_form":
            form_results = bulk_form_collect(form, template_set)
            for obj in form_results.objects:
                # form_results.objects[obj] = json.dumps(form_results.objects[obj].__dict__)
                form_results.objects[obj] = form_results.objects[obj].__dict__
            # object_send = json.dumps(form_results.objects)
            object_send = form_results.objects
            # result_send = json.dumps(form_results.data)
            result_send = form_results.data
            """for d in form_results.data:
                print(d,form_results.data[d])"""
            searchable_data = ["fraud", "competancy", "risk"]
            # print(form_results.element_relevances['questions'])
            # sub_tables = json.dumps(form_results.sub_tables)
            sub_tables = form_results.sub_tables
            questions = form_results.element_relevances["questions"]
            sections = form_results.element_relevances["sections"]
            section_names = [
                section["section_name"] for section in template["Sections"]
            ]
            subforms = form_results.sub_forms
            # print(form_results.__dict__)
            # template_send = json.dumps(templates['TA6_Part_1']['template'])

            form_set = {
                "questions": questions,
                "sections": sections,
                "section_names": section_names,
                "results": result_send,
                "form_name": form_name,
                "p_type": p_type,
                "particular_id": particular_id,
                "rsections": form_results.element_relevances["sections"],
                "reached_section": form_results.section_marker,
                "objects": object_send,
                "sub_tables": sub_tables,
                "form": form,
                "searchable_data": searchable_data,
                "sub_forms": subforms,
            }
            return render_template(
                "synopsis_template.jinja",
                form_set=json.dumps(form_set),
                p_type=p_type,
                particular_id=particular_id,
            )

        else:
            return redirect(
                url_for(TA6_Part_1(p_type, particular_id, form=[form, "new"]))
            )
    else:
        data = micro_synop_return(
            {
                "form_name": form_name,
                "root_linkage": p_type,
                "root_linkage_id": particular_id,
            }
        )
        data["form"] = particular_id
        # print(data['form_name'])
        return render_template(
            "synopsis_template.jinja",
            form_set=json.dumps(data),
            p_type=p_type,
            particular_id=particular_id,
        )


"""@TA6_forms.route("/synopsis_temp", methods=['POST'])
def synopsis_temp_create_new_work_task():
    work_task = request.form.get('work_task')
    query = "INSERT INTO `form_data`./`{}_work_tasks(\
                task_creation_date,\
                task_completion_target,\
                task_title,\
                task_body,\
                attatched_identifier,\
                identifier_value)\
                VALUES(%s,%s,%s,%s,%s,%s);"
    return None"""


@TA6_forms.route("/create_form_work_task", methods=["POST"])
def create_work_task():
    work_task = json.loads(request.form.get("data"))
    cursor = db.cursor()
    query = "INSERT INTO `form_data`.`work_tasks`(\
                    form,\
                    form_id,\
                    identifier,\
                    work_task_header,\
                    work_task_date,\
                    work_task_info,\
                    client_issue\
                )VALUES( %s,  %s,  %s,  %s,  %s,  %s,  %s\
                )"
    work_task_set = (
        work_task["form_name"],
        work_task["form"],
        work_task["identifier"],
        work_task["work_task_header"],
        work_task["work_task_date"],
        work_task["work_task_info"],
        work_task["client_issue"],
    )
    cursor.execute(query, work_task_set)
    db.commit()
    query = """SELECT
        `work_tasks`.`id`,
        `work_tasks`.`identifier`,
        `work_tasks`.`work_task_header`,
        `work_tasks`.`work_task_date`,
        `work_tasks`.`work_task_info`,
        `work_tasks`.`client_issue`
    FROM `form_data`.`work_tasks`
        WHERE  `work_tasks`.`form` = %s
        AND `work_tasks`.`form_id` = %s
        AND `work_tasks`.`identifier` = %s;"""

    params = (work_task["form_name"], work_task["form"], work_task["identifier"])

    new_work_tasks_set = []

    cursor.execute(query, params)

    tasks = cursor.fetchall()
    for r in tasks:
        task = work_task_class(r)
        new_work_tasks_set.append(task.__dict__)

    cursor.close()
    return json.dumps(new_work_tasks_set)


@TA6_forms.route("/delete_form_work_task", methods=["POST"])
def delete_work_task():
    work_task_id = json.loads(request.form.get("data"))
    cursor = db.cursor()
    query = "DELETE FROM `form_data`.`work_tasks`\
        WHERE id = %s\
        AND form_id = %s"

    params = (work_task_id["id"], work_task_id["form"])
    cursor.execute(query, params)
    db.commit()
    cursor.close()
    return "success"


@TA6_forms.route("/complete_work_task", methods=["POST"])
def complete_work_task():
    work_task_id = json.loads(request.form.get("data"))
    cursor = db.cursor()
    query = """ UPDATE `form_data`.`work_tasks` 
                    SET status = 'complete' 
                    WHERE id = %s """

    params = ()
    cursor.execute(query, params)
    db.commit()
    cursor.close()
    return "success"


# prep generic form data to send to templating system
def template_send_prep(form_name, **kwargs):
    form_set = templates[form_name]
    template = form_set["template"]
    returns = template_sort(template)
    flow_controls = json.dumps(returns["flow_controls"])
    js_template = json.dumps(returns["template"])
    questions = json.dumps(returns["questions"])
    sections = json.dumps(returns["sections"])
    # section_controls = json.dumps(returns['section_controls'])
    return {
        "flow_controls": flow_controls,
        "questions": questions,
        "sections": sections,
        "template": returns["template"],
    }  #'section_controls':section_controls}


# evaluate if particular currently has active form of this type
def form_age_eval(form_search, form_name, p_type, particular_id):
    if "form" in form_search:
        form = form_search["form"][0]
        form_age = form_search["form"][1]
    else:
        results = form_particular_creation(form_name, p_type, particular_id)
        form = results[0]
        form_age = results[1]
    return {"form": form, "form_age": form_age}


# prefi form wth already collected data
def form_data_prefil(form, form_set, template):
    if form["form_age"] == "old_form":
        form_results_collection(
            data["root_linkage"],
            data["root_linkage_id"],
            data["form_name"],
            "ancilliary_form",
        )
        form_results = form_results_collection(
            collect_form_data(form_set["query_columns"], form["form"]),
            form["form"],
            template["form_identifier"],
        )
        form_results.fetch_detail_data()
        form_results.collect_multi_row_data(form_set["sub_tables"])
        result_send = json.dumps(form_results.data)
        sub_tables_send = json.dumps(form_results.sub_tables)
        return {
            "result_send": result_send,
            "sub_tables_send": sub_tables_send,
            "section_marker": form_results.section_marker,
        }
    else:
        return {
            "result_send": json.dumps("none"),
            "sub_tables_send": json.dumps("none"),
            "section_marker": 0,
        }


@TA6_forms.route("/form/<form_name>/<p_type>/<particular_id>")
@login_required
def template_form(form_name, p_type, particular_id, **kwargs):
    def form_send_data(form_search, form_name):
        form_set = templates[form_name]
        main_form_data = template_send_prep(form_name)
        form = form_age_eval(form_search, form_name, p_type, particular_id)
        main_form_data["form_id"] = form["form"]
        template = main_form_data["template"]
        send_set = form_data_prefil(form, form_set, template)
        for key in main_form_data:
            send_set[key] = main_form_data[key]
        return send_set

    sub_forms = []

    if "form_extension" in kwargs:
        extension_forms = kwargs["form_extension"]
        for extension_data in extension_forms:
            sub_form_data = form_send_data(extension_data, extension_data["form_name"])
            sub_form_data["form_flows"] = extension_data["form_flows"]
            sub_forms.append(sub_form_data)
    """query = 'SELECT form_template from `form_data`.`form_data` where form_identifier = {}'.format(form_name)"""

    """if results[1] == 'old_form':
        form_results = form_results_collection(collect_form_data(TA6_Part_1_query_columns,form), ta6_part_1_query_select, form, template['Form'])
        """
    main_form_data = form_send_data(kwargs, form_name)
    template = copy.deepcopy(main_form_data["template"])
    if p_type == "market_particulars":
        query = """SELECT sudo_name FROM  `particulars_and_objects`.`market_particulars` WHERE market_particulars_ID  = %s"""
        params = (particular_id,)
        parent_data = {}
        cursor = db.cursor()
        cursor.execute(query, params)
        parent_data["name"] = cursor.fetchall()[0][0]
        cursor
    else:
        parent_data = "none"
    main_form_data["template"] = json.dumps(main_form_data["template"])

    if len(sub_forms) > 0:
        pass
    return render_template(
        "Json_form_templating/Json_form_templating.html",
        main_form_data=main_form_data,
        template=template,
        sub_forms=sub_forms,
        parent_data=parent_data,
        col_type="query_pairings",
    )

    # return render_template("Json_form_templating/Json_form_templating.html", template = template, flow_controls = flow_controls, js_template=js_template, questions=questions ,form_id = form['form'], sections=sections, results = result_send, sub_table_data = sub_tables_send, section_marker=form_results.section_marker)

    # return render_template("Json_form_templating/Json_form_templating.html", template = template, flow_controls = flow_controls, js_template=js_template, questions=questions ,form_id = form['form'], sections=sections, results = result_send, sub_table_data = sub_tables_send)


def prepare_lead_creation(self, lead_set, data_type):
    email_reg_ex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    insert = """INSERT INTO `lead_creation`.`created_links`(
                    link_created, 
                    link_code,
                    form_id,
                    target_email,
                    target_organisation,
                    ) VALUES (CURDATE(),%s,%s, %s, %s);"""
    cursor = db.cursor()
    import smtplib, ssl

    port = 465
    password = ""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("noreply@despatches.com", "S1lk-5carf(55)*2f@tlads(88)")
    for lead in lead_set:
        if re.fullmatch(email_reg_ex, lead[0]):
            code = create_rand_string(12)
            params = (code, self.form_name, lead[0], lead[1])
            cursor.execute(insert, params)
            # sending email
            server.sendmail(
                "noreply@despatches.com",
                lead[0],
                "http://127.0.0.1:5000/synopsis_temp/TA6_Part_1/market_particular/1",
            )
    cursor.close()


def lead_form_creation(form, data_type):
    if form in launch.templates:
        form_set = launch.templates[form]
        template_data = template_sort(form_set[template])


@TA6_forms.route("/redeemlinkq/<sepcific_link>")
def redeem_leed_form(sepcific_link):
    query = """
            SELECT form_id 
                FROM `lead_creation`.`created_links`
                WHERE link_code = %s
            """
    cursor = db.cursor()
    cursor.execute(query, (sepcific_link,))
    link = cursor.fetchall()
    if len(link) > 0:
        form = link[0][0]
        return template_micro_form(form, 0, 0, col_type="leed_create")


# TA6_forms.route("/form/micro/<form_name>/<root_linkage>/<root_linkage_id>", defaults={'parent_data': 'none'})
@TA6_forms.route("/form/micro/<form_name>/<root_linkage>/<root_linkage_id>")
@login_required
def template_micro_form(form_name, root_linkage, root_linkage_id, **kwargs):
    form_set = templates[form_name]
    main_form_data = template_send_prep(form_name)
    col_type = "micro"
    if "col_type" in kwargs:
        col_type = kwargs[col_type]

    main_form_data["result_send"] = json.dumps("none")
    main_form_data["section_marker"] = 0
    main_form_data["form_id"] = 0
    if col_type != "leed_create":
        form = form_results_collection(
            root_linkage, root_linkage_id, form_name, "ancilliary_form"
        )
        main_form_data["form_id"] = form.form
        # main_form_data["template"] = form_set["template"]
        if form.data != None:
            main_form_data["result_send"] = json.dumps(form.data)
            main_form_data["section_marker"] = form.section_marker

    main_form_data["sub_tables_send"] = json.dumps("none")

    template = copy.deepcopy(main_form_data["template"])
    main_form_data["template"] = json.dumps(main_form_data["template"])
    sub_forms = "micro"
    main_form_data["template_type"] = "micro"
    parent_data = "none"
    if root_linkage == "market_particular":
        query = """SELECT sudo_name FROM  `particulars_and_objects`.`market_particulars` WHERE market_particulars_ID = %s"""
        params = (root_linkage_id,)
        parent_data = {}
        cursor = db.cursor()
        cursor.execute(query, params)
        parent_data["name"] = cursor.fetchall()[0][0]
        cursor.close()
    else:
        parent_data = "none"

    return render_template(
        "Json_form_templating/Json_form_templating.html",
        main_form_data=main_form_data,
        template=template,
        sub_forms=sub_forms,
        submission_url="/micro_submission",
        root_linkage=root_linkage,
        root_linkage_id=root_linkage_id,
        col_type="micro",
        parent_data=parent_data,
    )


@TA6_forms.route("/micro_submission", methods=["POST"])
@login_required
def micro_submission():
    form_id = request.form.get("form_ID")
    inputs = json.loads(request.form.get("inputs"))
    section = request.form.get("section")
    sec_status = request.form.get("sec_status")
    linkage = json.loads(request.form.get("linkage"))

    form = form_results_collection(
        linkage["root_linkage"],
        linkage["root_linkage_id"],
        linkage["form_name"],
        "ancilliary_form",
    )
    form.micro_upload_section(inputs, section, sec_status)

    return "success"


@TA6_forms.route("/sequence_next_q", methods=["POST"])
@login_required
def sequence_next_q():
    form = request.form.get("form")
    next_q = request.form.get("next_q")
    template_set = templates[form]

    def iter_sequence(snip):
        for q in snip:
            if q["identifier"] == next_q:
                return q
            elif "sub_questions" in q:
                m = iter_sequence(q["sub_questions"])
                if m["identifier"] == next_q:
                    return m
        return False

    found = False
    sec_count = 0
    sec_num = len(template_set["template"]["Sections"])
    while sec_count < sec_num and found == False:
        found = iter_sequence(section["main_questions"])

    if found != False:
        new_html = render_template(input_type_eval.html, question=found)

    return new_html


@TA6_forms.route("/alter_meaning_text", methods=["POST"])
@login_required
def alter_meaning_text():
    meaning_text_data = json.loads(request.form.get("data"))
    query = "CALL `form_data`.`TA6_Part_1_text_edit_add`(%s,%s,%s);"
    params = (
        meaning_text_data["form"],
        meaning_text_data["identifier"],
        meaning_text_data["new_text"],
    )
    # print(params)
    cursor = db.cursor()
    cursor.execute(query, params)
    db.commit()
    cursor.close()
    return "success"


@TA6_forms.route("/document_collection", methods=["POST"])
@login_required
def document_collection():
    cursor = db.cursor()

    form_name = request.form.get("form_name")
    # print(form_name, 'the form_name')
    form = request.form.get("form_ID")
    text_reference = request.form.get("text_reference")
    for uploaded_file in request.files.getlist("documents"):
        if uploaded_file.filename != "":
            cursor.execute("USE form_data;")
            if len(uploaded_file.filename) > 30:
                filename = uploaded_file.filename[0:30]
            else:
                filename = uploaded_file.filename
            # print(filename)
            query = """
            INSERT INTO `{}_docu_storage`(
                parent_form,
                document,
                text_reference,
                document_name,
                upload) VALUES(
                %s, %s, %s,%s, curdate()
                );""".format(
                form_name
            )
            params = (form, uploaded_file.stream.read(), text_reference, filename)

            cursor.execute(query, params)
        uploaded_file.close()
    db.commit()
    cursor.close()
    return "success"


@TA6_forms.route("/report_constructor", methods=["POST"])
@login_required
def report_construction():
    data = json.loads(request.form.get("data"))
    template_set = templates[data["form_name"]]
    form_results = bulk_form_collect(data["form"], template_set, "gather")
    return "{}".format(
        render_template(
            "template_report_maker/template_report_maker.html.jinja",
            form_object=form_results,
        )
    )


def micro_synop_return(data):
    template_set = templates[data["form_name"]]
    template = template_set["template"]
    form = form_results_collection(
        data["root_linkage"],
        data["root_linkage_id"],
        data["form_name"],
        "ancilliary_form",
    )
    form.bulk_micro_collect()
    result_send = form.data
    questions = form.element_relevances["questions"]
    section_names = [section["section_name"] for section in template["Sections"]]
    sections = form.element_relevances["sections"]
    # print({'results':result_send, 'questions':questions,'section_names':section_names, 'reached_section':form.section_marker, 'sections':sections, 'form_name':form.form_name})
    """return render_template('synopsis_template.html', results = result_send, searchable_data = searchable_data, 
            questions = questions, sections=sections, rsections=form_results.element_relevances['sections'], 
            objects=object_send, sub_tables=sub_tables, reached_section=form_results.section_marker,
            form_name = form_name, form = form, particular_id=particular_id,
            p_type=p_type, section_names=section_names)"""
    data = {
        "results": result_send,
        "questions": questions,
        "section_names": section_names,
        "reached_section": form.section_marker,
        "sections": sections,
        "form_name": data["form_name"],
        "form": form.form,
    }
    return data


@TA6_forms.route("/extend_synopsis", methods=["POST"])
@login_required
def extend_synopsis():
    data = json.loads(request.form.get("data"))
    data = micro_synop_return(data)

    return json.dumps(data)


@TA6_forms.route("/pro_meanings", methods=["POST"])
def pro_meanings_fetch():
    data = json.loads(request.form.get("data"))
    data = micro_synop_return(data)

    return json.dumps(data)


# @TA6_forms.route("/synopsis_micro/<form_name>/<p_type>/<particular_id>"):
# @login_required
