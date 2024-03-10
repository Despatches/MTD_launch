from flask import Flask, render_template, session, redirect, url_for
from config import Config
import mysql.connector as mysql
import string
import random

# from flask_bootstrap import Bootstrap
from flask_login import LoginManager
import os
import re
import stat
import json

# import mimetypes
# import humanize
from datetime import datetime
from flask.views import MethodView
import os
import openai

cnx = mysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="10010010",
    auth_plugin="mysql_native_password",
)
db = cnx
currency = {"name": "pound", "icon": "£"}
from .blueprints.form_templates.templates import templates

# openai.api_key = "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"
# openai.Model.list()


def create_rand_string(string_length):
    code = string.ascii_letters
    code2 = string.digits
    codes = (code, code2)
    rand = ""
    counter = 0

    def character_type(codes):
        choice = random.choice(codes)
        return choice

    while counter != string_length:
        a = character_type(codes)
        rand = f"{rand}" + (random.choice(a))
        counter += 1
    return rand


def create_app():
    app = Flask(__name__)  # ,static_url_path='/static',static_folder='launch/static')
    app.config.from_object(Config)
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

    from .blueprints.offers import offers as offers_blueprint

    app.register_blueprint(offers_blueprint)

    from .blueprints.blu_auth import blu_auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # from .blueprints.mp_ajax import mp_ajax as mp_ajax_blueprint
    # app.register_blueprint(mp_ajax_blueprint)

    from .blueprints.spatial import spatial as spatial_blueprint

    app.register_blueprint(spatial_blueprint)

    # blueprint for non-blu_auth parts of app
    from .blueprints.blu_main import blu_main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .blueprints.blu_objects_title_derivatives import title_derivatives

    app.register_blueprint(title_derivatives)

    from .blueprints.blu_market_partics import mp as mp_blueprint

    app.register_blueprint(mp_blueprint)

    from .blueprints.blu_party_wall_register import (
        party_Wall_register as party_Wall_register_blueprint,
    )

    app.register_blueprint(party_Wall_register_blueprint)

    from .blueprints.blu_TA6 import TA6_forms as TA6_forms_blueprint

    app.register_blueprint(TA6_forms_blueprint)

    # from .blueprints.file_server import file_server as file_server_blueprint
    # app.register_blueprint(file_server_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = "blu_auth.login"
    login_manager.init_app(app)

    from .models.models import User

    @login_manager.user_loader
    def load_user(user_id):
        if user_id == None or 0:
            return redirect(url_for("blu_auth.login"))
        else:
            return User(user_id)

    @app.context_processor
    def handle_context():
        return dict(os=os)

    @app.after_request
    def add_header(response):
        """
        Add headers to both force latest IE rendering engine or Chrome Frame,
        and also to cache the rendered page for 10 minutes.
        """
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response

    # Bootstrap(app)

    return app
