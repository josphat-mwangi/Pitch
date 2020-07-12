from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class Formpitch(FlaskForm):

    title = StringField('title',validators=[Required()])
    category = SelectField('Category', choices=[('Interviews','Interviewss'),('Promotion','Promotion'),('Adv','Advertisement'),('Technology','Technology')],validators=[Required()])
    post = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')
class FormComments(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')
