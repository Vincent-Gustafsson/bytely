"""Blueprint that handles the main parts e.g. the index page"""
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, abort, make_response
from flask_login import login_required, current_user

from bytely.models import Link

from bytely.main.utils import generate_anon_id

main = Blueprint("main", __name__)


@main.route("/")
def index():
    if not request.cookies.get("anon_id"):
        anon_id = generate_anon_id()

        resp = make_response(render_template("index.html"))
        resp.set_cookie("anon_id", anon_id, expires=datetime(2030, 1, 1))
        
        return resp
    
    anon_id = request.cookies.get("anon_id")
    links = Link.query.filter_by(user_id=anon_id).all()
    print(links)
    return render_template("index.html", links=links, host=request.url_root)


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
