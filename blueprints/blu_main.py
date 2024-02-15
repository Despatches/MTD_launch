from flask import Blueprint, render_template, url_for, redirect
from launch import db
from flask_login import login_required, current_user
from launch.models.models import User
import mysql.connector as mysql

blu_main = Blueprint("blu_main", __name__)


@blu_main.route("/")
@login_required
def index():
    # if not current_user.id:
    # login_required()
    # if not current_user.id== None:
    # else:
    return render_template(
        "index.html",
    )


@blu_main.route("/profile/", methods=["GET"])
@login_required
def profile():
    user_profile = current_user.id
    return render_template("profile.html", name=current_user.first_name)


@blu_main.route("/landing")
@login_required
def landing():
    return render_template("landing_page.html")


@blu_main.route("/FAQ")
@login_required
def FAQ():
    return render_template("FAQ/FAQ.html")


@blu_main.route("/management/<agency>/<user>")
@login_required
def management_entry():
    return render_template("management_splash.html.jinja")
