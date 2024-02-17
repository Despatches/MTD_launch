from flask import json, jsonify, render_template
import copy
import launch
from launch.blueprints.form_templates.json_form_templates import template_sort


class form_set:
    def __init__(self, form_name):
        self.form_name = form_name
        if self.form_name in launch.templates:
            self.form_set = launch.templates[self.form_name]
        else:
            return "none"

    def filter_for_risky(sort_type):
        cfr_file = self.form_set["comp_risk_fraud"]
        meaning_file = self.form_set["meanings"]
        keep_questions = []
        for q_id in cfr_file:
        	question_option_range = q_id
        	for answer in question_option_range
        		if question_option_range[answer][sort_type] == 1:
        			keep_questions.append({
        					"question" : q_id,
        					"answer" : answer
        				})
        if (len(keep_questions)>0):
        	keep_copy = copy.deep_copy(keep_questions)
        	for qid in meaning_file:
        		i=0
        		while i<len(keep_copy):
	        		if keep_copy[i]["question"] == qid:
	        			if keep_copy[i]["question"][]


       # template_sort(self.form_set.template, false)


def generate_risk_template(form_name):
    form_set_data = launch.templates[form_name]
    sorted_data = template_sort(form_set_data[template])
