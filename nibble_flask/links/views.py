from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from nibble_flask.models import db, User, Link

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
    link = Link.query.filter_by(short_link=short_link).first()

    if link:
        link.times_clicked = link.times_clicked + 1
        db.session.commit()
        return redirect(link.full_link)
    else:
        abort(404)


@links.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = "404"), 404