from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length

class HelloForm(FlaskForm):
    sender = StringField('sender',validators=[DataRequired(),Length(1,20)])
    content = TextAreaField('content',validators=[DataRequired(),Length(1,200)])
    submit = SubmitField()
