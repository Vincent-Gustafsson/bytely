"""Blueprint that handles the main parts e.g. the index page"""
from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user

from bytely.models import Link

main = Blueprint("main", __name__)


@main.route("/")
def index():
    if not request.cookies.get("anon_id"):
        
        
    return render_template("index.html")


@main.route("/dashboard")
@login_required
def dashboard():
    links = Link.query.filter_by(user_id=current_user.id).all()

    return render_template("dashboard.html",
                           user=current_user,
                           links=links,
                           host=request.url_root)


@main.route("/details/<id>")
@login_required
def details(id):
    link = Link.query.filter_by(id=id).first()

    if current_user.id != link.user_id:
        # Can't visit other peoples links.
        abort(404)

    return render_template("details.html",
                           user=current_user,
                           link=link,
                           host=request.url_root)
