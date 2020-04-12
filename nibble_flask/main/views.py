from flask import Blueprint, render_template
from flask_login import login_required, current_user
from nibble_flask.models import db, User, Link

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/dashboard")
@login_required
def dashboard():
    links = User.query.filter_by(id=current_user.id).first().links

    return render_template("dashboard.html", user = current_user, links=links)