from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):

    name = StringField("What is the owner's name? ", validators=[DataRequired()])
    puppy_id = SelectField("Please choose the puppy you want to adopt: ", coerce=int)
    submit = SubmitField("Add Owner")


class DeleteForm(FlaskForm):

    owner_id = SelectField("Please choose the owner you want to delete from database: ", coerce=int)
    submit = SubmitField("Delete Owner")