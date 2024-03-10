from flask import json, jsonify, render_template
import copy
import launch
from launch.blueprints.form_templates.json_form_templates import template_sort
import numpy as np
import pandas as pd


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
        keep_questions =  []
        custom_template =    {"Form": "TA6 Part 1",
        						    "form_identifier": "TA6_Part_1",
        						    "Sections": [
        						    	"section_name": "Risk assessments",
							            "section_identifier": "risk_assessments",
							            #'question_set_data':{'set_numbering':"3.2"},
							            "main_questions": []
            						]
        					}
        for q_id in cfr_file:
        	question_option_range = cfr_file[q_id]
        	for answer in question_option_range
        		if question_option_range[answer][sort_type] == 1:
        			keep_questions.append({
        					"question" : q_id,
        					"answer" : answer
        				})

        			
        if (len(keep_questions)>0):
        	keep_copy = copy.deep_copy(keep_questions)
        	template_qs = custom_template["Sections"]["main_questions"]
        	i=0
        	custom_template = {}
        	while i<len(keep_copy):
        		qa_set = keep_copy[i]
        		if !(qa_set["question"] in meaning_file):
        			remove_questions.append(i)
        		else if !(qa_set["answer"] in meaning_file[qa_set["question"]]):
        			remove_questions.append(i)
        		else:
        			template_qs.append({
                             "question_title": meaning_file[qa_set["question"]][qa_set["answer"]],
                            "input_type": "number",
                            "identifier": qa_set["question"],       				
        				})


       # template_sort(self.form_set.template, false)


def generate_risk_template(form_name):
    form_set_data = launch.templates[form_name]
    sorted_data = template_sort(form_set_data[template])
