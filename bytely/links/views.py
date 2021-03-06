"""Blueprint that handles everything with the links"""
import requests
import json

from flask import Blueprint, render_template, request, redirect, url_for, abort, make_response
from flask_login import login_required, current_user

from bytely.models import db, Link, Click

links = Blueprint("links", __name__)


@links.route("/links/create-link", methods=["POST"])
@login_required
def create_link():
    full_link = request.form.get("link")
    custom_link = request.form.get("custom-link")

    if custom_link == "":
        custom_link = None

    link = Link(full_link=full_link, short_link=custom_link, user_id=current_user.id)

    db.session.add(link)
    db.session.commit()

    return redirect(url_for("main.dashboard"))


@links.route("/links/create-anonymous-link", methods=["POST"])
def create_anonymous_link():
    full_link = request.form.get("link")
    anon_id = request.cookies.get("anon_id")

    link = Link(full_link=full_link, user_id=anon_id)

    db.session.add(link)
    db.session.commit()

    return redirect(url_for("main.index"))


@links.route("/links/edit-link/<id>", methods=["POST"])
@login_required
def edit_link(id):
    title = request.form.get("title")
    custom_link = request.form.get("custom-link-edit")

    link = Link.query.filter_by(id=id).first()

    if link and link.user_id == current_user.id:
        link.title = title
        link.short_link= custom_link
        
        db.session.add(link)
        db.session.commit()
        return redirect(url_for("main.dashboard"))
    else:
        print("Link doesn't exist.")
        abort(404)


@links.route("/links/delete-link/<id>", methods=["POST"])
@login_required
def delete_link(id):
    link = Link.query.filter_by(id=id).first()

    if link and link.user_id == current_user.id:
        db.session.delete(link)
        db.session.commit()
        return redirect(url_for("main.dashboard"))
    else:
        print("Link doesn't exist.")
        abort(404)


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
