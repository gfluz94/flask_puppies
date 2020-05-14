from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):

    name = StringField("What is the puppy's name? ", validators=[DataRequired()])
    submit = SubmitField("Add Puppy")


class DeleteForm(FlaskForm):

    puppy_id = SelectField("Please choose the puppy you want to delete from database: ", coerce=int)
    submit = SubmitField("Delete Puppy")