"""Blueprint that handles everything with the users and authentication"""
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from bcrypt import hashpw, checkpw, gensalt

from bytely.models import db, User

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    # This is done because if a HTML checkbox
    # is unchecked it doesn't return anything.
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()

    # If mail is invalid OR the password doesn't match.
    if not user or not checkpw(password.encode('utf-8'), user.password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))

    login_user(user, remember=remember)

    return redirect(url_for("main.dashboard"))


@auth.route("/signup")
def signup():
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()

    if user:
        flash("Email address already exists.")
        return redirect(url_for("auth.signup"))

    new_user = User(email=email,
                    username=username,
                    password=hashpw(password.encode('utf-8'), gensalt()))

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=remember)
    return redirect(url_for("main.dashboard"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
