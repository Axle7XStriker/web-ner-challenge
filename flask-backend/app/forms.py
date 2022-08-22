from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import InputRequired

class TextForm(FlaskForm):
    text = TextAreaField(u'Text', validators=[InputRequired()])
    submit = SubmitField(u'Process')
