from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required



class PitchForm(FlaskForm):
    content = TextAreaField('Post your Pitch', validators=[Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class CategoryForm(FlaskForm):
    name = StringField('Category Name',validators=[Required()])
    submit = SubmitField('Create')

