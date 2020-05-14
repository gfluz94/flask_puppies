from flask import Blueprint, render_template, redirect, url_for
from my_project.puppies.forms import AddForm, DeleteForm
from my_project import db
from my_project.models import Puppy, Owner

puppies_blueprint = Blueprint("puppies", __name__, template_folder="templates/puppies")

@puppies_blueprint.route("/add", methods=["GET", "POST"])
def add_puppy():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data

        puppy = Puppy(name)

        db.session.add(puppy)
        db.session.commit()

        return redirect(url_for("puppies.list_puppies"))

    return render_template("add.html", form=form)

@puppies_blueprint.route("/delete", methods=["GET", "POST"])
def delete_puppy():

    form = DeleteForm()
    form.puppy_id.choices = [(puppy.id, str(puppy.id)+" - "+puppy.name) for i, puppy in enumerate(Puppy.query.all())]
    print(form.puppy_id.data)
    if form.validate_on_submit():
        puppy = Puppy.query.get(form.puppy_id.data)
        owner = Owner.query.filter_by(puppy_id=form.puppy_id.data).first()
        db.session.delete(puppy)
        db.session.commit()
        db.session.delete(owner)
        db.session.commit()

        return redirect(url_for("puppies.list_puppies"))

    return render_template("delete.html", form=form)


@puppies_blueprint.route("/list")
def list_puppies():
    puppies = Puppy.query.all()
    return render_template("list.html", puppies=puppies)