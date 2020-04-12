"""Blueprint that handles everything with the links"""
import requests
import json

from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user

from bytely.models import db, Link, Click

links = Blueprint("links", __name__)


@links.route("/create-link", methods=["POST"])
@login_required
def create_link():
    full_link = request.form.get("link")

    link = Link(full_link=full_link, user_id=current_user.id)

    db.session.add(link)
    db.session.commit()

    return redirect(url_for("main.dashboard"))


@links.route("/<short_link>")
def redirect_to_url(short_link):
    # This block gets the users geolocation data.
    api_url = f"http://ip-api.com/json/{request.remote_addr}"
    r = requests.get(api_url)
    geolocation = json.loads(r.text)

    country = ""

    if geolocation["status"] == "fail":
        country = "None"
    else:
        country = geolocation["country"]

    link = Link.query.filter_by(short_link=short_link).first()

    if link:
        click = Click(country=country, link_id=link.id)
        link.amount = len(link.clicks) + 1

        db.session.add(click)
        db.session.commit()

        return redirect(link.full_link)
    else:
        abort(404)

# Custom 404 error to display when a user tries to
# access a link that doesn't exist.
@links.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title="404"), 404
