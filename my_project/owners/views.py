from flask import Blueprint, render_template, redirect, url_for
from my_project.owners.forms import AddForm, DeleteForm
from my_project import db
from my_project.models import Puppy, Owner

owners_blueprint = Blueprint("owners", __name__, template_folder="templates/owners")

@owners_blueprint.route("/add", methods=["GET", "POST"])
def add_owner():

    form = AddForm()
    form.puppy_id.choices = [(puppy.id, str(puppy.id)+" - "+puppy.name) for i, puppy in enumerate(Puppy.query.all())]

    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data

        print(puppy_id)

        owner = Owner(name, puppy_id)

        db.session.add(owner)
        db.session.commit()

        return redirect(url_for("puppies.list_puppies"))

    return render_template("add_owner.html", form=form)

@owners_blueprint.route("/delete", methods=["GET", "POST"])
def delete_owner():

    form = DeleteForm()
    form.owner_id.choices = [(owner.id, owner.name) for i, owner in enumerate(Owner.query.all())]

    if form.validate_on_submit():
        owner = Owner.query.get(form.owner_id.data)
        db.session.delete(owner)
        db.session.commit()

        return redirect(url_for("puppies.list_puppies"))

    return render_template("delete_owner.html", form=form)