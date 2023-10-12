from launch import db, templates
from flask_login import login_user, current_user, login_required
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
from launch.blueprints.form_templates import json_form_templates

# from launch.blueprints.form_templates.TA6_part_1_comp_risk_fraud import comp_risk_fraud as TA6_part_1_comp_risk_fraud
from launch.blueprints.form_templates.new_db_sql_code_writer import (
    create_new_sql_table,
    element_relevancy,
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
import mysql.connector
import string, random, datetime, ast


def print_for_eqivilents(template):
    equiv_list = []
    returns = json_form_templates.template_sort(template, full_q=True)
    template = returns["template"]
    questions = returns["questions"]

    def set_loop(sets):
        n = 0
        for question in sets:
            n += 1
            if question["input_type"] == "multi_row":
                equiv_list.append(
                    {"TA6": "", "TA6_part_1": {"identifier": question["identifier"]}}
                )
                set_loop(question["data_rows"])
            elif "question_title" in question:
                equiv_list.append(
                    {
                        "TA6": "",
                        "TA6_part_1": {
                            "identifier": question["identifier"],
                            "question_title": question["question_title"],
                        },
                    }
                )
            else:
                equiv_list.append(
                    {"TA6": "", "TA6_part_1": {"identifier": question["identifier"]}}
                )

    for section in questions:
        set_loop(questions[section])
    return equiv_list


def print_text_modifier(template):
    equiv_list = {}
    returns = json_form_templates.template_sort(template, full_q=True)
    template = returns["template"]
    questions = returns["questions"]

    def set_loop(sets):
        n = 0
        for question in sets:
            n += 1
            if question["input_type"] == "multi_row":
                equiv_list[question["identifier"]] = {
                    "question_title": None,
                    "other_question_text": None,
                }
                set_loop(question["data_rows"])
            else:
                equiv_list[question["identifier"]] = {
                    "question_title": None,
                    "other_question_text": None,
                }

    for section in questions:
        set_loop(questions[section])
    return equiv_list


# transfer db results back into py_object results
def output_py_return(val, input_type, reverse=False):
    if input_type == "checkbox":
        if reverse == True:
            if val == "checked":
                val = "yes"
        else:
            if val == "yes":
                val = "checked"
    if input_type == "bool" or "bool_extra":
        if reverse == True:
            if val == "1":
                val = "yes"
            elif val == "0":
                val = "no"
        else:
            if val == "yes":
                val = "1"
            elif val == "no":
                val = "0"
    return val


# def standard_form_render():


def bool_java_conversion(vari):
    if vari == "empty":
        convert = 1
    elif vari == "1":
        convert = 2
    elif vari == "0":
        convert = 3
    else:
        convert = None
    return convert


def collect_form_data(query_column, form_id, db_table="`form_data`.`TA6_Part_1_data`"):
    cursor = db.cursor()

    params = (form_id,)  # TA6_part_1_query_columns

    query = f"SELECT {query_column}, section_marker, user_initiator, ceation_moment FROM {db_table}\
                WHERE form_id = %s"

    cursor.execute(query, params)

    form_results = cursor.fetchone()

    cursor.fetchall()

    cursor.close()

    return form_results


def db_true_false_transition(val):
    # print(val)
    if val == 0:
        new_val = False
    elif val == 1:
        new_val = True
    else:
        new_val = val
    return new_val


class work_task:
    def __init__(self, db_row):
        self.id = db_row[0]
        self.identifier = db_row[1]
        self.work_task_header = db_row[2]
        self.work_task_date = db_row[3]
        self.work_task_info = db_row[4]
        self.client_issue = db_row[5]


class template_question:
    def __init__(self, identifier, value):
        return None


# form_result_collection represents one line of a given database for a specified template


class form_results_collection:
    def __init__(
        self, results, form, form_name, collection_type="query_pairings", **kwargs
    ):
        # template and accompanying files e.g meanings
        self.template_set = templates[form_name]

        if collection_type == "query_pairings":
            # either colected form data has custom db table or is held in a no sql fashion
            self.collection_type = collection_type
            query_pairings = self.template_set["query_select"]
            data = {}
            col_count = 0
            for key in query_pairings:
                data[key] = {}
                ini_type = query_pairings[key]["input_type"]
                value = results[query_pairings[key]["db_position"]]
                data[key]["input_type"] = ini_type
                """if ini_type == 'detail_text' or 'docu':
                    value = db_true_false_transition(value)
                if ini_type == 'bool' or 'cheakbox' or 'bool_extra':
                    value = output_py_return(value, 'bool')"""
                data[key]["value"] = value
                data[key]["work_tasks"] = []
                data[key]["documents"] = []
                # data[key] = output_py_return(data[key],query_pairings[key]['input_type'])
                col_count += 1
            # dictionary containing one entry for each 'identifier' in template
            self.data = data
            # marker of where in form has been reached by user
            self.section_marker = results[col_count]
            # user that initiated form
            self.user_initiator = results[col_count] + 1
            # moment that form was created
            self.ceation_moment = results[col_count] + 2
        elif collection_type == "ancilliary_form":
            root_linkage = results
            # type that sub form is linked to e.g market patrticular or TA6_Part_1 form
            self.root_linkage = root_linkage
            root_linkage_id = form
            # id of specific root_linkage object
            self.root_linkage_id = root_linkage_id
            query = """SELECT 
                form_id, 
                root_linkage, 
                root_linkage_id, 
                form_identifier, 
                form_results,
                section_marker, 
                user_initiator,
                ceation_moment,
                revision_date,
                revision_count
                FROM `form_data`.`ancilliary_forms`
                WHERE form_identifier = '{form_name}' AND root_linkage = '{root_linkage}' AND root_linkage_id = {root_linkage_id}
                AND form_id=(
                     SELECT max(form_id) FROM `form_data`.`ancilliary_forms`
                     WHERE form_identifier = '{form_name}' AND root_linkage = '{root_linkage}' AND root_linkage_id = {root_linkage_id}
                );""".format(
                form_name=form_name,
                root_linkage=root_linkage,
                root_linkage_id=root_linkage_id,
            )

            cursor = db.cursor()

            cursor.execute(query)

            results = cursor.fetchall()
            if len(results) > 0:
                result = results[0]
                if result[4] != None:
                    self.data = {}
                    self.results = json.loads(result[4])

                    for s in self.results["form_results"]:
                        for key in self.results["form_results"][s]:
                            self.data[key] = self.results["form_results"][s][key]
                            self.data[key]["work_tasks"] = []
                            self.data[key]["documents"] = []
                else:
                    self.data = None
                self.section_marker = result[5]
                self.user_initiator = result[6]
                self.ceation_moment = result[7]
                # id of form
                self.form = result[0]
                # date of most recent revision to form
                self.revision_date = result[8]
                # number of revisions to form
                self.revision_count = result[9]
                # type of storage micro=nosql json file
                self.collection_type = "micro"

            else:
                self.results = {"form_results": {}, "other_data": {"revsion_dates": []}}
                for section in self.template_set["template"]["Sections"]:
                    self.results["form_results"][section["section_identifier"]] = {}
                query = """INSERT INTO  `form_data`.`ancilliary_forms`(
                        root_linkage, 
                        root_linkage_id,
                        user_initiator,
                        ceation_moment,
                        form_identifier,
                        form_results
                        ) VALUES (%s,%s,%s, NOW(), %s, %s);"""

                params = (
                    root_linkage,
                    root_linkage_id,
                    current_user.id,
                    form_name,
                    json.dumps(self.results),
                )

                cursor.execute(query, params)
                cursor.execute(
                    "SELECT LAST_INSERT_ID() FROM `form_data`.`ancilliary_forms`"
                )
                self.data = None
                self.form = cursor.fetchall()[0][0]
                self.section_marker = 0

            db.commit()
            cursor.close()
        self.form = form
        # identifier of template results relate to
        self.form_name = form_name
        # any sub_forms with data collected relating to this form
        self.sub_forms = {}
        # list of section names and identifiers in template
        self.sections = [
            {
                "section_name": sec["section_name"],
                "section_identifier": sec["section_identifier"],
            }
            for sec in self.template_set["template"]["Sections"]
        ]

    def sub_forms_gather(self, create=False):
        cursor = db.cursor()
        query = """SELECT DISTINCT(`form_identifier`) FROM  `form_data`.`ancilliary_forms`
            WHERE `root_linkage` = %s and root_linkage_id = %s ;"""
        params = (self.form_name, self.form)

        cursor.execute(query, params)

        results = cursor.fetchall()
        for r in results:
            if create == False:
                self.sub_forms[r[0]] = {
                    "form_name": templates[r[0]]["template"]["Form"]
                }
            else:
                self.sub_forms[r[0]] = form_results_collection(
                    self.form_name, self.form, r[0], "ancilliary_form"
                )
                self.sub_forms[r[0]].bulk_micro_collect()
                self.sub_forms[r[0]] = self.sub_forms[r[0]].__dict__

    def bulk_micro_collect(self, *args):
        template_set = self.template_set
        self.append_data(template_set["meanings"], "meanings")
        self.add_element_relevances()
        self.exclude_irrelevants()
        if "comp_risk_fraud" in template_set:
            self.append_data_group(template_set["comp_risk_fraud"])
        if "object_links" in template_set:
            self.evaluate_objects(template_set["object_links"])

    def micro_upload_section(self, section_data, section, sec_status):
        cursor = db.cursor()
        if section in self.results["form_results"]:
            self.results["form_results"][section] = section_data
        self.results["other_data"]["revsion_dates"].append(self.revision_date)
        if sec_status != "steady":
            self.section_marker = sec_status
        query = """UPDATE `form_data`.`ancilliary_forms`
         SET 
            form_results = %s,
            revision_date = NOW(),
            revision_count = %s,
            section_marker = %s
        WHERE form_identifier = %s and root_linkage = %s and root_linkage_id = %s"""

        params = (
            json.dumps(self.results),
            self.revision_count + 1,
            self.section_marker,
            self.form_name,
            self.root_linkage,
            self.root_linkage_id,
        )

        cursor.execute(query, params)

        db.commit()

        cursor.close()

    def add_forms(self, form_identifier, root_linkage, root_linkage_id):
        query = """SELECT form_id, form_results, section_marker, user_initiator, creation_moment
                    FROM `form_data`.`ancilliary_forms` 
                    WHERE root_linkage = %s AND root_linkage_id = %s AND form_identifier = %s"""
        cursor = db.cursor()
        params = (rooe_linkage, root_linkage_id, form_identifier)
        cursor.execute(query, params)
        results = cursor.fetchall()
        if len(results) > 0:
            self.sub_forms[form_identifier] = []
            for res in results:
                new_form = form_results_collection(
                    res[1],
                    res[0],
                    form_identifier,
                    "ancilliary_forms",
                    section_marker=res[2],
                    user_initiator=res[3],
                    creation_moment=res[3],
                )
                self.sub_forms[form_identifier].append(new_form)

    def fraud_risk_comp(self, templates):
        for q in self.data:
            crf = ["risk", "fraud", "competancy"]
            if q in templates[self.form_name]["comp_risk_fraud"]:
                for key in templates[self.form_name]["comp_risk_fraud"][q]:
                    for groupy in crf:
                        if f"{groupy}_potential" not in self.data[q]:
                            if (
                                templates[self.form_name]["comp_risk_fraud"][q][key][
                                    groupy
                                ]
                                == 1
                            ):
                                self.data[q][f"{groupy}_potential"] = 1

    # assign any colleted detail text for questions with the inoput type of detail_text
    def fetch_detail_data(self):
        cursor = db.cursor()
        query = "SELECT text_content, ref, text_reference, viewed FROM `form_data`.`{}_detail_text` WHERE parent_form= %s;".format(
            self.form_name
        )
        params = (self.form,)

        cursor.execute(query, params)

        detail_text = cursor.fetchall()
        if len(detail_text) > 0:
            for key in self.data:
                for d in detail_text:
                    if d[2] == key:
                        self.data[key]["non_format_text"] = {}
                        container = self.data[key]["non_format_text"]
                        self.data[key]["value"] = d[0]
                        container["value"] = d[0]
                        container["viewed"] = d[3]
                        container["value_ref"] = d[1]

        cursor.close()

    # collect data for information pieces that are stored in multi row data tables
    def collect_multi_row_data(self, sub_tables):
        cursor = db.cursor()

        self.sub_tables = {}

        for sub in sub_tables:
            table_route = sub["table_route"][24:-1]
            # print(table_route)
            self.sub_tables[table_route] = {}
            self.sub_tables[table_route]["data"] = []
            select_string = ""
            for key in sub["table_key"]:
                select_string = f"{select_string}{key},"

            select_string = f"{select_string} ref"

            query = f"SELECT {select_string} FROM {sub['table_route']} WHERE parent_form = %s;"

            params = (self.form,)

            cursor.execute(query, params)
            sub_data = cursor.fetchall()
            if len(sub_data) > 0:
                """for sub_d in sub_data:
                ref = sub_d[-1]
                self.sub_tables[table_route]['data'][ref] = {}
                for key in sub['table_key']:
                        self.sub_tables[table_route]['data'][ref][key] = sub_d[sub['table_key'][key]['db_position']]
                """
                self.data[f"{table_route}_count"]["data_rows"] = []
                for sub_d in sub_data:
                    new_row = {}
                    for key in sub["table_key"]:
                        new_row[key] = sub_d[sub["table_key"][key]["db_position"]]

                    self.data[f"{table_route}_count"]["data_rows"].append(new_row)

                # self.data[f'{table_route}_count']['data_rows'] = self.sub_tables[table_route]['data']

            else:
                # self.sub_tables[table_route] = 'empty'
                self.data[f"{table_route}_count"]["data_rows"] = "none"

    # alter values for machine learning and analysis purposes
    def value_interpret(self):
        for ident in self.data:
            ident["value"] = collected_value_interpretation(ident["value"])

    # collect edited meaning values for synopsis module
    def edited_text_meaning(self):
        if self.collection_type != "micro":
            table = "`form_data`.`{}_text_editations`".format(self.form_name)
            query = """SELECT `reference_edit`, `editation_data` FROM {}
                        WHERE `parent_form` =  {}""".format(
                table, self.form
            )
            cursor = db.cursor()
            cursor.execute(query)
            editations = cursor.fetchall()
            for edits in editations:
                for key in self.data:
                    if edits[0] == key:
                        self.data[key]["meanings"]["edit_meaning"] = edits[1]

    # currently just for the purpose of answer meanings allowing answer meanings to be tagged to be assigned based on question answer
    def append_data(self, data_set, data_name):
        def data_loop(append_set, data_group):
            for key in append_set:
                if key in data_group:
                    identifier = key  # grab identifier
                    # ensure that database collected json values are correct
                    collected_value = output_py_return(
                        collected_value_interpretation(data_group[identifier]["value"]),
                        data_group[identifier]["input_type"],
                        reverse=True,
                    )
                    # new area for appended data to go
                    data_group[identifier][data_name] = {"meaning": {}}
                    fill_spot = data_group[identifier][data_name]
                    # if the data set has data for the gove identifier value
                    if collected_value in append_set[identifier]:
                        fill_spot["meaning"] = append_set[identifier][collected_value][
                            "meaning"
                        ]

                    # if the value is continuos and needs further processing
                    # otherwise jsut straigth collect value
                    elif (
                        "value" in append_set[identifier] and collected_value != "none"
                    ):
                        # ways f precessing value to get to an end data value
                        if "equation" in append_set[identifier]["value"]:
                            new_meaning = None

                            # run data through template controller functions till there is a match
                            # then run function
                            for key in append_set[identifier]["value"]["equation"]:
                                result = templates["controllers"][key](
                                    data_group[identifier]["value"],
                                    append_set[identifier]["value"]["equation"][key][
                                        "vari"
                                    ],
                                )
                                if result:
                                    new_meaning = append_set[identifier]["value"][
                                        "equation"
                                    ][key]["meaning"]
                                    break
                            data_group[identifier][data_name] = {}
                            if new_meaning == None:
                                fill_spot["meaning"] = append_set[identifier]["value"][
                                    "default"
                                ]["meaning"]
                            else:
                                fill_spot["meaning"] = new_meaning

                        else:
                            meaning_string = append_set[identifier]["value"][
                                "meaning"
                            ].format(data_group[identifier]["value"])
                            if meaning_string != "":
                                data_group[identifier][data_name] = {}
                                data_group[identifier][data_name][
                                    "meaning"
                                ] = meaning_string.format(
                                    data_group[identifier]["value"]
                                )
                    if "rows" in append_set[identifier]:
                        data_group[identifier]["rows"] = data_loop(
                            append_set[identifier]["rows"],
                            data_group[identifier]["rows"],
                        )
            return data_group

        self.data = data_loop(data_set, self.data)
        self.edited_text_meaning()

    # apply extra data to set based off identifiers for example risk, fraud or competancy markers
    def append_data_group(self, data_set):
        def data_loop(append_set, data_group):
            for key in append_set:
                if key in data_group:
                    identifier = key
                    collected_value = collected_value_interpretation(
                        data_group[identifier]["value"]
                    )
                    if collected_value in append_set[identifier]:
                        for key in append_set[identifier][collected_value]:
                            data_group[identifier][key] = append_set[identifier][
                                collected_value
                            ][key]

                    elif (
                        "value" in append_set[identifier] and collected_value != "none"
                    ):
                        if "equation" in append_set[identifier]["value"]:
                            new_value = None

                            # run data through template controller functions till there is a match
                            # then run function
                            for key in append_set[identifier]["value"]["equation"]:
                                result = templates["controllers"][key](
                                    data_group[identifier]["value"],
                                    append_set[identifier]["value"]["equation"][key][
                                        "vari"
                                    ],
                                )
                                if result:
                                    new_value = append_set[identifier]["value"][
                                        "equation"
                                    ][key]["meaning"]
                                    break

                        for key in append_set[identifier][collected_value]:
                            data_group[identifier][key] = append_set[identifier][
                                collected_value
                            ][key]
                    if "rows" in append_set[identifier]:
                        data_group[identifier]["rows"] = data_loop(
                            append_set[identifier]["rows"],
                            data_group[identifier]["rows"],
                        )
            return data_group

        self.data = data_loop(data_set, self.data)

    # find out which identifiers are essentially irrelivant due
    # to not being possible as determined by flow controls or display reliance"""
    def add_element_relevances(self):
        self.element_relevances = element_relevancy(self.template_set["template"])

    # add relevancy markers to data pieces based off of element relevances so they are not displayed or processed"""
    def exclude_irrelevants(self):
        flows = self.element_relevances["flow_controls"]
        for key in self.data:
            if key in flows:
                ident_relevant = flow_control_tiers(flows[key], self.data)
                if ident_relevant == True:
                    self.data[key]["relevant"] = 1
                else:
                    self.data[key]["relevant"] = 0
            else:
                self.data[key]["relevant"] = 1

    # collect and assign data that belongs to a tmeplate specific object
    def find_documents(self, gather=False):
        cursor = db.cursor()
        gathering = ""
        if gather == True:
            gathering = ",document"

        query = """SELECT ref, text_reference, document_name, document_description,viewed, upload{}
                    FROM `form_data`.`{form_name}_docu_storage`
                    WHERE parent_form = {form_id}""".format(
            gathering, form_name=self.form_name, form_id=self.form
        )

        cursor.execute(query)

        documents = cursor.fetchall()

        for doc in documents:
            for key in self.data:
                if key == doc[1]:
                    new_doc = {
                        "ref": doc[0],
                        "document_name": doc[2],
                        "document_description": doc[3],
                        "viewed": doc[4],
                        "upload_date": doc[5],
                    }
                    if gather == True:
                        new_doc["document"] = doc[6]
                    self.data[key]["documents"].append(new_doc)

        cursor.close()

    def evaluate_objects(self, object_set):
        self.objects = {}
        pairings = {}
        for key in object_set:
            cur_obj = object_set[key]
            if cur_obj["object"] in objects:
                object_type = objects[cur_obj["object"]]
                for key_2 in cur_obj["links"]:
                    if cur_obj["links"][key_2] != None:
                        pairings[key_2] = self.data[cur_obj["links"][key_2]]
                        pairings[key_2]["original_identifier"] = cur_obj["links"][key_2]
                        self.data[cur_obj["links"][key_2]]["meanings"]["meaning"] = ""
                    else:
                        pairings[key_2] = None
                allowed = True
                for requ in object_type["requirements"]:
                    allowed = object_requirements[requ["type"]](pairings)
                    if allowed == False:
                        break
                if allowed == True:
                    self.objects[key] = object_type["create"](pairings)

                    # print(self.objects[key])
                    if cur_obj["position"] == "first":
                        self.element_relevances["questions"][cur_obj["section"]] = [
                            {"object": key}
                        ] + self.element_relevances["questions"][cur_obj["section"]]

    # collect work tasks from database for given form id
    def work_tasks(self):
        query = """SELECT
            `work_tasks`.`id`,
            `work_tasks`.`identifier`,
            `work_tasks`.`work_task_header`,
            `work_tasks`.`work_task_date`,
            `work_tasks`.`work_task_info`,
            `work_tasks`.`client_issue`
        FROM `form_data`.`work_tasks`
        WHERE  `work_tasks`.`form` = %s AND 
            `work_tasks`.`form_id` = %s"""

        cursor = db.cursor()

        params = (self.form_name, self.form)

        cursor.execute(query, params)

        results = cursor.fetchall()

        self.work_tasks = []

        for r in results:
            task = work_task(r)
            if task.identifier in self.data:
                self.data[task.identifier]["work_tasks"].append(task.__dict__)
            self.work_tasks.append(task)


# take python specific values out of python to allow for interchangability within Json format
def collected_value_interpretation(value):
    eval_dict = {None: "none", True: "true", False: "false"}
    if value in eval_dict:
        new_val = eval_dict[value]
    else:
        new_val = value
    return new_val


# alter collected values in order to generate sql input queries also rationalization of multi row inputs
def input_type_jiggling(e, data, form, docu_det, ident):
    val = data["value"]
    if "false" in data:
        if int(data["false"]) == 1:
            val = False

    if data["input_type"] == "bool" or data["input_type"] == "bool_extra":
        db_ready_value = bool_java_conversion(val)
        if db_ready_value == None:
            db_ready_value = f"'{val}'"

    elif data["input_type"] == "radio":
        if val != False:
            db_ready_value = f"'{val}'"
        else:
            db_ready_value = repr("empty")

    elif data["input_type"] == "text":
        if val != False:
            db_ready_value = f"'{val}'"
        else:
            db_ready_value = "NULL"

    elif data["input_type"] == "detail_text":
        # print(data['false'])
        if val != False:
            db_ready_value = 1
            details_row = (form, val, ident)
            docu_det["details"].append(details_row)
        else:
            db_ready_value = 0

    elif data["input_type"] == "docu":
        if val != False:
            db_ready_value = 1
        else:
            db_ready_value = 0

    elif data["input_type"] == "checkbox":
        if val != False:
            db_ready_value = val
        else:
            val = 0

    elif data["input_type"] == "date":
        if val != False:
            db_ready_value = f"'{val}'"
        else:
            db_ready_value = False

    elif data["input_type"] == "postcode":
        if val != False:
            db_ready_value = f"'{val}'"
        else:
            db_ready_value = False

    elif data["input_type"] == "number":
        if val != False:
            db_ready_value = f"{val}"
        else:
            db_ready_value = False

    elif data["input_type"] == "multi_row":
        # if multi row main value =  false add no rows
        if val != False:
            sub_table_docu_det = {"docu": [], "details": []}

            for row in e["rows"]:
                row["data"] = []
            # r represents one full entry row of data from form ub object
            for r in data["rows"]:
                # e[rows] represents list of possible db matches for sub table
                for sub_row_matches in e["rows"]:
                    # if input reference name is referenced in java and python
                    if (
                        sub_row_matches["form"] in r
                        and r[sub_row_matches["form"]]["value"] != False
                    ):
                        # sub_row_matches['data'].append(r[sub_row_matches['form']])
                        returns = input_type_jiggling(
                            "none",
                            r[sub_row_matches["form"]],
                            form,
                            sub_table_docu_det,
                            sub_row_matches["form"],
                        )

                        def alter_date(output):
                            if output == False:
                                return "null"

                        alter_functions = {"date": alter_date}
                        if r[sub_row_matches["form"]]["input_type"] in alter_functions:
                            data_piece = alter_functions[
                                r[sub_row_matches["form"]]["input_type"]
                            ](returns[0])
                        else:
                            data_piece = returns[0]
                        sub_row_matches["data"].append(data_piece)
                        sub_table_docu_det = returns[1]
                    else:
                        sub_row_matches["data"].append("")

            multi_pairs = []

            for row in e["rows"]:
                multi_pairs.append({"row": row["database"], "value": row["data"]})

            # print(multi_pairs)
            query = multi_line_input(
                multi_pairs, e["table"], form={"row": "parent_form", "id": form}
            )

            if len(sub_table_docu_det["details"]) > 0:
                cursor = db.cursor()
                table = e["table"]
                query = f"SELECT ref FROM {table} WHERE parent_form = {form}\
                            and sub_attributes = FALSE"

                cursor.execute(query)

                final_input = []
                for det in sub_table_docu_det["details"]:
                    ref = cursor.fetchone()
                    det += (ref[0],)
                    final_input.append(det)

                cursor.fetchall()

                cursor.execute(
                    f"UPDATE {table} set sub_attributes = TRUE WHERE parent_form = {form} AND sub_attributes = FALSE"
                )

                query = "INSERT INTO `form_data`.`TA6_Part_1_detail_text` (parent_form, text_content, text_reference, ref) VALUES (%s,%s, %s, %s )"

                # print(final_input)
                cursor.executemany(query, final_input)
                cursor.close()
            # db_ready_value = true
            db_ready_value = val
        else:
            db_ready_value = False

    elif data["input_type"] == "bool_extra":
        if val != False:
            if val == "1":
                db_ready_value = "'yes'"
            elif val == 0:
                db_ready_value = "'no'"
            else:
                db_ready_value = f"'{val}'"
        else:
            db_ready_value = 1

    elif data["input_type"] == "currency":
        if val != False:
            db_ready_value = float(val)
        else:
            db_ready_value = False

    else:
        db_ready_value = val

    return (db_ready_value, docu_det)


# creation of multi line input strings
def multi_line_input(pairs, table, **kwargs):
    cursor = db.cursor()

    u_num = 0

    values = ""

    """#if len(pairs[0]['value']) == 1:
    #   for p in pairs:
    #       p['value'] = p['value'][0]
    #       generic_input(pairs, table)
    #       return None"""

    row_input_num = len(pairs[0]["value"])

    row_input_counter = 0

    row_vals = []

    # while row_input_counter < row_input_num:
    for p in pairs:
        u_num += 1
        if u_num == 1:
            rows = f"{p['row']} "

            row_input_counter = 0
            while row_input_counter < row_input_num:
                row_vals.append(f"({p['value'][row_input_counter]}")
                # values = f"{p['value']}"
                row_input_counter += 1
        else:
            rows = f"{rows} ,{p['row']}"
            row_input_counter = 0
            while row_input_counter < row_input_num:
                row_vals[
                    row_input_counter
                ] = f"{row_vals[row_input_counter]}, {p['value'][row_input_counter]} "
                row_input_counter += 1

    if "form" in kwargs:
        changer = []
        for row in row_vals:
            form_id = kwargs["form"]["id"]
            row = f"{row}, {form_id}"
            changer.append(row)

        row_vals = changer

        form_id_row = kwargs["form"]["row"]
        rows = f"{rows},{form_id_row}"

    row_input_counter = 0
    while row_input_counter < row_input_num:
        if row_input_counter == row_input_num - 1:
            row_vals[row_input_counter] = f"{row_vals[row_input_counter]})"
        else:
            row_vals[row_input_counter] = f"{row_vals[row_input_counter]}),"

        values = f"{values} {row_vals[row_input_counter]}"

        row_input_counter += 1

    query = f"INSERT into {table}\
                ({rows})\
                VALUES{values};"
    # print(query)
    cursor.execute(query)

    db.commit()

    cursor.close()


# creation of standard single line input string (sql)
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


# first of trial set of functions for determining viability of object creation
def one_not_none(possibilities):
    set_possible = False
    for sets in possibilities:
        if possibilities[sets]["value"] != None or False or "empty":
            set_possible = True
            break
    return set_possible


# dictionary object to store object creation viability testers
object_requirements = {"one_not_none": one_not_none}


# standard template object
class conjoined_objects:
    def __init__(self):
        self.work_tasks = []


# postal address
class postal_address(conjoined_objects):
    def __init__(self, data):
        super().__init__()
        self.first_line = data["first_line"]
        self.second_line = data["second__line"]
        self.third_line = data["third_line"]
        self.fourth_line = data["fourth_line"]
        self.postcode = data["postcode"]
        self.meaning = ""

    """def create_meaning(self, specifics):
        if 'meaning' not in specifics:
            self.meaning = 'the Address is'
            n = 0
            for s in [self.first_line,self.second_line,self.third_line,self.fourth_line]
                if s != None or '':
                    if n != 0:
                        self.meaning += ', {}'.format(s)
                    else: 
                        self.meaning += ' {}'.format(s)
            if n == 0:
                if self.postcode == '' or None:
                    continue"""


objects = {
    "postal_address": {
        "requirements": [{"type": "one_not_none", "inputs": "all"}],
        "create": postal_address,
    }
}


# first of function set to apply flow control to template collections
def larger_than(value, controller):
    if value > controller:
        return True
    else:
        return False


# reading of flow controls in order to assess whether an aidentifier is relevant
def flow_control_tiers(control_set, data):
    item_relevant = False
    for control in control_set:
        if control["identifier"] in data:
            comp = data[control["identifier"]]["value"]
            comp = output_py_return(comp, data[control["identifier"]]["input_type"])

            for val in control["value"]:
                if val == comp:
                    item_relevant = True
                    if control["identifier"] in control_set:
                        # doc_controllers.append(flow_controls[doc['identifier']])
                        item_relevant = flow_control_tiers(
                            control_set[control["identifier"]], data
                        )

                else:
                    item_relevant = False
            if item_relevant == False:
                return False
    if item_relevant == True:
        return True
    return False


def single_layer_flow_control(control_set, data):
    item_relevant = False
    for control in control_set:
        if control["identifier"] in data:
            return False
    return True


def form_equals_evaluation(equals, form_data, form):
    pairs = []
    details = []
    docu = []
    for e in equals:
        if e["form"] in form_data:
            data = form_data[e["form"]]
            ident = e["form"]
            returns = input_type_jiggling(
                e, data, form, {"docu": docu, "details": details}, ident
            )
            db_ready_value = returns[0]
            docu_det = returns[1]

            docu = docu_det["docu"]
            details = docu_det["details"]

            if db_ready_value == False:
                continue
        else:
            continue

        pairs.append({"row": e["database"], "value": f"{db_ready_value}"})

    return {"pairs": pairs, "details": details, "docu": docu}


def evaluate_form_mp_relation(form_name, p_type, p_id):
    cursor = db.cursor()

    query = f"""SELECT max(form_id) 
                FROM `form_data`.`{form_name}_{p_type}_relationship` 
                WHERE market_particulars = %s AND attachment_type = 'mp'"""

    params = (p_id,)

    cursor.execute(query, params)

    result = cursor.fetchone()

    cursor.close()

    return result
