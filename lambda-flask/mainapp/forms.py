from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, InputRequired, Optional
from flask_wtf import Form

class UserInputForm(Form):
    user_name = StringField(label='user_name', validators=[InputRequired()])