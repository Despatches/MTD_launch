from flask import Blueprint, render_template, redirect, url_for, request, flash
import mysql.connector as mysql
from werkzeug.security import generate_password_hash, check_password_hash
from launch import db
from flask_login import login_user, login_required, current_user, logout_user
from launch.models.models import User

blu_auth = Blueprint("blu_auth", __name__)


@blu_auth.route("/login")
def login():
    return render_template("auth_and_login/login.html")


@blu_auth.route("/login", methods=["post"])
def login_post():
    login_cursor = db.cursor()
    email = request.form.get("email")
    unhash_password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    cursor = db.cursor()
    query = f"select exists(select user_email from user_data.user where user_email = '{email}')as truth;"
    cursor.execute(query)
    email_exist = cursor.fetchone()
    if email_exist[0] == 1:
        query = f"select user_password, user_ID from user_data.user where user_email = '{email}';"
        cursor.execute(query)
        user_data = cursor.fetchone()
        if not check_password_hash(user_data[0], unhash_password):
            flash("check your login details and try again")
            cursor.close()
            return redirect(url_for("blu_auth.login"))
        else:
            active_user = User(user_data[1])
            login_user(active_user, remember=remember)
            cursor.close()
            return redirect(url_for("blu_main.profile", userid=user_data[1]))
    else:
        flash("Email not recognised")
        cursor.close()
        return redirect(url_for("blu_auth.login"))


@blu_auth.route("/basic_signup")
def basic_signup():
    return render_template("auth_and_login/signup.html")


@blu_auth.route("/signup")
def signup():
    return render_template("auth_and_login/new_account_type.html")


@blu_auth.route("/basic_signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    other_names = request.form.get("other_names")
    password = request.form.get("password")

    cursor = db.cursor(prepared=True)
    query = f"select exists(select user_email from user_data.user where user_email = '{email}')as truth;"
    cursor.execute(query)
    email_duplicate = cursor.fetchone()
    if email_duplicate[0] == 1:
        flash("email address already in use")
        cursor.close()
        return redirect(url_for("blu_auth.signup"))

    else:
        password = generate_password_hash(password, method="sha256")
        query = "call user_data.enter_user_data(%s, %s, %s, %s, %s)"
        params = (first_name, last_name, other_names, email, password)
        cursor.execute(query, params)
        db.commit()
        cursor.close()
        return redirect(url_for("blu_auth.login"))


@blu_auth.route("/new_account")
def new_account_types():
    return render_template("auth_and_login/new_account_type.html")


@blu_auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("blu_auth.login"))
