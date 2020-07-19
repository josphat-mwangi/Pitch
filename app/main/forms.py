from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required



class PitchForm(FlaskForm):

    title = StringField('Pitch title', validators=[Required()])
    text = TextAreaField('Text', validators=[Required()])
    category = SelectField('Type', choices=[('interview', 'Interview pitch'), (
        'product', 'Product pitch'), ('promotion', 'Promotion pitch')], validators=[Required()])
    submit = SubmitField('Submit')

    
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Submit')


