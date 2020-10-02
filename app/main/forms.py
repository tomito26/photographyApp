from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('create your bio.', validators=[Required()])
    submit = SubmitField('submit')
class CommentsForm(FlaskForm):
    comment = TextAreaField('Comments',validators=[Required()])
    submit = SubmitField('submit')
